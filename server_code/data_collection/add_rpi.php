<?php require "connection.php";
  if(isset($_GET['pos'])){
    $rpi_position = $_GET['pos'];
    $sql = "INSERT INTO `placements`(`room_id`) VALUES ('$rpi_position')";
    $result = mysqli_query($con, $sql);

    $rpi_id = mysqli_insert_id($con);
    $table_name = "rpi_" . $rpi_id;

    $sql = "CREATE TABLE $table_name (id varchar(64) NOT NULL, date_time DATETIME, rpi_id int, PRIMARY KEY (id))";
    $result = mysqli_query($con, $sql);

    echo "<script> document.location.href='modify_rpi.php';</script>";
  }
?>
