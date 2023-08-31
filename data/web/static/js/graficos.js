const ctx = document.getElementById('views-chart').getContext('2d');

fetch('/api/views_data/') 
  .then(response => response.json())
  .then(data => {
    const viewsChart = new Chart(ctx, {
      type: 'bar',
      data: {
        labels: data.labels,
        datasets: [{
          label: 'Visualizações',
          data: data.data,
          backgroundColor: 'rgba(75, 192, 192, 0.2)',
          borderColor: 'rgba(75, 192, 192, 1)',
          borderWidth: 1
        }]
      },
      options: {
        scales: {
          y: {
            beginAtZero: true
          }
        }
      }
    });
  });
