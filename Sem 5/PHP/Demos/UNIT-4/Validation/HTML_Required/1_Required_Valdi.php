<html>
<body>
  <h2>Registration Form</h2>
  <form action="submit.php" method="post">
    
    <!-- Name -->
    <label for="name">Full Name:</label>
    <input type="text" id="name" name="name" required minlength="3" placeholder="Enter your name">
    <br><br>

    <!-- Email -->
    <label for="email">Email:</label>
    <input type="email" id="email" name="email" required placeholder="example@email.com">
    <br><br>

    <!-- Password -->
    <label for="password">Password:</label>
    <input type="password" id="password" name="password" required minlength="6" maxlength="12" placeholder="6–12 characters">
    <br><br>

    <!-- Phone -->
    <label for="phone">Phone Number:</label>
    <input type="tel" id="phone" name="phone" pattern="[0-9]{10}" required placeholder="10-digit number">
    <br><br>

    <!-- Age -->
    <label for="age">Age:</label>
    <input type="number" id="age" name="age" min="18" max="60" required>
    <br><br>

    <!-- Gender -->
    <label>Gender:</label>
    <input type="radio" name="gender" value="male" required> Male
    <input type="radio" name="gender" value="female" required> Female
    <br><br>

    <!-- Submit -->
    <input type="submit" value="Register">
  </form>
</body>
</html>

