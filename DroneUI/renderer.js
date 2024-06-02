const { ipcRenderer } = require('electron');
const socket = require('socket.io-client')('http://localhost:5000');

socket.on('drone_data', (data) => {
  document.getElementById('temperature').innerText = data.temperature;
  document.getElementById('battery').innerText = data.battery;
});
