<?php

// Зачем этот коментарий? 
/*
CREATE TABLE `message` (
`remote_addr` TEXT NOT NULL ,
`user_agent` TEXT NOT NULL ,
`name` TEXT NOT NULL ,
`text` TEXT NOT NULL
) ENGINE = MYISAM ;  //Тип хранения MYISAM
INSERT INTO `message` (`remote_addr`, `user_agent`, `name`, `text`) VALUES('127.0.0.0', 'Fire Walk With Me', 'test name', 'test text');
INSERT INTO `message` (`remote_addr`, `user_agent`, `name`, `text`) VALUES('127.0.0.0', 'Abandon all hope, ye who enter here', 'test name2', 'test text2');
*/

$link = mysql_connect("localhost", "root", "");//Коннект, Нет проверки на успешность коннекта, ошибка логики? 
mysql_select_db("positive", $link);// Выбор бд
$ip = $_SERVER["REMOTE_ADDR"];
if(isset($_SERVER["HTTP_X_REAL_IP"])) 
{
   $ip = $_SERVER["HTTP_X_REAL_IP"];
}
$ip = addslashes($ip);//Экранирование
$user_agent = addslashes($_SERVER["HTTP_USER_AGENT"]);//Экранирование
$ip = substr($ip, 0, 15); // max length 15  // Тут неуверенно, зачем это ваще?
if(isset($_POST["name"]) && isset($_POST["text"])) 
{
   $text = addslashes($_POST["text"]);//Экранирование
   $name = addslashes($_POST["name"]);//Экранирование
   $query = mysql_query("INSERT INTO `message` (`remote_addr`, `user_agent`, `name`, `text`) VALUES('{$ip}', '{$user_agent}', '{$name}', '{$text}');", $link);
}//возможно с $ip
$query = mysql_query("SELECT * FROM `message`;", $link);
echo("<table>");
while($row = mysql_fetch_assoc($query)) // Выводит все именна и данные
{
   echo("<tr><td>{$row["name"]}</td><td>{$row["text"]}</td></tr>");
}
echo("</table>");
?>
