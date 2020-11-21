<?php require "connection.php";
  if(isset($_GET['rpi_id']) && isset($_GET['sensor_name']) && isset($_GET['type']) && isset($_GET['pin'])){
    $rpi_id = $_GET['rpi_id'];
    $sensor_name = $_GET['sensor_name'];
    $type = $_GET['type'];
    $pin = $_GET['pin'];

    $sql = "INSERT INTO `sensors`(`rpi_id`, `sensor`, `type`, `pin`) VALUES ('$rpi_id', '$sensor_name', '$type', '$pin')";
    $result = mysqli_query($con, $sql);

    $table_name = "rpi_" . $rpi_id;
    $sql = "ALTER TABLE $table_name ADD `$sensor_name` double DEFAULT NULL;";
    $result = mysqli_query($con, $sql);

    $sql = "UPDATE `placements` SET `updated`='1' WHERE `rpi_id`='$rpi_id';";
    $result = mysqli_query($con, $sql);

    echo $result;

    echo "<script> document.location.href='modify_sensors.php';</script>";
  }
?>
