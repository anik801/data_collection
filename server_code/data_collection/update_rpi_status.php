<?php require "connection.php";
  if(isset($_GET['rpi_id'])){
    $rpi_id = $_GET['rpi_id'];
    $sql = "UPDATE `placements` SET `updated`='0' WHERE `rpi_id`='$rpi_id'";
    $result = mysqli_query($con, $sql);
  }
?>
