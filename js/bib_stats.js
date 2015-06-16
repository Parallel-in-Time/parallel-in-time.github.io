$(document).ready(function() {
  //
  // Generate Links to Years
  //
  var toc_html = '';
  $('h2').each(function() {
    if ($(this).attr('id') && $(this).attr('id').match(/year/g)) {
      toc_html += '<li><a href="#'+$(this).attr('id')+'">'+$(this).clone().children().remove().end().text()+'</a></li>';
    }
  });
  $('.dropdown-menu.years').html(toc_html);

  //
  // Gather Publications-by-Year Statistics
  //
  var yc_prelim = {};
  var min_year = 9999, max_year = 0;
  $('#total-num-pubs').text("Total number of publications: " + $('li pre.abstract').length);
  $('#total-num-pubs').addClass('alert alert-info');

  $('li pre.abstract').each(function() {
    var abstract_text = $(this).text().toString();
    var matched = abstract_text.match(/year = .*/g).join('');
    var year = parseInt(matched.match(/[0-9]+/g).join(''));
    if (year < min_year) { min_year = year; }
    if (year > max_year) { max_year = year; }
    if (year in yc_prelim) {
      yc_prelim[year] = yc_prelim[year] + 1;
    } else {
      yc_prelim[year] = 1;
    }
  });
  var years = [];
  var counts = [];
  var years_counts = {};
  for (var y = min_year; y <= max_year; ++y) {
    years.push(y);
    if (y in yc_prelim) {
      counts.push(yc_prelim[y]);
      years_counts[y] = yc_prelim[y];
    } else {
      counts.push(0);
      years_counts[y] = 0;
    }
  }

  //
  // Gather statistics per section
  //
  $('ol').each(function() {
    var count = $(this).children('li').length;
    $(this).prev('h2').children('.count-stat').addClass('badge').text(count);
  });

  //
  // Render the Chart
  //
  Chart.defaults.global.responsive = true;
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
    //Boolean - Whether the scale should start at zero, or an order of magnitude down from the lowest value
    scaleBeginAtZero: true,
    //Boolean - Whether grid lines are shown across the chart
    scaleShowGridLines: true,
    //String - Colour of the grid lines
    scaleGridLineColor: "rgba(0,0,0,.05)",
    //Number - Width of the grid lines
    scaleGridLineWidth: 1,
    //Boolean - Whether to show horizontal lines (except X axis)
    scaleShowHorizontalLines: true,
    //Boolean - Whether to show vertical lines (except Y axis)
    scaleShowVerticalLines: false,
    //Boolean - If there is a stroke on each bar
    barShowStroke: false,
    //Number - Pixel width of the bar stroke
    barStrokeWidth: 0,
    //Number - Spacing between each of the X value sets
    barValueSpacing: 1,
    //Number - Spacing between data sets within X values
    barDatasetSpacing: 0,
    //String - A legend template
    legendTemplate : "<ul class=\"<%=name.toLowerCase()%>-legend\"><% for (var i=0; i<datasets.length; i++){%><li><span style=\"background-color:<%=datasets[i].fillColor%>\"></span><%if(datasets[i].label){%><%=datasets[i].label%><%}%></li><%}%></ul>"
  };
  Chart.defaults.global.responsive = false;
  Chart.defaults.global.maintainAspectRatio = false;
  Chart.defaults.global.tooltipXOffset = 0;
  Chart.defaults.global.tooltipYOffset = 0;
  var pint_pub_chart = new Chart(ctx).Bar(data, options);
  $("#stats-buttons").append('<div class="btn-group btn-group-xs" role="group"><button class="btn btn-xs btn-default" data-toggle="collapse" data-target="#chart-raw-data" aria-expanded="false" aria-controls="#chart-raw-data">JSON data of plot</button></div>');
  $("#chart-raw-data").html('<pre>'+JSON.stringify(years_counts, null, 2)+'</pre>');
  $("#image-download-docu").text('To download the plot and use it in your publications, right-click it. It is licensed under a Creative Commons Attribution 3.0 license.');

  $('.year-btn-group').removeClass('hidden');
});