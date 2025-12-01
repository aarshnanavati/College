<?php
if(isset($_POST['Color']))
{
	foreach ($_POST['Color'] as $val)
	{
		echo "You have selected :" .$val; // Displaying Selected Value
	}
}
?>
<form action="<?php $_PHP_SELF ?>" method="post">
<select name="Color[]" size = 5 multiple>
<option value="Red">Red</option>
<option value="Green">Green</option>
<option value="Blue">Blue</option>
<option value="Pink">Pink</option>
<option value="Yellow">Yellow</option>
</select>
<input type="submit" name="submit" value="Get Selected Values" />
</form>


