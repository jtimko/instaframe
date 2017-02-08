<?php
  require_once('connection.php');
  
  if (isset($_GET['id'])) {
    if (strlen($_GET['id']) == 6) {
      if (is_numeric($_GET['id'])) {
        $nick = $db->grabUser($_GET['id']);
        echo $nick;
      } else {
        echo "no hak0rz";
      }
    } else {
      echo "u no l33t";
    }
  }

?>
