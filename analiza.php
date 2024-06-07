<?php 

$content = $_POST['content'];
$file = "correo.txt";
$Saved_File = fopen($file, 'w');
fwrite($Saved_File, $content);
fclose($Saved_File);


$output = array();
echo "Análisis de las cabeceras de correo";
echo "</br>";
echo "</br>";
echo "</br>";

exec("python resumen_cabeceras.py -f correo.txt",$output);

for ($i = 0; $i < count($output); $i++) {
    echo $output[$i];
	echo "</br>";
} 

$output = array();
echo "</br>";

exec("python busqueda_urls.py -f correo.txt",$output);

for ($i = 0; $i < count($output); $i++) {
    echo $output[$i];
	echo "</br>";
} 

$output = array();
echo "</br>";

exec("python muestra_html.py -f correo.txt",$output);

for ($i = 0; $i < count($output); $i++) {
    echo $output[$i];
	echo "</br>";
} 

unlink('correo.txt');

$output = array();
echo "</br>";

exec("python vt_buscaIP.py",$output);

for ($i = 0; $i < count($output); $i++) {
    echo $output[$i];
	echo "</br>";
} 

$output = array();
echo "</br>";

exec("python vt_buscaURL.py",$output);

for ($i = 0; $i < count($output); $i++) {
    echo $output[$i];
	echo "</br>";
} 
 ?>