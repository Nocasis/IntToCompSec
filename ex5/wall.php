<?php
    session_start();
    function is_log ()
    {
        alert($_SESSION['username'], $_SESSION['id']);
        if (empty($_SESSION['username']) or empty($_SESSION['id']))
        {
            echo "Вы не вошли, как пользователь";
            alert("Вы не вошли, как пользовтель");
            return false;
        }
        return true;
    }
    ?>
    <html>
    <head>
    <title>Стена для письма.</title>
    </head>
    <body>
    <h2>Стена для письма.</h2>
    <form action="message.php" method="post" onsubmit="return is_log()">

 <p>
    <label>Сообщение:<br></label>
    <input name="msg" type="text" size="32" maxlength="256">
    </p>
    <p>
    <input type="submit" name="submit" value="Написать">
    <br>
    <a href="index.php">Главная страница</a> 
    </p></form>
    <a href="reg.php">Зарегистрироваться</a> 
    </p></form>
    <?php
    if (empty($_SESSION['username']) or empty($_SESSION['id']))
    {
    echo "Вы вошли на сайт, как гость<br><a href='#'>Эта ссылка  доступна только зарегистрированным пользователям</a>";
    }
    else
    {
    echo "Вы вошли на сайт, как ".$_SESSION['username']."<br><a  href='http://google.com/'>Эта ссылка доступна только  зарегистрированным пользователям</a>";
    }
?>
</body>
</html>
