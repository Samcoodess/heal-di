<?php
$host = "localhost";
$username = "root";
$password = "your_database_password";
$database = "users_table";

$conn = new mysqli($host, $username, $password, $database);

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}
?>
