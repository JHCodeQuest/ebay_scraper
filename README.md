# Product Research Dashboard

A local Flask Product Research Dashboard for exploring a saved eBay dataset of iPhone 14 listings. It uses the included CSV and does not scrape eBay or require an account.

## Run locally

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python app.py
```

Open http://127.0.0.1:5000 in your browser. The displayed listings and prices are a static snapshot, not live sold-price results.
