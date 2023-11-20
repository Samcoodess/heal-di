<?php
function hash_password($password) {
    // Use a secure hashing algorithm like bcrypt or Argon2
    return password_hash($password, PASSWORD_BCRYPT);
}

function verify_password($password, $hashed_password) {
    return password_verify($password, $hashed_password);
}
?>
