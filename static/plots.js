

// Fetch the JSON data and console log it
d3.json('/index').then(function(data) {
    var col2data = data.map(function(d) { return d.totalwords })
    var col3data = data.map(function(d) { return d.descriptivewords })
    var col4data = data.map(function(d) { return d.points })

    console.log(col2data)
    
    var trace1 = {
        x: col2data,
        y: col4data,
        mode: 'markers',
        type: 'scatter'
      };
      
      var trace2 = {
        x: col3data,
        y: col4data,
        xaxis: 'x2',
        yaxis: 'y2',
        mode: 'markers',
        type: 'scatter'
      };

      var trace3 = {
        x: (col2data/col3data),
        y: col4data,
        xaxis: 'x3',
        yaxis: 'y3',
        mode: 'markers',
        type: 'scatter'
      };
      
      var data = [trace1, trace2, trace3];
      
      var layout = {title: "total words vs points, descriptive words vs points, descriptive/total vs points",
        grid: {rows: 1, columns: 3, pattern: 'independent'},
      };
      
      Plotly.newPlot('plot', data, layout);
});
