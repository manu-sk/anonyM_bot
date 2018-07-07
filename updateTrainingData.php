<?php
$servername = "localhost";
$username = "root";
$password = "hacker";
$dbname = "chatbot";

$intents = $_POST['Intents'];
$questions = $_POST['QuestionPatterns'];
$answers = $_POST['Responses'];

echo $intents;
echo $questions;
echo $answers;
// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

$sql = "INSERT INTO MyGuests SET lastname='Doe' WHERE id=2";

if ($conn->query($sql) === TRUE) {
    echo "Record updated successfully";
} else {
    echo "Error updating record: " . $conn->error;
}

$conn->close();
?>