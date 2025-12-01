<!DOCTYPE html>
<html lang="en">

<head>
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
    <h2>Product Catelog</h2>

    <?php
    $products = [
        ["Wireless mouse", 350, "Electronincs"],
        ["Bluetooth speaker", 1200, "Electronics"],
        ["Notebok", 80, "Stationery"],
        ["Pen drive 64 GB", 700, "Electronics"],
        ["Water bottle", 150, "Home and kitchen"],
        ["Desk lamp", 950, "Home and kitchen"],
    ];

    echo "<table><tr><th>Name</th><th>Price</th><th>Category</th></tr>";
    for ($i = 0; $i < count($products); $i++) {
        echo "<tr>";
        for ($j = 0; $j < count($products[$i]); $j++) {
            echo "<td>" . $products[$i][$j] . "</td>";
        }
        echo "</tr>";
    }

    echo "</table>";
    ?>

    <?php
    echo "<br> <br>";
    echo "<table><tr><th>Name</th><th>Price</th><th>Category</th></tr>";
    for ($i = 0; $i < count($products); $i++) {
        echo "<tr>";
        if ($products[$i][1] > 500) {
            for ($j = 0; $j < count($products[$i]); $j++) {
                echo "<td>" . $products[$i][$j] . "</td>";
            }
        }
        echo "</tr>";
    }

    echo "</table>";
    ?>
</body>

</html>