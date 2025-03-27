const express = require('express');
const { exec } = require('child_process');
const { PythonShell } = require('python-shell');
const cors = require('cors');
const app = express();

app.use(cors());
app.use(express.json());

app.post('/predict', (req, res) => {
  const { text } = req.body;
  if (!text) return res.status(400).json({ error: 'Text is required' });

  const pythonCmd = `/Users/akshaydodkade/Documents/htdocs/ai-fake-news-detection/venv/bin/python3 predict.py "${text}"`;
  exec(pythonCmd, (err, stdout, stderr) => {
    if (err) {
      return res.status(500).json({ error: stderr || err.message });
    }
    const prediction = stdout.trim() === '1' ? 'Real' : 'Fake';
    res.json({ prediction });
  });
});

app.listen(5000, () => console.log('Server running on port 5000'));