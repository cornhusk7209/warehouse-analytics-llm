const express = require('express');
const fs = require('fs');
const path = require('path');
const csv = require('csv-parser');
const cors = require('cors');  // Allow cross-origin requests

const app = express();
const PORT = 5000;

// Use CORS to allow requests from frontend
app.use(cors());
console.log("Debug server...");
// Endpoint to get warehouse data from CSV
app.get('/api/warehouse-data', (req, res) => {
  const results = [];
  const filePath = path.join(__dirname, '../data/warehouse_data.csv');  // Adjust path if needed

  console.log("Request received for warehouse data...");
  console.log("File path being used:", filePath);  // Log the file path to ensure it’s correct

  console.log("Request received for warehouse data...");

  // Read the CSV file and parse it
  fs.createReadStream(filePath)
    .pipe(csv())
    .on('data', (data) => {
      console.log('Data row:', data);  // Print each row of data as it is parsed
      results.push(data);  // Collect each row of CSV data
    })
    .on('end', () => {
      console.log('Finished reading CSV file. Sending data...');
      res.json(results);  // Send the parsed data as JSON to the frontend
    })
    .on('error', (err) => {
      console.error('Error reading CSV file:', err);
      res.status(500).json({ error: 'Error reading CSV file' });  // Handle file read errors
    });
});

// Start the server
app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
  console.log(`Run http://localhost:${PORT}/api/warehouse-data`)
});