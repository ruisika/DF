<?php
require "./inc/conn.php";

$sql1 = "select status from status where id=1";
$sql2 = "select status from status where id=2";
$resu1 = mysqli_query($conn,$sql1);
$resu2 = mysqli_query($conn,$sql2);
$stust1 = mysqli_fetch_array($resu1);
$stust2 = mysqli_fetch_array($resu2);
$res1 = $stust1['status'];
$res2 = $stust2['status'];

if($res1==0){
//    eval(system('python3 5.py'));
    $sql3 = "UPDATE status set status=1 where id=1";
    $resu3 = mysqli_query($conn,$sql3);
    var_dump($resu3);
    echo "11";
}else{
//    eval(system('python3 kill_id1'));
    $sql3 = "UPDATE status set status=0 where id=1";
    $resu3 = mysqli_query($conn,$sql3);
    echo "123";
}

header("Location:index.php");

?>