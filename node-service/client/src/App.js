import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [text, setText] = useState('');
  const [prediction, setPrediction] = useState('');
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!text.trim()) {
      setPrediction('Please enter some text');
      return;
    }
    setLoading(true);
    setPrediction('');
    try {
      const res = await axios.post('http://localhost:5000/local-predict', { text });
      // const res = await axios.post('https://fake-news-frontend.onrender.com/predict', { text });
      setPrediction(res.data.prediction);
    } catch (err) {
      console.error(err);
      setPrediction('Error occurred while predicting');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="App">
      <header className="header">
        <h1>AI Fake News Detector</h1>
        <p>Enter news text to check if it’s real or fake</p>
      </header>
      <main className="main">
        <form onSubmit={handleSubmit} className="form">
          <textarea
            value={text}
            onChange={(e) => setText(e.target.value)}
            placeholder="Paste news article or headline here..."
            className="textarea"
            disabled={loading}
          />
          <button type="submit" className="button" disabled={loading}>
            {loading ? 'Detecting...' : 'Detect'}
          </button>
        </form>
        {loading && <div className="loader"></div>}
        {prediction && !loading && (
          <div className={`result ${prediction.toLowerCase()}`}>
            <h2>Prediction: {prediction}</h2>
          </div>
        )}
      </main>
    </div>
  );
}

export default App;