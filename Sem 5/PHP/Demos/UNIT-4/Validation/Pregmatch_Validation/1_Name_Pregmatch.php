<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $name = $_POST['name'];

    // Regex: only lowercase letters, 1 to 15 characters
    if (preg_match("/^[a-z]{1,15}$/", $name)) {
        echo "Valid name: " . htmlspecialchars($name);
    } else {
        echo "Invalid name. Please enter only lowercase letters (1–15 characters).";
    }
}
?>

<html>
<body>
    <h2>Enter Your Name</h2>
    <form method="post">
        <input type="text" name="name" required>
        <input type="submit" value="Validate">
    </form>
</body> 

<!--Explanation of regex /^[a-z]{1,15}$/

^ → start of string

[a-z] → only lowercase alphabets allowed

{1,15} → between 1 and 15 characters long

$ → end of string

So input like bharti passes, but Bharti123 fails.
-->
</html>


