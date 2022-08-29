$.ajaxSetup({ cache: false });

function update_sensor_table() {
  if (window.XMLHttpRequest) {
    xmlhttp=new XMLHttpRequest();
  } else {
    xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
  }


  xmlhttp.onreadystatechange=function() {
    if (xmlhttp.readyState==4 && xmlhttp.status==200) {
      document.getElementById("table_div").innerHTML=xmlhttp.responseText;
      // eval(document.getElementById("inner_script").innerHTML);
      $("#table_div").find("script").each(function(){
        eval($(this).text());
      });
    }
  }

  var rpi_id = document.getElementById("placement_select").value;
  var start = document.getElementById("start_date_time").value;
  var end = document.getElementById("end_date_time").value;
  var interval = document.getElementById("interval_select").value;
  var sensor_id = document.getElementById("sensor_select").value;


  xmlhttp.open("GET","fetch_data_for_table.php?rpi_id="+rpi_id+"&start="+start+"&end="+end+"&sensor_id="+sensor_id, true);
  xmlhttp.setRequestHeader("Cache-Control", "no-cache, no-store, max-age=0");
  xmlhttp.send();
}

function get_sersor_name(sensor){
  if(sensor === "temp"){
    return "Temperature";
  }else if(sensor === "co"){
    return "CO";
  }else if(sensor === "lpg"){
    return "LPG";
  }

  return sensor.replace(/^./, sensor[0].toUpperCase());
}

function show_sensor_chart(rpi_id, sensor, start, end){
  // var sensor = 'temp';
  $.ajax({
    // url : "http://localhost/data_collection/get_sensor_data.php?sensor="+sensor+"&rpi_id="+rpi_id+"&start="+start+"&end="+end,
    url : "get_sensor_data.php?sensor="+sensor+"&rpi_id="+rpi_id+"&start="+start+"&end="+end,
    type : "GET",
    success : function(data){

      data = JSON.parse(data);
      var date_time = [];
      var sensor_data = [];
      var data_sum = 0;
      var count = 0;

      for(var i in data) {
        // console.log(data[i][sensor]);
        date_time.push(data[i].date_time);
        sensor_data.push(data[i][sensor]);
        data_sum += parseFloat(data[i][sensor]);
        count++;
      }

      var data_max = Math.max.apply(Math,sensor_data);
      var data_min = Math.min.apply(Math,sensor_data);
      var data_avg = data_sum/count;

      var additional_info = "Maximum: "+data_max+" | Minimum: "+data_min+" | Average: "+data_avg;
      // var sensor_canvas_info = 'canvas_info_' + sensor;
      // console.log(sensor_canvas_info);
      // sensor_canvas_info.innerHTML = additional_info;
      document.getElementById("additional_info_td").innerHTML = additional_info;

      // sensor_name = get_sersor_name(sensor);
      sensor_name = sensor;
      var chartdata = {
        labels: date_time,
        datasets: [
          {
            label: sensor_name,
            fill: true,
            lineTension: 0.1,
            backgroundColor: "rgba(51, 204, 51, 0.2)",
            borderColor: "rgba(51, 204, 51, 0.8)",
            pointHoverBackgroundColor: "rgba(59, 89, 152, 1)",
            pointHoverBorderColor: "rgba(59, 89, 152, 1)",
            pointRadius: 0,
            // showLine : true,
            data: sensor_data
          }
        ]
      };
      var sensor_canvas = "#"  + 'canvas_' + sensor;
      var ctx = $(sensor_canvas);

      var LineGraph = new Chart(ctx, {
        type: 'line',
        data: chartdata,
        options: {
          legend: {
            display: true,
            labels: {
              // fontColor: 'rgb(255, 99, 132)'
              fontSize: 16,
              fontStyle: 'bold',
              fontColor: "rgba(0, 0, 0, 1)"
            }
          }
        }
      });
    },
    error : function(data) {

    }
  });
}

function clickedDataDownloadBtn(){
  document.location.href = "data_download.php"
}

function clickedErrorLogBtn(){
  document.location.href = "error_log.php"
}

function goToDashboard(){
  document.location.href = "index.php"
}

function modifySensorsBtnClicked(){
  document.location.href = "modify_sensors.php"
}

function modifyRpiBtnClicked(){
  document.location.href = "modify_rpi.php"
}

function selectAllBtnClicked(){
  var items=document.getElementsByName('sensor_checkbox');
	for(var i=0; i<items.length; i++){
		if(items[i].type=='checkbox')
			items[i].checked=true;
	}
}

function deleteSensor(id){
  var response = confirm("Are you sure you want to remove this sensor from the system? [ID: "+id+"]");

  if (response == true) {
    document.location.href = "delete_sensor.php?id="+id;
  }
}

function deleteRpi(id){
  var response = confirm("Are you sure you want to remove this Raspberry Pi from the system? [ID: "+id+"]");

  if (response == true) {
    document.location.href = "delete_rpi.php?rpi_id="+id;
  }
}

function clickedAddRpiBtn(){
  rpi_position = document.getElementById("rpi_position_input").value;
  rpi_position = rpi_position.trim();
  if(rpi_position.length == 0){
    alert("Please enter the location of the newly placed Raspberry Pi.");
  }else{
    document.location.href = "add_rpi.php?pos="+rpi_position;
  }
}

function clickedAddSensorBtn(){
  rpi_id = document.getElementById("placement_select").value;
  rpi_id = rpi_id.trim();

  if(rpi_id.length == 0){
    alert("Please select a Raspberry Pi.");
  }else{
    sensor_name = document.getElementById("sensor_name_input").value;
    sensor_name = sensor_name.trim();

    type = document.getElementById("sensor_type_select").value;

    pin = document.getElementById("pin_input").value;
    pin = pin.trim();

    if(sensor_name.length == 0 || pin.length == 0){
      alert("Please check the inputs.");
    }else{
      document.location.href = "add_sensor_to_rpi.php?rpi_id="+rpi_id+"&sensor_name="+sensor_name+"&type="+type+"&pin="+pin;
    }
  }
}

function updateSensorListForModificaiton(){
  if (window.XMLHttpRequest) {
    xmlhttp=new XMLHttpRequest();
  } else {
    xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
  }
  xmlhttp.onreadystatechange=function() {
    if (xmlhttp.readyState==4 && xmlhttp.status==200) {
      document.getElementById("sensor_modification_div").innerHTML=xmlhttp.responseText;
      $("#sensor_modification_div").find("script").each(function(){
        eval($(this).text());
      });
    }
  }

  var rpi_id = document.getElementById("placement_select").value;

  xmlhttp.open("GET","fetch_sensors_for_edit.php?rpi_id="+rpi_id, true);
  xmlhttp.setRequestHeader("Cache-Control", "no-cache, no-store, max-age=0");
  xmlhttp.send();
}

function rpiSelectedInIndex(rpi_id){
  if (window.XMLHttpRequest) {
    xmlhttp=new XMLHttpRequest();
  } else {
    xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
  }
  xmlhttp.onreadystatechange=function() {
    if (xmlhttp.readyState==4 && xmlhttp.status==200) {
      document.getElementById("sensor_select_td").innerHTML=xmlhttp.responseText;
      $("#sensor_select_td").find("script").each(function(){
        eval($(this).text());
      });
    }
  }


  xmlhttp.open("GET","fetch_sensors_in_select.php?rpi_id="+rpi_id, true);
  xmlhttp.setRequestHeader("Cache-Control", "no-cache, no-store, max-age=0");
  xmlhttp.send();
}

function rpiSelectedInDataDownload(rpi_id){
  if (window.XMLHttpRequest) {
    xmlhttp=new XMLHttpRequest();
  } else {
    xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
  }
  xmlhttp.onreadystatechange=function() {
    if (xmlhttp.readyState==4 && xmlhttp.status==200) {
      document.getElementById("sensor_select_div").innerHTML=xmlhttp.responseText;
      $("#sensor_select_div").find("script").each(function(){
        eval($(this).text());
      });
    }
  }

  xmlhttp.open("GET","fetch_sensors_for_data_download.php?rpi_id="+rpi_id, true);
  xmlhttp.setRequestHeader("Cache-Control", "no-cache, no-store, max-age=0");
  xmlhttp.send();
}

function showRecentErrors(){
  if (window.XMLHttpRequest) {
    xmlhttp=new XMLHttpRequest();
  } else {
    xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
  }
  xmlhttp.onreadystatechange=function() {
    if (xmlhttp.readyState==4 && xmlhttp.status==200) {
      document.getElementById("recent_error_div").innerHTML=xmlhttp.responseText;
      $("#recent_error_div").find("script").each(function(){
        eval($(this).text());
      });
    }
  }

  var rpi_id = document.getElementById("placement_select").value;
  var start_date_time = document.getElementById("start_date_time").value;
  var end_date_time = document.getElementById("end_date_time").value;
  if(start_date_time.length>0 && end_date_time.length>0){
    xmlhttp.open("GET","fetch_recent_errors.php?rpi_id="+rpi_id+"&t1="+start_date_time+"&t2="+end_date_time, true);
  }else{
    xmlhttp.open("GET","fetch_recent_errors.php?rpi_id="+rpi_id, true);
  }
  xmlhttp.setRequestHeader("Cache-Control", "no-cache, no-store, max-age=0");
  xmlhttp.send();
}

function clickedDownloadErrorLogBtn(){
  var rpi_id = document.getElementById("placement_select").value;
  var start_date_time = document.getElementById("start_date_time").value;
  var end_date_time = document.getElementById("end_date_time").value;
  if(start_date_time.length>0 && end_date_time.length>0){
    var url = "download_error_log.php?rpi_id="+rpi_id+"&t1="+start_date_time+"&t2="+end_date_time;
  }else{
    var url = "download_error_log.php?rpi_id="+rpi_id;
  }
  if(rpi_id.length>0)
    document.location.href = url;
}

function clickedDownloadDataBtn(){
  var rpi_id = document.getElementById("placement_select").value;
  var start_date_time = document.getElementById("start_date_time").value;
  var end_date_time = document.getElementById("end_date_time").value;

  var selected_sensors = [];
  var items=document.getElementsByName('sensor_checkbox');
	for(var i=0; i<items.length; i++){
		if(items[i].type=='checkbox')
			if(items[i].checked == true){
        selected_sensors.push(items[i].id);
      }
	}
  selected_sensors = JSON.stringify(selected_sensors);
  if(start_date_time.length>0 && end_date_time.length>0 && rpi_id.length>0 && selected_sensors.length>0){
    var url = "download_data.php?rpi_id="+rpi_id+"&t1="+start_date_time+"&t2="+end_date_time+"&selected_sensors="+selected_sensors;
    document.location.href = url;
  }
}

function clickedAddEnviroPlusBtn(){
  rpi_position = document.getElementById("rpi_enviro_plus_position_input").value;
  rpi_position = rpi_position.trim();
  if(rpi_enviro_plus_position_input.length == 0){
    alert("Please enter the location of the newly placed Raspberry Pi.");
  }else{
    document.location.href = "add_enviro_plus.php?pos="+rpi_position;
  }
}

function clickedAddEnviroBtn(){
  rpi_position = document.getElementById("rpi_enviro_position_input").value;
  rpi_position = rpi_position.trim();
  if(rpi_enviro_position_input.length == 0){
    alert("Please enter the location of the newly placed Raspberry Pi.");
  }else{
    document.location.href = "add_enviro.php?pos="+rpi_position;
  }
}

function invalidLoginAttempt(){
  alert("Invalid username/password!");
  document.getElementById("username_input").value = "";
  document.getElementById("password_input").value = "";
}

function checkUserCredentials(username, password){
  $.ajax({
    url: "check_user_credentials.php?username="+username+"&password="+password,
    type: 'GET',
    dataType: 'json', // added data type
    success: function(res) {
      console.log(res);
      // alert(res);
      if(res.available){
        document.getElementById("login_div").style.display = "none";
        showUserPage();
      }else{
        invalidLoginAttempt();
      }
    }
  });
}

function showUserPage(){
  // document.getElementById("login_div").style.display = "none";
  document.getElementById("modify_sensors_btn").style.display = "inline";
  document.getElementById("modify_rpi_btn").style.display = "inline";
  document.getElementById("main_body_div").style.display = "inline";
}

function showGuestPage(){
  // document.getElementById("login_div").style.display = "none";
  document.getElementById("modify_sensors_btn").style.display = "none";
  document.getElementById("modify_rpi_btn").style.display = "none";
  document.getElementById("main_body_div").style.display = "inline";
}

function clickedGuestLoginBtn(){
  document.location.href = "guest_login.php";
}

function clickedUserLoginBtn(){
  var username = document.getElementById("username_input").value;
  var password = document.getElementById("password_input").value;

  if(username == "" || password == ""){
    alert("Username/password cannot be empty!");
  }else{
    checkUserCredentials(username, password);
  }
}

function logOutButtonPressed(){
  document.location.href="destroy_session.php";
}
