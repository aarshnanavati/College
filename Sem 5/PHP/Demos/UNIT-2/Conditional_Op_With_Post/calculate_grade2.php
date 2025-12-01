<?php
if (isset($_POST['math']) && isset($_POST['science']) && isset($_POST['english'])) {
    $math = $_POST['math'];
    $science = $_POST['science'];
    $english = $_POST['english'];

    $total = $math + $science + $english;
    $percentage = $total / 3;

    echo "<h2>Result</h2>";
    echo "Total Marks: $total<br>";
    echo "Percentage: $percentage%<br>";

    // Nested if-else for grade
    if ($percentage >= 90) {
        echo "Grade: A+";
    } else {
        if ($percentage >= 75) {
            echo "Grade: A";
        } else {
            if ($percentage >= 60) {
                echo "Grade: B";
            } else {
                if ($percentage >= 50) {
                    echo "Grade: C";
                } else {
                    if ($percentage >= 35) {
                        echo "Grade: D";
                    } else {
                        echo "Grade: F (Fail)";
                    }
                }
            }
        }
    }
}
?>
