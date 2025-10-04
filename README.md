# CORD-19 Research Dataset Analysis

This project provides a basic analysis of the CORD-19 research dataset and a simple Streamlit web application for exploration.  
It was developed as part of a data analysis assignment.  

---

## 📂 Project Structure

CORD19-Analysis/
│── CORD19_Analysis.ipynb # Jupyter Notebook with analysis
│── app.py # Streamlit web application
│── metadata_sample.csv # Sample dataset (5000 rows)
│── README.md # Project documentation

yaml
Copy code

---

## 📊 Dataset

The original dataset is from [CORD-19](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge) and contains COVID-19 research papers metadata.  
- The full **metadata.csv** is ~1.65 GB (too large for GitHub).  
- This repository uses a smaller **sample file (`metadata_sample.csv`)** with **5000 rows** for demonstration.  

➡️ To use the full dataset:  
1. Download it from Kaggle.  
2. Place `metadata.csv` in the project directory.  
3. Update your code to load `metadata.csv` instead of `metadata_sample.csv`.  

---

## ⚙️ Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/your-username/CORD19-Analysis.git
cd CORD19-Analysis
2. Install dependencies
Make sure you have Python 3.8+ installed, then run:

bash
Copy code
pip install pandas numpy matplotlib seaborn jupyter streamlit
3. Run the Jupyter Notebook
bash
Copy code
jupyter notebook CORD19_Analysis.ipynb
4. Run the Streamlit App
bash
Copy code
streamlit run app.py
🚀 Features
Load and explore metadata sample (titles, authors, journals, publication years).

Basic statistics and visualization in Jupyter Notebook.

Interactive search and filtering with Streamlit app.

📌 Notes
This project demonstrates working with a large dataset by sampling.

All results are based on the sample (metadata_sample.csv).

