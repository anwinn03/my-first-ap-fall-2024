import os
import json
from pprint import pprint
from statistics import mean
from dotenv import load_dotenv
import requests
from plotly.express import line
from IPython.display import Image 

load_dotenv()
API_KEY = os.getenv("ALPHAVANTAGE_API_KEY", default="demo")

request_url = f"https://www.alphavantage.co/query?function=UNEMPLOYMENT&apikey={API_KEY}"
response = requests.get(request_url)
parsed_response = json.loads(response.text)
print(type(parsed_response))
pprint(parsed_response)

data = parsed_response["data"]

# Challenge A
print("-------------------------")
print("LATEST UNEMPLOYMENT RATE:")
print(f"{data[0]['value']}%", "as of", data[0]["date"])

# Challenge B
this_year = [d for d in data if "2022-" in d["date"]]
rates_this_year = [float(d["value"]) for d in this_year]
print("-------------------------")
print("AVG UNEMPLOYMENT THIS YEAR:", f"{mean(rates_this_year)}%")
print("NO MONTHS:", len(this_year))

# Challenge C
dates = [d["date"] for d in data]
rates = [float(d["value"]) for d in data]
fig = line(x=dates, y=rates, title="United States Unemployment Rate over time", labels={"x": "Month", "y": "Unemployment Rate"})

# Save and display the image
file_path = "unemployment_overtime.png"
fig.write_image(file_path)

# Display the image
Image(filename=file_path)
