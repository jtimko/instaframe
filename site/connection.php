<?php

class dbc {
  public $dbc;

  public function __construct() {
    $user;
    $pass;
    try {
      $this->dbc = new PDO('mysql:host=localhost;dbname=instaframe', $user, $pass);
      $this->dbc->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
      $this->dbc->setAttribute(PDO::ATTR_EMULATE_PREPARES, false);
    } catch (PDOException $e) {
      echo $e->getMessage();
    }
  }

  public function insertUser($user) {
    try {
      $stmt = $this->dbc->prepare("UPDATE user SET target_name = ? WHERE user_id = 143756");
      $stmt->execute(array($user));
    } catch (PDOException $e) {
      echo $e->getMessage();
    }
  }

  public function grabUser($id) {
    $stmt = $this->dbc->prepare("SELECT target_name FROM user WHERE user_id = ?");
    $stmt->execute(array($id));
    $rows = $stmt->fetch(PDO::FETCH_ASSOC);
    return $rows['target_name'];
  }
}

$db = new dbc();

 ?>
