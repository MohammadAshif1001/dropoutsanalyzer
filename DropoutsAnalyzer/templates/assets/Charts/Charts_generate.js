const ctx = document.getElementById('Dropout_states');

  new Chart(ctx, {
    type: 'bar',
    data: {
      labels: result.state,
      datasets: [{
        label: '# of Dropouts',
        data: result.student_count,
        borderWidth: 1
      }]
    },
    options: {
      indexAxis: 'y',
    }
    }
    
  );





  const ctx_castefilter = document.getElementById('Dropout_castes');

  new Chart(ctx_castefilter, {
    type: 'pie',
    data: {
      labels: [
        "Andhra Pradesh",
        "Arunachal Pradesh",
        "Assam",
        
      ],
      datasets: [{
        label: '# of Dropouts',
        data: [42,15,73],
        borderWidth: 1
      }]
    },
    options: {
      indexAxis: 'y',
    }
    }
    
  );


  const ctx_cityfilter = document.getElementById('Dropout_city');

  new Chart(ctx_cityfilter, {
    type: 'doughnut',
    data: {
      labels: [
        "Andhra Pradesh",
        "Arunachal Pradesh",
        "Assam",
        
      ],
      datasets: [{
        label: '# of Dropouts',
        data: [42,15,73],
        borderWidth: 1
      }]
    },
    options: {
      indexAxis: 'y',
    }
    }
    
  );