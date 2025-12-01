<?php
//array_chunk(array $array, int $length, bool $preserve_keys = false): array
$fruits = ["apple", "banana", "cherry", "date", "fig", "grape"];

$chunks = array_chunk($fruits, 4);

print_r($chunks);
echo "<br>";
?>
<!--
Array
(
    [0] => Array
        (
            [0] => apple
            [1] => banana
        )

    [1] => Array
        (
            [0] => cherry
            [1] => date
        )

    [2] => Array
        (
            [0] => fig
            [1] => grape
        )
)
-->
<?php
$fruits = ["a" => "apple", "b" => "banana", "c" => "cherry", "d" => "date"];

$chunks = array_chunk($fruits, 2, false);

print_r($chunks);
?>
