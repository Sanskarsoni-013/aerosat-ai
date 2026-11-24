# AeroSat AI: Earth Observation, Orbital Mechanics & Satellite Geospatial ML Platform

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.0%2B-EE4C2C.svg)](https://pytorch.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100%2B-009688.svg)](https://fastapi.tiangolo.com/)
[![Web Deployment](https://img.shields.io/badge/Live%20Platform-stringstrange.online-22c55e.svg)](https://www.stringstrange.online)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

**AeroSat AI** is an open-source, production-grade geospatial intelligence and satellite orbital mechanics framework. It combines real-time SGP4 Keplerian orbital propagation with deep learning computer vision on multi-spectral satellite imagery (Sentinel-2, Landsat-9, MODIS, and VIIRS).

🌐 **Interactive Live Web Platform:** [https://www.stringstrange.online](https://www.stringstrange.online)

---

## 🌟 Key Capabilities

### 1. 🛰️ Real-Time SGP4 Orbital Tracking & Telemetry
- Computes instantaneous satellite state vectors (position $\vec{r}$, velocity $\vec{v}$) from Two-Line Element (TLE) ephemeris data using SGP4/SDP4 perturbation models.
- Real-time ground track visualization, sub-satellite footprint computation, and next-overhead-pass azimuth/elevation prediction for:
  - **ISS (Zarya)**: International Space Station
  - **Landsat-9**: NASA/USGS Earth Observation
  - **Sentinel-2A**: European Space Agency Copernicus Constellation
  - **Terra (EOS AM-1)**: NASA MODIS Instrument
  - **NOAA-20 / Suomi NPP**: Day/Night Radiometry & Thermal Infrared
  - **Starlink Constellation Fleet**

### 2. 🧠 Multi-Spectral Deep Learning Computer Vision
- **Normalized Difference Vegetation Index (NDVI)**:
  $$\text{NDVI} = \frac{\text{NIR (Band 8)} - \text{Red (Band 4)}}{\text{NIR (Band 8)} + \text{Red (Band 4)}}$$
  Pixel-wise vegetation health segmentation, canopy biomass density scoring, and temporal deforestation rate calculation.
- **Thermal Infrared Anomaly & Wildfire Detection**:
  Thermal gradient anomaly modeling on MODIS/VIIRS 3.9µm and 11µm channels to compute **Fire Radiative Power (FRP)** in Megawatts and predict active fire spread vectors.
- **Deep Land Cover Semantic Segmentation (U-Net)**:
  5-class high-resolution surface classification: Dense Forest, Agriculture, Urban/Impervious, Water Bodies, and Barren Soil.
- **Atmospheric Cloud Masking & Optical Depth Filter**:
  Isolates high-altitude cirrus scattering and ground shadows to deliver standardized surface reflectance.

---

## 📁 Repository Structure

```text
aerosat-ai/
│
├── api/
│   └── server.py                  # High-performance FastAPI geospatial inference server
│
├── orbit/
│   ├── sgp4_propagator.py         # SGP4 Keplerian orbital mechanics engine
│   └── pass_predictor.py          # Ground station pass & Doppler shift calculator
│
├── model/
│   ├── train_ndvi_unet.py         # PyTorch U-Net for multispectral land cover segmentation
│   └── thermal_anomaly_detector.py# Machine learning wildfire and heat signature model
│
├── data/                          # Sample multispectral TIF/Numpy matrices
│
├── requirements.txt               # Dependencies
├── .gitignore
└── README.md
```

---

## ⚡ Quick Start

### 1. Clone & Install
```bash
git clone https://github.com/Sanskarsoni-013/aerosat-ai.git
cd aerosat-ai
pip install -r requirements.txt
```

### 2. Compute Real-Time Satellite Pass & Orbit State
```bash
python orbit/sgp4_propagator.py --satellite ISS
```

### 3. Run Multispectral NDVI & Thermal ML Inference
```bash
python model/thermal_anomaly_detector.py
```

### 4. Explore the Interactive Web Platform
Visit [https://www.stringstrange.online](https://www.stringstrange.online) to explore real-time orbital maps, multispectral satellite scene analyses, and live inference controls.

---

## 👤 Author
- **Sanskar Soni** - [LinkedIn](https://linkedin.com/in/sanskar-soni-669382311) • [GitHub](https://github.com/Sanskarsoni-013)
