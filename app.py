
import streamlit as st
import easyocr
import pandas as pd
from PIL import Image
import numpy as np
import os
from datetime import datetime

st.set_page_config(page_title="Expense Tracker", layout="centered")

st.title("📤 Receipt Analyzer & Expense Tracker")

uploaded_file = st.file_uploader("Upload a receipt (image or screenshot)", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Receipt", use_column_width=True)

    with st.spinner("🔍 Reading and analyzing..."):
        reader = easyocr.Reader(['en', 'ar'])
        # ✅ FIX: Convert PIL image to numpy array before passing to EasyOCR
        results = reader.readtext(np.array(image))

        # Extracted text lines
        extracted_text = [res[1] for res in results]
        st.subheader("📄 Extracted Text:")
        for line in extracted_text:
            st.write("- " + line)

        # Look for amount
        amount = None
        for line in extracted_text:
            if "EGP" in line:
                try:
                    amount = float(line.split("EGP")[-1].strip().replace(",", ""))
                    break
                except:
                    continue

        # Auto-classification: look for keywords
        keywords = {
            "trip": "Transportation",
            "fare": "Transportation",
            "taxi": "Transportation",
            "gas": "Fuel",
            "electricity": "Utilities",
            "grocery": "Groceries",
            "fruit": "Groceries"
        }

        expense_type = "Uncategorized"
        for line in extracted_text:
            for key in keywords:
                if key.lower() in line.lower():
                    expense_type = keywords[key]
                    break
            if expense_type != "Uncategorized":
                break

        st.subheader("🧠 Auto-categorized as:")
        st.success(f"{expense_type}")

        # Save to Excel
        if amount:
            save_button = st.button("💾 Save to Excel")

            if save_button:
                filename = "expenses_log.xlsx"
                if os.path.exists(filename):
                    df = pd.read_excel(filename)
                else:
                    df = pd.DataFrame(columns=["Date", "Item", "Amount", "Category", "Source"])

                new_row = {
                    "Date": datetime.now().strftime("%Y-%m-%d %H:%M"),
                    "Item": "Auto Extracted",
                    "Amount": amount,
                    "Category": expense_type,
                    "Source": uploaded_file.name
                }

                df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
                df.to_excel(filename, index=False)
                st.success("✅ Saved to Excel file!")
        else:
            st.error("❗ Could not find a valid amount in the receipt.")
