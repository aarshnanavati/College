
<html>
<body>

<?php
print_r(str_word_count("Hello world! how are you ",0));
echo "<br>";
print_r(str_word_count("Hello world! how are you ",1));
echo "<br>";
print_r(str_word_count("Hello world! how ar!e yo?u ",2));

echo "<br>";


print_r(str_word_count("Hello world how ar!e yo?u ",2,"!,?, "));
?>

</body>
</html>
