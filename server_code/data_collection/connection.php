<?php
  // $host="localhost";
  // $username="buildlt7_admin21";
  // $password="rkcBTXKwXEnpC78";
  // $database="buildlt7_room_data";
  // $con = mysqli_connect($host,$username,$password,$database);
  // if(!$con){
  //   die("Can not connect: ".mysql_error());
  // }
  // mysqli_select_db($con, $database);

  $host="localhost";
  $username="root";
  $password="";
  $database="room_data";
  $con = mysqli_connect($host,$username,$password,$database);
  if(!$con){
    die("Can not connect: ".mysql_error());
  }
  mysqli_select_db($con, $database);
?>
