$(document).ready(function(){
  // console.log("Hello");
  $.ajax({
    url : "http://localhost/data_collection/get_data.php",
    type : "GET",
    success : function(data){
      data = JSON.parse(data);

      var userid = [];
      var facebook_follower = [];
      var twitter_follower = [];
      var googleplus_follower = [];

      for(var i in data) {
        userid.push("UserID " + data[i].userid);
        facebook_follower.push(data[i].facebook);
        twitter_follower.push(data[i].twitter);
        googleplus_follower.push(data[i].googleplus);
      }

      var chartdata = {
        labels: userid,
        datasets: [
          {
            label: "facebook",
            fill: false,
            lineTension: 0.1,
            backgroundColor: "rgba(59, 89, 152, 0.75)",
            borderColor: "rgba(59, 89, 152, 1)",
            pointHoverBackgroundColor: "rgba(59, 89, 152, 1)",
            pointHoverBorderColor: "rgba(59, 89, 152, 1)",
            data: facebook_follower
          },
          {
            label: "twitter",
            fill: false,
            lineTension: 0.1,
            backgroundColor: "rgba(29, 202, 255, 0.75)",
            borderColor: "rgba(29, 202, 255, 1)",
            pointHoverBackgroundColor: "rgba(29, 202, 255, 1)",
            pointHoverBorderColor: "rgba(29, 202, 255, 1)",
            data: twitter_follower
          },
          {
            label: "googleplus",
            fill: false,
            lineTension: 0.1,
            backgroundColor: "rgba(211, 72, 54, 0.75)",
            borderColor: "rgba(211, 72, 54, 1)",
            pointHoverBackgroundColor: "rgba(211, 72, 54, 1)",
            pointHoverBorderColor: "rgba(211, 72, 54, 1)",
            data: googleplus_follower
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




// var svgWidth = 500;
// var svgHeight = 300;
//
// var svg = d3.select('svg')
//     .attr("width", svgWidth)
//     .attr("height", svgHeight)
//     .attr("class", "bar-chart");
//
// var dataset = [80, 100, 56, 120, 180, 30, 40, 120, 160];
//
// var barPadding = 5;
// var barWidth = (svgWidth / dataset.length);
//
// var barChart = svg.selectAll("rect")
//     .data(dataset)
//     .enter()
//     .append("rect")
//     .attr("y", function(d) {
//         return svgHeight - d
//     })
//     .attr("height", function(d) {
//         return d;
//     })
//     .attr("width", barWidth - barPadding)
//     .attr("transform", function (d, i) {
//          var translate = [barWidth * i, 0];
//          return "translate("+ translate +")";
//     });
// /////////////////////////////////
//
// chart = {
//   const svg = d3.create("svg")
//       .attr("viewBox", [0, 0, width, height]);
//
//   svg.append("g")
//       .call(xAxis);
//
//   svg.append("g")
//       .call(yAxis);
//
//   svg.append("path")
//       .datum(data)
//       .attr("fill", "none")
//       .attr("stroke", "steelblue")
//       .attr("stroke-width", 1.5)
//       .attr("stroke-linejoin", "round")
//       .attr("stroke-linecap", "round")
//       .attr("d", line);
//
//   return svg.node();
// }
