<html>
<head>
	<title>run my python</title>
	<?PHP
	echo shell_exec("python skrypt.py");
	?>
</head>
<body>
	<?PHP
		$yeet = shell_exec("python skrypt.py");
		echo $yeet
	?>
</body>