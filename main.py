import requests
from send_email import send_email

api_key = "f35f9b1357fa499f892171e58c36c193"
url = ("https://newsapi.org/v2/top-headlines?sources="
       "techcrunch&apiKey=f35f9b1357fa499f892171e58c36c193")

# Make a request
request = requests.get(url)

# Get a dictionary with data
content = request.json()
email = " "
# Access the article titles and description
for article in content["articles"]:
    if article["title"] is not None:
        email = email + article["title"] + "\n" + article["description"] + 2*"\n"

email = email.encode("utf-8")
send_email(message=email)
