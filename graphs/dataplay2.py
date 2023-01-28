'''
1/19/23 --> made an aper funct as proof of
	concept 

1/22 --> changed aper funct, so if same teacher
	taught more than one class, the average
	percent would be used

1/26 --> started to pull from parser.py

1/28 --> dealing with if ask for whole department 



'''

#import json
import matplotlib.pyplot as plt
import pparser as p 



def A_percent(dep: str, level:str , classNum: str, allInstrucs: bool):
		#Takes all the info and deals with all the cases
			########
			# DOESN'T DEAL WITH ALLiINSTUCS YET
			########

		## dep = deparment type = string
		## level = 100, 200, 300, 400, 500, 600 type = string
		##	(None, if not used)
		## classN = class number; type = string (None, if not used)
		## allInstrucs = wether or not they want all instuctors
		##	or just faculty; type = boolean 
		##	(True is want all instuctor, False is just faculty)

		if level == None and classNum == None:
			#we only have department name, go through all the classes
			d = p.parseGradeData(dep, None, None)

			for c in d:
				#plots each individual class
				aPer(c, d[c])

		elif level != None and classNum == None:
			# we have the level of the department
			allC = p.getClassNumbers(dep)
			d = allC[int(level)]

			print(d)

			for c in d:
				da = p.parseGradeData(dep, c, None)
				#plots each individual class
				aPer(dep + c, da)
				pass


		elif classNum != None:
			# we have department and class number
			#get data
			d = p.parseGradeData(dep, classNum, None)
			#plug into aPer
			aPer(dep + classNum, d)



def aPer(class_name, data):
	myDict = {}
	#'instructor': [ average_aper, count] 
	# 	eventually will probably want passing / d - f rate as well
	for i in data:
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

	#create lists, so mathplots is easier		
	instrucs = []
	a_per = []

	for i in myDict:
		#add how many classes this professors done to name
		instrucs.append(i + " (" + str(myDict[i][1]) + ")")
		a_per.append(myDict[i][0])

	#graphing 
	fig, ax = plt.subplots(figsize = (12, 8))
	ax.barh(instrucs, a_per)
	ax.set_xlabel("Percentage of A's")
	ax.set_ylabel("Professors' Last Names")
	#ax.invert_yaxis()
	ax.set_title(class_name)
	plt.show()


	#print(myDict)


#aPer("AAAP510")
#aPer("AAAP511")
#aPer("AAD199")

#A_percent("BI", "200", None, True)
#A_percent("MATH", None, "111", True)


#What if bad input?! (not this problem)


#f.close()



