<?php
   session_start();
   unset($_SESSION["username"]);
   unset($_SESSION["id"]);
   
   echo 'Сессия чиста';
   header('Refresh: 2; URL = index.php');
?>
