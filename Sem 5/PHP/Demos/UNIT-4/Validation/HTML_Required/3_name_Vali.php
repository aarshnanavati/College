<form action="action_page.php" method="POST">
 <label for="username">Username <i>(letters and numbers only, no  punctuation or special characters)</i></label><br>
 <input name="username" id="username" pattern="[A-Za-z0-9]+">
</form>

<?php

/*[a-zA-Z0-9]+ is a pattern that matches against a string of any length, as long as the string contains only lowercase letters (a-z), uppercase letters (A-Z), or numerals (0-9).*/



/*
Only letters (either case), numbers, and the underscore; no more than 15 characters.  [A-Za-z0-9_]{1,15} 


*/

/*
Only letters (either case), numbers, hyphens, underscores, and periods. (Not the slash character, that is being used to escape the period.) The username must start with a letter and must be between 1 and 20 characters long (inclusive).  [a-zA-Z][a-zA-Z0-9-_.]{1,20} 


*/

/*

Phone number: <input type="text" required pattern="(\+?\d[- .]*){7,13}" title="international, national or local phone number"/>*/	

?>




