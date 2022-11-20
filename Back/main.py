
import nltk
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
import pickle
import numpy as np
import re
from keras.models import load_model
import json
import random
import pandas as pd



from typing import Union
from pydantic import BaseModel
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware  # NEW

from numpy.lib import type_check


df = pd.read_json('DF_Recommendation_11_14_2022.json')


def getData(concept):
  inputs=[]
  outputs=[]
  tools=[]
  definition=''
  type_concept=''
  ind = get_ind_concept(concept)
  
  if df.iloc[ind]['Section'][2]=='0':
    type_concept = 'Title_1'
  elif df.iloc[ind]['Section'][2]!='0' and  df.iloc[ind]['Section'][4]=='0':
    type_concept = 'Title_2'
  else:
    type_concept = 'Title_4'


  if type_concept=='Title_1':
    definition = get_definition(concept)
  elif type_concept=='Title_2':
    definition = get_definition(concept)
    for i in range(ind+1,216):
      if df.iloc[i]['Type'].lower()=="has_inputs":
        inputs.append(dict(df.iloc[i]))
      if df.iloc[i]['Type'].lower()=="has_outputs":
        outputs.append(dict(df.iloc[i]))
      if df.iloc[i]['Type'].lower()=="has_tools_and_techniques":
        tools.append(dict(df.iloc[i]))
      if df.iloc[i]['Type'].lower()=="":
        break
  elif type_concept=='Title_4':
    definition = get_definition(concept)
  return {'Type_concept':type_concept, 'Inputs':inputs,'Outputs':outputs,'Tools_and_techniques':tools,'Definition':definition}


def get_definition(concept):
  concept = get_ind_concept(concept)
  #if df['Type'][concept]!='':
  return dict(df.iloc[concept])

def get_ind_concept(concept):
  for i in range(len(df)):
    if concept==df['Concept'][i]:
      return i




app = FastAPI()
# NEW
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



model = load_model('chatbot_model_pmbok.h5')

intents = json.loads(open('intents_pmbok.json', encoding="utf8").read())
words = pickle.load(open('words.pkl','rb'))
classes = pickle.load(open('classes.pkl','rb'))

def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
    return sentence_words

def bow(sentence, words, show_details=True):
    # tokenize the pattern
    sentence_words = clean_up_sentence(sentence)
    # bag of words - matrix of N words, vocabulary matrix
    bag = [0]*len(words)
    for s in sentence_words:
        for i,w in enumerate(words):
            if w == s:
                # assign 1 if current word is in the vocabulary position
                bag[i] = 1
                if show_details:
                    print ("found in bag: %s" % w)
    return(np.array(bag))

def predict_class(sentence, model):
    # filter out predictions below a threshold
    p = bow(sentence, words,show_details=False)
    res = model.predict(np.array([p]))[0]
    ERROR_THRESHOLD = 0.01
    results = [[i,r] for i,r in enumerate(res) if r>ERROR_THRESHOLD]
    # sort by strength of probability
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({"intent": classes[r[0]], "probability": str(r[1])})
    return return_list

def getResponse(ints, intents_json):
    
    tag = ints[0]['intent']
    # list_of_intents = intents_json['intents']
    # priority = 0 
    # for i in list_of_intents:
    #     if(i['tag']== tag) :
    #         result = random.choice(i['tag'])
    return tag
    
def chatbot_response(msg):
    ints = predict_class(msg, model)
    print(ints)
    res = getResponse(ints, intents)
    return res
    
    


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


class Item(BaseModel):
    msg: str


@app.post("/recommendation")
async def recommendation(item: Item):
    msg = item.dict().get('msg')
    print("msg", msg)
    concept = chatbot_response(msg)
    data = getData(concept)
    json_compatible_item_data = jsonable_encoder(data)
    return JSONResponse(content=json_compatible_item_data)



@app.post("/suggestion")
async def recommendation(item: Item):
    msg = item.dict().get('msg')
    print("msg", msg)
    ints = predict_class(msg,model)
    return ints
