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
      labels: caste_data.caste,
      datasets: [{
        label: '# of Dropouts',
        data: caste_data.student_count,
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
      labels: city_data.city,
      datasets: [{
        label: '# of Dropouts',
        data: city_data.student_count,
        borderWidth: 1
      }]
    },
    options: {
      indexAxis: 'y',
    }
    }
    
  );