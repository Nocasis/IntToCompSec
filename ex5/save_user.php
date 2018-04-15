<?php
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
        exit ("Вы ввели не всю информацию, вернитесь назад и заполните все поля!<br>");
    }
    //$username = stripslashes($username);
    //$username = htmlspecialchars($username);
    //$password = stripslashes($password);
    //$password = htmlspecialchars($password);
    //$username = trim($username);
    //$password = trim($password);
 
 // подключаемся к базе
    include ("bd.php");
    $result = mysqli_query($db,"SELECT id FROM users WHERE username='$username';");
    $myrow = mysqli_fetch_array($result);
    
    if (!empty($myrow['id'])) 
    {
        exit ("Извините, введённый вами логин уже зарегистрирован. Введите другой логин.<br>");
    }
    $result2 = mysqli_query ($db,"INSERT INTO users (username,password) VALUES('$username','$password');");
    if ($result2=='TRUE')
    {
        echo "Вы успешно зарегистрированы! Теперь вы можете зайти на сайт. <a href='index.php'>Главная страница</a>";
    }
 else 
    {
        echo "Ошибка! Вы не зарегистрированы.<br>";
    }
    ?>
