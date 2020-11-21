<?php require "connection.php";
  if(isset($_GET['rpi_id'])){
    $rpi_id = $_GET['rpi_id'];

    $sql = "SELECT `sensor`, `type`, `pin` FROM `sensors` WHERE `rpi_id`='$rpi_id' ORDER BY `sensor`";
    $result = mysqli_query($con, $sql);

    $records = array();
    while($row = mysqli_fetch_assoc($result)) {
        $records[] = $row;
    }
    // echo $records;
    echo json_encode($records);
  }
?>
