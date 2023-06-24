const express = require('express');
const { spawn } = require('child_process');

const app = express();
const port = process.env.PORT || 3000;

app.get('/', (req, res) => {
  const python = spawn('python', ['Hangman.py']);

  python.stdout.on('data', (data) => {
    console.log(data.toString());
  });

  python.stderr.on('data', (data) => {
    console.error(data.toString());
  });

  python.on('close', (code) => {
    console.log(`Child process exited with code ${code}`);
  });

  res.send('Hangman game is running!');
});

app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
