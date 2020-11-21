<?php
  require "connection.php";
  if(isset($_GET['rpi_id']) && isset($_GET['t1']) && isset($_GET['t2']) && isset($_GET['selected_sensors'])){
    $rpi_id = $_GET['rpi_id'];
    $t1 = $_GET['t1'];
    $t2 = $_GET['t2'];
    $selected_sensors=json_decode($_GET['selected_sensors']);

    $sensors = "";
    foreach($selected_sensors as $str){
      $sensors = $sensors."`$str`,";
    }
    $sensors = substr($sensors, 0, -1);
    $sql = "SELECT `date_time`, $sensors FROM `storage_v2` WHERE (`rpi_id`='$rpi_id' && `date_time`>='$t1' && `date_time`<='$t2') ORDER BY `date_time` DESC";

    $result = mysqli_query($con, $sql);

    if (!$result) die('Couldn\'t fetch records');
    $num_fields = mysqli_num_fields($result);
    $headers = array();
    while ($fieldinfo = mysqli_fetch_field($result)) {
        $headers[] = $fieldinfo->name;
    }
    $fp = fopen('php://output', 'w');
    if ($fp && $result) {
        header('Content-Type: text/csv');
        header('Content-Disposition: attachment; filename="sensor_data.csv"');
        header('Pragma: no-cache');
        header('Expires: 0');
        fputcsv($fp, $headers);
        while ($row = $result->fetch_array(MYSQLI_NUM)) {
            fputcsv($fp, array_values($row));
        }
        die;
    }
  }
?>
