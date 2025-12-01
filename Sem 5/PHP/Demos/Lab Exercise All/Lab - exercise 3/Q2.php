<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>L3Q2</title>
    <style>
        input {
            margin: 5px 0px;
        }
    </style>
</head>

<body>
    <div style="display:flex;">
        <form action="" method="GET">
            <table>
                <tr>
                    <td colspan="2">
                        <h1>School ID Registration Form</h1>
                    </td>
                </tr>
                <tr>
                    <td colspan="2">
                        <p style="font-weight:bolder">Name</p>
                    </td>
                </tr>
                <tr>
                    <td>
                        <input style="margin-right:" type="text" name="first" id="">
                        <br>
                        <span>First</span>
                    </td>
                    <td>
                        <input style="margin-right:10px" type="text" name="last" id="">
                        <br>
                        <span>Last</span>
                    </td>
                </tr>
                <tr>
                    <td>
                        <p style="font-weight:bolder">Expected Year of Graduation</p>
                        <input type="text" name="year">
                    </td>
                </tr>
                <tr>
                    <td colspan="2">
                        <p style="font-weight:bolder">Address</p>
                        <input type="text" name="address1" id=""><br>
                        <label for="">Street Address</label><br>
                        <input type="text" name="address2" id=""><br>
                        <label for="">Address Line 2</label>
                    </td>
                </tr>
                <tr>
                    <td><button type="submit" style="margin-top:10px">Submit</button></td>
                </tr>
            </table>
        </form>
        <table>
            <tr>
                <td colspan="2">
                    <h1>School ID Registration Form (copy)</h1>
                </td>
            </tr>
            <tr>
                <td colspan="2">
                    <p style="font-weight:bolder">Name</p>
                </td>
            </tr>
            <tr>
                <td>
                    <input style="margin-right:" type="text" name="first" id="" disabled="true" value=<?php
                    if (isset($_GET['first']))
                        echo $_GET['first']
                            ?>>
              <br>
                        <span>First</span>
                    </td>
                    <td>
                        <input style="margin-right:10px" type="text" name="last" id="" disabled="true" value=<?php
                    if (isset($_GET['last']))
                        echo $_GET['last']
                            ?>>
              <br>
                        <span>Last</span>
                    </td>
                </tr>
                <tr>
                    <td>
                        <p style="font-weight:bolder">Expected Year of Graduation</p>
                        <input type="text" name="year" disabled="true" value=<?php
                    if (isset($_GET['year']))
                        echo $_GET['year']
                            ?>>
            </td>
                </tr>
                <tr>
                    <td colspan="2">
                        <p style="font-weight:bolder">Address</p>
                        <input type="text" name="address1" id="" disabled="true" value=<?php
                    if (isset($_GET['address1']))
                        echo $_GET['address1']
                            ?>><br>
              <label for="">Street Address</label><br>
                        <input type="text" name="address2" id="" disabled="true" value=<?php
                    if (isset($_GET['address2']))
                        echo $_GET['address2']
                            ?>><br>
              <label for="">Address Line 2</label>
                    </td>
                </tr>
            </table>
        </div>

    </body>

    </html>