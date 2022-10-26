<?php 
$day=(int)$_POST['day'];
$time=(int)$_POST['time'];
$id=$_POST['id'];

$content = file_get_contents('test.txt');

$days=explode("\n", $content);
$times=explode(',', $days[$day]);
$times[$time].=$id;
$days[$day]=join(',', $times);
$content=join("\n",$days);

file_put_contents('test.txt', $content);
//header("Expires: Mon, 20 Feb 2005 20:12:03 GMT"); //Didnt try this one yet, maybe it works better than js cache work-around? :)
header('Location: http://tjemsland.rf.gd/demo');
?>  