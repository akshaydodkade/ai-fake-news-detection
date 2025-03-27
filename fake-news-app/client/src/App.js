import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [text, setText] = useState('');
  const [prediction, setPrediction] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const res = await axios.post('http://localhost:5000/predict', { text });
      setPrediction(res.data.prediction);
    } catch (err) {
      console.error(err);
      setPrediction('Error occurred');
    }
  };

  return (
    <div className="App">
      <h1>Fake News Detector</h1>
      <form onSubmit={handleSubmit}>
        <textarea
          value={text}
          onChange={(e) => setText(e.target.value)}
          placeholder="Enter news text here"
          rows="5"
          cols="50"
        />
        <br />
        <button type="submit">Detect</button>
      </form>
      {prediction && <h2>Prediction: {prediction}</h2>}
    </div>
  );
}

export default App;