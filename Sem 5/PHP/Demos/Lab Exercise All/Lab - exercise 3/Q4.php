
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>L3Q4</title>
</head>
<body>
  <h1>Form with Multiple Submit button</h1>
  <form action="">
    <table>
      <tr>
        <td><label for="">Value 1</label></td>
        <td><input type="text" name="a" value="<?php if(isset($_GET['a'])) echo $_GET['a']; ?>"></td>
      </tr>
      <tr>
        <td><label for="">Value 2</label></td>
        <td><input type="text" name="b" value="<?php if(isset($_GET['b'])) echo $_GET['b']; ?>"></td>
      </tr>
      <tr>
        <td><label for="">Result</label></td>
        <td><input type="text" id="" value=<?php
          if (isset($_GET['a'])&&isset($_GET['b'])) {
            if ($_GET['act']=="add") {
              echo $_GET['a'] + $_GET['b'];
            }else if ($_GET['act']=="sub") {
              echo $_GET['a'] - $_GET['b'];
            }else if ($_GET['act']=="div") {
              echo $_GET['a'] / $_GET['b'];
            }else {
              echo $_GET['a'] * $_GET['b'];
            }
          }
        ?>>
        </td>
      </tr>
      <tr>
        <td><button type="submit" name="act" value="add">Add</button></td>
        <td><button type="submit" name="act" value="sub">Subtract</button></td>
      </tr>
      <tr>
        <td><button type="submit" name="act" value="mul">Multiply</button></td>
        <td><button type="submit" name="act" value="div">Divide</button></td>
      </tr>
    </table>
  </form>
</body>
</html>
