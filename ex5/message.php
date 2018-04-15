<?php
    session_start();

    if (isset($_POST['msg'])) 
    { 
        $msg = $_POST['msg'];
        if ($msg == '') 
            {
                unset($msg);
            }
    }
    
    /*if (empty($_SESSION['username']) or empty($_SESSION['id']))
        {
            exit ("Вы не вошли, как пользователь.");
        }
*/
    if (empty($msg))
    {
    exit ("Вы ввели пустое сообщение!");
    }
    
    //$msg = stripslashes($msg);
    //$msg = htmlspecialchars($msg);
    //$msg = trim($msg);
    echo "Вы написали: <br>".$msg;

?>
