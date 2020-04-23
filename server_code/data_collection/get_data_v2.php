<?php
  require "connection.php";

  // //query to get data from the table
  // $query = sprintf("SELECT userid, facebook, twitter, googleplus FROM followers");
  //
  // //execute query
  // $result = $con->query($query);
  //
  // //loop through the returned data
  // $data = array();
  // foreach ($result as $row) {
  //   $data[] = $row;
  // }
  //
  // //free memory associated with result
  // $result->close();
  //
  // //close connection
  // $con->close();
  //
  // //now print the data
  // print json_encode($data);

  if (isset($_GET['sensor'])) {
    $sensor = $_GET['sensor'];

    $rpi_id = 'm1';
    $room_id = 'r1';
    // $sensor = 'sound';

    $sql = "SELECT userid, facebook, twitter, googleplus FROM followers";

    // $sql = "SELECT `date_time`, `$sensor` FROM `storage_v2` WHERE (`rpi_id`='$rpi_id' AND `room_id`='$room_id') ORDER BY `date_time`";
    $result = mysqli_query($con, $sql);

    if ($result->num_rows > 0) {
      $data = array();

      for ($x = 0; $x < mysqli_num_rows($result); $x++) {
          $data[] = mysqli_fetch_assoc($result);
      }

      echo json_encode($data);
        //
        // while($row = $result->fetch_assoc()) {
        //     echo $row["sound"] . "<br>";
        // }
    } else {
        echo "0";
    }
  }

?>
