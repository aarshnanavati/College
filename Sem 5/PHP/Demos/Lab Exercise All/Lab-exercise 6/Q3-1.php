<?php
// Create associative array
$student = [
    'RollNumber' => 101,
    'Name' => 'John Doe',
    'Course' => 'Computer Science',
    'Marks' => 85
];

// Display details
echo "<table border='1'>";
echo "<tr><th>Roll Number</th><th>Name</th><th>Course</th><th>Marks</th></tr>";
echo "<tr><td>{$student['RollNumber']}</td><td>{$student['Name']}</td><td>{$student['Course']}</td><td>{$student['Marks']}</td></tr>";
echo "</table>";
?>