<?php
  function get_con(){
    require "connection.php";
    return $con;
  }

  function insert_rows_from_csv($file_name){
    set_time_limit(3600); ## long time for larger files

    $con = get_con();

    $csvFile = file($file_name);
    $i = 0;
    $keys = [];
    foreach ($csvFile as $line) {
      $i = $i + 1;
      if($i == 1){
        $keys = str_getcsv($line);
        $keys_len = sizeof($keys);
      }else{
        $row = str_getcsv($line);

        $fields = "";
        $values = "";
        for($i=0; $i<$keys_len; $i++){
          if($i == $keys_len-1){
            $fields .= "`" . $keys[$i] . "`";
            $values .= "'" . $row[$i] . "'";
          }else{
            $fields .= "`" . $keys[$i] . "`,";
            $values .= "'" . $row[$i] . "',";
          }
        }

        $rpi_id = $row[2];
        $table_name = "rpi_" . $rpi_id;

        $sql = "INSERT INTO `$table_name`($fields) VALUES ($values)";
        $result = mysqli_query($con, $sql);
      }
    }
  }

  /// Executable funtion ////////////////////////////////////////////////
  $file_name = "test_file";

  if(isset($_FILES['file'])){
    // echo "1";
    $received = $_FILES['file'];
    // echo $received;

    $uploaddir = 'data/';
    $uploadfile = $uploaddir . basename($_FILES['file']['name']);

    if (move_uploaded_file($_FILES['file']['tmp_name'], $uploadfile)) {
        // echo "File is valid, and was successfully uploaded.\n";
        // file successfully uploaded
        insert_rows_from_csv($uploadfile);
        echo "0";
    } else {
        echo "1";
    }

  }else{
    echo "1";
  }

?>
