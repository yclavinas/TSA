#!/usr/bin/python
import re

# phone = "2004-959-559 # This is Phone Number http://www.google.com \n"
# # Delete Python-style comments
# num = re.sub(r'#.*$', "", phone)
# # print "Phone Num : ", num

# # Remove anything other than digits
# num = re.sub(r'\D', "", phone)    
# # print "Phone Num : ", num

# phone = "2004-959-559 # This http://www.google.com is Phone Number http://www.google.com \n"
# text = re.sub(r'http.*', '', phone, flags=re.MULTILINE)
# print text


text = open('TsukubaShi.txt', 'r')
saveFile = open('TsukubaShi_noUrl.txt', 'w')

for line in text:
	data = re.sub(r'^RT.*', '', line, flags=re.MULTILINE)
	data = re.sub(r'http(s)*://(\S)*', '', data, flags=re.MULTILINE)
	data = re.sub(r'Wed\ .*', '', data, flags=re.MULTILINE)
	data = re.sub(r'Tue\ .*', '', data, flags=re.MULTILINE)
	#melhorar ne?
	data = re.sub(r'[a-z]*@[a-z]+mail.com', '', data, flags=re.MULTILINE)
	
	saveFile.write(data)
	saveFile.write('\n')

print("End :D")

saveFile.close()
text.close()