from openai import OpenAI
from config import api_key  
import speech_recognition as sr
import pyttsx3
import os
import webbrowser

# Text-to-speech function
def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

client = OpenAI(api_key=api_key)

# Chat function
def chat(prompt):
    response = client.chat.completions.create(
        model="gpt-4o-mini",        
        messages=[{"role": "user", "content": prompt}],
        temperature=0.8,
        max_tokens=400,
    )
    reply = response.choices[0].message.content
    print(f"Assistant: {reply}")
    say(reply)

# Speech recognition function
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en')
        print(f"User said: {query}")
        return query
    except Exception:
        say("Sorry, I did not understand that.")
        return None

if __name__ == "__main__":
    say("WELEOME JARVIS A.I.")
    print("Welcome to Jarvis A.I.")
    while True:
        query = takeCommand()
        if query is None:
            continue

        if query.lower() == "bye":
            say("Goodbye sir.")
            print("Exiting the chat.")
            break

        # Check for website commands
        sites = {
    ["Google", "https://www.google.com"],
    ["YouTube", "https://www.youtube.com"],
    ["Facebook", "https://www.facebook.com"],
    ["Amazon", "https://www.amazon.com"],
    ["Wikipedia", "https://www.wikipedia.org"],
    ["Twitter", "https://www.twitter.com"],
    ["Instagram", "https://www.instagram.com"],
    ["Yahoo", "https://www.yahoo.com"],
    ["Reddit", "https://www.reddit.com"],
    ["WhatsApp", "https://www.whatsapp.com"],
    ["Netflix", "https://www.netflix.com"],
    ["LinkedIn", "https://www.linkedin.com"],
    ["Baidu", "https://www.baidu.com"],
    ["Twitch", "https://www.twitch.tv"],
    ["Microsoft", "https://www.microsoft.com"],
    ["Zoom", "https://www.zoom.us"],
    ["eBay", "https://www.ebay.com"],
    ["Pinterest", "https://www.pinterest.com"],
    ["Apple", "https://www.apple.com"],
    ["Quora", "https://www.quora.com"],
    ["IMDB", "https://www.imdb.com"],
    ["Stack Overflow", "https://stackoverflow.com"],
    ["Bing", "https://www.bing.com"],
    ["Office", "https://www.office.com"],
    ["Live", "https://www.live.com"],
    ["Adobe", "https://www.adobe.com"],
    ["Spotify", "https://www.spotify.com"],
    ["CNN", "https://www.cnn.com"],
    ["BBC", "https://www.bbc.com"],
    ["NY Times", "https://www.nytimes.com"],
    ["Trello", "https://www.trello.com"],
    ["Canva", "https://www.canva.com"],
    ["Dropbox", "https://www.dropbox.com"],
    ["WordPress", "https://www.wordpress.com"],
    ["GitHub", "https://www.github.com"],
    ["Fandom", "https://www.fandom.com"],
    ["Udemy", "https://www.udemy.com"],
    ["Coursera", "https://www.coursera.org"],
    ["Khan Academy", "https://www.khanacademy.org"],
    ["Flipkart", "https://www.flipkart.com"],
    ["Snapchat", "https://www.snapchat.com"],
    ["TikTok", "https://www.tiktok.com"],
    ["Telegram", "https://web.telegram.org"],
    ["Hulu", "https://www.hulu.com"],
    ["Crunchyroll", "https://www.crunchyroll.com"],
    ["DuckDuckGo", "https://www.duckduckgo.com"],
    ["Indeed", "https://www.indeed.com"],
    ["Glassdoor", "https://www.glassdoor.com"],
    ["Weather", "https://www.weather.com"],
    ["Booking", "https://www.booking.com"],
    ["Airbnb", "https://www.airbnb.com"],
    ["Zillow", "https://www.zillow.com"],
    ["AliExpress", "https://www.aliexpress.com"],
    ["PayPal", "https://www.paypal.com"],
    ["ICICI Bank", "https://www.icicibank.com"],
    ["HDFC Bank", "https://www.hdfcbank.com"],
    ["SBI", "https://www.onlinesbi.com"],
    ["IRCTC", "https://www.irctc.co.in"],
    ["Myntra", "https://www.myntra.com"],
    ["Jio", "https://www.jio.com"],
    ["Airtel", "https://www.airtel.in"],
    ["Speedtest", "https://www.speedtest.net"],
    ["W3Schools", "https://www.w3schools.com"],
    ["GeeksforGeeks", "https://www.geeksforgeeks.org"],
    ["HackerRank", "https://www.hackerrank.com"],
    ["LeetCode", "https://www.leetcode.com"],
    ["Codeforces", "https://codeforces.com"],
    ["CodeChef", "https://www.codechef.com"],
    ["Replit", "https://www.replit.com"],
    ["GitLab", "https://www.gitlab.com"],
    ["Notion", "https://www.notion.so"],
    ["Medium", "https://www.medium.com"],
    ["Naukri", "https://www.naukri.com"],
    ["Times of India", "https://timesofindia.indiatimes.com"],
    ["Hindustan Times", "https://www.hindustantimes.com"],
    ["NDTV", "https://www.ndtv.com"],
    ["Zee News", "https://zeenews.india.com"],
    ["Moneycontrol", "https://www.moneycontrol.com"],
    ["TradingView", "https://www.tradingview.com"],
    ["Investopedia", "https://www.investopedia.com"],
    ["CoinMarketCap", "https://www.coinmarketcap.com"],
    ["Binance", "https://www.binance.com"],
    ["Coinbase", "https://www.coinbase.com"],
    ["OpenAI", "https://www.openai.com"],
    ["ChatGPT", "https://chat.openai.com"],
    ["Discord", "https://www.discord.com"],
    ["Opera", "https://www.opera.com"],
    ["Brave", "https://www.brave.com"],
    ["Tor", "https://www.torproject.org"],
    ["Wayback Machine", "https://archive.org/web"],
    ["Archive.org", "https://www.archive.org"],
    ["YCombinator", "https://www.ycombinator.com"],
    ["Product Hunt", "https://www.producthunt.com"],
    ["Crunchbase", "https://www.crunchbase.com"],
    ["AngelList", "https://www.angel.co"],
    ["Dribbble", "https://dribbble.com"],
    ["Behance", "https://www.behance.net"],
    ["Pixabay", "https://www.pixabay.com"],
    ["Unsplash", "https://www.unsplash.com"],
    ["Pexels", "https://www.pexels.com"],
    ["Remove.bg", "https://www.remove.bg"],
    ["Photopea", "https://www.photopea.com"],
    ["Kaggle", "https://www.kaggle.com"],
        }


        opened_site = False
        for site in sites:
            if f"open {site[0]}" in query.lower():
                say(f"Opening {site[0]} sir...")
                webbrowser.open(site[1])
                opened_site = True
                break

        if not opened_site:
            chat(prompt=query)

