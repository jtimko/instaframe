<?php

  require_once('connection.php');

  if (isset($_POST['user'])) {
    $user = htmlentities($_POST['user']);
    $db->insertUser($user);

    echo "Updated!";
  }


?>
