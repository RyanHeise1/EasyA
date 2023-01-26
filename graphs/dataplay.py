'''
1/19/23 --> made an aper funct as proof of
	concept 

1/22 --> changed aper funct, so if same teacher
	taught more than one class, the average
	percent would be used

1/25 --> code pushed to github


'''

import json
import matplotlib.pyplot as plt

f = open('gd.js', 'r')

data = json.load(f)

def aPer(class_name):
	myDict = {}
	#'instructor': [ average_aper, count] 
	# 	eventually will probably want passing / d - f rate as well
	for i in data[class_name]:
		lname = i['instructor'].split(',')[0].strip()

		if lname in myDict:
			# we have a teacher who has taught already
			# add to the count of classes taught
			myDict[lname][1] += 1; 
			# average the a precentages 
			myDict[lname][0] = ( myDict[lname][0] + float(i['aprec']) ) / 2
		else:
			# first time this teacher has shown up (count is 1)
			myDict[lname] = [float(i['aprec']), 1]
	myDict = sort_dict_by_value(myDict, key_func=lambda x: x[0])

	#create lists, so mathplots is easier		
	instrucs = []
	a_per = []

	for i in myDict:
		#add how many classes this professors done to name
		instrucs.append(i + " (" + str(myDict[i][1]) + ")")
		a_per.append(myDict[i][0])


	#graphing 
	fig, ax = plt.subplots()
	ax.bar(instrucs, a_per)
	ax.set_ylabel("Percentage of A's")
	ax.set_xlabel("Professors' Last Names")
	ax.set_title(class_name)
	plt.show()

	#print(myDict)

def sort_dict_by_value(d, key_func, reverse=True):
	return dict(sorted(d.items(), key=lambda item: key_func(item[1]), reverse=reverse))


aPer("AAAP510")
aPer("AAAP511")
aPer("AAD199")


#What if bad input?! (not this problem)


f.close()



