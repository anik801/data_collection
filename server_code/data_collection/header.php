<?php


header("Cache-Control: no-cache, no-store, must-revalidate"); // HTTP 1.1.
header("Pragma: no-cache"); // HTTP 1.0.
header("Expires: 0"); // Proxies.
?>

<html>
  <head>
    <meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate">
    <meta http-equiv="Pragma" content="no-cache">
    <meta http-equiv="Expires" content="0">

    <title>Building Data Lite</title>
    <link rel="icon" href="images/icon.ico">
    <link rel="stylesheet" href="stylesheet.css">
    <script type="text/javascript" src="js/jquery-3.5.0.js"></script>
    <script type="text/javascript" src="js/scripts.js"></script>

    <script src="lib/bootstrap.js"></script>
    <link href="lib/bootstrap.css" rel="stylesheet">
    <link rel="stylesheet" type="stylesheet" href="lib/bootstrap-theme.css">

    <?php require "helperMethods.php"; ?>
  </head>
<body>

<div id="title_div">
  <a id="title_text" href="index.php">Building Data Lite</a>
</div>
