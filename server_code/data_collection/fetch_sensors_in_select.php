<?php
  require "connection.php";
  if(isset($_GET['rpi_id'])){
    $rpi_id = $_GET['rpi_id'];
    $sql = "SELECT `id`, `sensor` FROM `sensors` WHERE `rpi_id` = '$rpi_id'";
    $result = mysqli_query($con, $sql);

    if ($result->num_rows > 0) {
      echo "<select id='sensor_select' class='form-control' onchange='update_sensor_table();'>";
      echo "<option value = -1>Select Sensor</option>";
      while($row = $result->fetch_assoc()) {
        $sensor_id = $row['id'];
        $sensor_name = $row['sensor'];
        echo "<option value = $sensor_id>$sensor_name</option>";
      }
      echo "<option value = 0>SHOW ALL</option>";
      echo "</select>";
    }
  }
?>
