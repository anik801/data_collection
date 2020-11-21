<?php
  require "connection.php";
  if(isset($_GET['rpi_id'])){
    $rpi_id = $_GET['rpi_id'];
    if(isset($_GET['t1']) && isset($_GET['t2'])){
      $t1 = $_GET['t1'];
      $t2 = $_GET['t2'];
      $sql = "SELECT `id`, `date_time`, `message` FROM `error_log` WHERE (`rpi_id`='$rpi_id' && `date_time`>='$t1' && `date_time`<='$t2') ORDER BY `date_time` DESC";
    }else{
      $sql = "SELECT `id`, `date_time`, `message` FROM `error_log` WHERE `rpi_id` = '$rpi_id' ORDER BY `date_time` DESC";
    }
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
        header('Content-Disposition: attachment; filename="error_log.csv"');
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
