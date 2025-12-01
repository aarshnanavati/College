<?php
// Create associative array for 5 students
$students = [
    [
        'RollNumber' => 101,
        'Name' => 'John',
        'Course' => 'CS',
        'Marks' => 85
    ],
    [
        'RollNumber' => 102,
        'Name' => 'Jane',
        'Course' => 'IT',
        'Marks' => 90
    ],
    [
        'RollNumber' => 103,
        'Name' => 'Alice',
        'Course' => 'CS',
        'Marks' => 75
    ],
    [
        'RollNumber' => 104,
        'Name' => 'Bob',
        'Course' => 'IT',
        'Marks' => 95
    ],
    [
        'RollNumber' => 105,
        'Name' => 'Charlie',
        'Course' => 'CS',
        'Marks' => 80
    ]
];

// Find the student with the highest marks
$highestMarksStudent = max(array_column($students, 'Marks'));

// Display details of the student with highest marks
foreach ($students as $student) {
    if ($student['Marks'] == $highestMarksStudent) {
        echo "Highest marks student: <br>";
        echo "Roll Number: {$student['RollNumber']}<br>";
        echo "Name: {$student['Name']}<br>";
        echo "Course: {$student['Course']}<br>";
        echo "Marks: {$student['Marks']}<br>";
    }
}
?>