<?php
require_once 'db_connection.php';
require_once 'password_hashing.php';

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $username = $_POST['username'];
    $password = $_POST['password'];

    // Retrieve hashed password from the database
    $query = "SELECT password_hash FROM users WHERE username = ?";
    $stmt = $conn->prepare($query);
    $stmt->bind_param("s", $username);
    $stmt->execute();
    $stmt->bind_result($hashed_password);
    $stmt->fetch();
    $stmt->close();

    // Verify the entered password
    if (verify_password($password, $hashed_password)) {
        // Password is correct, log in the user
        // You can redirect to the user's dashboard or another page
        header("Location: dashboard.html");
        exit();
    } else {
        // Password is incorrect, handle accordingly (e.g., show an error message)
        echo "Incorrect username or password";
    }
}
?>
