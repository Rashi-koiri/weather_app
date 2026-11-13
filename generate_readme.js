/**
 * SkySimple Weather App - Automated README.md Generator (Node.js)
 * Run: node generate_readme.js
 */

const fs = require('fs');
const path = require('path');

const readmePath = path.join(__dirname, 'README.md');

const content = `# ⛅ SkySimple Weather App

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
- [License](#-license)

---

## 🌟 Overview
**SkySimple** provides accurate atmospheric data in an elegant, distraction-free interface. Designed to look clean across desktop and mobile screens, it offers immediate current conditions, 24-hour hourly projections, and extended 5-day / 7-day outlooks.

---

## 🚀 Key Features
- **⚡ Real-Time Meteorological Data**: Live temperature, feels like, humidity %, wind speed & direction, pressure, visibility, precipitation, and UV index.
- **🔍 Smart Global City Search**: Instant debounced search with live geocoding suggestions.
- **📍 GPS Geolocation**: Instant local weather via browser GPS coordinates.
- **📅 5-Day & 7-Day Forecasts**: Visual high/low indicators with weather art.
- **🕒 24-Hour Hourly Timeline**: Interactive hourly temperature slider.
- **⭐ Saved Places**: Bookmark favorite cities with localStorage persistence.
- **🌡️ Unit Conversion**: 1-click switcher between Celsius (°C) and Fahrenheit (°F).
- **🔑 Dual API Support**: Open-Meteo (zero key required) + OpenWeatherMap (custom key support with auto-fallback).

---

## 📁 Project Architecture
\`\`\`text
skysimple-weather-app/
├── index.html           # Main semantic HTML5 markup & dashboard views
├── style.css            # Responsive CSS3 styling, grid layouts & animations
├── app.js               # Application state, API fetchers, SVG icons & DOM engine
├── generate_readme.py   # Python script to regenerate this documentation
├── generate_readme.js   # Node.js script to regenerate this documentation
└── README.md            # Comprehensive project documentation
\`\`\`

---

## 💻 Getting Started
Simply double-click \`index.html\` to open the app directly in any web browser!

---

## 📄 License
This project is licensed under the **MIT License**.
`;

fs.writeFileSync(readmePath, content.trim() + '\n', 'utf8');
console.log('✅ Successfully generated README.md at: ' + readmePath);
