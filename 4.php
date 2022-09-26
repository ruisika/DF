<?php
require "./inc/conn.php";

eval(system('python3 4.py'));

$file_path = "D:\\WBED\\PHPTutorial\\WWW\\2.txt";
if (file_exists($file_path)) {
    $fp = fopen($file_path, "r");
    $str = fread($fp, filesize($file_path));//指定读取大小，这里把整个文件内容读取出来
    echo $str = str_replace("\r\n", "<br />", $str);
}
?>