<!DOCTYPE html>
<html>

<body>
    <form method="post">
        Username: <input type="text" name="username"><br>
        ID: <input type="text" name="id"><br>
        <input type="submit" value="Submit">
    </form>

    <?php
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        $user = $_POST['username'];
        $id = $_POST['id'];

        if (empty($id) && !empty($user)) {
            echo "Welcome $user, but ID is required!";
        } elseif (!empty($user) && !empty($id)) {
            echo "Invalid login";
        }
    }
    ?>
</body>

</html>