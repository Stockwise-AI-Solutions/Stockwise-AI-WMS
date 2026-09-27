# Stockwise-AI-WMS

**Organization:** Stockwise-AI-Solutions
**Module:** Business Analysis 3.2 Capstone
**Theme:** AI Solution for Industries

## Project Overview
Stockwise-AI-WMS is an intelligent warehouse management system designed for the Emfuleni Municipality. It leverages machine learning to optimise warehouse operations, including demand forecasting, anomaly detection for theft prevention, and intelligent slotting.

## Features
- **Demand Forecasting:** Uses Linear Regression to predict future stock requirements.
- **Anomaly Detection:** Uses Isolation Forest to identify suspicious picking times (potential theft).
- **Intelligent Slotting:** Uses K-Means clustering to arrange stock based on popularity and demand.
- **Chatbot Interface:** Provides a simple NLP bot for quick stock queries.
- **Dashboard:** A Streamlit web app for real-time tracking and AI alerts.

## Repository Structure
- `app.py`: Streamlit dashboard code.
- `src/stockwise_ai.py`: Main AI script (Forecasting, Anomaly Detection, Slotting, Chatbot).
- `data/cleaned_warehouse_data.csv`: The cleaned dataset used by the models.
- `docs/`: Project reports and site visit images.
- `clean_data.py`: Script used to clean and filter the raw Kaggle data.

## How to Run
1. Install the required libraries: `pip install pandas numpy scikit-learn streamlit`
2. Run the AI models: `python src/stockwise_ai.py`
3. Launch the dashboard: `streamlit run app.py`
