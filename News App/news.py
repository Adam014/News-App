import requests
import tkinter as tk


def getNews():
    api_key = "0a88c3de8ff949a5923a595decaa6b61"
    url = "https://newsapi.org/v2/top-headlines?country=cz&apiKey="+api_key
    news = requests.get(url).json()

    articles = news["articles"]

    my_articles = []
    my_news = ""

    for article in articles:
        my_articles.append(article["title"])
    
    for i in range(15):
        my_news = my_news + str(i+1) + ". " + my_articles[i] + "\n"

    label.config(text = my_news)

canvas = tk.Tk()
canvas.geometry("1200x500")
canvas.title("News")

button = tk.Button(canvas, font = 24, text = "Reload", command = getNews)
button.pack(pady = 20)

label = tk.Label(canvas, font = 18, justify="left")
label.pack(pady = 20)

getNews()

canvas.mainloop()