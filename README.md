# PWTools  
A small collection of tools designed to increase password cracking success.  

##Combination-Builder
Merge multiple wordlists to create every combination of the words in the wordlists.  
Usage is: ./combination-builder.py <input wordlist> <input wordlist 2> <additional lists optional>  

./combination-builder.py sample\ wordlists/speeds.txt sample\ wordlists/colors.txt sample\ wordlists/cars.txt   
FastRedFord  
FastRedChevy  
FastRedToyota  
FastBlueFord  
FastBlueChevy  
FastBlueToyota  
FastWhiteFord  
FastWhiteChevy  
...  


##DictPhrase-Builder  
Using a single wordlist, match each word with every other word in the file (x) amount of times.  
Usage is: ./dictphrase-builder.py <input wordlist> <word hamming distance>  

./dictphrase-builder.py sample\ wordlists/listall.txt 3  
FastFastFast  
FastFastSlow  
FastFastGreen  
FastFastBlue  
FastFastRed  
FastFastFord  
FastFastChevy  
...  


##Phrase Builder  
Using an imported song/movie script/book/etc, generate phrases from the input (x) long.  
Usage is: ./phrase-builder.py <input file> <output file> <word hamming distance>  

./phrase-builder.py sample\ wordlists/starwarsv.txt starwarsv-out.txt  4  
grep force starwarsv-out.txt   
disturbanceintheforce  
intheforcevader  
theforcevaderi  
forcevaderihave  
himemperortheforce  
emperortheforceis  
theforceisstrong  
...  


##Mask-Builder  
Using an imported wordlist(cracked passwords), generate the password masks and sort by most common.  
Usage is: ./mask-builder.py <input wordlist> <output masklist>  

./mask-builder.py sample\ wordlists/passwords.txt passwords-mask.txt  
Outputting Data  
Total time was 0.000359058380127  
Speed was 50131.123506 words per second  

head -n 5 passwords-mask.txt   
?u?l?l?l?l?l?d?d?s,3 Occurances,16.6666666667%  
?u?l?l?l?l?d?d?d?s,3 Occurances,16.6666666667%  
?u?l?l?l?l?l?l?l?d?s,3 Occurances,16.6666666667%  
?u?l?l?l?d?d?d?s,2 Occurances,11.1111111111%  
?u?l?l?l?l?l?d?s,2 Occurances,11.1111111111%  


##NTLMmyLM.py
Using a output potfile list from LM Cracked hashes (which lose case-sensitivity) this script will generate all possibilities to be fed into STDIN oclHashcat Password Dump Format.

python NTLMmyLM.py lm-cracked.txt 
winter2017
winteR2017
wintEr2017
wintER2017
winTer2017
winTeR2017
winTEr2017
winTER2017
wiNter2017
wiNteR2017
wiNtEr2017
wiNtER2017
wiNTer2017
wiNTeR2017
wiNTEr2017
wiNTER2017
wInter2017
wInteR2017
wIntEr2017
wIntER2017
wInTer2017
wInTeR2017

