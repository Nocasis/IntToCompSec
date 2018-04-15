<?php
 if (isset($_GET['redirect'])) {
     header('Location: '.$_GET['redirect']);
 }
 header('Set-Cookie: _afUserId='. $_GET['userId']);//То что мы отправляем в хедарах, мы можем менять -> 14 строка
 header('Set-Cookie: _afGroupId='. $_GET['groupId']);
 ?>
 <html>
 <head>
     <meta http-equiv="refresh" content="5;url=<?=$_GET['url']?>"></meta> //Возможо тут что то с get
 </head>
 <body>
       <?php
           $roleId = explode(":", base64_decode($_COOKIE['roleId']))[0]; // Можем как то заенкодить в куки admin:(перед любыми куками). и получим доступ к admin_interface.php
           if ($roleId == 'admin') {
               include 'admin_interface.php';
           }
           elseif ($roleId == 'user') {
               include 'user_interface.php'
           }
           else {
               echo '<h2>Unknown role '.$roleId.'\n</h2>';
           }
       ?>

 </body>
 </html>
