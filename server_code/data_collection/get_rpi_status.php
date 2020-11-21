<?php require "connection.php";
  if(isset($_GET['rpi_id'])){
    $rpi_id = $_GET['rpi_id'];

    $sql = "SELECT `updated` FROM `placements` WHERE `rpi_id`='$rpi_id';";
    $result = mysqli_query($con, $sql);
    $row = $result->fetch_assoc();
    $status = $row['updated'];
    echo $status;
  }
?>
