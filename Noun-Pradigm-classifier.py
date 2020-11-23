###############################################
#Author: K. Sarveswaran, iamsarves@gmail.com
#License: GPL3
#This script has the following functionalities:
#Classify nouns based on the pradigm,
#Here I used the theory / rules proposed by Prof. Rajendran in PRELIMINARIES TO THE PREPARATION OF A SPELL AND GRAMMAR CHECKER FOR TAMIL
#
#Version 0.9-06-08-2019
#Numbers points to the formula in Nanool. Everything here are written based on Nanool
##############################################

import re
import os
import subprocess

uyir=["அ","ஆ","இ","ஈ","உ","ஊ","எ","ஏ","ஐ","ஒ","ஓ","ஔ"]
shortv=["அ","இ","உ","எ","ஒ"]
longv=["ஆ","ஈ","ஊ","ஏ","ஐ","ஓ","ஔ"]
mei=["க","ச","ஞ","ட","ண","த","ந","ப","ம","ய","ர","ல","வ","ழ","ள","ற","ன"]

mei2=["ர","ல","ழ","ள","ன","ண"]

meiDaRa=["க","ச","ஞ","ண","த","ந","ப","ம","ய","ர","ல","வ","ழ","ள","ன"]
vm=["ா","ி","ீ","ு","ூ","ெ","ே","ை","ொ","ோ","ௌ"]

shortvm=["ி","ு","ெ","ொ"]
longvm=["ா","ீ","ூ","ே","ை","ோ","ௌ"]

plural=["பலர்","சிலர்","மக்கள்","குடிமக்கள்","பொதுமக்கள்"]


aa="ா"
i="ி"
ii="ீ"
u="ு"
uu="ூ"
e="ெ"
ee="ே"
ai="ை"
o="ொ"
oo="ோ"
au="ௌ"
ka="க"
ca="ச"
tha="த"
na="ந"
pa="ப"
ma="ம"
va="வ"
ya="ய"
gna="ஞ"
ng="ங"
da="ட"
raa="ற"
naa="ண"
la="ல"
zha="ழ"
ra="ர"
na2="ன"
La="ள"

pulli="்"

#Class 1

##def paradigm(word):
##        classno=[]
##        letters=[aa,oo,uu]
##        for x in letters:
##                p=re.compile(x+"$")
##                if p.search(word):
##                        classno.append(1)
##
##        letters=[i,ii,ai]
##        for x in letters:
##                p=re.compile(x+"$")
##                if p.search(word):
##                        classno.append(2)
##
##        letters=[i,ii,ai,ya+pulli]
##        for x in letters:
##                p=re.compile(x+"$")
##                if p.search(word):
##                        classno.append(3)
##
##        for itemmei in mei:
##            for itemvm in vm:
##                for itemmei2 in meiDaRa:
##                    textpattern="^"+itemmei+"("+itemvm+")?"+itemmei2+u+"$"
##                    p=re.compile(textpattern)
##                    #print(p)
##                    if re.search(p,word):
##                        classno.append(4)
##                        break
##                if len(classno)!=0 :
##                    break
##            if len(classno)!=0 :
##                break
##
##        for itemmei in mei:
##            for itemvm in vm:
##                textpattern=itemmei+"("+itemvm+")?"+da+u+"$"
##                p=re.compile(textpattern)
##                #print(p)
##                if re.search(p,word):
##                    classno.append(5)
##                    break
##            if len(classno)!=0 :
##                break
##                
##        for itemmei in mei:
##            for itemvm in vm:
##                textpattern=itemmei+"("+itemvm+")?"+ra+u+"$"
##                p=re.compile(textpattern)
##                if re.search(p,word):
##                    classno.append(6)
##                    break
##            if len(classno)!=0 :
##                break
##    
##
##        return classno
	

def paradigm(word):


#Class 5 - Plural words
	for itempl in plural:
		if itempl==word:
			return 5

#Class 3 - தே னீ
	for itemmei in mei:
		textpattern=itemmei+ii+"$"
		p=re.compile(textpattern)
		if re.search(p,word):
			return 3

#Class 3 - ஈ
	textpattern="ஈ"+"$"
	p=re.compile(textpattern)
	if re.search(p,word):
		return 3


#Class 7 - வண் டு
	textpattern=naa+pulli+da+u+"$"
	p=re.compile(textpattern)
	if re.search(p,word):
		return 7


#Class 6 - கா  டு

	textpattern=da+u+"$"
	p=re.compile(textpattern)
	if re.search(p,word):
		return 6    

#Class 15 - அகம்

	textpattern=ma+pulli+"$"
	p=re.compile(textpattern)
	if re.search(p,word):
		return 15

#Class 16 - ர்

	textpattern=ra+pulli+"$"
	p=re.compile(textpattern)
	if re.search(p,word):
		return 16

#Class 12 - பு,ல் க,ல்
	for itemmei in mei:
		for itemvm in shortvm:
			for itemsv in shortv:
				textpattern="^"+"["+itemmei+itemvm+","+itemmei+","+itemsv+"]"+la+pulli+"$"
				#print(textpattern)
				p=re.compile(textpattern)
				if re.search(p,word):
					return 12
			
#Class 9 - எ ண்
	for itemmei in mei:
		for itemsvm in shortvm:
			for itemsv in shortv:
				textpattern="["+itemmei+itemsvm+","+itemmei+","+itemsv+"]"+naa+pulli+"$"
				p=re.compile(textpattern)
				if re.search(p,word):
					return 9

#Class 10
	for itemmei in mei:
		for itemsvm in shortvm:
			for itemsv in shortv:
				textpattern="["+"^"+itemmei+itemsvm+","+"^"+itemmei+","+"^"+itemsv+"]"+na2+pulli+"$"
				#print(textpattern)
				p=re.compile(textpattern)
				if re.search(p,word) and len(word)==4:
					return 10
#Class 12
	for itemmei in mei:
		for itemsvm in shortvm:
			for itemsv in shortv:
				textpattern="["+"^"+itemmei+itemsvm+","+"^"+itemmei+","+"^"+itemsv+"]"+la+pulli+"$"
				#print(textpattern)
				p=re.compile(textpattern)
				if re.search(p,word) and len(word)==4:
					return 12
#Class 13
	for itemmei in mei:
		for itemsvm in shortvm:
			for itemsv in shortv:
				textpattern="["+itemmei+itemsvm+","+itemmei+","+itemsv+"]"+La+pulli+"$"
				#print(textpattern)
				p=re.compile(textpattern)
				if re.search(p,word) and len(word)==4:
					return 13
				elif re.search(p,word) and len(word)>4:
					return 14
#Class 14
	for itemmei in mei:
		for itemsvm in longvm:
			for itemsv in longv:
				textpattern="["+itemmei+itemsvm+","+itemmei+","+itemsv+"]"+La+pulli+"$"
				#print(textpattern)
				p=re.compile(textpattern)
				if re.search(p,word):
					return 14

#Class 11
	for itemmei in mei:
		for itemsvm in shortvm:
			for itemsv in shortv:
				textpattern=na2+pulli+"$"
				p=re.compile(textpattern)
				if re.search(p,word):
					return 11

# Class 2 for நெ ய்
	for itemmei in mei:
		for itemsvm in shortvm:
			for itemsv in shortv:
				textpattern="["+itemmei+itemsvm+","+itemsv+"]"+ya+pulli+"$"
				#print(textpattern)
				p=re.compile(textpattern)
				#print(p)
				if re.search(p,word):
					return 2
#Class 4 நா ய்
	for itemvm in longvm:
		for itemlv in longv:
			textpattern="["+itemvm+","+itemlv+"]"+ya+pulli+"$"
			p=re.compile(textpattern)
			if re.search(p,word):
				return 4
#Class 1 - க டா,  பூ, 
	letters=[aa,oo,uu,zha+u,ra+u,naa+u,ya+u]
	for x in letters:
			p=re.compile(x+"$")
			if p.search(word):

					return 1
#Class 8 - 
	letters=[raa+u]
	for x in letters:
			p=re.compile(x+"$")
			if p.search(word):
					return 8

#Class 7 - 
	letters=[u]
	for x in letters:
			p=re.compile(x+"$")
			if p.search(word):
					return 7

				
#Class 2 - க டா,  பூ, 
	letters=[i,ai]
	for x in letters:
			p=re.compile(x+"$")
			if p.search(word):
					return 2

#Class 3 - ஈ,  பீ
	letters=[ii,"ஈ"]
	for x in letters:
			p=re.compile(x+"$")
			if p.search(word):
					return 3

# Class 4 - ல், ,ன் ,ள் 
	for itemmei in mei2:
		textpattern=itemmei+pulli+"$"
		p=re.compile(textpattern)
		if re.search(p,word):
			return 4

#for x in words:
#	outt = paradigm(x)
#	print(x+"-")
#	print(outt)
wordf = open("noun-list-processed-unique", "r")

for word in wordf:
	classnos=paradigm(word)
	print(str(word).strip()+' '+"C"+str(classnos)+";")
	fh=open("noun-paradigm/class"+str(classnos)+".txt", "a")
	fh.write(str(word).strip()+' '+"C"+str(classnos)+";")
	fh.write("\n")
	fh.close()










#words=["எலி","புலி","காபி","சிறுமி","அங்காடி","கோழி","மொழி","வழி","பழி","இறைச்சி","பள்ளி","நாற்காலி","அரசி","யானை","பாடசாலை","பண்டகச்சாலை","படை","கோட்டை","கொட்டை","நடிகை","விடுமுறை","சந்தை","மந்தை","இலை","மலை","தலை","சாலை","பொய்","மெய்","வெண்ணெய்","ரொட்டி","கட்டி","சட்டி","பாட்டி","வேட்டி","தாடி","மாலை","தலை","பை","மை","கை"]
#words=["ஈ","தீ","பீ","தேனீ"]
#words=["பாய்","சேய்","நோய்","காய்","பேய்","தாய்","வாய்","கால்வாய்","கண்மாய்","தேங்காய்","ரூபாய்","போர்","தேர்","வேர்","நடிகர்","மாணவர்","கணவர்","மனிதர்","கால்","பால்","கோயில்","சேவல்","தோல்","நூல்","மீன்","பையன்","வான்","மான்","தேன்","தோள்","தேள்","வாள்","செவிள்","தாள்","ஆண்","இதழ்"]
#words=["தகடு","உதடு","நாடு","ஏடு","ஐயப்பாடு","தொடுகோடு","பாகுபாடு","மாடு","காடு"]
#words=["காசு","கதவு","கடுகு","உணவு","கிழங்கு","பந்து","கொத்து","வெண்ணிலவு","கள்ளு","எள்ளு","கொள்ளு","இருட்டு","தகராறு","தொண்டு","வண்டு"]
#words=["வயிறு","கயிறு","பயறு","வழக்காறு","ஆறு"]
#words=["எண்","மண்","விண்","புண்","பெண்","கண்"]
#words=["பையன்"]
#words=["பொன்"]
#words=["ஆள்","சித்தாள்","பொருள்","நாள்"]
#words=["மனிதன்","கணவன்","நடிகன்","அரசன்","மாணவன்"]
#words=["பல்","கல்","வில்","சொல்","நெல்","புல்"]
#words=["மரம்","குணம்","பழம்","கோலம்","மதம்","மாதம்","நகரம்","கட்டிடம்","புத்தகம்","சிங்கம்","குடும்பம்","மாநிலம்","கூட்டம்","நூலகம்"]
#words=["சுவர்","கார்"]
#words=["பலர்"]


#Class 1 - "கடா","பசு","தெரு","மடு","தெரு","பூ","குழு","உயிரணு","எண்ணுரு","கலைவிழா","கல்கத்தா","மது","வழு","வாயு","ரோஜா"
#Class 2 - "எலி","புலி","காபி","சிறுமி","அங்காடி","கோழி","மொழி","வழி","பழி","இறைச்சி","பள்ளி","நாற்காலி","அரசி","யானை","பாடசாலை","பண்டகச்சாலை","படை","கோட்டை","கொட்டை","நடிகை","விடுமுறை","சந்தை","மந்தை","இலை","மலை","தலை","சாலை","பொய்","மெய்","வெண்ணெய்","ரொட்டி","கட்டி","சட்டி","பாட்டி","வேட்டி","தாடி","மாலை","தலை","பை","மை","கை"
#Class 3 - "ஈ","தீ","பீ","தேனீ"
#Class 4 - "பாய்","சேய்","நோய்","காய்","பேய்","தாய்","வாய்","கால்வாய்","கண்மாய்","தேங்காய்","ரூபாய்","போர்","தேர்","வேர்","நடிகர்","மாணவர்","கணவர்","மனிதர்","கால்","பால்","கோயில்","சேவல்","தோல்","நூல்","மீன்","பையன்","வான்","மான்","தேன்","தோள்","தேள்","வாள்","செவிள்","தாள்","ஆண்","இதழ்"

#Class 6 - "தகடு","உதடு","நாடு","ஏடு","ஐயப்பாடு","தொடுகோடு","பாகுபாடு","மாடு","காடு"
#Class 7 - "காசு","கதவு","கடுகு","உணவு","கிழங்கு","பந்து","கொத்து","வெண்ணிலவு","கள்ளு","எள்ளு","கொள்ளு","இருட்டு","தகராறு","தொண்டு","வண்டு"
#Class 8 - "வயிறு","கயிறு","பயறு","வழக்காறு","ஆறு"
#Class 9 - "எண்","மண்","விண்","புண்","பெண்","கண்"

#Class 11 - "மனிதன்","கணவன்","நடிகன்","அரசன்","மாணவன்"
#Class 12 - "பல்","கல்","வில்","சொல்","நெல்","புல்"
