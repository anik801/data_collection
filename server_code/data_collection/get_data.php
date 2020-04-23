<?php
  require "connection.php";
  if(isset($_GET['sensor'])){
    $sensor = $_GET['sensor'];

    $rpi_id = 'm1';
    $room_id = 'r1';
    // $sensor = 'sound';

    $sql = "SELECT `date_time`, `$sensor` FROM `storage_v2` WHERE (`rpi_id`='$rpi_id' AND `room_id`='$room_id') ORDER BY `date_time`";
    $result = mysqli_query($con, $sql);

    if ($result->num_rows > 0) {
      $data = array();

      for ($x = 0; $x < mysqli_num_rows($result); $x++) {
          $data[] = mysqli_fetch_assoc($result);
      }

      echo json_encode($data);
        //
        // while($row = $result->fetch_assoc()) {
        //     echo $row["sound"] . "<br>";
        // }
    } else {
        echo "0";
    }
  }

?>
