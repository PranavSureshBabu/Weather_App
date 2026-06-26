<template>
  <div class="landing-page">

    <div class="overlay"></div>

    <div class="glass-card">

      <h1>☁ Weather Dashboard</h1>

      <p class="caption">
        Every forecast tells a story.
        Stay one step ahead of the weather.
      </p>

      <input
        v-model="city"
        type="text"
        placeholder="Enter your City"
        @keyup.enter="searchCity"
      />

      <button @click="searchCity">
        Search
      </button>

    </div>

  </div>
</template>

<script>
import { getWeather } from "../services/weatherService"

export default {

  data() {
    return {
      city: ""
    }
  },

  methods: {

    async searchCity() {

      if (!this.city.trim()) {
        alert("Please enter a city.")
        return
      }

      try {

        const weather = await getWeather(this.city)

        this.$router.push({
          path: "/weather",
          query: weather
        })

      }

      <template>
  <div class="landing-page">

    <div class="overlay"></div>

    <div class="glass-card">

      <h1>☁ Weather Dashboard</h1>

      <p class="caption">
        Every forecast tells a story.
        Stay one step ahead of the weather.
      </p>

      <input
        v-model="city"
        type="text"
        placeholder="Enter your City"
        @keyup.enter="searchCity"
      />

      <button @click="searchCity">
        Search
      </button>

    </div>

  </div>
</template>

<script>
import { getWeather } from "../services/weatherService"

export default {

  data() {
    return {
      city: ""
    }
  },

  methods: {

    async searchCity() {

      if (!this.city.trim()) {
        alert("Please enter a city.")
        return
      }

      try {

        const weather = await getWeather(this.city)

        this.$router.push({
          path: "/weather",
          query: weather
        })

      }

      catch (error) {
        if (error.response && error.response.data.error) {

        alert(error.response.data.error)
        }
        
    else {

        alert("Something went wrong. Please try again.")

    }
        
  }

}
</script>


}
</script>
