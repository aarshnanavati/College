<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>L3Q1</title>
</head>

<body>
    <form method="GET">
        <table cellpadding="10">
            <tr>
                <td>Enter the First Number:</td>
                <td><input type="text" name="a" value="<?php if (isset($_GET['a']))
                    echo $_GET['a']; ?>"></td>
            </tr>
            <tr>
                <td>Enter the Second Number:</td>
                <td><input type="text" name="b" value="<?php if (isset($_GET['b']))
                    echo $_GET['b']; ?>"></td>
            </tr>
            <tr>
                <td colspan="2"><button type="submit">Add</button></td>
            </tr>
            <tr>
                <td>Sum =</td>
                <td>
                    <input type="text" value="<?php
                    if (isset($_GET['a']) && isset($_GET['b']))
                        echo $_GET['a'] + $_GET['b'];
                    ?>" readonly>
                </td>
            </tr>
        </table>
    </form>
</body>

</html>