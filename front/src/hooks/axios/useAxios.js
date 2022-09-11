import axios from "axios";

export default function useAxios() {

    const setJwtToken = (token) => {
        if (token && token.jwt) sessionStorage.setItem("jwt", token.jwt)
    }
    const getJwtToken = () => {
        return sessionStorage.getItem("jwt")
    }

    const addBearerHeader = () => {
        return {
            headers: {
                Authorization:
                    `Bearer ${getJwtToken()}`,
            }
        }
    }

    const plainBearerHeader = () =>{
        return `Bearer ${getJwtToken()}`
    }

    const get = async (url_path) => {
        try {
            const response = await axios.get(url_path,
            addBearerHeader()
            )
            return response
        } catch (err) {
            console.error(err);
        }

    }

    const post = async (url_path, data) => {
        try {
            const response = await axios.post(url_path, data, {
                withCredentials: true
            },
            addBearerHeader()
            )
            return response
        } catch (err) {
            console.error(err);
        }

    }


    return { get, post, setJwtToken, getJwtToken, addBearerHeader, plainBearerHeader }

}