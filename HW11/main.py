import requests


def search_gifs(searched_gif, api_key):
    gif_url = "https://api.giphy.com/v1/gifs/search"
    params = {
        "q": searched_gif,
        "api_key": api_key,
        "limit": 1,
        "rating": "g",
        "lang": "en",
    }

    try:
        response = requests.get(gif_url, params=params)
        data = response.json()
        gif_link = data["data"][0]["images"]["original"]["url"]
        return gif_link
    except requests.exceptions.RequestException as e:
        print("Error", e)
        return []


def main():
    API_KEY = "nXLp5bVa5X9zH6N7CwPWlEwuxHmyM27Q"
    searched_gif = input("Enter the search gif: ")
    gif_link = search_gifs(searched_gif, API_KEY)

    if gif_link:
        print(f"GIF link: {gif_link}")
    else:
        print("No GIFs found")


if __name__ == "__main__":
    main()
