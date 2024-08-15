import requests
api_key = "f35f9b1357fa499f892171e58c36c193"
url = ("https://newsapi.org/v2/top-headlines?sources="
       "techcrunch&apiKey=f35f9b1357fa499f892171e58c36c193")

# Make a request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and descriotion
for article in content["articles"]:
    print(article["title"])
    print(article["description"])
