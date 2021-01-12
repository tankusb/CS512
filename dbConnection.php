<?php

$dbhost = 'classmysql.engr.oregonstate.edu';
$dbname = 'tankusm-db';
$dbuser = 'tankusm-db';
$dbpass = 'Wn4F7dtr7Cw7zZeQ';

$mysqli = new mysqli($dbhost, $dbuser, $dbpass, $dbname);
if ($mysqli->connect_errno) {
    echo "Failed to connect to MySQL: (" . $mysqli->connect_errno . ") " . $mysqli->connect_error;
}

echo 'Successfully connected to database!';

$mysqli->close();

?>