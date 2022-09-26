
<?php
require './inc/checklogin.php';
require './inc/conn.php';
$sql1 = "select status from status where id=1";
$sql2 = "select status from status where id=2";
$resu1 = mysqli_query($conn,$sql1);
$resu2 = mysqli_query($conn,$sql2);
$stust1 = mysqli_fetch_array($resu1);
$stust2 = mysqli_fetch_array($resu2);
$res1 = $stust1['status'];
$res2 = $stust2['status'];
?>
<!DOCTYPE html>
<html>
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    <title>
        后台
    </title>
</head>
<body>
<p align="center"><a href="./1.php">
        <button>1.日志入侵检测(基于机器学习)</button>
    </a><br></p>
<p align="center"><a href="./2.php">
        <button>2.ssh入侵检测</button>
    </a><br></p>
<p align="center"><a href="3.php">
        <button>3.webshell在线查杀</button>
    </a><br></p>
<p align="center"><a href="4.php">
        <button>4.sql或xss日志检测</button>
    </a><br></p>
<!--<p align="center">5.webshell防护<a href="5.php">-->
<!--        <button>--><?php //if($res1==0){
//            echo "关闭";
//            }else{
//            echo "开启";
//            }
//            ?><!--</button>-->
<!--    </a><br></p>-->
<!--<p align="center">6.sqlxss防护<a href="6.php">-->
<!--        <button>--><?php //if($res2==0){
//                echo "关闭";
//            }else{
//                echo "开启";
//            }
//            ?><!--</button>-->
<!--    </a><br></p>-->

<p align="center"> <a href="7.php">
        <button>5.封禁ip</button>
    </a><br></p>

<!--<form action="" method="post" style="text-align: center">-->
<!--    <input type="button" value="运行" name=""/><br>-->
<!--</form>-->

<p style="text-align: center"><a href="10.php">历史查询</a></p>
</body>
</html>
