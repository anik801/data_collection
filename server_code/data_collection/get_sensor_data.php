<?php
  require "connection.php";
  if(isset($_GET['sensor']) && isset($_GET['rpi_id']) && isset($_GET['start']) && isset($_GET['end'])){
    $sensor = $_GET['sensor'];
    $rpi_id = $_GET['rpi_id'];;
    $start = $_GET['start'];
    $end = $_GET['end'];

    $table = "rpi_".$rpi_id;

    $sql = "SELECT `date_time`, `$sensor` FROM `$table` WHERE (`rpi_id`='$rpi_id' AND `date_time`>='$start' AND `date_time`<='$end') ORDER BY `date_time`";
    $result = mysqli_query($con, $sql);

    if ($result->num_rows > 0) {
      $data = array();
      for ($x = 0; $x < mysqli_num_rows($result); $x++) {
          $data[] = mysqli_fetch_assoc($result);
      }
      echo json_encode($data);
    } else {
        echo "0";
    }
  }
?>
