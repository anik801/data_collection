<?php
  function get_con(){
    require "connection.php";
    return $con;
  }

  function update_date_time(){
    $con = get_con();
    $sql = "SELECT `id`, `date_time` FROM `storage_v2` WHERE 1";
    $result = mysqli_query($con, $sql);

    if ($result->num_rows > 0) {
      while($row = $result->fetch_assoc()) {
          $id = $row['id'];
          $date_time = $row['date_time'];

          $new_date_time = substr($date_time, 0, 19);

          // echo $new_date_time . "----" . $id . "<br>";
          $sql_2 = "UPDATE `storage_v2` SET `date_time`='$new_date_time' WHERE (`id` = '$id')";
          $result_2 = mysqli_query($con, $sql_2);
      }
      echo "DONE";
    }
  }

  set_time_limit(3000);
  update_date_time();
?>
