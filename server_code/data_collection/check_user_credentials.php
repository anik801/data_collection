<?php
  ob_start();
  session_start();
?>


<?php
  require "connection.php";

  if(isset($_GET['username']) && isset($_GET['password'])){
    $username = $_GET['username'];
    $password = $_GET['password'];

    $hash = hash('sha512', $password);

    $sql = "SELECT `id` FROM `users` WHERE (`username`='$username' AND `password_hash`='$hash')";
    $result = mysqli_query($con, $sql);

    $response = new stdClass();

    if ($result->num_rows > 0) {
      $response->available = true;
      $_SESSION['bdl_user']="user";
    }else{
      $response->available = null;
      $_SESSION['bdl_user']="guest";
    }

    header('Content-type: application/json');
    echo json_encode($response);

  }
?>
