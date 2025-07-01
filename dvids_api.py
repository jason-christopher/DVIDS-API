import requests
import pandas as pd
import time
from dotenv import load_dotenv
import os

# --- LOAD .ENV ---
load_dotenv()

API_KEY = os.getenv("API_KEY")

# -------------------------
# 1. Get the initial search data
# -------------------------
names_to_search = ["Haden+Tolbert", "Cambrie+Cannon", "Kayla+Christopher", "Brooklyn+Clark", "Anthony+Jones"]
all_records = []

for name in names_to_search:
    print(f"Searching for: {name}")
    params = {
        "credit": name,
        "from_date": "2024-09-01T12:00:00Z",
        "api_key": API_KEY,
    }
    response = requests.get("https://api.dvidshub.net/search", params=params)
    data = response.json()

    if "results" in data:
        for item in data["results"]:
            all_records.append({
                "id": item.get("id"),
                "credit": item.get("credit"),
                "url": item.get("url"),
                "publishdate": item.get("publishdate"),
                "title": item.get("title"),
                "type": item.get("type"),
            })
    time.sleep(1)

df1 = pd.DataFrame(all_records)

# -------------------------
# 2. Get detailed asset data
# -------------------------
detailed_records = []

for vid_id in df1["id"].unique():
    print(f"Fetching details for ID: {vid_id}")
    asset_url = "https://api.dvidshub.net/asset"
    params = {
        "id": vid_id,
        "fields": "credit,views,title",
        "api_key": API_KEY,
    }
    response = requests.get(asset_url, params=params)
    data = response.json()
    result = data.get("results", {})

    title = result.get("title", "")
    views = result.get("views", "")
    credit_list = result.get("credit", [])

    for person in credit_list:
        detailed_records.append({
            "id": vid_id,
            "title": title,
            "name": person.get("name", ""),
            "views": views,
        })
    time.sleep(1)

df2 = pd.DataFrame(detailed_records)

# -------------------------
# 3. Outer join on `id`
# -------------------------
final_df = df2.merge(df1, how="outer", on=["id", "title"])
final_df = final_df.drop_duplicates()

# -------------------------
# 4. Save to Excel
# -------------------------
output_file = "joined_data.xlsx"
final_df.to_excel(output_file, index=False)
print(f"\nSaved joined data to {output_file}")
