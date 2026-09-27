# Stockwise-AI-WMS
**Module:** Business Analysis 3.2 Capstone (AI Solution for Industries)
**Project:** Intelligent Warehouse Management System for Emfuleni Municipality

## Overview
Stockwise-AI-WMS is an AI-powered solution designed to modernise municipal warehouse operations. It uses Machine Learning to predict demand, detect anomalies (theft/misplacement), optimise storage layout (slotting), and provide a chatbot interface for staff. This project addresses the critical lack of real-time visibility and manual tracking issues found in local municipal warehouses.

## Project Structure
- `data/`: Contains the raw and cleaned warehouse datasets.
- `src/`: Contains the Python scripts for data cleaning and AI model training.
- `docs/`: Contains the final report, site visit evidence, and presentation materials.
- `app.py`: The Streamlit dashboard for real-time inventory tracking.
- `requirements.txt`: List of Python libraries required to run the project.

## Setup Instructions
1. Clone this repository.
2. Install the required libraries: `pip install -r requirements.txt`
3. Run the AI models: `python src/stockwise_ai.py`
4. Run the dashboard: `streamlit run app.py`