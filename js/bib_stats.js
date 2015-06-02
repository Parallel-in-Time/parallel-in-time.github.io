$(document).ready(function() {
  var yc_prelim = {};
  $('#total-num-pubs').text("Total number of publications: " + $('li pre.abstract').length);
  $('#total-num-pubs').addClass('alert alert-info');

  $('li pre.abstract').each(function() {
    var abstract_text = $(this).text().toString();
    var matched = abstract_text.match(/year = .*/g).join('');
    var year = parseInt(matched.match(/[0-9]+/g).join(''));
    if (year in yc_prelim) {
      yc_prelim[year] = yc_prelim[year] + 1;
    } else {
      yc_prelim[year] = 1;
    }
  });
  var years = $.map(yc_prelim, function(v, k) { return k; });
  years.sort();
  var counts = [];
  var years_counts = {};
  years.forEach(function(v) {
    counts.push(yc_prelim[v]);
    years_counts[v] = yc_prelim[v];
  });

  var ctx = $("#pint-pubs-chart").get(0).getContext("2d");
  // This will get the first returned node in the jQuery collection.
  var data = {
    labels: years,
    datasets: [
      {
        label: "Number Publications per Year",
        data: counts
      }
    ]
  };
  var options = {
    ///Boolean - Whether grid lines are shown across the chart
    scaleShowGridLines : true,
    //String - Colour of the grid lines
    scaleGridLineColor : "rgba(0,0,0,.05)",
    //Number - Width of the grid lines
    scaleGridLineWidth : 1,
    //Boolean - Whether to show horizontal lines (except X axis)
    scaleShowHorizontalLines: true,
    //Boolean - Whether to show vertical lines (except Y axis)
    scaleShowVerticalLines: true,
    //Boolean - Whether the line is curved between points
    bezierCurve : true,
    //Number - Tension of the bezier curve between points
    bezierCurveTension : 0.4,
    //Boolean - Whether to show a dot for each point
    pointDot : true,
    //Number - Radius of each point dot in pixels
    pointDotRadius : 4,
    //Number - Pixel width of point dot stroke
    pointDotStrokeWidth : 1,
    //Number - amount extra to add to the radius to cater for hit detection outside the drawn point
    pointHitDetectionRadius : 10,
    //Boolean - Whether to show a stroke for datasets
    datasetStroke : true,
    //Number - Pixel width of dataset stroke
    datasetStrokeWidth : 2,
    //Boolean - Whether to fill the dataset with a colour
    datasetFill : true,
    //String - A legend template
    legendTemplate : "<ul class=\"<%=name.toLowerCase()%>-legend\"><% for (var i=0; i<datasets.length; i++){%><li><span style=\"background-color:<%=datasets[i].strokeColor%>\"></span><%if(datasets[i].label){%><%=datasets[i].label%><%}%></li><%}%></ul>"
  };
  var pint_pub_chart = new Chart(ctx).Line(data, options);
  $("#stats-buttons").append('<div class="btn-group btn-group-xs" role="group"><button class="btn btn-xs btn-default" data-toggle="collapse" data-target="#chart-raw-data" aria-expanded="false" aria-controls="#chart-raw-data">JSON data of plot</button></div>');
  $("#chart-raw-data").html('<pre>'+JSON.stringify(years_counts, null, 2)+'</pre>');
  $("#image-download-docu").text('To download the plot and use it in your publications, right-click it. It is licensed under a Creative Commons Attribution 3.0 license.');
});