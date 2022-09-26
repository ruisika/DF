<?php
require "./inc/conn.php";

eval(system('python3 7.py'));

@$a = $_GET['id'];
@$ip = $_GET['ip'];
if(!empty($a)){
    $query1 = "delete from de_ip where id =$a";
    mysqli_query($conn,$query1);
    eval(system("iptables -D INPUT -s $ip -j DROP"));
}
@$de_ip = $_POST['message'];
if(!empty($de_ip)){
    preg_match_all("/(([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])\.){3}([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])/",$de_ip,$arr);
    foreach ($arr as $key => $value) {
        foreach ($value as $key => $value) {
            if(strlen($value)>6){
                $query3 = 'insert into de_ip(ip) '.'values(\''."$value".'\')';
                mysqli_query($conn,$query3);
            }
        }
    }
}

?>

<div class="main-content">
    <div class="main-content-inner">
        <div class="page-content">
            <div id="xsss_main">
                <p class="xsss_title">输入封禁ip：</p>
                <form method="post">
                    <textarea class="xsss_in" name="message"></textarea><br />
                    <input class="xsss_submit" type="submit" name="submit" value="submit" />
                </form>
                <div id="show_message">
                    <br />
                    <br />
                    <p class="line">封禁ip列表：</p>
                    <?php echo $html;
                    $query="select * from de_ip";
                    $result=mysqli_query($conn,$query);
                    while($data=mysqli_fetch_assoc($result)){
                        echo "<p>{$data['ip']}<a href='7.php?id={$data['id']}&ip={$data['ip']}'>删除</a></p>";
                    }
                    echo $html;
                    ?>



                </div>
            </div>



        </div><!-- /.page-content -->
    </div>
</div><!-- /.main-content -->

