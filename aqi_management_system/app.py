"""Air Quality Management System - Home / Dashboard"""
import plotly.express as px
import streamlit as st

from utils import aqi as A
from utils import live

st.set_page_config(page_title="Air Quality Management System", page_icon="🌫️", layout="wide")

st.sidebar.header("Settings")
use_live = st.sidebar.toggle("Use live data", value=True,
                             help="Fetches real-time data from Open-Meteo. Turn off to use offline sample data.")
st.session_state["use_live"] = use_live

st.title("🌫️ Air Quality Management System")
st.caption("Indian National AQI (CPCB scale) for cities across India")

with st.spinner("Loading air quality for all cities..."):
    df = live.current_all(use_live)

if (df["Source"] == "Sample").any():
    st.warning("Some or all values are **sample data** (live API not reachable). "
               "They are for demonstration only, not real measurements.")

worst = df.loc[df["AQI"].idxmax()]
best = df.loc[df["AQI"].idxmin()]
c1, c2, c3, c4 = st.columns(4)
c1.metric("Cities tracked", len(df))
c2.metric("National average AQI", int(df["AQI"].mean()))
c3.metric("Most polluted", f"{worst['City']}", f"AQI {worst['AQI']}", delta_color="off")
c4.metric("Cleanest", f"{best['City']}", f"AQI {best['AQI']}", delta_color="off")

st.divider()
left, right = st.columns(2)
colour_map = {name: colour for _, _, name, colour, _ in A.BANDS}

with left:
    st.subheader("🔴 10 most polluted cities")
    top = df.sort_values("AQI", ascending=False).head(10).sort_values("AQI")
    fig = px.bar(top, x="AQI", y="City", orientation="h", color="Category",
                 color_discrete_map=colour_map, text="AQI")
    fig.update_layout(height=400, margin=dict(l=0, r=0, t=10, b=0), legend_title_text="")
    st.plotly_chart(fig, width="stretch")

with right:
    st.subheader("🟢 10 cleanest cities")
    low = df.sort_values("AQI").head(10).sort_values("AQI", ascending=False)
    fig = px.bar(low, x="AQI", y="City", orientation="h", color="Category",
                 color_discrete_map=colour_map, text="AQI")
    fig.update_layout(height=400, margin=dict(l=0, r=0, t=10, b=0), legend_title_text="")
    st.plotly_chart(fig, width="stretch")

st.subheader("🗺️ Map of Indian cities")
fig = px.scatter_geo(df, lat="Lat", lon="Lon", color="Category", size="AQI",
                     hover_name="City", hover_data={"AQI": True, "State": True, "Lat": False, "Lon": False},
                     color_discrete_map=colour_map, scope="asia")
fig.update_geos(lataxis_range=[6, 37], lonaxis_range=[67, 98], showcountries=True,
                countrycolor="#999", showland=True, landcolor="#f3f3f3")
fig.update_layout(height=520, margin=dict(l=0, r=0, t=0, b=0), legend_title_text="")
st.plotly_chart(fig, width="stretch")

st.subheader("📋 All cities")
states = ["All states"] + sorted(df["State"].unique())
f1, f2 = st.columns([1, 2])
state = f1.selectbox("Filter by state", states)
q = f2.text_input("Search city", placeholder="Type a city name...")
view = df if state == "All states" else df[df["State"] == state]
if q:
    view = view[view["City"].str.contains(q, case=False)]
st.dataframe(view[["City", "State", "AQI", "Category", "Main pollutant", "Source"]]
             .sort_values("AQI", ascending=False).reset_index(drop=True),
             width="stretch", hide_index=True)

st.info("👈 Use the sidebar pages for **City AQI Search**, **About AQI** and **Ways to Reduce AQI**.")
