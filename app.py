import csv
import re
from pathlib import Path

from flask import Flask, render_template

app = Flask(__name__)
SAMPLE_DATA_FILE = Path(__file__).with_name("iphone 14.csv")
FORBIDDEN_TERMS = [
    "refurbished",
    "iphone 11",
    "iphone 12",
    "iphone 13",
    "iphone 14 pro",
    "iphone 14 plus",
    "iphone 15",
    "iphone 16",
    "iphone 17",
    "parts",
    "damaged",
    "locked",
    "case only",
    "phone case",
    "screen protector",
    "replacement screen",
    "charger only",
    "box only",
    "dummy phone",
    "not working",
    "read description",
]
FORBIDDEN_PATTERN = re.compile(
    r"\b(?:" + "|".join(re.escape(term) for term in FORBIDDEN_TERMS) + r")\b",
    re.IGNORECASE,
)


@app.route("/")
def display_csv():
    with SAMPLE_DATA_FILE.open(newline="", encoding="utf-8-sig") as sample_file:
        reader = csv.DictReader(sample_file)
        headers = reader.fieldnames or []
        rows = list(reader)
        listings = [
            row for row in rows
            if not FORBIDDEN_PATTERN.search(row.get("Title", "") or "")
        ]
        data = [
            [row.get(header, "") or "" for header in headers]
            for row in listings
        ]

    return render_template("index.html", headers=headers, data=data, listings=listings)


if __name__ == "__main__":
    app.run(debug=False)