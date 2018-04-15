<?php
    session_start();
if (isset($_POST['username'])) 
    { 
        $username = $_POST['username'];
        if ($username == '') 
            {
                unset($username);
            }
    }
    
    if (isset($_POST['password']))
    {
    $password=$_POST['password'];
        if ($password =='') 
        {
            unset($password);
        }
    }
    
    if (empty($username) or empty($password))
    {
    exit ("Вы ввели не всю информацию, вернитесь назад и заполните все поля!");
    }

    //$username = stripslashes($username);//Удалить 
    //$username = htmlspecialchars($username);
    //$password = stripslashes($password);
    //$password = htmlspecialchars($password);
    //$username = trim($username);
    //$password = trim($password);
    
    include ("bd.php");
    $result = mysqli_query($db,"SELECT * FROM users WHERE (username='$username') and (password='$password');");
    //exit("SELECT * FROM users WHERE username='$username';");
    $myrow = mysqli_fetch_array($result);
    //exit($myrow);
    
    if (empty($myrow['password']))
    {
    exit ("Извините, введённый вами имя пользователя или пароль неверный.<br>");
    }
    else
    {
            $_SESSION['username']=$myrow['username']; 
            $_SESSION['id']=$myrow['id'];
            echo "Вы успешно вошли на сайт! <br> <a href='index.php'>Главная страница</a>";
    }
?>
