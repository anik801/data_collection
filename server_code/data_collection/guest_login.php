<?php
  ob_start();
  session_start();
  $_SESSION['bdl_user']="guest";
  header('Location: index.php');
?>
