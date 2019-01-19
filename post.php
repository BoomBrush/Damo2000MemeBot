<?php 

// Software written by Scott Howie
// Published on 20 Janurary 2019
// Created some time before July 2018

error_reporting( E_ALL );
ini_set('display_errors', 1);
define('FACEBOOK_SDK_V4_SRC_DIR', __DIR__.'/src/Facebook/');
require_once(__DIR__.'/src/Facebook/autoload.php');
$fb = new \Facebook\Facebook([
  'app_id' => '9999999999999999999999999999999999 YOUR APP ID',
  'app_secret' => '9999999999999999999999999999 YOUR APP SECRET',
  'default_graph_version' => 'v2.11',
  //'default_access_token' => '{access-token}', // optional
]);

$img_url = (@$_GET['img_url']);
$img_msg = (@$_GET['img_msg']);

if (empty($img_url)) {
	exit('please supply image url');
}
if (isset($img_msg) && empty($img_msg)) {
	exit('please supply msg');
}

$img_url = urldecode($img_url);
$img_msg = urldecode($img_msg);

print("Memebot 8000 v3 - before the cuckening<br>\n"); 
// version 1 stopped working after facebook changed their API
// version 2 was meant to fix it but turns out it was still broken
print("Image URL: " . $img_url . "<br>\n");
print("Message: " . $img_msg . "<br>\n");
//Post property to Facebook
$linkData = [ 'link' => 'www.yoururl.com', 'message' => 'chicken man', 'message' => $img_msg, 'url' => $img_url ];
 
$pageAccessToken = '9999999999999 PAGE ACCESS TOKEN';
try { 
	$response = $fb->post('/me/photos', $linkData, $pageAccessToken);
} catch(Facebook\Exceptions\FacebookResponseException $e) { 
	echo 'Graph returned an error: '.$e->getMessage();
	exit;
} catch(Facebook\Exceptions\FacebookSDKException $e) {
	echo 'Facebook SDK returned an error: '.$e->getMessage();
	exit;
}	$graphNode = $response->getGraphNode();

?>