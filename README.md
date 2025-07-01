# DVIDS Asset Scraper

This Python script searches the [DVIDS API](https://www.dvidshub.net) for assets credited to a list of names, fetches detailed asset information, joins the data into a single table, and saves the results to an Excel file.

---

## 🚀 What it does

- Searches for media (videos, photos, etc.) credited to specific people using the DVIDS API.
- Retrieves:
  - `id`
  - `credit`
  - `url`
  - `publishdate`
  - `title`
  - `type`
- Then for each asset ID, it fetches detailed metadata (individual names credited and view counts).
- Merges this data into a single Excel file.

---

## 🔧 Setup

### 1. Clone or download
Place the script in your working directory.

### 2. Create a virtual environment
Recommended: use a hidden `.venv` folder.

```bash
python -m venv .venv
```

Activate it with:

- **macOS/Linux:**
  ```bash
  source .venv/bin/activate
  ```
- **Windows CMD:**
  ```cmd
  .venv\Scripts\activate
  ```
- **Windows PowerShell:**
  ```powershell
  .venv\Scripts\Activate.ps1
  ```

### 3. Install required packages

```bash
pip install pandas requests openpyxl python-dotenv
```

---

## 🔑 .env file

Create a `.env` file in the same directory as your script, and add your DVIDS API key:

```
API_KEY=your_api_key_here
```

(If the API doesn’t actually require the key for your calls, it will still run, but this keeps it configurable.)

---

## ▶️ Run the script

Inside your activated virtual environment, simply run:

```bash
python your_script.py
```

It will:

✅ Search for all names specified in `names_to_search`  
✅ Fetch and join asset data  
✅ Save everything into:

```
joined_data.xlsx
```

in the current directory.

---

## 📝 Output format

The Excel file includes columns like:

| id         | title                                     | name           | views | credit                                 | url              | publishdate          | type  |
|------------|-------------------------------------------|----------------|-------|----------------------------------------|-------------------|-----------------------|-------|
| video:1234 | Oklahoma Guardsmen face off against drones| Haden Tolbert  | 328   | SPC Cambrie Cannon and SGT Haden Tolbert| https://...       | 2025-06-18T20:28:53Z | video |

---

## ⚠️ Notes

- Each run **overwrites `joined_data.xlsx`**.
- Includes a `time.sleep(1)` to avoid hammering the DVIDS API.

---

## ✅ License

MIT or your preferred license.

---

## 🙌 Credits

Built by Jason Christopher to automate DVIDS media pulls.
