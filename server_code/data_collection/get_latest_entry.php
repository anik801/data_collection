<?php
  require "connection.php";
  if(isset($_GET['rpi_id'])){
    $rpi_id = htmlspecialchars($_GET["rpi_id"]);

    $table_name = "rpi_" . $rpi_id;

    $sql = "SELECT `date_time` FROM `$table_name` ORDER BY `date_time` DESC LIMIT 1";
    $result = mysqli_query($con, $sql);

    if ($result->num_rows > 0) {
        while($row = $result->fetch_assoc()) {
            echo $row["date_time"];
        }
    } else {
        echo "0";
    }
  }
?>
