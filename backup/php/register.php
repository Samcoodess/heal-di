<?php
// Include the database connection script
include('dbconnection.php');

// Check if the form is submitted
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Retrieve user-entered data from the form
    $username = $_POST['username'];
    $password = $_POST['password'];

    // Hash the password for security
    $hashedPassword = password_hash($password, PASSWORD_DEFAULT);

    // SQL query to insert user information into the 'users' table
    $sql = "INSERT INTO users (username, password) VALUES ('$username', '$hashedPassword')";

    // Execute the query
    if ($conn->query($sql) === TRUE) {
        echo "User registered successfully!";
    } else {
        echo "Error: " . $sql . "<br>" . $conn->error;
    }
}

// Close the database connection
$conn->close();
?>
