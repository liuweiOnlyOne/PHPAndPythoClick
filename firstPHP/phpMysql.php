<?php
/**
 * Created by PhpStorm.
 * User: LKL
 * Date: 2019/1/10
 * Time: 15:38
 */
$post1=$_POST['inputID'];
//$post1 = 1;
//$arr=array(1);//定义空数组
//1.建立连接
$connect=mysqli_connect('127.0.0.1','root','','test2','3306');
//2.定义sql语句
$sql='select * from account where id ='.$post1;
mysqli_query($connect,'set names utf8');
//3.发送SQL语句
$result=mysqli_query($connect,$sql);
$arr=array();//定义空数组
while($row =mysqli_fetch_row($result)){
    // var_dump($row);
    //array_push(要存入的数组，要存的值)
    array_push($arr,$row);
}

//for ($x=0; $x<count($arr); $x++) {
//    for($y=0;$y<count($arr[$x]);$y++){
//        echo $arr[$x][$y]."   ";
//    }
//    echo "\n";
//}
//4.关闭连接
mysqli_close($connect);

echo json_encode($arr);
?>
