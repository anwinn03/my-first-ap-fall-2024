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

Run the stock apps:
```sh
python app/stocks.py
```