<?php
  require "connection.php";
  if(isset($_GET['rpi_id'])){
    $rpi_id = $_GET['rpi_id'];
    if(isset($_GET['t1']) && isset($_GET['t2'])){
      $t1 = $_GET['t1'];
      $t2 = $_GET['t2'];
      $sql = "SELECT `id`, `date_time`, `message` FROM `error_log` WHERE (`rpi_id`='$rpi_id' && `date_time`>='$t1' && `date_time`<='$t2') ORDER BY `date_time` DESC LIMIT 5";
    }else{
      $sql = "SELECT `id`, `date_time`, `message` FROM `error_log` WHERE `rpi_id` = '$rpi_id' ORDER BY `date_time` DESC LIMIT 5";
    }
    $result = mysqli_query($con, $sql);

    if ($result->num_rows > 0) {
      echo "
      <table class='table'>
        <thead>
          <tr>
            <th>Date-time</th>
            <th>Error</th>
          </tr>
        </thead>
        <tbody>
      ";
      while($row = $result->fetch_assoc()) {
        $id = $row['id'];
        $date_time = $row['date_time'];
        $message = $row['message'];

        echo "
        <tr>
          <td>$date_time</td>
          <td>$message</td>
        </tr>
        ";
      }
      echo "
        </tbody>
      </table>
      ";
    }
  }
?>
