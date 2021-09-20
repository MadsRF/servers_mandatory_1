const express = require('express');
const app = express();

// Parser Middleware
const parser = require('fast-xml-parser');
const axios = require("axios");
app.use(express.urlencoded({ extended: false }));
app.use(express.json());



// Recieves XML from Benedict through route
app.post('/', (req, res) => {

  // REMOVE THIS AND COMMENT IN req.body.data on line 20
  const testData = "<data>10</data>";
  console.log(testData);

  try {
    const requestXMLData = testData; //req.body.data;
    console.log("request", requestXMLData);

    // Checks if the received format is XML
    if (parser.validate(requestXMLData) === true) {

      // XML parsed to JSON
      const JSONData = parser.parse(requestXMLData);
      console.log("JSONData", JSONData);
      
      // Calculation
      const changedJSONData = {
        number: JSONData.data * 2
      }
      console.log("changedData", changedJSONData);

      // Send JSON to server-three (OLIVER) then wait for response and repsonse back to Benedict 
      axios.post("http://10.130.178.13:3333/", changedJSONData).then(response => {
        console.log("response.data", response.data);
        res.json(response.data);
      }).catch(error => {
        res.status(500).send(error);
      });

    } else {
      // Incorrect data 
      res.status(400).send("Not XML recived");
    }

  } catch (error) {
    // Internal server error
    res.status(500).send(error);
  }
});



// Takes the PORT from env. if nothing specified then pick port 2222
const port = process.env.PORT ? process.env.PORT : 2222;

// Error handling on server upstart
app.listen(port, (error) => {
  if (error) {
    console.log("Error starting the server");
  }
  console.log("This server is running on port:", port);
});
