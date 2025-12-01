<form action="action_page.php">
    <input type="text" name="username" placeholder="Username" pattern="[a-z]{1,15}">
<input type="submit">
<!--
[a-z] → allows only lowercase letters from a to z.

{1,15} → means the input must be at least 1 character long and at most 15 characters long.
Hello (capital H, uppercase not allowed)

hello123 (numbers not allowed)

hello_world (special character _ not allowed)

`` (empty input, unless field is optional and required is not set)

abcdefghijklmnop (16 characters, exceeds 15)
-->

</form>

