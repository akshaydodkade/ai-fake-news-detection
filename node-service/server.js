const express = require('express');
const axios = require('axios');
const cors = require('cors');
const path = require('path');
const app = express();
const { exec } = require('child_process');

app.use(cors());
app.use(express.json());

app.use(express.static(path.join(__dirname, 'client/build')));

app.post('/predict', async (req, res) => {
  const { text } = req.body;
  if (!text) return res.status(400).json({ error: 'Text is required' });

  try {
    const pythonUrl = 'https://fake-news-predictor-wa1s.onrender.com/predict';
    const response = await axios.post(pythonUrl, { text });
    const prediction = response.data.prediction === 1 ? 'Real' : 'Fake';
    res.json({ prediction });
  } catch (err) {
    res.status(500).json({
      error: 'Prediction failed',
      message: err.message,
    });
  }
});

app.post('/local-predict', (req, res) => {
  const { text } = req.body;
  if (!text) return res.status(400).json({ error: 'Text is required' });

  const pythonCmd = `python3 local-predict.py "${text}"`;
  exec(pythonCmd, (err, stdout, stderr) => {
    if (err) {
      console.error('Exec error:', err, stderr);
      return res.status(500).json({ error: stderr || err.message });
    }
    console.log(stdout.trim());
    const prediction = stdout.trim() === '1' ? 'Real' : 'Fake';
    res.json({ prediction });
  });
});

app.get('*', (req, res) => {
  res.sendFile(path.join(__dirname, 'client/build', 'index.html'));
})

const port = process.env.PORT || 5000;
app.listen(port, () => console.log(`Server running on port ${port}`));