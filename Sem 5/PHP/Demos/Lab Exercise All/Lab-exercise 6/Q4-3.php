<?php
// Create 2D associative array for students' marks
$students = [
    [
        'Name' => 'John',
        'Subject1' => 80,
        'Subject2' => 90,
        'Subject3' => 85
    ],
    [
        'Name' => 'Jane',
        'Subject1' => 70,
        'Subject2' => 60,
        'Subject3' => 75
    ]
];

// Calculate total marks
foreach ($students as $student) {
    $totalMarks = $student['Subject1'] + $student['Subject2'] + $student['Subject3'];
    echo "Student: {$student['Name']} - Total Marks: $totalMarks<br>";
}
?>