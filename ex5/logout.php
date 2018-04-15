<?php
   session_start();
   unset($_SESSION["username"]);
   unset($_SESSION["id"]);
   
   echo 'Сессия чиста';
   header('Refresh: 1; URL = index.php');
?>
