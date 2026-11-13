"""
SkySimple Weather App - Automated README.md Generator
Run this script to automatically generate or update the project README.md file:
    python generate_readme.py
"""

import os
from datetime import datetime

PROJECT_NAME = "SkySimple Weather App"
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
README_PATH = os.path.join(PROJECT_DIR, "README.md")

README_CONTENT = f"""# ⛅ {PROJECT_NAME}

> A sleek, responsive real-time weather forecasting web application with live global city search, GPS geolocation, customizable API providers, and multi-day meteorological insights.

![SkySimple App Preview](https://img.shields.io/badge/Status-Complete-success?style=for-the-badge)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![License](https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge)

---

## 📖 Table of Contents
- [Overview](#-overview)
- [Key Features](#-key-features)
- [Visual Design & UI](#-visual-design--ui)
- [Weather APIs & Keys](#-weather-apis--keys)
- [Project Architecture](#-project-architecture)
- [Getting Started](#-getting-started)
- [How It Works](#-how-it-works)
- [Customization & Settings](#-customization--settings)
- [License](#-license)

---

## 🌟 Overview

**SkySimple** provides accurate atmospheric data in an elegant, distraction-free interface. Designed to look clean across desktop and mobile screens, it offers immediate current conditions, 24-hour hourly projections, and extended 5-day / 7-day outlooks.

---

## 🚀 Key Features

- **⚡ Real-Time Meteorological Data**:
  - Live temperature & "Feels Like" temperature index
  - Humidity percentage, Wind speed & 8-point compass direction (NW, SE, etc.)
  - Atmospheric surface pressure (hPa), Visibility (km), and Precipitation (mm)
  - UV Index rating with sun exposure recommendations

- **🔍 Smart Global City Search**:
  - Live debounced autocomplete using the Open-Meteo Geocoding database.
  - Search any city, state, province, or country worldwide.

- **📍 GPS Geolocation**:
  - One-click *Current Location* button using HTML5 Geolocation and reverse geocoding.

- **📅 Multi-Day & Hourly Forecasts**:
  - **5-Day Daily Outlook**: High and low temperature indicators with corresponding weather conditions.
  - **24-Hour Hourly Slider**: Interactive timeline of upcoming temperatures.
  - **7-Day Extended View**: Full week breakdown with temperature progress ranges.

- **⭐ Saved Places (Bookmarks)**:
  - Bookmark favorite cities with mini weather preview cards.
  - State saved to browser `localStorage` for instant return access.

- **🌡️ Unit Conversion**:
  - Instant one-click toggle between Celsius (°C) and Fahrenheit (°F).

- **🔑 Dual API Provider Support**:
  - **Open-Meteo (Default)**: Completely free, 0 config, no API key required, zero rate limits.
  - **OpenWeatherMap (Optional)**: Support for custom personal API keys with automatic graceful fallback.

---

## 🎨 Visual Design & UI

- **Palette**: Soft daylight sky gradients (`#eaf2fc` to `#e1effe`) with crisp white card containers.
- **Glassmorphism & Shadows**: Elevated floating cards with soft border radii (`24px`).
- **Dynamic Weather Graphics**: Custom SVG illustrations for all weather conditions (Sunny, Partly Cloudy, Overcast, Rain, Snow, Thunderstorm, Fog).
- **Responsive Layout**:
  - **Desktop**: Left persistent navigation sidebar, spacious dashboard grid.
  - **Mobile**: Collapsible layout with bottom mobile tab bar matching native app standards.

---

## 🔑 Weather APIs & Keys

| Provider | Key Required? | Status | Best For |
| :--- | :---: | :---: | :--- |
| **Open-Meteo API** | ❌ No | Active (Default) | Instant out-of-the-box global weather |
| **OpenWeatherMap** | ✔️ Yes (Optional) | Supported | Users with their own custom OWM accounts |

### Setting Up a Custom Key:
1. Open the app and click **API Settings** (or the profile icon in the top right).
2. Select **OpenWeatherMap API**.
3. Paste your 32-character API key from [OpenWeatherMap](https://home.openweathermap.org/users/sign_up).
4. Click **Save & Apply**.

> [!NOTE]
> If your OpenWeatherMap key is invalid or reaches its quota, SkySimple will automatically fall back to Open-Meteo so your app never stops working.

---

## 📁 Project Architecture

```text
skysimple-weather-app/
│
├── index.html           # Main semantic HTML5 markup & dashboard views
├── style.css            # Responsive CSS3 styling, grid layouts & animations
├── app.js               # Application state, API fetchers, SVG icons & DOM engine
├── generate_readme.py   # Python script to regenerate this documentation
├── generate_readme.js   # Node.js script to regenerate this documentation
└── README.md            # Comprehensive project documentation
```

---

## 💻 Getting Started

### Method 1: Direct Browser Launch
No build steps or dependencies required. Double-click `index.html` or run in terminal:

```bash
# Windows PowerShell
Start-Process index.html

# macOS
open index.html

# Linux
xdg-open index.html
```

### Method 2: Local HTTP Server (Optional)
```bash
# Using Python
python -m http.server 8080

# Using Node.js (npx)
npx serve
```
Then navigate to `http://localhost:8080` in your web browser.

---

## ⚙️ How It Works

```mermaid
flowchart TD
    User([User Enters City or Clicks GPS]) --> Action{{"Action Type"}}
    Action -- Search Input --> Geo[Open-Meteo Geocoding API]
    Action -- GPS Click --> HTML5[Browser Navigator Geolocation]
    Geo --> Coords[Obtain Latitude & Longitude]
    HTML5 --> Coords
    Coords --> ProviderCheck{{"Check Selected Provider"}}
    ProviderCheck -- Open-Meteo (Default) --> OM[Fetch Open-Meteo Forecast API]
    ProviderCheck -- OpenWeatherMap --> OWM[Fetch OpenWeatherMap 2.5 API]
    OWM -- If Error / Expired --> OM
    OM --> Parse[Parse Temperature, Wind, Daily & Hourly]
    Parse --> Render[Render SkySimple Dashboard & Forecast]
```

---

## 📄 License

This project is licensed under the **MIT License**. Free to use, modify, and distribute.

---

*Generated automatically on {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}*
"""

def generate():
    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(README_CONTENT.strip() + "\n")
    print(f"[OK] Successfully generated README.md at: {README_PATH}")

if __name__ == "__main__":
    generate()
