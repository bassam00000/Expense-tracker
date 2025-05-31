
# 📊 Expense Tracker App

Track and categorize your household spending automatically by uploading receipts (images or PDFs). The app uses OCR to read receipts in English and Arabic, then classifies the expense and logs it into an Excel file.

---

## 🚀 Features

- 📸 Upload image or screenshot of any receipt (supports JPG, PNG)
- 📄 Extracts text using OCR (EasyOCR)
- 🧠 Auto-categorizes expense type (e.g. Transportation, Utilities)
- 💾 Saves data into an Excel log file
- 📊 Future-ready for charts & reports

---

## 🛠 How to Run on Streamlit Cloud

1. Fork or clone this repository
2. Go to [https://streamlit.io/cloud](https://streamlit.io/cloud)
3. Click **"New App"**
4. Select:
   - **Repository:** this repo
   - **Branch:** `main`
   - **Main file:** `app.py`
5. Click **"Deploy"** — you're done!

---

## 📦 Required Libraries

Streamlit Cloud will install these from `requirements.txt` automatically:

```
streamlit
easyocr
pandas
openpyxl
Pillow
```

---

## 📁 Output

Each saved receipt will be logged to a file named:

```
expenses_log.xlsx
```

Containing columns:
- Date
- Item
- Amount
- Category
- Source (file name)

---

## 📧 Support

Feel free to open an issue or contact the developer if you'd like to contribute, suggest a feature, or report a bug.
