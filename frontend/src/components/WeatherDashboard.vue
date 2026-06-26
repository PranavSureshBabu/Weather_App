<template>

<div class="dashboard-page">

    <div class="dashboard-overlay"></div>

    <div class="dashboard-container">

        <!-- Header -->

        <div class="dashboard-header">

            <div>

                <h1 class="dashboard-title">
                    WeatherMap
                </h1>

                <p class="dashboard-subtitle">
                    Real-Time Weather Dashboard
                </p>

            </div>

            <button
                class="search-again"
                @click="$router.push('/')">

                Search Another City

            </button>

        </div>

        <!-- Main Content -->

        <div class="dashboard-content">

            <!-- Left Side -->

            <div class="left-panel">

                <p> 

                    📍 {{ weather.city }}, {{ weather.country }}

                </p>

                <div class="weather-main">

                    <i :class="weatherIcon" class="weather-icon"></i>

                    <h1 class="temperature">
                    {{ weather.temperature }}°C
                    </h1>

                </div>

                <h2 class="description">

                    {{ weather.description }}

                </h2>

                <p class="time">

                    🕒 {{ weather.time }}

                </p>

            </div>

            <!-- Right Side -->

            <div class="right-panel">

                <div class="stat-card">

                    <i class="fa-solid fa-droplet stat-icon"></i>

                    <h3>Humidity</h3>

                    <p>{{ weather.humidity }}%</p>

                </div>

                <div class="stat-card">

                    <i class="fa-solid fa-wind stat-icon"></i>

                    <h3>Wind</h3>

                    <p>{{ weather.wind }} m/s</p>

                </div>

                <div class="stat-card">

                    <i class="fa-solid fa-gauge-high stat-icon"></i>

                    <h3>Pressure</h3>

                    <p>{{ weather.pressure }} hPa</p>

                </div>

                <div class="stat-card">

                    <i class="fa-solid fa-temperature-half stat-icon"></i>

                    <h3>Feels Like</h3>

                    <p>{{ weather.feels_like }}°C</p>

                </div>

                <div class="stat-card">

                    <i class="fas fa-eye stat-icon"></i>

                    <h3>Visibility</h3>

                    <p>{{ weather.visibility }} km</p>

                </div>

                <div class="stat-card">

                    <i class="fa-solid fa-cloud stat-icon"></i>
                    
                    <h3>Condition</h3>

                    <p>{{ weather.description }}</p>

                </div>

            </div>

        </div>

    </div>

</div>

</template>

<script>
export default {

    data() {

        return {

            weather: this.$route.query

        }

    },

    computed: {

        weatherIcon() {

            switch (this.weather.condition) {

                case "Clear":
                    return "fa-solid fa-sun"

                case "Clouds":
                    return "fa-solid fa-cloud"

                case "Rain":
                    return "fa-solid fa-cloud-rain"

                case "Snow":
                    return "fa-solid fa-snowflake"

                case "Thunderstorm":
                    return "fa-solid fa-bolt"

                case "Drizzle":
                    return "fa-solid fa-cloud-rain"

                case "Mist":
                case "Fog":
                case "Haze":
                    return "fa-solid fa-smog"

                default:
                    return "fa-solid fa-cloud"

            }

        }

    }

}
</script>