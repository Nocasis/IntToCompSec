<?php
    $db = mysqli_connect('localhost', 'Nocasis', 'HeHe1234') or die('Не удалось соединиться: ' . mysqli_error());
    echo "Соединение успешно установлено. <br>";
    mysqli_select_db($db, "ex5") or die('Не удалось соединиться: ' . mysqli_error());//die('Не удалось выбрать базу данных');
?>
