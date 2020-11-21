<?php require "connection.php";
  if(isset($_GET['id'])){
    $id = $_GET['id'];

    $sql = "SELECT `rpi_id`, `sensor` FROM `sensors` WHERE (`id`='$id')";
    $result = mysqli_query($con, $sql);
    $row = $result->fetch_assoc();
    $rpi_id = $row['rpi_id'];
    $sensor_name = $row['sensor'];

    $sql = "DELETE FROM `sensors` WHERE (`id`='$id')";
    $result = mysqli_query($con, $sql);

    $table_name = "rpi_" . $rpi_id;
    $sql = "ALTER TABLE `$table_name` DROP COLUMN `$sensor_name`;";
    $result = mysqli_query($con, $sql);

    $sql = "UPDATE `placements` SET `updated`='1' WHERE `rpi_id`='$rpi_id';";
    $result = mysqli_query($con, $sql);

    echo "<script> document.location.href='modify_sensors.php';</script>";
  }
?>
