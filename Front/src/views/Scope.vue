<!-- =========================================================================================
    File Name: Search.vue
    Description: Search Page
    ----------------------------------------------------------------------------------------
    Item Name: Vuexy - Vuejs, HTML & Laravel Admin Dashboard Template
      Author: Pixinvent
    Author URL: http://www.themeforest.net/user/pixinvent
========================================================================================== -->


<template>
    <div id="search-page">
        <div class="search-page__search-bar flex items-center">
            <vs-input icon-no-border placeholder="Search" v-model="searchQuery" class="w-full input-rounded-full" icon="icon-search" icon-pack="feather" />
        </div>
        <div class="search-page__serch-menu flex flex-wrap items-center md:justify-between mt-8">
            <div class="flex flex-wrap">
                <div  class="flex flex-wrap" v-for="item in data.data.Definition.Keywords" :key="item[0]">
                    <span class="search-tab-filter shadow-drop">{{item[0]}}</span>
                </div>
                <!-- <vs-dropdown vs-trigger-click class="search-tab-filter shadow-drop">
                    <span>More</span>
                    <vs-dropdown-menu class="search-page__more-dropdown">
                        <vs-dropdown-item>Shopping</vs-dropdown-item>
                        <vs-dropdown-item>Books</vs-dropdown-item>
                        <vs-dropdown-item>Flight</vs-dropdown-item>
                        <vs-dropdown-item>Finance</vs-dropdown-item>
                        <vs-dropdown-item>Personal</vs-dropdown-item>
                    </vs-dropdown-menu>
                </vs-dropdown> -->
            </div>
            <div>
                <span class="mb-4">Approx  results (0.35s)</span>
                <!-- <vs-dropdown vs-trigger-click class="search-tab-filter shadow-drop">
                    <span>Settings</span>
                    <vs-dropdown-menu class="search-page__settings-dropdown w-64">
                        <vs-dropdown-item>Search settings</vs-dropdown-item>
                        <vs-dropdown-item>Language</vs-dropdown-item>
                        <vs-dropdown-item>Turn on SafeSearch</vs-dropdown-item>
                        <vs-dropdown-item>Hide Private Results</vs-dropdown-item>
                        <vs-dropdown-item>Advanced Search</vs-dropdown-item>
                    </vs-dropdown-menu>
                </vs-dropdown>
                <span class="search-tab-filter mr-0 shadow-drop">Tools</span> -->
            </div>
        </div>
        

        <!-- ROW 1-->
        <div class="vx-row">
            <div class="vx-col w-1/2 md:w-1/3 xl:w-1/6">
                <statistics-card-line
                  hideChart
                  class="mb-base"
                  icon="EyeIcon"
                  :statistic="data.data.Definition.Concept_range.length"
                  statisticTitle="Concept Range" />
            </div>

            <div class="vx-col w-1/2 md:w-1/3 xl:w-1/6">
                <statistics-card-line
                  hideChart
                  class="mb-base"
                  icon="MessageSquareIcon"
                  statisticTitle="Entities"
                  :statistic="data.data.Definition.Entities.length"
                  color='success' />
            </div>

            <div class="vx-col w-1/2 md:w-1/3 xl:w-1/6">
                <statistics-card-line
                  hideChart
                  class="mb-base"
                  icon="ShoppingBagIcon"
                  :statistic="data.data.Definition.Keywords.length"
                  statisticTitle="Keywords"
                  color='warning' />
            </div>

            <div class="vx-col w-1/2 md:w-1/3 xl:w-1/6">
                <statistics-card-line
                  hideChart
                  class="mb-base"
                  icon="HeartIcon"
                  :statistic="data.data.Definition.Relation_Non_Taxonomique.length"
                  statisticTitle="Relation Non Taxonomique"
                  color='danger' />
            </div>

            <div class="vx-col w-1/2 md:w-1/3 xl:w-1/6">
                <statistics-card-line
                  hideChart
                  class="mb-base"
                  icon="SmileIcon"
                  :statistic="data.data.Definition.Synonyms.length"
                  statisticTitle="Synonyms"
                  color='success' />
            </div>

            <div class="vx-col w-1/2 md:w-1/3 xl:w-1/6">
                <statistics-card-line
                  hideChart
                  class="mb-base"
                  icon="TruckIcon"
                  :statistic="data.data.Definition.Ref.length"
                  statisticTitle="References"
                  color='warning' />
            </div>
        </div>

        <!-- SEARCH RESULTS -->
        <div class="vx-row mt-4 md:flex-row flex-col-reverse">
            <div class="vx-col md:w-5/5 lg:w-3/3 w-full">
                <vx-card class="">
                    <!-- Definition -->
                    <div class="vx-col w-full md:w-3/3 lg:w-3/3 xl:w-3/3 mb-base" style="margin-top:-3%;">

                        <vx-card
                            :title="'Definition ' + data.data.Definition.Concept" 
                            title-color="#fff"
                            content-color="#fff"
                            :card-background="'linear-gradient(120deg, #7f7fd5c9, #86a8e7c9, #91eae4c9), url(' + card_bg_img_2 + ')'">
                            <p class="mb-3">{{this.data.data.Definition.Definition}}</p>
                        </vx-card>
                    </div>
                    <div class="vx-row" v-if="conceptType=='Title_2'">

                        <!-- Collapsable Cards Input  -->
                        <div class=" vx-col w-full sm:w-1/2 lg:w-1/3 mb-base">
                            <vx-card title='Input' collapse-action>

                                <div class="flex flex-warp" >
                                    <div class="flex flex-warp"  v-for="(item,index) in data.data.Inputs" :key="item.Concept">
                                        <span class="search-tab-filter shadow-drop" v-if="index < 3">{{item.Keywords[0][0]}}</span>
                                    </div>
                                </div>
                                <vs-collapse type="margin" accordion>
                                    <div  v-for="(item,index) in data.data.Inputs" :key="item.Concept">
                                        <vs-collapse-item>
                                        <div slot="header">
                                            {{item.Concept}}
                                        </div>
                                        {{item.Definition}}
                                        </vs-collapse-item>
                                    </div>  
                                </vs-collapse>
                            
                            </vx-card>
                        </div>

                        <!-- Collapsable Cards outputs  -->
                        <div class=" vx-col w-full sm:w-1/2 lg:w-1/3 mb-base">
                            <vx-card title='Output' collapse-action>

                                <div class="flex flex-warp" >
                                    <div class="flex flex-warp"  v-for="(item,index) in data.data.Outputs" :key="item.Concept">
                                        <span class="search-tab-filter shadow-drop" v-if="index < 3">{{item.Keywords[0][0]}}</span>
                                    </div>
                                </div>
                                <vs-collapse type="margin" accordion>
                                    <div  v-for="(item,index) in data.data.Outputs" :key="item.Concept">
                                        <vs-collapse-item>
                                        <div slot="header">
                                            {{item.Concept}}
                                        </div>
                                        {{item.Definition}}
                                        </vs-collapse-item>
                                    </div>  
                                </vs-collapse>
                            
                            </vx-card>
                        </div>

                        <!-- Collapsable Cards Input  -->
                        <div class=" vx-col w-full sm:w-1/2 lg:w-1/3 mb-base">
                            <vx-card title='Tools and Techniques' collapse-action>

                                <div class="flex flex-warp" >
                                    <div class="flex flex-warp"  v-for="(item,index) in data.data.Tools_and_techniques" :key="item.Concept">
                                        <span class="search-tab-filter shadow-drop" v-if="index < 3">{{item.Keywords[0][0]}}</span>
                                    </div>
                                </div>
                                <vs-collapse type="margin" accordion>
                                    <div  v-for="(item,index) in data.data.Tools_and_techniques" :key="item.Concept">
                                        <vs-collapse-item>
                                        <div slot="header">
                                            {{item.Concept}}
                                        </div>
                                        {{item.Definition}}
                                        </vs-collapse-item>
                                    </div>  
                                </vs-collapse>
                            
                            </vx-card>
                        </div>

                </div>
                </vx-card>
                <vs-pagination :total="1" v-model="currentPage" class="mt-base"></vs-pagination>
            </div>
        </div>
    </div>
</template>

<script>
import StatisticsCardLine from '@/components/statistics-cards/StatisticsCardLine.vue'
import axios from 'axios'
import { onMounted } from 'vue'
export default{
    components: {
        StatisticsCardLine
    },  
    data() {
        return {
            card_bg_img_2: require('@/assets/images/pages/cost-control-money.png'),
            searchQuery: 'Plan scope management',
            currentPage: 1,
            conceptType: 'Title_1',
            data: {}
        }
    },
    async mounted() {
        
        console.log('mounted');
        this.data = await axios.post('http://localhost:8000/recommendation', {
            msg: this.searchQuery
        })
        console.log(this.data);
        this.conceptType = this.data.data.Type_concept
    
    },
    computed: {
        playerOptions() {
            return (media) => {
                return {
                    height: '360',
                    fluid: true,
                    // rmeove this comment if you want to autoplay
                    // autoplay: true,
                    muted: true,
                    language: 'en',
                    playbackRates: [0.7, 1.0, 1.5, 2.0],
                    sources: media.sources,
                    poster: media.poster,
                }
            }
        }
    },
    methods: {},
}
</script>

<style lang="scss">
@import "@/assets/scss/vuexy/pages/search.scss";
</style>
