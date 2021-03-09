<html>
<body>

Welcome <?php echo $_GET["name"]; ?><br>
Your website is: <?php echo $_GET["website"]; ?><br><br>
<?php

system('nslookup '. $_GET["website"], $retval);

?>
</body>
</html>
