<html>
<body style="font-family: Courier New, Courier, monospace">

<h1 style="font-family: Helvetica, Sans-Serif; text-align: center">Here are your results:</h1>

<?php
function alert($msg) {
  echo "<script type='text/javascript'>alert('$msg');</script>";
}

$num_correct = 0;

if ($_POST['question1'] == "RTL8197D") {
  echo '<p style="color: lime; text-align: center">Question 1: Correct</p>';
  $num_correct++;
} else {
  echo '<p style="color: red; text-align: center">Question 1: Incorrect</p>';
}

if ($_POST['question2'] == "MIPS") {
  echo '<p style="color: lime; text-align: center">Question 2: Correct</p>';
  $num_correct++;
} else {
  echo '<p style="color: red; text-align: center">Question 2: Incorrect</p>';
}

if ($_POST['question3'] == "2.6.30") {
  echo '<p style="color: lime; text-align: center">Question 3: Correct</p>';
  $num_correct++;
} else {
  echo '<p style="color: red; text-align: center">Question 3: Incorrect</p>';
}

if (isset($_POST['question4b'])    &&
    $_POST['question4b'] == "wget" &&
    !isset($_POST['question4a'])   &&
    !isset($_POST['question4c'])   &&
    !isset($_POST['question4d'])) {
  echo '<p style="color: lime; text-align: center">Question 4: Correct</p>';
  $num_correct++;
} else {
  echo '<p style="color: red; text-align: center">Question 4: Incorrect</p>';
}

if ($_POST['question5'] == "wapac04_dlob_dap1650") {
  echo '<p style="color: lime; text-align: center">Question 5: Correct</p>';
  $num_correct++;
} else {
  echo '<p style="color: red; text-align: center">Question 5: Incorrect</p>';
}

if ($num_correct == 5) {
  echo '<p style ="text-align: center">Congratulations! The flag is <b>ATR[H4L0R3C0N4RM0R]</b></p>';
} else {
  echo '<p style ="text-align: center">Sorry, better luck next time.</p>';
  echo '<form action="index.html" method="post" style="text-align: center">';
  echo '<input type="submit" value="Try Again">';
  echo '</form>';
}
?>

</body>
</html>
