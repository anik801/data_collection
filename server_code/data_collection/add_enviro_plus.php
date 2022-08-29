<?php require "connection.php";
  if(isset($_GET['pos'])){
    $rpi_position = $_GET['pos'];
    $sql = "INSERT INTO `placements`(`room_id`) VALUES ('$rpi_position')";
    $result = mysqli_query($con, $sql);

    $rpi_id = mysqli_insert_id($con);
    $table_name = "rpi_" . $rpi_id;

    $sql = "CREATE TABLE $table_name (id varchar(64) NOT NULL, date_time DATETIME, rpi_id int,
    proximity double, humidity double, pressure double, light double, oxidised double,
    reduced double, nh3 double, temperature double, sound_high double,
    sound_mid double, sound_low double, sound_amp double, PRIMARY KEY (id))";
    $result = mysqli_query($con, $sql);

    $sql = "INSERT INTO `sensors`(`rpi_id`, `sensor`, `type`, `pin`) VALUES
    ('$rpi_id', 'proximity', '0', '0'),
    ('$rpi_id', 'humidity', '0', '0'),
    ('$rpi_id', 'pressure', '0', '0'),
    ('$rpi_id', 'light', '0', '0'),
    ('$rpi_id', 'oxidised', '0', '0'),
    ('$rpi_id', 'reduced', '0', '0'),
    ('$rpi_id', 'nh3', '0', '0'),
    ('$rpi_id', 'temperature', '0', '0'),
    ('$rpi_id', 'sound_high', '0', '0'),
    ('$rpi_id', 'sound_mid', '0', '0'),
    ('$rpi_id', 'sound_low', '0', '0'),
    ('$rpi_id', 'sound_amp', '0', '0')";
    $result = mysqli_query($con, $sql);

    echo "<script> document.location.href='modify_rpi.php';</script>";
  }
?>
