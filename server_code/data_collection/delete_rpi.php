<?php require "connection.php";
  if(isset($_GET['rpi_id'])){
    $rpi_id = $_GET['rpi_id'];
    $sql = "DELETE FROM `placements` WHERE (`rpi_id`='$rpi_id')";
    $result = mysqli_query($con, $sql);

    $sql = "DELETE FROM `sensors` WHERE (`rpi_id`='$rpi_id')";
    $result = mysqli_query($con, $sql);

    $table_name = "rpi_" . $rpi_id;
    $sql = "DROP TABLE $table_name";
    $result = mysqli_query($con, $sql);

    echo "<script> document.location.href='modify_rpi.php';</script>";
  }
?>
