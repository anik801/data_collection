<?php
  function get_con(){
    require "connection.php";
    return $con;
  }

  function get_placements(){
    $con = get_con();
    $sql = "SELECT `rpi_id`, `room_id` FROM `placements` WHERE 1";
    $result = mysqli_query($con, $sql);

    if ($result->num_rows > 0) {
      while($row = $result->fetch_assoc()) {
          echo $row["rpi_id"] . "\t" . $row["room_id"] . "<br>";
      }
    }
  }

  function get_all_sensors(){
    $con = get_con();
    $sql = "SELECT `rpi_id`, `sensor` FROM `sensors` WHERE 1";
    $result = mysqli_query($con, $sql);

    if ($result->num_rows > 0) {
      while($row = $result->fetch_assoc()) {
          echo $row["rpi_id"] . "\t" . $row["sensor"] . "<br>";
      }
    }
  }

  function get_all_placements_as_option(){
    $con = get_con();
    $sql = "SELECT `rpi_id`, `room_id` FROM `placements` WHERE 1";
    $result = mysqli_query($con, $sql);

    if ($result->num_rows > 0) {
      while($row = $result->fetch_assoc()) {
        $rpi_id = $row['rpi_id'];
        $room_id = $row['room_id'];
        echo "<option value = $rpi_id>$rpi_id - $room_id</option>";
      }
    }
  }

  function get_sensors_for_modification(){
    $rpi_id = "m1";
    $con = get_con();
    $sql = "SELECT `id`, `sensor` FROM `sensors` WHERE `rpi_id` = '$rpi_id'";
    $result = mysqli_query($con, $sql);

    if ($result->num_rows > 0) {
      while($row = $result->fetch_assoc()) {
        $sensor_id = $row['id'];
        $sensor_name = $row['sensor'];
        echo "
          <tr>
            <td>
              <label for='$sensor_id'>$sensor_name</label>
            </td>
            <td>??</td>
            <td>??</td>
            <td>
              <input type='button' id='$sensor_id' class='btn btn-danger' value='Delete' class='form-control' onclick='deleteSensor($sensor_id);'>
            </td>
          </tr>
        ";
      }
    }
  }

  function get_rpi_for_modification(){
    $con = get_con();
    $sql = "SELECT `rpi_id`, `room_id` FROM `placements`";
    $result = mysqli_query($con, $sql);

    if ($result->num_rows > 0) {
      while($row = $result->fetch_assoc()) {
        $rpi_id = $row['rpi_id'];
        $room_id = $row['room_id'];

        echo "
          <tr>
            <td>
              $rpi_id
            </td>
            <td>
              $room_id
            </td>
            <td>
              <input type='button' id='$rpi_id' class='btn btn-danger' value='Delete' class='form-control' onclick='deleteRpi($rpi_id);'>
            </td>
          </tr>
        ";
      }
    }
  }
?>
