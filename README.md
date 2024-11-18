# my-first-ap-fall-2024

Create and activate a virtual environment:

```sh
conda create -n reports-env-2024 python=3.11
```

Activate the environment:

```sh
conda activate reports-env-2024
```

Install packages:
```sh
pip install -r requirements.txt
```

[Obtain an API Key](https://www.alphavantage.co/support/#api-key) from AlphaVantage.

Create a ".env" file and add contents like the following (using your own AlphaVantage API Key):

```sh
# this is the ".env" file:
ALPHAVANTAGE_API_KEY="..."
```

Run the example script:

```sh
python app/my_script.py
```

Run the unemployment report:
```sh
python app/unemployment_report.py
```

Since running visualization doesn't work on my local, I decided to output an visualization through a PNG file

Run the stock apps:
```sh
python -m app.stocks
```

```sh
python -m app.rps
```

```sh
pytest
```

### Web App
Run the web app (then view in the browser at http://localhost:5000/):

```sh
# Mac OS:
FLASK_APP=web_app flask run

# Windows OS:
# ... if `export` doesn't work for you, try `set` instead
# ... or set FLASK_APP variable via ".env" file
export FLASK_APP=web_app
flask run
```
## Testing

Run tests: