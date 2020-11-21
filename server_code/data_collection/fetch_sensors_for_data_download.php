<?php
  require "connection.php";
  if(isset($_GET['rpi_id'])){
    $rpi_id = $_GET['rpi_id'];
    $sql = "SELECT `id`, `sensor` FROM `sensors` WHERE `rpi_id` = '$rpi_id'";
    $result = mysqli_query($con, $sql);

    if ($result->num_rows > 0) {
      echo "
      <table class='table table-sm' id='sensor_modify_table'>
      <tbody>
      <tr>
        <th>Sensor</th>
        <th>Select</th>
      </tr>
      ";

      while($row = $result->fetch_assoc()) {
        $sensor_id = $row['id'];
        $sensor_name = $row['sensor'];
        echo "
          <tr>
            <td>
              <label for='$sensor_id'>$sensor_name</label>
            </td>
            <td>
              <input type='checkbox' id='$sensor_name' name='sensor_checkbox' value='$sensor_name' class='form-control'>
            </td>
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
