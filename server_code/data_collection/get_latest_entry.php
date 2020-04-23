<?php
  require "connection.php";
  if(isset($_GET['rpi_id'])){
    $rpi_id = htmlspecialchars($_GET["rpi_id"]);
    $room_id = htmlspecialchars($_GET["room_id"]);

    $sql = "SELECT `date_time` FROM `storage` WHERE (`rpi_id`='$rpi_id' AND `room_id`='$room_id') ORDER BY `date_time` DESC LIMIT 1";
    $result = mysqli_query($con, $sql);

    if ($result->num_rows > 0) {
        while($row = $result->fetch_assoc()) {
            echo $row["date_time"];
        }
    } else {
        echo "0";
    }
  }
?>
