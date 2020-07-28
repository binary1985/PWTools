#!/bin/bash
while read p;
do echo $p;
p1=$p;p1+="1";echo $p1;
p1=$p;p1+='1!';echo $p1;
p1=$p;p1+="123";echo $p1;
p1=$p;p1+='123!';echo $p1;
echo $p|sed 's/.*/\u&/';
p1=$p;p1+="1";echo $p1|sed 's/.*/\u&/';
p1=$p;p1+='1!';echo $p1|sed 's/.*/\u&/';
p1=$p;p1+="123";echo $p1|sed 's/.*/\u&/';
p1=$p;p1+='123!';echo $p1|sed 's/.*/\u&/';
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
p1=$p;p1+="2015";echo $p1|sed 's/.*/\u&/';
p1=$p;p1+="2016";echo $p1|sed 's/.*/\u&/';
p1=$p;p1+="2017";echo $p1|sed 's/.*/\u&/';
p1=$p;p1+="2018";echo $p1|sed 's/.*/\u&/';
p1=$p;p1+="2019";echo $p1|sed 's/.*/\u&/';
p1=$p;p1+="2020";echo $p1|sed 's/.*/\u&/';
p1=$p;p1+="2015!";echo $p1|sed 's/.*/\u&/';
p1=$p;p1+="2016!";echo $p1|sed 's/.*/\u&/';
p1=$p;p1+="2017!";echo $p1|sed 's/.*/\u&/';
p1=$p;p1+="2018!";echo $p1|sed 's/.*/\u&/';
p1=$p;p1+="2019!";echo $p1|sed 's/.*/\u&/';
p1=$p;p1+="2020!";echo $p1|sed 's/.*/\u&/';
done<$1>$1-xmute.txt
sort -u $1-xmute.txt > $1-xmute.txt.tmp
mv $1-xmute.txt.tmp $1-xmute.txt
