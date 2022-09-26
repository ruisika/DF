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

if($res2==0){
//    eval(system('python3 6.py'));
    $sql3 = "UPDATE status set status=1 where id=2";
    $resu3 = mysqli_query($conn,$sql3);
    echo "11";
}else{
//    eval(system('python3 kill_id2'));
    $sql3 = "UPDATE status set status=0 where id=2";
    $resu3 = mysqli_query($conn,$sql3);
    echo "123";
}

header("Location:index.php");

?>