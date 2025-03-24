// frontend/src/App.js
import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { Line } from 'react-chartjs-2';
import { Chart as ChartJS, CategoryScale, LinearScale, LineElement, PointElement, Title, Tooltip, Legend } from 'chart.js';

ChartJS.register(CategoryScale, LinearScale, LineElement, PointElement, Title, Tooltip, Legend);

function App() {
  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // Fetch data from the backend API
    axios.get('http://localhost:5000/api/warehouse-data')
      .then(response => {
        setData(response.data);
        setLoading(false);
      })
      .catch(error => {
        console.error('There was an error fetching the data!', error);
        setLoading(false);
      });
  }, []);

  // Process data for visualizations (e.g., orders processed by status)
  const statusData = data.reduce((acc, order) => {
    const status = order.Status;
    acc[status] = (acc[status] || 0) + 1;
    return acc;
  }, {});

  const statusLabels = Object.keys(statusData);
  const statusValues = Object.values(statusData);

  const chartData = {
    labels: statusLabels,
    datasets: [
      {
        label: 'Orders by Status',
        data: statusValues,
        borderColor: 'rgba(75, 192, 192, 1)',
        backgroundColor: 'rgba(75, 192, 192, 0.2)',
        fill: true,
      },
    ],
  };

  return (
    <div className="App">
      <h1>Warehouse Dashboard</h1>

      {loading ? (
        <p>Loading...</p>
      ) : (
        <>
          <h2>Order Status Overview</h2>
          <Line data={chartData} />

          {/* Add more visualizations for other data like Employee Performance */}
        </>
      )}
    </div>
  );
}

export default App;
