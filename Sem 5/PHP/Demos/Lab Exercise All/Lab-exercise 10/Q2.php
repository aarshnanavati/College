<?php
session_start();

// Check if the count is set, if not, initialize it
if (!isset($_SESSION['counter'])) {
    $_SESSION['counter'] = 0;
}
$_SESSION['counter']++;

echo "You have refreshed this page " . $_SESSION['counter'] . " times.";
?>