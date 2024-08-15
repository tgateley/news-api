import requests
from send_email import send_email

topic = "techcrunch"

api_key = "f35f9b1357fa499f892171e58c36c193"
url = ("https://newsapi.org/v2/top-headlines?"
       f"sources={topic}&"
       "apiKey=f35f9b1357fa499f892171e58c36c193&"
       "language=en")

# Make a request
request = requests.get(url)

# Get a dictionary with data
content = request.json()
email = "Subject: Today's News" + 2*"\n"
# Access the article titles and description
for article in content["articles"][:5]:
    if article["title"] is not None:
        email = (email + article["title"] + 2*"\n"
                 + article["description"] +
                 "\n" + article["url"] + 3*"\n")

email = email.encode("utf-8")
send_email(message=email)
