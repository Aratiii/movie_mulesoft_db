<?php

//define PDO - tell about the database file

$pdo = new PDO( 'sqlite:movie_mulesoft.db' ) ;

//write SQL

$statement = $pdo->query ("SELECT * FROM MOVIEDB") ;

//run the SQL

$rows = $statement->fetchAll(PDO:: FETCH_ASSOC) ;

//show it on the screen var_dump ($rows) ;
var_dump($rows);
