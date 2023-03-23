function myFunction() {
  var x = document.getElementById("url").value;
  document.getElementById("display").innerHTML = x;


  // const axios = require('axios');
  // const url = x;

  // axios.post('http://localhost:5000/api', {
  //   url: url
  // })
  //   .then(response => {
  //     console.log(`Python output: ${response.data}`);
  //   })
  //   .catch(error => {
  //     console.error(`Python error: ${error}`);
  //   });













  // const { spawn } = require('child_process');
  // const url = x;

  // const pythonProcess = spawn('python', [main.py, url]);

  // pythonProcess.stdout.on('data', (data) => {
  //   console.log(`Python output: ${data}`);
  // });

  // pythonProcess.stderr.on('data', (data) => {
  //   console.error(`Python error: ${data}`);
  // });

  // pythonProcess.on('close', (code) => {
  //   console.log(`Python process exited with code ${code}`);
  // });

}