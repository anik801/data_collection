<?php
  require "connection.php";

  if(isset($_GET['rpi_id'])){
    $rpi_id = $_GET['rpi_id'];
    $sql = "SELECT `id`, `sensor`, `type`, `pin` FROM `sensors` WHERE `rpi_id` = '$rpi_id'";
    $result = mysqli_query($con, $sql);

    if ($result->num_rows > 0) {
      echo "
      <table class='table table-sm' id='sensor_modify_table'>
      <tbody>
      <tr>
        <th>Sensor</th>
        <th>Type</th>
        <th>Pin #</th>
        <th>Action</th>
      </tr>
      ";
      while($row = $result->fetch_assoc()) {
        $sensor_id = $row['id'];
        $sensor_name = $row['sensor'];
        $type = $row['type'];
        $pin = $row['pin'];
        echo "
          <tr>
            <td>
              $sensor_name
            </td>
            <td>
              $type
            </td>
            <td>
              $pin
            </td>
            <td>
              <input type='button' id='$sensor_id' class='btn btn-danger btn-sm' value='Delete' class='form-control' onclick='deleteSensor($sensor_id);'>
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
