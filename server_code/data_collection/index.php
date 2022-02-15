<?php
  ob_start();
  session_start();
?>

<?php require "header.php"; ?>

  <div id="main_body_div">
  <?php
    require "main_body.php";
  ?>
  </div>

  <?php
    if(isset($_SESSION['bdl_user'])){
      $session_type = $_SESSION['bdl_user'];

      if($session_type == "guest"){
        echo'
          <script type="text/javascript">
            showGuestPage();
          </script>
        ';
      }else if($session_type == "user"){
        echo'
          <script type="text/javascript">
            showUserPage();
          </script>
        ';
      }
    }else{
      require "login.php";
    }
  ?>



  <!-- javascript -->
  <script type="text/javascript" src="js/Chart.js"></script>
<?php require "footer.php"; ?>
