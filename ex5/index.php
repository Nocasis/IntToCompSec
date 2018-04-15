<?php
    session_start();
    ?>
    <html>
    <head>
    <title>Главная страница</title>
    </head>
    <body>
    <h2>Главная страница</h2>
    <form action="testreg.php" method="post">

    <!--****  testreg.php - это адрес обработчика. То есть, после нажатия на кнопку  "Войти", данные из полей отправятся на страничку testreg.php методом  "post" ***** -->
 <p>
    <label>Ваш логин:<br></label>
    <input name="username" type="text" size="16" maxlength="32">
    </p>


 
    <p>

    <label>Ваш пароль:<br></label>
    <input name="password" type="password" size="16" maxlength="64">
    </p>


    <p>
    <input type="submit" name="submit" value="Войти">

    <!--**** Кнопочка (type="submit") отправляет данные на страничку testreg.php ***** --> 
    <br>
    <!--**** ссылка на регистрацию, ведь как-то же должны гости туда попадать ***** --> 
    <a href="reg.php">Зарегистрироваться</a> 
    </p></form>
    <a href="wall.php">Стена</a> 
    </p></form>
    <a href="logout.php">Выйти</a> 
    </p></form>
    <br>
    <?php
    if (empty($_SESSION['username']) or empty($_SESSION['id']))
    {
    echo "Вы вошли на сайт, как гость<br><a href='#'>Эта ссылка  доступна только зарегистрированным пользователям</a>";
    }
    else
    {
    echo "Вы вошли на сайт, как ".$_SESSION['username']."<br><a  href='http://localhost:1337'>Эта ссылка доступна только  зарегистрированным пользователям</a>";
    }
?>
</body>
</html>
