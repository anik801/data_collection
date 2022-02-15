<?php
  header("Cache-Control: no-cache, no-store, must-revalidate"); // HTTP 1.1.
  header("Pragma: no-cache"); // HTTP 1.0.
  header("Expires: 0"); // Proxies.
  
  require "helperMethods.php";

  if(isset($_GET['rpi_id']) && isset($_GET['start']) && isset($_GET['end']) && isset($_GET['sensor_id'])){
    $rpi_id = $_GET['rpi_id'];
    $start = $_GET['start'];
    $end = $_GET['end'];
    $sensor_id = $_GET['sensor_id'];

    // echo $rpi_id . " " . $start . " " . $end;

    echo "
    <table id='sensors_table' class='table'>
      <thead>
      </thead>

      <tbody>";
        get_sensors_for_table($rpi_id, $start, $end, $sensor_id);
    echo "
      </tbody>
    </table>
    ";
  }

function generate_sensor_td($rpi_id, $sensor, $start, $end){
  $sensor_canvas = "canvas_".$sensor;
  $sensor_canvas_info = "canvas_info_".$sensor;
  echo "
  <td class = 'sensor_td'>
    <div class = 'chart-container'>
      <canvas id = '$sensor_canvas'></canvas>
    </div>
    <script>
      show_sensor_chart('$rpi_id', '$sensor', '$start', '$end');
    </script>
  </td>";
}

function get_sensors_for_table($rpi_id, $start, $end, $sensor_id){
  $con = get_con();

  if($sensor_id == "0"){
    $sql = "SELECT `sensor` FROM `sensors` WHERE (`rpi_id` = '$rpi_id')";
    $result = mysqli_query($con, $sql);

    if ($result->num_rows > 0) {
      $i = 0;
      $entry_per_row = 2;
      while($row = $result->fetch_assoc()) {
        $sensor = $row['sensor'];
        if($i % $entry_per_row == 0){
          echo "<tr class = 'sensor_tr'>";
          generate_sensor_td($rpi_id, $sensor, $start, $end);
        }else if($i % $entry_per_row == $entry_per_row - 1){
          generate_sensor_td($rpi_id, $sensor, $start, $end);
          echo "</tr>";
        }else{
          generate_sensor_td($rpi_id, $sensor, $start, $end);
        }
        $i = $i + 1;
      }
    }
        echo "<tr style='display:none;'><td id='additional_info_td'></td></tr>";
  }else{
    $sql = "SELECT `sensor` FROM `sensors` WHERE (`id` = '$sensor_id')";
    $result = mysqli_query($con, $sql);
    if($result->num_rows > 0){
      echo "<tr><td id='additional_info_td'></td></tr>";
      $row = $result->fetch_assoc();
      $sensor_name = $row['sensor'];
      echo "<tr class = 'sensor_tr'>";
      generate_sensor_td($rpi_id, $sensor_name, $start, $end);
      echo "</tr>";
    }

  }

}

?>
