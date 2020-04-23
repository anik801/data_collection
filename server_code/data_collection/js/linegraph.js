$(document).ready(function(){
  // console.log("Hello");
  var sensor = 'motion';
  $.ajax({
    url : "http://localhost/data_collection/get_data.php?sensor="+sensor,
    type : "GET",
    success : function(data){
      data = JSON.parse(data);

      // console.log(data);

      var date_time = [];
      var sensor_data = [];



      for(var i in data) {
        // console.log(data[i][sensor]);
        date_time.push(data[i].date_time);
        sensor_data.push(data[i][sensor]);
      }

      var chartdata = {
        labels: date_time,
        datasets: [
          {
            label: sensor,
            fill: true,
            lineTension: 0.1,
            backgroundColor: "rgba(59, 89, 152, 0.75)",
            borderColor: "rgba(59, 89, 152, 1)",
            pointHoverBackgroundColor: "rgba(59, 89, 152, 1)",
            pointHoverBorderColor: "rgba(59, 89, 152, 1)",
            data: sensor_data
          }
        ]
      };

      var ctx = $("#mycanvas");

      var LineGraph = new Chart(ctx, {
        type: 'line',
        data: chartdata
      });
    },
    error : function(data) {

    }
  });
});
