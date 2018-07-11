 <!-- <?php 
    $myfile = fopen("newfile.txt", "w") or die("Unable to open file!"); //query pra inserir

    $binanceKey = "t16ZOkbUCetVG9FZyRl949WRHAYmOSJiBUjVVcanvznZWlzWRfpBa9V8fLfAX5XB"; 
    $secret = "lIQodpmCeu3fAOLpBJvGZJg5ClkB34U4EHJ7d5s09xsSEJc2kylFXXT3w1E2tjAz";
    $key = substr($binanceKey, 0, 32); 
    $iv = substr($binanceKey, -16); 
    $enc = base64_encode(mcrypt_encrypt(MCRYPT_RIJNDAEL_128, $key, $secret, MCRYPT_MODE_CBC, $iv));
    fwrite($myfile, $enc);
    echo($enc); //insere no banco apos criptografar
    
    $decod = base64_decode($enc);
    $dec = mcrypt_decrypt(MCRYPT_RIJNDAEL_128, $key, $decod , MCRYPT_MODE_CBC, $iv);
    echo("\n decod \n");
    echo($dec);
 ?>  -->

<?php
class Criptografia{
    private $binancekey;
    private $oprSecret;
    //construtor da classe
    function Criptografia($key, $secret){
        $this-> $binanceKey = $key;
        $this-> $oprSecret = $secret;
    }

    function criptografa(){
        $key = substr($this->$binanceKey, 0, 32); 
        $iv = substr($this->$binanceKey, -16); 
        $enc = base64_encode(mcrypt_encrypt(MCRYPT_RIJNDAEL_128, $key, $this->$oprSecret, MCRYPT_MODE_CBC, $iv));
        return $enc;
    }

    function decriptografa(){
        $key = substr($this->$binanceKey, 0, 32); 
        $iv = substr($this->$binanceKey, -16); 
        $decod = base64_decode($this-> $oprSecret);
        $dec = mcrypt_decrypt(MCRYPT_RIJNDAEL_128, $key, $decod , MCRYPT_MODE_CBC, $iv);
        return $dec;
    }
} ?>

