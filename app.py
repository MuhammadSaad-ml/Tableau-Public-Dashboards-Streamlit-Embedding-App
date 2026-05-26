import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Tableau Dashboards",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Tableau Public Dashboards")
st.markdown("---")

# Dashboard configurations
DASHBOARDS = {
    "Sales Dashboard": {
        "url": "https://public.tableau.com/views/SalesDashboardUsingSampleSuperstore_17111719024770/SalesDashboard",
        "description": "Sales performance dashboard using Sample Superstore data.",
        "height": 800,
    },
    "HR Dashboard": {
        "url": "https://public.tableau.com/views/HrDashboardBySaad/Dashboard1",
        "description": "HR analytics dashboard by Saad.",
        "height": 800,
    },
}

def embed_tableau(url: str, height: int = 800):
    """Embed a Tableau Public dashboard using the JavaScript embed API."""
    html = f"""
    <div style="width:100%; overflow:hidden;">
        <script type="module" src="https://public.tableau.com/javascripts/api/tableau.embedding.3.latest.min.js"></script>
        <tableau-viz
            src="{url}"
            width="100%"
            height="{height}px"
            toolbar="bottom"
            hide-tabs>
        </tableau-viz>
    </div>
    """
    components.html(html, height=height + 20, scrolling=False)


# Sidebar navigation
st.sidebar.title("Navigation")
selected = st.sidebar.radio(
    "Select a Dashboard",
    list(DASHBOARDS.keys()),
    index=0
)

st.sidebar.markdown("---")
st.sidebar.markdown("### About")
st.sidebar.info(
    "This app embeds Tableau Public dashboards using Streamlit. "
    "Select a dashboard from the menu to explore the data."
)

# Render selected dashboard
dash = DASHBOARDS[selected]
st.header(selected)
st.caption(dash["description"])

with st.spinner("Loading dashboard..."):
    embed_tableau(dash["url"], height=dash["height"])

st.markdown("---")
st.markdown(
    "<p style='text-align:center; color:grey; font-size:0.85rem;'>"
    "Powered by Tableau Public &amp; Streamlit"
    "</p>",
    unsafe_allow_html=True,
)
