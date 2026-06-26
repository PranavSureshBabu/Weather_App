import axios from "axios"

const API_URL = "/api/weather"

export async function getWeather(city){

    const response = await axios.get(

        `${API_URL}/${city}`

    )

    return response.data

}