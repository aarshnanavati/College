<?php
$tech = 'PHP';
$msg = '';
switch($tech){
 case 'PHP':
 $msg =  'PHP is cool';
 break;
 case 'Perl':
 $msg = 'Perl is awesome';
 break;
 case 'Python':
 $msg = 'Perl is beautiful';
 break;
 case 'Java/JSP':
 $msg = 'JSP is robust';
 break;
 case 'C#/ASP.NET':
 $msg = 'C#/ASP.NET is awesome';
 break;
 default:
 $msg = 'What technology are you using?';
 break;
}
 
echo $msg;
