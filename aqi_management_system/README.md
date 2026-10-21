# Air Quality Management System (India)

A Streamlit web app with:

* **Home dashboard** - live AQI of 60+ Indian cities, most/least polluted, map, filterable table
* **City AQI Search** - type to search any city: AQI gauge, pollutant levels, 7-day trend, health advice
* **About AQI** - what AQI is, categories, pollutants, causes, health effects, myths
* **Ways to Reduce AQI** - actions for individuals, homes, transport, industry, agriculture, government,
  plus advice for each AQI level

AQI is computed with the **Indian National AQI (CPCB)** breakpoints.
Live data comes from the free Open-Meteo Air Quality API (no API key needed).
If there is no internet, the app falls back to clearly labelled sample data.

## Run

```bash
python -m venv venv
venv\Scripts\activate        # Windows      (Mac/Linux: source venv/bin/activate)
pip install -r requirements.txt
streamlit run app.py
```

## Structure

```
aqi_management_system/
├── app.py                         # Home dashboard
├── pages/
│   ├── 1_🔍_City_AQI_Search.py
│   ├── 2_📘_About_AQI.py
│   └── 3_🌱_Ways_to_Reduce_AQI.py
├── utils/
│   ├── data.py                    # list of Indian cities
│   ├── aqi.py                     # CPCB AQI calculation + health advice
│   └── live.py                    # live API + offline fallback
├── .streamlit/config.toml
├── requirements.txt
└── README.md
```

## Add a city
Add a row `(name, state, latitude, longitude, typical_aqi)` to `CITIES` in `utils/data.py`.
