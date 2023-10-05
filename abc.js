const express = require('express');
const axios = require('axios');
const app = express();
const port = process.env.PORT || 3000;

app.use(express.json()); // Enable JSON request body parsing

// Define a route that accepts a string input, makes an API call, and prints the 'abc' field to the console
app.get('/get-abc', async (req, res) => {
  const inputString = req.query.inputString; // Retrieve the input string from the query parameter (e.g., /get-abc?inputString=example)

  if (!inputString) {
    return res.status(400).json({ error: 'Input string is missing.' });
  }

  try {
    // Make an API call using the input string (modify the URL as needed)
    const response = await axios.get(`https://example.com/api?query=${inputString}`); // Replace with your API URL and parameters

    // Check if the response contains a valid 'abc' field
    if (response.data && response.data.abc) {
      const abcValue = response.data.abc;
      console.log(`'abc' Field Value for Input '${inputString}': ${abcValue}`);
      res.json({ abc: abcValue });
    } else {
      console.error(`No 'abc' field found in the API response for Input '${inputString}'.`);
      res.status(500).json({ error: `No 'abc' field found in the API response for Input '${inputString}'.` });
    }
  } catch (error) {
    console.error(`Error fetching data from the API for Input '${inputString}':`, error);
    res.status(500).json({ error: `Error fetching data from the API for Input '${inputString}'.` });
  }
});

app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});
