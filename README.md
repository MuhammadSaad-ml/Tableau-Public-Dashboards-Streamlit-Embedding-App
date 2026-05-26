<img src="https://img.shields.io/badge/Framework-Streamlit-yellow"> <img src="https://img.shields.io/badge/Build_with-Python-red"> <img src="https://img.shields.io/badge/Webapp-Interactive-purple"> <img src="https://img.shields.io/badge/Data_Viz-Tableau_Public-blue"> <img src="https://img.shields.io/badge/Embedding_API-v3-brightgreen"> <img src="https://img.shields.io/badge/Open_Source-Yes-brightgreen"> <img src="https://img.shields.io/badge/Beginner_Friendly-Yes-blue"> <img src="https://img.shields.io/badge/End--to--End-Dashboard_Project-gold">

<img src="https://img.shields.io/badge/Sales-Analytics-orange"> <img src="https://img.shields.io/badge/HR-Analytics-hotpink"> <img src="https://img.shields.io/badge/Market-Analytics-teal">

<img src="https://img.shields.io/badge/Streamlit_Components-HTML_Embed-f7931e"> <img src="https://img.shields.io/badge/Tableau-Public_Dashboards-3f4f75"> <img src="https://img.shields.io/badge/Toolbar-Hidden-lightgrey">

<img src="https://img.shields.io/badge/VS_Code-IDE-blueviolet"> <img src="https://img.shields.io/badge/Anaconda-Environment-a8b59c">

---

# 📊 Tableau Public Dashboards — Streamlit Embedding App

This repository contains an interactive **Tableau Dashboard Viewer** built using **Streamlit**.

The application embeds **live Tableau Public dashboards** directly in the browser using the modern **Tableau Embedding API v3**, covering three real-world analytics domains:

- 💼 **Sales Dashboard** — Sales performance analysis using Sample Superstore data
- 👥 **HR Dashboard** — Human resources analytics by Saad
- 📈 **Market Dashboard** — Market KPI overview and performance metrics

The project demonstrates how to integrate **Tableau Public visualizations** into a clean, navigable **Streamlit web application** — deployable for free on Streamlit Community Cloud.

---

## ▶ Click On Image To Open App

[![Tableau Streamlit App](https://public.tableau.com/static/images/Sa/SalesDashboardUsingSampleSuperstore_17111719024770/SalesDashboard/1.png)](https://share.streamlit.io)

---

## ✨ Features

### 🗂 Multi-Dashboard Navigation
- Sidebar navigation to switch between **3 dashboards** instantly
- Each dashboard loads with its own title and description

### 📊 Live Tableau Embeds
- Dashboards streamed directly from **Tableau Public** — always up to date
- No static screenshots — fully interactive charts, filters, and tooltips

### 💼 Sales Dashboard
Explores sales performance across:
- Product categories & sub-categories
- Regional sales trends
- Profitability analysis

### 👥 HR Dashboard
Analyses workforce metrics including:
- Headcount and department breakdowns
- Employee performance indicators
- Attrition and retention insights

### 📈 Market Dashboard
Covers market KPI metrics including:
- KPI overview and benchmarks
- Market performance trends
- Business intelligence reporting

### 🔒 Toolbar Hidden
- Download, share, and data buttons are **not visible** to viewers
- Clean, distraction-free embed experience
- Users can interact with filters and tooltips only

### ⚡ Modern Embedding
- Uses **Tableau Embedding API v3** (`<tableau-viz>` web component)
- No deprecated iframes — clean, responsive, and future-proof

### ☁️ One-Click Cloud Deployment
- Deployable to **Streamlit Community Cloud** for free
- Minimal dependencies — only `streamlit` required

---

## 📁 Project Structure

```text
tableau-streamlit/
│
├── app.py                # Main Streamlit application
├── requirements.txt      # Python dependencies
├── .gitignore            # Git ignore rules
└── README.md             # Project documentation
```

---

## 📄 File Description

### `app.py`
Main Streamlit application file containing:
- Sidebar navigation between dashboards
- Tableau Embedding API v3 HTML component
- Dashboard metadata (URL, title, description, height)
- Toolbar hidden configuration
- Responsive layout configuration

> Easily extendable — add new dashboards by adding entries to the `DASHBOARDS` dictionary.

---

### `requirements.txt`
Includes:
- Streamlit

> No additional dependencies required — Tableau embed is handled via a browser-side JavaScript API.

---

## 🚀 Run Locally

### 1. Clone the repo
```bash
git clone https://github.com/MuhammadSaad-ml/Tableau-Public-Dashboards-Streamlit-Embedding-App.git
cd Tableau-Public-Dashboards-Streamlit-Embedding-App
```

### 2. Create a virtual environment (recommended)
```bash
python -m venv venv
source venv/bin/activate        # macOS/Linux
venv\Scripts\activate           # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the app
```bash
streamlit run app.py
```

Then open [http://localhost:8501](http://localhost:8501) in your browser.

---

## ☁️ Deploy to Streamlit Community Cloud (Free)

1. Push this repo to **GitHub**
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Click **New app** → select your repo → set `app.py` as the main file
4. Click **Deploy** — done!

---

## ➕ Adding More Dashboards

Open `app.py` and add a new entry to the `DASHBOARDS` dictionary:

```python
DASHBOARDS = {
    "My New Dashboard": {
        "url": "https://public.tableau.com/views/YOUR_WORKBOOK/YOUR_VIEW",
        "description": "A short description shown under the title.",
        "height": 800,
    },
    # ... existing dashboards
}
```

The sidebar navigation updates **automatically** — no other changes needed.

To find your Tableau Public URL, take the `host_url` + `name` params from the embed code Tableau generates.

---

## 🔄 How the Embedding Works

1. Tableau Public hosts your viz at a public URL
2. Streamlit renders an HTML component using `streamlit.components.v1`
3. The **Tableau Embedding API v3** (`<tableau-viz>` web component) loads the viz inline
4. `toolbar="hidden"` removes all download and share buttons
5. The dashboard is fully interactive — filters, tooltips, and drill-downs all work

---

## 🕒 Version History

- **Initial Commit** — Base Streamlit app with two Tableau dashboard embeds
- **Market Dashboard Added** — Third dashboard (Market KPI Overview) included
- **Toolbar Hidden** — Download and share buttons removed from all embeds
- **README Updated** — Documentation updated to reflect all changes

---

## ℹ Notes
- Dashboards must be published to **Tableau Public** for this embed method to work
- Ensure your Tableau viz URL matches the `name` param from the embed code exactly
- The app is best viewed on a **widescreen layout** — set in `st.set_page_config`
- Even with toolbar hidden, the underlying Tableau Public URL remains publicly accessible

---

## 👤 Author

**Muhammad Saad**  
Data Analyst & Data Scientist 📊
