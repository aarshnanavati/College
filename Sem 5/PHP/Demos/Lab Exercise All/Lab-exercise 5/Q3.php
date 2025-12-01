<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>L5Q2</title>
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
  <h1 style="font-size: 30px;">Student Exam Result</h1>
  <form action="" method="GET">
    <label>Student Name : </label>
    <input type="text" name="name" />
    <?php
    $subjects = [
      "English",
      "Math",
      "Science",
      "Computer",
      "Social Studies",
    ];

    for ($i = 0; $i < count($subjects); $i++) {
      echo "<br></br>";
      echo "<label>" . $subjects[$i] . " : </label";
      echo "<td><input type=\"number\" name=\"" . $i . "\"/> </td>";
      echo "</tr>";
    }

    echo "</table>";
    ?>
    <br />
    <br />
    <button type="submit">Get Result</button>
  </form>


  <?php

  if ($_GET) {
    // Printing the first table, displaying all the items.
    echo "<h1 style=\"font-size: 30px;\">Result of " . $_GET['name'] . "</h1>";
    echo "<table><tr><th>Subject</th><th>Marks</th></tr>";
    $total = 0;
    for ($i = 0; $i < count($subjects); $i++) {
      echo "<tr>";
      echo "<td>" . $subjects[$i] . "</td><td>" . $_GET[$i] . "</td>";
      $total = $total + $_GET[$i];
      echo "</tr>";
    }
    echo "<tr><th style=\"text-align:left\">Sub Total</th><th >" . $total . "</th></tr>";
    $percentage = ($total * 100 / (100 * count($subjects)));
    $grade = "";
    if ($percentage > 90 && $percentage < 100) {
      $grade = "A";
    } else if ($percentage > 70 && $percentage < 90) {
      $grade = "B";
    } else if ($percentage > 50 && $percentage < 70) {
      $grade = "c";
    } else if ($percentage > 30 && $percentage < 50) {
      $grade = "B";
    } else if ($percentage > 0 && $percentage < 30) {
      $grade = "F";
    } else {
      $grade = "NULL";
    }
    echo "<tr><th style=\"text-align:left\">Total</th><th >" . $total . "</th></tr>";
    echo "<tr><th style=\"text-align:left\">Percentage</th><td>" . $percentage . "% </td></tr>";
    // echo "<tr><th style=\"text-align:left\">Result</th><th >". $grade == "F" ? echo "Fail":echo "Pass" .
    // "</th></tr>";
    echo "<tr><th style=\"text-align:left\">Grade</th><th >" . $grade . "</th></tr>";
    echo "</table>";
  }
  ?>

</body>

</html>