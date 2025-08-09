# 🚰 Community Water Quality Analysis Tool  

An interactive, bilingual (English & Tamil) web-based application for monitoring and evaluating the safety of local water sources. Built with **Streamlit**, the tool compares user-provided water quality parameters with **WHO** and **BIS** standards to determine potability and provide actionable feedback.  

CHECK IT OUT HERE - [Potabl.](https://potabl.streamlit.app/)

---

## 📜 Features  
- **Water Quality Assessment** – Instant evaluation of water safety based on pH, TDS, turbidity, hardness, chloride, and more.  
- **Bilingual Support** – Fully functional in both **English** and **Tamil** to reach rural and underserved communities.  
- **CSV Export** – Download test results for record-keeping or sharing with authorities.  
- **Awareness & Education** – Integrated article on the importance of clean water and safe consumption practices.  

---

## 🛠 Tools & Technologies  
- **Python** – Core programming language  
- **Streamlit** – Web application framework  
- **Pandas** – Data processing and CSV export  
- **JSON** – Language translation and configuration  

## 📦 Installation  

1. **Clone the Repository**  
```bash
git clone https://github.com/samgabrielbilshan/water-quality-analysis-tool.git
cd water-quality-analysis-tool
```

2. **Create a Virtual Environment (Optional but Recommended)**
```bash
python -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate      # On Windows
```

3. Install Dependencies
```bash
pip install -r requirements.txt
```

4. Run the Application
```bash
streamlit run Home.py
```


References
---
1.	World Health Organization (WHO) – Guidelines for drinking-water quality: fourth edition incorporating the first and second addenda. World Health Organization, Geneva, 2022. https://www.who.int/publications/i/item/9789240045064
2.	Bureau of Indian Standards (BIS) – IS 10500: 2012 – Drinking Water Specification. Bureau of Indian Standards, New Delhi, 2012. https://cpcb.nic.in/wqm/BIS_Drinking_Water_Specification.pdf
3.	Streamlit Documentation – Streamlit: The fastest way to build data apps in Python. https://docs.streamlit.io/
4.	Pandas Documentation – Python Data Analysis Library. https://pandas.pydata.org/docs/
5.	Python Software Foundation – Python Programming Language. https://www.python.org/




> This project was done under 1M1B - Green Internship Batch-4
