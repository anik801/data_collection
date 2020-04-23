<?php
  require "connection.php";
  if(isset($_GET['row_id'])){
    $row_id = htmlspecialchars($_GET["row_id"]);
    $date_time = htmlspecialchars($_GET["date_time"]);
    $rpi_id = htmlspecialchars($_GET["rpi_id"]);
    $room_id = htmlspecialchars($_GET["room_id"]);
    $sensor = htmlspecialchars($_GET["sensor"]);
    $data = htmlspecialchars($_GET["data"]);

    // $sql = "INSERT INTO `room1`(`id`, `data`) VALUES (DEFAULT, '$firstname')";
		// $result=mysqli_query($con, $sql);
    $sql = "INSERT INTO `storage`(`id`, `date_time`, `rpi_id`, `room_id`, `sensor`, `data`) VALUES ('$row_id', '$date_time', '$rpi_id', '$room_id', '$sensor', '$data' )";
    if ($con->query($sql) === TRUE) {
        echo "0"; // inserted
    } else {
        echo "1"; // error
    }
  }
?>
