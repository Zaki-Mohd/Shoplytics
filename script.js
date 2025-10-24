const form = document.getElementById('customer-form');
const resultDiv = document.getElementById('result');
const chartCanvas = document.getElementById('customer-chart');
let customerChart;

// Function to render the chart
const renderChart = async () => {
    const response = await fetch('/data');
    const data = await response.json();

    const datasets = data.cluster_centers.map((center, i) => ({
        label: `Cluster ${i + 1}`,
        data: data.customers.filter((_, j) => data.labels[j] === i).map(c => ({ x: c[0], y: c[1] })),
        backgroundColor: `rgba(${Math.random() * 255}, ${Math.random() * 255}, ${Math.random() * 255}, 0.6)`,
        pointRadius: 5
    }));

    datasets.push({
        label: 'Centroids',
        data: data.cluster_centers.map(c => ({ x: c[0], y: c[1] })),
        backgroundColor: 'black',
        pointRadius: 10,
        pointStyle: 'rectRot'
    });

    if (customerChart) {
        customerChart.destroy();
    }

    customerChart = new Chart(chartCanvas, {
        type: 'scatter',
        data: { datasets },
        options: {
            scales: {
                x: {
                    title: { display: true, text: 'Annual Income (k$)' }
                },
                y: {
                    title: { display: true, text: 'Spending Score (1-100)' }
                }
            }
        }
    });
};

// Handle form submission
form.addEventListener('submit', async (e) => {
    e.preventDefault();

    const income = document.getElementById('income').value;
    const score = document.getElementById('score').value;

    const response = await fetch('/predict', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ income, score })
    });

    const result = await response.json();

    resultDiv.innerHTML = `
        <p>Predicted Cluster: ${result.cluster}</p>
        <p>Cluster Insight: ${result.insight}</p>
    `;

    // Add the new point to the chart
    const newPoint = { x: parseFloat(income), y: parseFloat(score) };
    customerChart.data.datasets.push({
        label: 'New Customer',
        data: [newPoint],
        backgroundColor: 'red',
        pointRadius: 8
    });
    customerChart.update();
});

// Initial chart render
renderChart();