import requests
from newspaper import Article
import ollama
from ollama import chat
from ollama import ChatResponse
import time

age = input("What is your age: ")
articles = int(input("How many articles would you like to read: "))

start_time = time.perf_counter()  # Start timer

api_key = "API_KEY"
url = "https://newsapi.org/v2/top-headlines"
params = {
    "country": "us",
    "apiKey": api_key,
}

response = requests.get(url, params=params)
data = response.json()

titles = []
contents = []

for article in data.get("articles", []):
    title = article.get("title", "No Title")
    link = article.get("url", None)
    
    if not link:
        # If no URL, skip this article or use description/content
        contents.append(article.get("content") or article.get("description") or "No Content")
        titles.append(title)
        continue
    
    # Use newspaper3k to download and parse full article text
    try:
        news_article = Article(link)
        news_article.download()
        news_article.parse()
        full_text = news_article.text
    except Exception as e:
        print(f"Failed to parse article at {link}: {e}")
        full_text = article.get("content") or article.get("description") or "No Content"
    
    titles.append(title)
    contents.append(full_text)

# ------------------------------------------------------------------------------------------------------------------------


with open("summaries.txt", "w", encoding="utf-8") as f:
    for i in range(articles):
        response = ollama.generate(model='llama3.2', prompt=f'Summarize this text as if you were doing so to a {age} year old in a fun and exciting way: {contents[i]}' )
        summary_text = response.response
        
        # Write title and summary to file
        f.write(f"Title: {titles[i]}\n")
        f.write("Summary:\n")
        f.write(summary_text + "\n")
        f.write("\n" + "-"*80 + "\n\n")  # separator between articles

end_time = time.perf_counter()  # End timer
print(f"Program took {end_time - start_time:.3f} seconds")
