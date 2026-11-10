# iPhone 14 Price Research

A local Flask app for browsing saved iPhone 14 listing data. It uses the included CSV sample and does not contact eBay or require an account.

## Run locally

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python app.py
```

Open http://127.0.0.1:5000 in your browser. The displayed listings and prices are a static snapshot, not live sold-price results.
