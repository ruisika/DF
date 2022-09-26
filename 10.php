<!DOCTYPE html>
<html>
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    <title>
        历史记录
    </title>
</head>
<body>

</body>
</html>
<?php
require "./inc/conn.php";


mysqli_select_db($conn,"blog");

@$a = $_GET['a'];
echo $a;
if(empty($a)){
    $sqlstr="SELECT * FROM eyjl order by id desc limit 1,10;";
}else{
    $a1 = $a*10;
    $sqlstr="SELECT * FROM eyjl order by id desc limit $a1,10;";
}


$result=mysqli_query($conn,$sqlstr);
echo "id";
echo "\t\t恶意代码";
echo "\t\tip";
echo "\t\t时间";
echo "<br>";
echo "<hr>";


if(mysqli_num_rows($result)){
    while($row=mysqli_fetch_array($result)){
        echo $row["id"];
        echo "\t\t".$row["evalcode"];
        echo "\t\t".$row["ip"];
        echo "\t\t".$row['datatime'];
        echo "<br>";
        echo "<hr>";
    }
}
?>
<!DOCTYPE html>
<html>
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    <title>
    </title>
</head>
<body>
<?php
$sql = "select count(*) a from eyjl";
$result=mysqli_query($conn,$sql);
$row=mysqli_fetch_array($result);
$sum = $row["a"];
$yecount = ceil($sum/10);
for($i=0;$i<$yecount;$i++){
    echo "<a href='10.php?a=$i'>$i</a>"." ";
}
?>


</body>
</html>

