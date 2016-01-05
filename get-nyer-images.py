import datetime
import json

a = datetime.datetime.today()
numdays = 500
dateList = []
for x in range (0, numdays):
    dateList.append(a - datetime.timedelta(days = x))
    #print a- datetime.timedelta(days=x)
#print dateList
date_dict = {}
date_lst = []
a = 1
for j in dateList:
	if j.weekday() == 0:
		yyyy = str(j.year)
		yy = yyyy[-2:]
		if len(str(j.month)) == 1:
			mm = "0"+str(j.month)
		else:
			mm = str(j.month)
		if len(str(j.day)) == 1:
			dd = "0"+str(j.day)
		else:
			dd = str(j.day)
		url = 'http://www.newyorker.com/wp-content/uploads/%s/%s/%s%s%s_contest-690.jpg' %(yyyy, mm, yy, mm, dd)
		print url
		print j.date()
		date_dict[a] = ['%s-%s-%s'%(yyyy,mm,dd),url]
		date_lst.append(url)
		a += 1

print date_lst

#print date_dict

with open('nyer-data.txt','w') as outfile:
	json.dump(date_dict, outfile)






