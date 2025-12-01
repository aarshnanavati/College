<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>L5Q1</title>
    <style>
        table,
        td,
        th {
            border: 1px solid black;
            border-collapse: collapse;
        }

        td,
        th {
            padding: 5px;
            font-size: 20px;
        }
    </style>
</head>

<body>
    <h1 style="font-size: 30px;">Product Catalog</h1>
    <form action="" method="GET">
        <?php
        $products = [
            ["Starters", "Spring Roll", 120],
            ["Starters", "Panner Tikka", 180],
            ["Main Course", "Butter Panner", 250],
            ["Main Course", "Veg Briyani", 200],
            ["Dessert", "Gulab Jamun", 60],
            ["Dessert", "Ice Cream", 80],
        ];

        // Printing the first table, displaying all the items.
        echo "<table><tr><th>Category</th><th>Item</th><th>Price</th><th>Quantity</th></tr>";
        for ($i = 0; $i < count($products); $i++) {
            echo "<tr>";
            for ($j = 0; $j < count($products[$i]); $j++) {
                echo "<td>" . $products[$i][$j] . "</td>";
            }
            echo "<td><input type=\"number\" name=\"" . $i . "\"/> </td>";
            echo "</tr>";
        }

        echo "</table>";
        ?>
        <br />
        <br />
        <button type="submit">Submit</button>
    </form>


    <?php

    if ($_GET) {
        // Printing the first table, displaying all the items.
        echo "<h1 style=\"font-size: 30px;\">Bill</h1>";
        echo "<table><tr><th>Item</th><th>Quantity</th><th>Price</th><th>Total</th></tr>";
        $total = 0;
        for ($i = 0; $i < count($products); $i++) {
            echo "<tr>";
            echo "<td>" . $products[$i][1] . "</td><td>" . $_GET[$i] . "</td><td>" . $products[$i][2] . "</td><td>" . $products[$i][2] * $_GET[$i] . "</td>";
            $total = $total + ($products[$i][2] * $_GET[$i]);
            echo "</tr>";
        }
        echo "<tr><th colspan=\"3\" style=\"text-align:left\">Sub Total</th><th >" . $total . "</th></tr>";
        echo "<tr><td colspan=\"3\" style=\"text-align:left\">GST (18%)</td><td>" . ($total * 18 / 100) . "</td></tr>";
        echo "<tr><th colspan=\"3\" style=\"text-align:left\">Grand Total</th><th >" . $total + ($total * 18 / 100) . "</th></tr>";
        echo "</table>";
    }
    ?>
</body>

</html>