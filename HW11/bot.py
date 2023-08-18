import telebot
import requests
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TOKEN")
API_KEY = os.getenv("API_KEY")

bot = telebot.TeleBot(TOKEN)


def search_gifs(searched_gif, api_key, limit=5):
    gif_url = "https://api.giphy.com/v1/gifs/search"
    params = {
        "q": searched_gif,
        "api_key": api_key,
        "limit": limit,
        "rating": "g",
        "lang": "en",
    }

    try:
        response = requests.get(gif_url, params=params)
        data = response.json()
        gif_links = [item["images"]["original"]["url"] for item in data["data"]]
        return gif_links
    except requests.exceptions.RequestException as e:
        print("Error", e)
        return None


@bot.message_handler(func=lambda message: True)
def get_user_text(message):
    API_KEY = API_KEY
    searched_gif = message.text
    gif_links = search_gifs(searched_gif, API_KEY, limit=5)

    if not gif_links:
        bot.send_message(message.chat.id, "No GIFs found")
        return
    for gif_link in gif_links:
        bot.send_message(
            message.chat.id, f"Your mood is: {gif_link}", parse_mode="html"
        )


if __name__ == "__main__":
    bot.polling(non_stop=True)
