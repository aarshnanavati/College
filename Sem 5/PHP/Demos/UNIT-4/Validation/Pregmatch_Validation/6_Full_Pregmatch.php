<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $username = $_POST['username'];
    $email = $_POST['email'];
    $mobile = $_POST['mobile'];
    $pincode = $_POST['pincode'];
    $date = $_POST['date'];
    $url = $_POST['url'];
    $password = $_POST['password'];

    echo "<h3>Validation Results:</h3>";

    // Username: letters, numbers, underscore, 3–16 chars
    if (preg_match("/^[A-Za-z0-9_]{3,16}$/", $username)) {
        echo "Username is valid<br>";
    } else {
        echo " Invalid Username (3–16 chars, letters/numbers/_)<br>";
    }

    // Email
    if (preg_match("/^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$/", $email)) {
        echo "Email is valid<br>";
    } else {
        echo "Invalid Email<br>";
    }

    // Mobile: 10 digits
    if (preg_match("/^[0-9]{10}$/", $mobile)) {
        echo "Mobile number is valid<br>";
    } else {
        echo "Invalid Mobile (must be 10 digits)<br>";
    }

    // PIN Code: Indian 6-digit
    if (preg_match("/^[1-9][0-9]{5}$/", $pincode)) {
        echo "PIN Code is valid<br>";
    } else {
        echo "Invalid PIN Code (6 digits, cannot start with 0)<br>";
    }

    // Date: DD-MM-YYYY
    if (preg_match("/^(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[0-2])-[0-9]{4}$/", $date)) {
        echo "Date format is valid<br>";
    } else {
        echo "Invalid Date (use DD-MM-YYYY)<br>";
    }

    // URL
    if (preg_match("/\bhttps?:\/\/[A-Za-z0-9.-]+\.[A-Za-z]{2,}(\/\S*)?/", $url)) {
        echo "URL is valid<br>";
    } else {
        echo "Invalid URL (must start with http/https)<br>";
    }

    // Password: min 8 chars, upper, lower, number, special char
    if (preg_match("/^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$/", $password)) {
        echo " Password is strong<br>";
    } else {
        echo " Weak Password (Min 8 chars, 1 upper, 1 lower, 1 number, 1 special)<br>";
    }
}
?>

<html>
<body>
    <h2>Form Validation using preg_match()</h2>
    <form method="post">
        <label>Username:</label>
        <input type="text" name="username" required><br><br>

        <label>Email:</label>
        <input type="text" name="email" required><br><br>

        <label>Mobile:</label>
        <input type="text" name="mobile" required><br><br>

        <label>PIN Code:</label>
        <input type="text" name="pincode" required><br><br>

        <label>Date (DD-MM-YYYY):</label>
        <input type="text" name="date" required><br><br>

        <label>Website URL:</label>
        <input type="text" name="url" required><br><br>

        <label>Password:</label>
        <input type="password" name="password" required><br><br>

        <input type="submit" value="Validate">
    </form>
</body>
</html>

