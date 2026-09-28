# Stockwise-AI-WMS

**Module:** Business Analysis 3.2 Capstone (AI Solution for Industries)

**Project:** Intelligent Warehouse Management System for Emfuleni Municipality

## What is this project?
We built Stockwise-AI-WMS for our Business Analysis 3.2 project. The theme was "AI Solution for Industries," and we chose to focus on warehouses. 

During a site visit to a municipal warehouse in Vereeniging, we saw that staff were still using paper logbooks and clipboards to track stock. This makes it hard to know what is in the warehouse, leads to theft, and causes long delays. Our system uses machine learning to solve these problems. It predicts what stock is needed, spots suspicious activity, organises the warehouse layout, and answers staff questions through a chatbot.

1.BUSINESS OBJECTIVES
The main objective of Stockwise AI is to develop an affordable, AI-powered Warehouse Management System [WMS] that automates inventory control, optimizes warehouse space, and predicts future stock needs.

Specific Objectives:

To reduce inventory holding costs by 35% within 12 months.
To achieve 99.9% inventory accuracy through automation.
To reduce time taken to find and dispatch an item from 2 hours to under 5 minutes.
To provide a corruption-proof, transparent reporting system for municipal audit.

2. BUSINESS SUCCESS CRITERIA
The project will be considered successful if:

System adoption by at least 1 municipal warehouse.
>95% accuracy in stock prediction.
50% reduction in expired goods.
Positive Return on Investment [ROI] within 6 months.
Community Benefit: Ensuring 100% stock accuracy, reducing wasteful expenditure by up to 40%, accelerating service delivery [potholes, water leaks, electricity faults fixed faster], improving transparency with automated audit trails, and ensuring clinics never run out of medicine and food parcels are delivered before expiry.

3. REQUIREMENTS, CONSTRAINTS & RISKS
Requirements:

Basic internet connectivity
Android phones / tablets for staff
CCTV cameras / Drones for scanning
Integration with existing municipal financial system
Constraints:

Low digital literacy of warehouse staff
Poor Wi-Fi coverage in warehouses
Resistance to change from officials benefiting from the manual system
Risks & Mitigation:

Risk of data privacy: Mitigated by on-premise deployment.
Risk of inaccurate initial data: Mitigated by 2-week manual verification phase.
Risk of power failure: Mitigated by offline mode that syncs when power returns.

4. INITIAL ASSESSMENT OF TOOLS & TECHNIQUES
How AI Will Be Applied:

Computer Vision for Automated Stock-Taking: Drones and CCTV with object detection [YOLOv8 / ResNet] will scan shelves daily, automatically count stock, read barcodes/QR codes, and detect misplaced items.
Predictive Analytics for Demand Forecasting: Using Time-Series models [LSTM / Prophet] trained on 3 years of municipal consumption data. Example output: "You will run out of 110mm water pipes in 14 days" and auto-generate a purchase requisition.
Intelligent Slotting Optimization: ML algorithm [Clustering + Genetic Algorithm] analyzes picking frequency and places fast-moving items near dispatch, reducing forklift travel time by 30%.
Chatbot for Warehouse Staff: Multilingual voice assistant in English, Sesotho, and IsiZulu. Worker can ask "Where is the blue cable?" and get instant location and quantity.
Anomaly Detection for Theft Prevention: Isolation Forest and One-Class SVM models to flag unusual stock movements e.g., stock leaving at midnight.
Data & Model Strategy from your theoretical section:

Data Types: Structured [Item ID, quantity, expiry, GRN], Unstructured [CCTV video, drone images, handwritten logbooks], Time-Series [3 years daily consumption], Image/Barcode [QR codes], and IoT Sensor Data [temperature for medicines, GPS for forklifts].
Evaluation: Computer Vision: mAP >95% and IoU. Demand Forecasting: MAE, MAPE target <10%, RMSE. Anomaly Detection: Precision, Recall, F1-Score with high Recall for theft.
Improvement Techniques: Transfer Learning [pre-trained YOLOv8], Continuous Learning [retrains Sunday nights], Human-in-the-Loop [manager confirms prediction].
NLP / Speech: BERT for queries like "Show me expired medicine", OpenAI Whisper for Sesotho/IsiZulu voice-to-text, and TTS for hands-free replies: "Blue cable is in Aisle 3, Shelf 2, Quantity 50"

## What does the system do?
1. **Demand Forecasting:** Uses Time Series Analysis (Linear Regression) to predict future stock needs.
2. **Theft Detection:** Uses Isolation Forest and a Deep Learning model (MLP) to find unusual picking times.
3. **Smart Slotting:** Uses K-Means Clustering to group fast-moving items near the dispatch area.
4. **Chatbot:** A simple Natural Language Processing bot that answers staff questions about stock.

## Screenshots of the System

### Terminal Output
![Terminal Output](screenshots/terminal_output.png)
Figure 1: The Python script running in the terminal. It shows the demand forecast, anomaly detection and clustering results.

### Dashboard Interface
![Dashboard Screenshot](screenshots/dashboard_screenshot_minimized.png)
Figure 2: The main dashboard of our system. It gives an overview of the current stock levels and key warehouse metrics.

### AI Alerts
![AI Alerts](screenshots/AI_alerts.png)
Figure 3: The AI alerts tab, it warns us about low stock items and unusual activity.

### Chatbot Interface (Greeting)
![Chatbot Greeting](screenshots/chatbot_screenshot1.png)
Figure 4: The chatbot responding to a simple greeting from a staff member.

### Chatbot Interface (Features)
![Chatbot Features](screenshots/chatbot_screenshot5.png)
Figure 5: The chatbot explaining the different things it can help with.

### Chatbot Interface (Low Stock)
![Chatbot Low Stock](screenshots/chatbot_screenshot3.png)
Figure 6: The chatbot responding to a staff question about low stock items.

### Chatbot Interface (Theft Detection)
![Chatbot Theft](screenshots/chatbot_screenshot6.png)
Figure 7: The chatbot giving an alert about recent anomalies and possible theft detected by the system.
