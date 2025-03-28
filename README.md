# Fake News Detection AI

A full-stack application to detect fake news using machine learning, built with MERN (MongoDB, Express.js, React, Node.js) and Python. Deployed on Render, this project combines a React frontend with a Node.js backend that integrates a Python-based ML model for real-time predictions.

## Live Demo
Try it out at: [https://fake-news-frontend.onrender.com](https://fake-news-frontend.onrender.com)

## Features
- **Real-time Prediction**: Enter news text to classify it as "Real" or "Fake."
- **MERN Stack**: Frontend built with React, backend with Node.js and Express.js.
- **Machine Learning**: Python-based Logistic Regression model with TF-IDF vectorization.
- **Dual-Service Architecture**: Node.js service for UI/API, Python service for ML predictions.

## Project Structure
  fake-news-app/
  ├── node-service/        # Node.js service (Frontend + Backend)
  │   ├── client/          # React frontend
  │   ├── server.js        # Node.js backend
  │   ├── package.json     # Node.js dependencies
  ├── python-service/      # Python service (ML Prediction)
  │   ├── predict.py       # Flask API for predictions
  │   ├── model.pkl        # Trained model
  │   ├── tfidf.pkl        # TF-IDF vectorizer
  │   ├── requirements.txt # Python dependencies
  └── render.yaml          # Render deployment config


## How It Works
1. **Frontend**: Users input news text via a React interface.
2. **Node.js Backend**: Receives the input and forwards it to the Python service via HTTP.
3. **Python Service**: Processes the text using a pre-trained ML model and returns a prediction (0 = Fake, 1 = Real).
4. **Response**: Node.js converts the prediction to "Fake" or "Real" and displays it on the frontend.

## Installation (Local Setup)
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/akshaydodkade/ai-fake-news-detection.git
   cd fake-news-app

2. **Node.js Service**:
  ```bash
  cd node-service
  npm install
  cd client && npm install && npm run build

3. **Python Service**:
  ```bash
  cd ../python-service
  python3 -m venv venv
  source venv/bin/activate
  pip install -r requirements.txt

4. **Run Locally**:
  - Start Python service: python predict.py (runs on port 5001)
  - Start Node.js service: cd ../node-service && npm start (runs on port 5000)
  - Visit http://localhost:5000

## Deployment on Render
  - Node.js Service: Deployed as a web service with npm start.
  - Python Service: Deployed as a Python web service with Flask.
  - Configured via render.yaml for dual-service deployment.

## Technologies Used
  - Frontend: React
  - Backend: Node.js, Express.js
  - ML: Python, scikit-learn, NLTK
  - API: Flask
  - Hosting: Render.com