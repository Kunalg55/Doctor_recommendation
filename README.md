# Doctor Recommendation System

## Overview
This web app helps users find the right doctor based on their symptoms. It takes symptom input and suggests a specialist using an Excel-based dataset.

## Features
- Recommends doctors based on symptoms
- Simple web interface using Flask
- Autocomplete for symptom input
- Mobile-friendly design

## Technologies Used
- **Backend:** Flask (Python)
- **Frontend:** HTML, CSS
- **Data Handling:** Pandas, Excel

## Setup Guide
### Requirements
- Python 3
- pip (Python package manager)

### Steps to Install
1. **Clone the project:**
   ```sh
   git clone https://github.com/yourusername/doctor-recommendation-system.git
   cd doctor-recommendation-system
   ```

2. **Install required packages:**
   ```sh
   pip install -r requirements.txt
   ```

3. **Run the app:**
   ```sh
   python app.py
   ```

4. **Open in browser:**
   ```
   http://127.0.0.1:5000/
   ```

## How It Works
1. Enter symptoms separated by commas.
2. Click **Submit** to get recommended doctors.
3. If symptoms are invalid, an error message appears.

## Future Improvements
- Connect to a medical database
- Store patient history
- Improve accuracy with AI

