<?php
  // method declaration
  function get_con(){
    require "connection.php";
    return $con;
  }

  //method to insert @param data in 2nd table
  function insert_in_v2($id, $date_time, $rpi_id, $room_id, $sensor, $data){
    $con = get_con();
    $sql = "SELECT `id` FROM `storage_v2` WHERE (`id`='$id')";
    $result = mysqli_query($con, $sql);

    if ($result->num_rows > 0) {
      //entry already exists
      $sql = "UPDATE `storage_v2` SET `$sensor`= '$data' WHERE (`id`='$id')";
    } else {
      //entry not found. insert new row
      $sql = "INSERT INTO `storage_v2`(`id`, `date_time`, `rpi_id`, `room_id`, `$sensor`) VALUES ('$id', '$date_time', '$rpi_id', '$room_id', '$data')";
    }
    $result = mysqli_query($con, $sql);
  }

  //@param last available datetime
  function update_after($date_time){
    $con = get_con();
    $sql = "";
    if ($date_time == 0){
      $sql = "SELECT * FROM `storage` WHERE 1 ORDER BY `id`";
    }else{
      $sql = "SELECT * FROM `storage` WHERE (`date_time`>'$date_time') ORDER BY `id`";
    }

    $result = mysqli_query($con, $sql);
    if ($result->num_rows > 0) {
        while($row = $result->fetch_assoc()) {
          $row_id = $row['id'];
          $row_date_time = $row['date_time'];
          $row_rpi_id = $row['rpi_id'];
          $row_room_id = $row['room_id'];
          $row_sensor = $row['sensor'];
          $row_data = $row['data'];

          $new_id = $row_date_time ."_". $row_rpi_id ."_". $row_room_id;
          insert_in_v2($new_id, $row_date_time, $row_rpi_id, $row_room_id, $row_sensor, $row_data);
        }
    } else {
      echo "NO ENTRIES FOUND!";
    }
  }

  function transfer_data(){
    $con = get_con();
    $sql = "SELECT `date_time` FROM `storage_v2` ORDER BY `date_time` DESC LIMIT 1";
    $result = mysqli_query($con, $sql);

    if ($result->num_rows > 0) {
        while($row = $result->fetch_assoc()) {
            update_after($row["date_time"]);
        }
    } else {
        // echo "NO ENTRIES FOUND!";
        update_after(0);
    }
  }

  // program execution
  transfer_data();
?>
