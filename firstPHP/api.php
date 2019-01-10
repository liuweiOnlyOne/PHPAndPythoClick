<?php
/**
 * Created by PhpStorm.
 * User: LKL
 * Date: 2019/1/10
 * Time: 15:29
 */
$post1=$_POST['post1'];
$post2=$_POST['post2'];
$post1=$post1."+echo2";
$post2=$post2."+echo2";
$array=array($post1, $post2);
echo json_encode($array);
?>
