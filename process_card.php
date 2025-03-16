<!DOCTYPE html>
<html lang="en">
<!-- HTML form page -->
<head>
    <title>Magic Card Details</title>
<style>
body {
		background-image:
		url('background.jpg');
  }
.center {
  text-align: center;
  border: 2px solid blue;
}
</style>
</head>
<body>
<div class=center>
	<h2>Enter Magic Card Details</h2>
<form method="post" action="<?php echo htmlspecialchars($_SERVER['PHP_SELF']);?>"
    <label for="card_name">Magic Card Name:</label><br>
    <input type="text" id="card_name" name="card_name"><br><br>

    <label for="card_rarity">Card Rarity:</label><br>
    <input type="text" id="card_rarity" name="card_rarity"><br><br>

    <label for="card_color">Color:</label><br>
    <input type="text" id="card_color" name="card_color"><br><br>

    <label for="card_type">Type:</label><br>
    <input type="text" id="card_type" name="card_type"><br><br>

    <label for="set_name">Set Name:</label><br>
    <input type="text" id="set_name" name="set_name"><br><br>
    
    <label for="card_value">Value:</label><br>
    <input type="text" id="card_value" name="card_value"><br><br>

    <input type="submit" value="Submit">
    <input type="submit" name="UndoLastEntry" class="button" value="Undo Last Entry">
    <input type="submit" name="Retrieve" class="button" value="Download File">
    
</form>
</div>
</body>
</html>
<!-- End of HTML section -->

<?php
/* Define functions of program */
function test_input($data){
	/* clean data retrieved from the form fields */
	$data=trim($data);
	$data=stripslashes($data);
	$data=str_replace(',','',$data);
	$data=str_replace("'","\'",$data);
	$data=htmlspecialchars($data);
	return $data;
}
function take_back_last(){
	/* Undo last table row inserted when button is pressed */
    $servername = "localhost";
    $username = "PHP";
    $password = "Forean24!";
    $db="mtgcardbase";
    $connection= new mysqli($servername,$username,$password,$db);
    if ($connection->connect_error){
            die("Connection failed: " . $connection->connect_error);
        }
	$sql="DELETE FROM cards ORDER BY id DESC LIMIT 1";

	if ($connection->query($sql) === TRUE) {
  echo '<script language="javascript">';
		echo 'alert("Last entry deleted.")';
		echo '</script>';
}else {
  echo "Error: " . $sql . "<br>" . $connection->error;
}
$connection->close();
}

function retrieve(){
/* delete csv file if it already exist since mySQL cannnot overwrite an existing one */
$filename = "card_inventory.csv";
$file = 'C:/xampp/htdocs/'.$filename;
if (!unlink($file)) { 
    echo ("$file cannot be deleted due to an error"); 
} 
else { 
    echo ("$file has been deleted"); 
} 

$servername = "localhost";
    $username = "PHP";
    $password = "Forean24!";
    $db="mtgcardbase";
    $connection= new mysqli($servername,$username,$password,$db);
    if ($connection->connect_error){
            die("Connection failed: " . $connection->connect_error);
        } 
/* Export cards table as CSV to user's computer */
$sql ="SELECT 'Name', 'Rarity', 'Color', 'Type', 'SetName', 'Value' UNION ALL SELECT Name, Rarity, Color, Type, SetName, Value FROM cards INTO OUTFILE 'C:/xampp/htdocs/card_inventory.csv'";

	if ($connection->query($sql) === TRUE) {
		echo '<script language="javascript">';
		echo 'alert("CSV file exported.")';
		echo '</script>';
	} else {
			echo "Error: " . $sql . "<br>" . $connection->error;
	}
$connection->close();
$filename = "card_inventory.csv";
$file = 'C:/xampp/htdocs/'.$filename;
if(!file_exists($file)){ // file does not exist
    die('file not found');
} else {
   header('Content-type: application/octet-stream');
header("Content-Type: ".mime_content_type($file));
header("Content-Disposition: attachment; filename=".$filename);
while (ob_get_level()) {
    ob_end_clean();
}
readfile($file);
}
} /*End of functions definitions */

/* Begin main body of program*/
if(isset($_POST['Retrieve'])) {
	retrieve();
}elseif(isset($_POST['UndoLastEntry'])) { 
    take_back_last();
}elseif($_SERVER["REQUEST_METHOD"] == "POST") 
{
    $cardName = test_input($_POST['card_name']) ?? ''; 
    $cardRarity = test_input($_POST['card_rarity']) ?? '';
    $cardColor = test_input($_POST['card_color']) ?? '';
    $cardType = test_input($_POST['card_type']) ?? '';
    $setName = test_input($_POST['set_name']) ?? '';
    $cardValue = test_input($_POST['card_value']) ?? ''; 
    $servername = "localhost";
    $username = "PHP";
    $password = "Forean24!";
    $db="mtgcardbase";
    $connection= new mysqli($servername,$username,$password,$db);
    if ($connection->connect_error){
            die("Connection failed: " . $connection->connect_error);
        }
    		
/* Default action: Insert data into mtgcardbase.cards */    
$sql = "INSERT INTO cards (`Name`, `Rarity`, `Color`, `Type`, `SetName`, `Value`) 
VALUES (\"$cardName\", \"$cardRarity\", \"$cardColor\", \"$cardType\", \"$setName\",\"$cardValue\")";
if ($connection->query($sql) === TRUE) {
  echo '<script language="javascript">';
		echo 'alert("Card details saved successfully!")';
		echo '</script>';
} else {
  echo "Error: " . $sql . "<br>" . $connection->error;
}
$connection->close();
header("Refresh:0; url=process_card.php");
}
?>
