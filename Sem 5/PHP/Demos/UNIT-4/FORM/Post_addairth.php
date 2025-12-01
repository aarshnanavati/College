
<?php		
if(isset($_POST['add']))
{
$x=$_POST['fnum'];		
$y=$_POST['snum'];				
$sum=$x+$y;		 
echo "Result:<input type='text' value='$sum'/>";			
}
?>
	
<body>
<form action="<?php $_PHP_SELF ?>"  method="post" >
Enter first number <input type="text" name="fnum"/><hr/>
Enter second number <input type="text" name="snum"/><hr/>	   		   
<input type="submit"  name="add" value="ADD"/>
</form>
</body>
