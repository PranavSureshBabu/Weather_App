import { createRouter, createWebHistory } from "vue-router"

import LandingPage from "../components/LandingPage.vue"
import WeatherDashboard from "../components/WeatherDashboard.vue"

const routes = [

    {
        path: "/",
        component: LandingPage
    },

    {
        path: "/weather",
        component: WeatherDashboard
    }

]

const router = createRouter({

    history: createWebHistory(),

    routes

})

export default router