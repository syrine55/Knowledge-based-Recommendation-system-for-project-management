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
                <span class="search-tab-filter shadow-drop">All</span>
                <span class="search-tab-filter shadow-drop">Images</span>
                <span class="search-tab-filter shadow-drop">Video</span>
                <span class="search-tab-filter shadow-drop">Maps</span>
                <span class="search-tab-filter shadow-drop">News</span>
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
                <span class="mb-4">Approx 84,00,00,000 results (0.35s)</span>
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

        <!-- SEARCH RESULTS -->
        <div class="vx-row mt-4 md:flex-row flex-col-reverse">
            <div class="vx-col md:w-5/5 lg:w-3/3 w-full">
                <vx-card class="">
                    <!-- Definition -->
                    <div class="vx-col w-full md:w-3/3 lg:w-3/3 xl:w-3/3 mb-base" style="margin-top:-3%;">

                        <vx-card
                            title="Definition Scope Management" 
                            title-color="#fff"
                            content-color="#fff"
                            :card-background="'linear-gradient(120deg, #7f7fd5c9, #86a8e7c9, #91eae4c9), url(' + card_bg_img_2 + ')'">
                            <p class="mb-3">You can use <strong>card-background</strong> prop to change background of card. This prop supports hex, rgba, rgb and theme colors.</p>
                            <p class="mb-3">Oat cake powder sesame snaps. Chocolate bar dessert bonbon chocolate bar pudding apple pie muffin chocolate ice cream. I love bear claw I love.</p>
                        </vx-card>
                    </div>
                    <div class="vx-row">

                        <!-- Collapsable Cards Input  -->
                        <div class=" vx-col w-full sm:w-1/2 lg:w-1/3 mb-base">
                            <vx-card title='Input' collapse-action>

                                <div class="flex flex-warp">
                                    <span class="search-tab-filter shadow-drop">All</span>
                                    <span class="search-tab-filter shadow-drop">Images</span>
                                </div>
                                
                                <p class="mb-3">You can create collapsible content card by setting <code>collapse-action</code> prop to <code>true</code>. By default it is set to false.</p>
                                <p class="mb-3">You can also get this action if you set <code>action-buttons</code> prop to <code>true</code>.</p>

                                <vs-collapse type="margin" accordion>
                                    <vs-collapse-item>
                                    <div slot="header">
                                        Collapse item
                                    </div>
                                    Lorem....metus.
                                    </vs-collapse-item>

                                    <vs-collapse-item>
                                    <div slot="header">
                                        Collapse item 2
                                    </div>
                                    Nunc....maximus.
                                    </vs-collapse-item>

                                    <vs-collapse-item>
                                    <div slot="header">
                                        Collapse item 3
                                    </div>
                                    Suspendisse....eu
                                    </vs-collapse-item>

                                    <vs-collapse-item>
                                    <div slot="header">
                                        Collapse item 4
                                    </div>
                                    Suspendisse....finibus.
                                    </vs-collapse-item>
                                </vs-collapse>
                            
                            </vx-card>
                        </div>

                        <!-- Collapsable Cards Input  -->
                    <div class=" vx-col w-full sm:w-1/2 lg:w-1/3 mb-base">
                        <vx-card title='Output' collapse-action>

                            <div class="flex flex-warp">
                                <span class="search-tab-filter shadow-drop">All</span>
                                <span class="search-tab-filter shadow-drop">Images</span>
                            </div>
                            
                            <p class="mb-3">You can create collapsible content card by setting <code>collapse-action</code> prop to <code>true</code>. By default it is set to false.</p>
                            <p class="mb-3">You can also get this action if you set <code>action-buttons</code> prop to <code>true</code>.</p>

                            <vs-collapse type="margin" accordion>
                                <vs-collapse-item>
                                <div slot="header">
                                    Collapse item
                                </div>
                                Lorem....metus.
                                </vs-collapse-item>

                                <vs-collapse-item>
                                <div slot="header">
                                    Collapse item 2
                                </div>
                                Nunc....maximus.
                                </vs-collapse-item>

                                <vs-collapse-item>
                                <div slot="header">
                                    Collapse item 3
                                </div>
                                Suspendisse....eu
                                </vs-collapse-item>

                                <vs-collapse-item>
                                <div slot="header">
                                    Collapse item 4
                                </div>
                                Suspendisse....finibus.
                                </vs-collapse-item>
                            </vs-collapse>
                        
                        </vx-card>
                    </div>
                    
                    <!-- Collapsable Cards Input  -->
                    <div class=" vx-col w-full sm:w-1/2 lg:w-1/3 mb-base">
                        <vx-card title='Tools & Techniques' collapse-action>

                            <div class="flex flex-warp">
                                <span class="search-tab-filter shadow-drop">All</span>
                                <span class="search-tab-filter shadow-drop">Images</span>
                            </div>
                            
                            <p class="mb-3">You can create collapsible content card by setting <code>collapse-action</code> prop to <code>true</code>. By default it is set to false.</p>
                            <p class="mb-3">You can also get this action if you set <code>action-buttons</code> prop to <code>true</code>.</p>

                            <vs-collapse type="margin" accordion>
                                <vs-collapse-item>
                                <div slot="header">
                                    Collapse item
                                </div>
                                Lorem....metus.
                                </vs-collapse-item>

                                <vs-collapse-item>
                                <div slot="header">
                                    Collapse item 2
                                </div>
                                Nunc....maximus.
                                </vs-collapse-item>

                                <vs-collapse-item>
                                <div slot="header">
                                    Collapse item 3
                                </div>
                                Suspendisse....eu
                                </vs-collapse-item>

                                <vs-collapse-item>
                                <div slot="header">
                                    Collapse item 4
                                </div>
                                Suspendisse....finibus.
                                </vs-collapse-item>
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
import { videoPlayer } from 'vue-video-player'
import 'video.js/dist/video-js.css'

export default{
    data() {
        return {
            card_bg_img_2: require('@/assets/images/pages/cost-control-money.png'),
            searchQuery: 'Modern Admin',
            currentPage: 1,
            knowledgePanel: {
                img         : require("@/assets/images/pages/modern.jpg"),
                title       : 'Modern Admin - Clean Bootstrap 4 Dashboard HTML Template',
                subtitle    : 'Clean Bootstrap 4 Dashboard HTML Template',
                description : 'Clean Bootstrap 4 Dashboard HTML Template + Bitcoin Dashboard can be used for any type of web applications: Project Management, eCommerce backends, CRM, Analytics, Fitness or any custom admin panels.',
                info: [
                    { title: '1,367', subtitle: 'Sales' },
                    { title: '74', subtitle: 'Comments' },
                    { title: '5', subtitle: 'Ratings' },
                ],
                externalLink: {
                    title: 'View on Themeforest',
                    icon: 'ExternalLinkIcon',
                    url: 'https://1.envato.market/modern_admin',
                },
                resultMetaList: [
                    { name: 'Bootstrap', value: 'v4.13 updated' },
                    { name: 'Created', value: 'Mar 8 2018' },
                    { name: 'Last Update', value: 'Nov 28 2018' },
                    { name: 'Documentation', value: 'Well Documented' },
                    { name: 'Layout', value: 'Responsive' },
                ],
                suggestedSearches: [
                    {
                      name: 'Apex',
                      img:  require("@/assets/images/pages/1-apex.png"),
                      url:  'https://1.envato.market/apex_admin'
                    },
                    {
                      name: 'Convex',
                      img:  require("@/assets/images/pages/3-convex.png"),
                      url:  'https://1.envato.market/convex_angular_admin'
                    },
                    {
                      name: 'Materialize',
                      img:  require("@/assets/images/pages/4-materialize.png"),
                      url:  'https://1.envato.market/materialize_admin'
                    },
                    {
                      name: 'Stack',
                      img:  require("@/assets/images/pages/2-stack.png"),
                      url:  'https://1.envato.market/stack_admin'
                    },
                ]
            },
            searchResults: [
                {
                    title: 'Modern Admin - Clean Bootstrap 4 Dashboard HTML Template',
                    linkUrl: 'https://1.envato.market/modern_admin',
                    resultUrl: 'https://1.envato.market/pixinvent_portfolio',
                    metaData: {
                        ratings: 5,
                        info: ['25 reviews', '25.00 USD', 'In Stock']
                    },
                    time: 'Mon Dec 10 2018 07:45:00 GMT+0000 (GMT)',
                    description: 'Cake sesame snaps cupcake gingerbread danish I love gingerbread. Apple pie pie jujubes chupa chups muffin halvah lollipop. Chocolate cake oat cake tiramisu marzipan sugar plum. Donut sweet pie oat cake dragée fruitcake cotton candy lemon drops. Sweet roll wafer bear claw tiramisu oat cake.',
                    sitelinks: [
                        {
                            title: 'Dashboard',
                            url: 'https://1.envato.market/modern_admin',
                            description: 'Halvah marzipan icing chocolate caramels candy canes carrot cake dragée apple pie. Croissant oat cake gummies biscuit.'
                        },
                        {
                            title: 'UI Components',
                            url: 'https://1.envato.market/modern_admin',
                            description: 'Brownie lollipop chocolate bar chocolate cake macaroon. Bonbon chocolate tootsie roll chocolate.'
                        },
                        {
                            title: 'Form Elements',
                            url: 'https://1.envato.market/modern_admin',
                            description: 'Lollipop cake wafer. Candy chocolate toffee icing. Chocolate cake cupcake toffee chupa chups topping.'
                        },
                        {
                            title: 'Support',
                            url: 'https://1.envato.market/modern_admin',
                            description: 'Carrot cake sweet soufflé cake bear claw lollipop. Muffin sugar plum chupa chups liquorice cotton candy halvah danish cake.'
                        },
                        {
                            title: 'Charts',
                            url: 'https://1.envato.market/modern_admin',
                            description: 'Gingerbread chupa chups toffee jelly chocolate cake tiramisu marshmallow. Donut tiramisu chocolate marshmallow.'
                        },
                        {
                            title: 'Documentation',
                            url: 'https://1.envato.market/modern_admin',
                            description: 'Powder brownie candy toffee soufflé. Gingerbread sweet roll gingerbread icing macaroon.'
                        },
                    ]
                },
                {
                    title: 'Attire bench - Quick win shoot me an email',
                    linkUrl: 'https://1.envato.market/modern_admin',
                    resultUrl: 'https://1.envato.market/pixinvent_portfolio',
                    resultImg: require("@/assets/images/pages/search-result.jpg"),
                    metaData: {
                        ratings: 4.5,
                        info: ['17 reviews', '12 votes', '28.00 USD', 'In Stock']
                    },
                    time: 'Mon Feb 23 2017 07:45:00 GMT+0000 (GMT)',
                    description: 'Tiramisu soufflé gummies ice cream liquorice gingerbread sweet roll. Cake cotton candy candy ice cream muffin donut soufflé danish. Dessert jelly beans wafer cheesecake. Sugar plum gingerbread caramels candy canes gummi bears bear claw donut. Oat cake cookie tiramisu sweet halvah sugar plum. Dessert danish oat cake.',
                },
                {
                    title: 'The Table - for what do you feel you would',
                    linkUrl: 'https://1.envato.market/modern_admin',
                    resultUrl: 'https://1.envato.market/pixinvent_portfolio',
                    resultVideo: [{sources: [ { type: "video/mp4", src: "http://vjs.zencdn.net/v/oceans.mp4" } ], poster: 'https://surmon-china.github.io/vue-quill-editor/static/images/surmon-1.jpg'}],
                    metaData: {
                        info: ['1M Views', 'Uploaded by PlayStation']
                    },
                    time: 'Mon Jun 25 2016 07:45:00 GMT+0000 (GMT)',
                    description: 'Tiramisu soufflé gummies ice cream liquorice gingerbread sweet roll. Cake cotton candy candy ice cream muffin donut soufflé danish. Dessert jelly beans wafer cheesecake. Sugar plum gingerbread caramels candy canes gummi bears bear claw donut. Oat cake cookie tiramisu sweet halvah sugar plum. Dessert danish oat cake.',
                },
                {
                    title: 'Microdosing - deep v actually schlitz chia',
                    linkUrl: 'https://1.envato.market/modern_admin',
                    resultUrl: 'https://1.envato.market/pixinvent_portfolio',
                    description: 'Wafer liquorice sweet roll jelly beans cake soufflé. Oat cake marzipan chocolate cake sesame snaps jujubes. Dragée biscuit dessert. Chocolate muffin wafer. Sugar plum icing tootsie roll gummi bears marzipan candy canes biscuit.',
                },
                {
                    title: 'Aesthetic neutra freegan, mlkshk literally',
                    linkUrl: 'https://1.envato.market/modern_admin',
                    resultUrl: 'https://1.envato.market/pixinvent_portfolio',
                    time: 'Mon Jun 30 2017 10:30:00 GMT+0000 (GMT)',
                    description: 'Donut jelly cake chupa chups powder chocolate cake cheesecake. Wafer macaroon sweet roll gingerbread cheesecake gummi bears. Marzipan jujubes sweet roll tootsie roll cookie apple pie brownie bear claw jelly beans.',
                },
                {
                    title: 'iCell - disrupt butcher pitchfork.',
                    linkUrl: 'https://1.envato.market/modern_admin#',
                    resultUrl: 'https://1.envato.market/pixinvent_portfolio',
                    time: 'Mon DEC 12 2015 08:39:00 GMT+0000 (GMT)',
                    description: 'Cake fruitcake cake caramels jelly beans chocolate bar. Macaroon gingerbread pastry. Gummies ice cream chocolate lollipop brownie cotton candy. Topping cotton candy brownie. Cake tiramisu macaroon sugar plum. Sweet cotton candy powder tootsie roll candy gummies brownie lollipop. Sweet muffin pudding.',
                },
            ]
        }
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
    components: {
        videoPlayer,
    }
}
</script>

<style lang="scss">
@import "@/assets/scss/vuexy/pages/search.scss";
</style>
