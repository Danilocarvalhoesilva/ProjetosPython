<html>
 <head>
  <title>Teste PHP</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
 </head>
 <body>
<div class="w3-container w3-teal">
  <h1>WEBSERVICE BOTICÁRIO</h1>
</div>
 </body>
</html>

<?php

//HEADER
header("Access-Control-Allow-Origin: *");
header("Access-Control-Allow-Headers: access");
header("Access-Control-Allow-Methods: POST");
header("Content-Type: application/json; charset=UTF-8");
header("Access-Control-Allow-Headers: Content-Type, Access-Control-Allow-Headers, Authorization, X-Requested-With");

// INCLUINDO DATABASE
require 'database.php';
$db_connection = new Database();
$conn = $db_connection->dbConnection();

// GET DADOS REQUEST
$data = json_decode(file_get_contents("php://input"));

//CRIANDO MESSAGEM ARRAY 
$msg['message'] = '';

// CHECHANDO E RECEBENDO DATA REQUEST
if(isset($data->name) && isset($data->email) && isset($data->password) && isset($data->status)){
	// CHECANDO SE O VALOR VAZIO OU NAO
    	if(!empty($data->name) && !empty($data->email) && !empty($data->password) && !empty($data->status)){
		//VERIFICANDO SE JA EXISTE NA TABELA
        	$select_query = "SELECT * FROM `users` WHERE name=:name ORDER BY id DESC limit 1";
		$select_stmt = $conn->prepare($select_query);
        	$select_stmt->bindValue(':name', htmlspecialchars(strip_tags($data->name)),PDO::PARAM_STR);
        	$select_stmt->execute();
        	if($select_stmt->rowCount() == 1){
        		$msg['message'] = 'Dados ja existem, atualizado a tabela!';
			$update_query = "UPDATE `users` SET status=:status WHERE name=:name ORDER BY id DESC limit 1";
			$update_stmt = $conn->prepare($update_query);
			$update_stmt->bindValue(':name', htmlspecialchars(strip_tags($data->name)),PDO::PARAM_STR);
			$update_stmt->bindValue(':status', htmlspecialchars(strip_tags($data->status)),PDO::PARAM_STR);
			$update_stmt->execute();
			echo  json_encode($msg);		
        	}else{
        		$insert_query = "INSERT INTO `users`(name,email,password,status) VALUES(:name,:email,:password,:status)";
        		$insert_stmt = $conn->prepare($insert_query);
        		// INSERINDO OS DADOS
        		$insert_stmt->bindValue(':name', htmlspecialchars(strip_tags($data->name)),PDO::PARAM_STR);
        		$insert_stmt->bindValue(':email', htmlspecialchars(strip_tags($data->email)),PDO::PARAM_STR);
        		$insert_stmt->bindValue(':password', htmlspecialchars(strip_tags($data->password)),PDO::PARAM_STR);
        		$insert_stmt->bindValue(':status', htmlspecialchars(strip_tags($data->status)),PDO::PARAM_STR);
        		$insert_stmt->execute();
            		$msg['message'] = 'Dados não existem, Inserido com Sucesso!';
			echo  json_encode($msg);
    		}    
    	}else{
        	$msg['message'] = 'Oops! Campos vazios detectados. Por favor preencha todos os campos!';
		echo  json_encode($msg);
    	}
}else{
	$msg['message'] = 'WEBSERVICE API BOTICÁRIO!';
	//echo  json_encode($msg);

}
?>


