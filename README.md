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




Run the unemployment report:
```sh
ALPHAVANTAGE_API_KEY="..." python app/unemployment_report.py
```