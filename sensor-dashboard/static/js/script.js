function updateData() {
    fetch('/sensor_data')
        .then(response => response.json())
        .then(data => {
            document.getElementById('temperature').textContent = `Temperature: ${data.temperature} °C`;
            document.getElementById('humidity').textContent = `Humidity: ${data.humidity} %`;
            document.getElementById('pressure').textContent = `Pressure: ${data.pressure} hPa`;
        });
}
setInterval(updateData, 5000);
updateData();
