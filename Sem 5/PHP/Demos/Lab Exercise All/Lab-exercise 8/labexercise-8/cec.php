<?php
session_start();
$error = "";
$success = "";

// Handle Registration
if (isset($_POST['register'])) {
    $username = trim($_POST['username']);
    $password = $_POST['password'];
    $phone = $_POST['phone'];
    $email = $_POST['email'];

    // Validation
    if (empty($username) || empty($password) || empty($phone) || empty($email)) {
        $error = "All fields are required!";
    } elseif (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        $error = "Invalid email format!";
    } elseif (!preg_match("/^[0-9]{10}$/", $phone)) {
        $error = "Phone number must be exactly 10 digits!";
    } elseif (strlen($password) < 8 || !preg_match("/[!@#$%^&*(),.?\":{}|<>]/", $password)) {
        $error = "Password must be at least 8 characters and contain a special character!";
    } else {
        $_SESSION['user'] = [
            "username" => $username,
            "password" => $password,  // ⚠ normally you'd hash this
            "phone" => $phone,
            "email" => $email
        ];
        $success = "✅ Registration successful!<br>
                   <strong>Username:</strong> $username <br>
                   <strong>Email:</strong> $email <br>
                   <strong>Phone:</strong> $phone";
    }
}
?>
<!DOCTYPE html>
<html>

<head>
    <title>My Website</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: #f0f2f5;
            margin: 0;
            padding: 0;
        }

        header {
            background: #007BFF;
            color: white;
            padding: 20px;
            text-align: center;
            font-size: 26px;
            font-weight: bold;
            letter-spacing: 1px;
        }

        .container {
            width: 450px;
            margin: 40px auto;
            background: #fff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 0 10px #aaa;
        }

        h2 {
            text-align: center;
            margin-bottom: 10px;
            color: #333;
        }

        form {
            margin: 20px 0;
        }

        input {
            width: 100%;
            padding: 10px;
            margin: 8px 0;
            border: 1px solid #ccc;
            border-radius: 5px;
        }

        .btn {
            background: #007BFF;
            color: white;
            border: none;
            padding: 10px;
            cursor: pointer;
            border-radius: 5px;
        }

        .btn:hover {
            background: #0056b3;
        }

        .error {
            color: red;
            text-align: center;
            font-weight: bold;
        }

        .success {
            color: green;
            text-align: center;
            font-weight: bold;
            line-height: 1.6;
        }
    </style>
</head>

<body>
    <header>📋 My Website</header>

    <div class="container">
        <h2>Register</h2>
        <?php if ($error)
            echo "<p class='error'>$error</p>"; ?>
        <?php if ($success)
            echo "<p class='success'>$success</p>"; ?>

        <!-- Registration Form -->
        <form method="post">
            <input type="text" name="username" placeholder="Username" required>
            <input type="email" name="email" placeholder="Email" required>
            <input type="text" name="phone" placeholder="Phone Number (10 digits)" maxlength="10" required>
            <input type="password" name="password" placeholder="Password (min 8 chars & special char)" required>
            <input type="submit" class="btn" name="register" value="Register">
        </form>
    </div>
</body>

</html>