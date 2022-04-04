#!/bin/bash
while read p;
do echo $p;
p1=$p;p1+="1";echo $p1;
p1=$p;p1+='1!';echo $p1;
p1=$p;p1+="123";echo $p1;
p1=$p;p1+='123!';echo $p1;
echo $p|awk '{ print toupper( substr( $0, 1, 1 ) ) substr( $0, 2 ); }';
p1=$p;p1+="1";echo $p1|awk '{ print toupper( substr( $0, 1, 1 ) ) substr( $0, 2 ); }';
p1=$p;p1+='1!';echo $p1|awk '{ print toupper( substr( $0, 1, 1 ) ) substr( $0, 2 ); }';
p1=$p;p1+="123";echo $p1|awk '{ print toupper( substr( $0, 1, 1 ) ) substr( $0, 2 ); }';
p1=$p;p1+='123!';echo $p1|awk '{ print toupper( substr( $0, 1, 1 ) ) substr( $0, 2 ); }';
p1=$p;p1+="2015";echo $p1;
p1=$p;p1+="2016";echo $p1;
p1=$p;p1+="2017";echo $p1;
p1=$p;p1+="2018";echo $p1;
p1=$p;p1+="2019";echo $p1;
p1=$p;p1+="2020";echo $p1;
p1=$p;p1+="2015!";echo $p1;
p1=$p;p1+="2016!";echo $p1;
p1=$p;p1+="2017!";echo $p1;
p1=$p;p1+="2018!";echo $p1;
p1=$p;p1+="2019!";echo $p1;
p1=$p;p1+="2020!";echo $p1;
p1=$p;p1+="2021!";echo $p1;
p1=$p;p1+="2022!";echo $p1;
p1=$p;p1+="2023!";echo $p1;
p1=$p;p1+="2024!";echo $p1;
p1=$p;p1+="2025!";echo $p1;
p1=$p;p1+="2015";echo $p1|awk '{ print toupper( substr( $0, 1, 1 ) ) substr( $0, 2 ); }';
p1=$p;p1+="2016";echo $p1|awk '{ print toupper( substr( $0, 1, 1 ) ) substr( $0, 2 ); }';
p1=$p;p1+="2017";echo $p1|awk '{ print toupper( substr( $0, 1, 1 ) ) substr( $0, 2 ); }';
p1=$p;p1+="2018";echo $p1|awk '{ print toupper( substr( $0, 1, 1 ) ) substr( $0, 2 ); }';
p1=$p;p1+="2019";echo $p1|awk '{ print toupper( substr( $0, 1, 1 ) ) substr( $0, 2 ); }';
p1=$p;p1+="2020";echo $p1|awk '{ print toupper( substr( $0, 1, 1 ) ) substr( $0, 2 ); }';
p1=$p;p1+="2015!";echo $p1|awk '{ print toupper( substr( $0, 1, 1 ) ) substr( $0, 2 ); }';
p1=$p;p1+="2016!";echo $p1|awk '{ print toupper( substr( $0, 1, 1 ) ) substr( $0, 2 ); }';
p1=$p;p1+="2017!";echo $p1|awk '{ print toupper( substr( $0, 1, 1 ) ) substr( $0, 2 ); }';
p1=$p;p1+="2018!";echo $p1|awk '{ print toupper( substr( $0, 1, 1 ) ) substr( $0, 2 ); }';
p1=$p;p1+="2019!";echo $p1|awk '{ print toupper( substr( $0, 1, 1 ) ) substr( $0, 2 ); }';
p1=$p;p1+="2020!";echo $p1|awk '{ print toupper( substr( $0, 1, 1 ) ) substr( $0, 2 ); }';
p1=$p;p1+="2021!";echo $p1|awk '{ print toupper( substr( $0, 1, 1 ) ) substr( $0, 2 ); }';
p1=$p;p1+="2022!";echo $p1|awk '{ print toupper( substr( $0, 1, 1 ) ) substr( $0, 2 ); }';
p1=$p;p1+="2023!";echo $p1|awk '{ print toupper( substr( $0, 1, 1 ) ) substr( $0, 2 ); }';
p1=$p;p1+="2024!";echo $p1|awk '{ print toupper( substr( $0, 1, 1 ) ) substr( $0, 2 ); }';
p1=$p;p1+="2025!";echo $p1|awk '{ print toupper( substr( $0, 1, 1 ) ) substr( $0, 2 ); }';
done<$1>$1-xmute.txt
sort -u $1-xmute.txt > $1-xmute.txt.tmp
mv $1-xmute.txt.tmp $1-xmute.txt
