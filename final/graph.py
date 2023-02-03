'''
Authors: Ryan Heise, Alexa Roskowski
CS 422 Software Methodologies
EasyA

Development Process:
1/19 --> made an aper funct as proof of
	concept 

1/22 --> changed aper funct, so if same teacher
	taught more than one class, the average
	percent would be used

1/25 --> code pushed to github

1/26 --> started to pull from parser.py

1/26 --> added function to sort teacher data 
	(sort_dict_by_value)

1/28 --> added department_graph() with if ask for 
	whole department. Displays class level 

1/30 --> added graph_data() so we dont need to
	resuse old code

1/31 --> added all_class_graph() that graphs
	all classes within a department.

2/1 --> finalized project and created tests

2/1 --> added comments describing what functions do

NOTE: There could be a bug the way we are storing professor names in dict. We store their last names, but what if 2 people have the same last name
		we should change the key to their full name and just display their last
	  Take out MI from name when graphing

'''

# Imports
import matplotlib.pyplot as plt
import parser as p 

# Globals

def main(dep: str, level:str , classNum: str, allInstrucs: bool, list_dept_num: bool, display_d_f: bool = False, countClasses: bool = False):
	"""
	Summary: 
		- This function processes a query about course grades based on various 
		inputs. It uses parseGradeData function to get grade data and calls different 
		graph functions (all_class_graph, department_graph, instructor_graph) based on 
		the inputs to display the results.

	Input:
		- department name (dep), 
		- level (100-600), 
		- class number (classNum), 
		- display all instructors or just faculty (allInstrucs)
	Return: 
		- None
	"""
	# Parse all classes in department
	if level == None and classNum == None:
		#we only have department name, go through all the classes
		data = p.parseGradeData(dep, None, None)
		if list_dept_num:
			department_graph(data, dep, level, display_d_f, allInstrucs, countClasses)
		else:
			all_class_graph(data, dep, display_d_f, allInstrucs, countClasses)

	# Parse level in department
	elif level != None and dep != None and classNum == None:
		# we have the level of the department
		allC = p.getClassNumbers(dep)
		data = allC[int(level)]
		if list_dept_num:
			department_graph(data, dep, level, display_d_f, allInstrucs, countClasses)
		else:
			# we have the level of the department
			dat = []
			for c in data:
				dat += p.parseGradeData(dep, c, None)
			#plug into grapher
			instructor_graph(dep+level, dat, display_d_f, allInstrucs, countClasses)

	# Parse individual class
	elif classNum != None and dep != None and level == None:
		# we have department and class number
		#get data
		d = p.parseGradeData(dep, classNum, None)
		#plug into aPer
		instructor_graph(dep + classNum, d, display_d_f, allInstrucs, countClasses)
	else:
		print("ERROR: Invalid querry")

# ------------------------------------------------------------------
#				FUNCTIONAL REQUIREMENT GRAPHS
# ------------------------------------------------------------------
def all_class_graph(class_list, dep, display_d_f, allInstrucs, countClasses):
	"""
	Summary: 
		- Displays graph with all classes in a department where the y-axis 
		  is the professor name and x-axis is the average percentage they 
		  give. Graph similar to a2 in Project 1 Document
	Input:
		- class_list (dict) : dictionary provided from web scraper 
		- dep (str) : Department of class (ie MATH, BI, CS)
	Return: 
		- None
	"""
	myDict = {}
	for i in class_list:
		for j in class_list[i]:
			lname = j['instructor'].split(',')[0].strip()
			fname = j['instructor'].split(',')[1].strip()
			full_name = fname + " " + lname

			total_failing = float(j['dprec']) + float(j['fprec'])
			aprec = float(j['aprec'])

			# Teacher name is already in dictionary. Add values to it
			if full_name in myDict:
				myDict[full_name][0] += aprec 			# a percentage
				myDict[full_name][1] += total_failing 	# d/f percentage
				myDict[full_name][2] += 1 				# number of classes
			# first time this teacher has shown up (count is 1)
			else:
				# check if we want all instructors or just faculty 
				if not allInstrucs and (i['instructor']) in p.getFacultyData(dep):
					# just Faculty
					myDict[full_name] = [aprec, total_failing, 1]
				elif allInstrucs:
					# all instructors
					myDict[full_name] = [aprec, total_failing, 1]
	myDict = average_dict(myDict)
	graph_data(myDict, "Instructor", f'All {dep} Classes', display_d_f, countClasses)

def department_graph(class_list, dep, level, display_d_f, allInstrucs, countClasses):
	"""
	Summary: 
		- Displays graph with all classes in a specified level where the 
		  y-axis is the class level and x-axis is the average percentage 
		  they give. Graph similar to graph (b) in Project 1 Document
	Input:
		- class_list () : 
		- dep (str) : Department of class (ie MATH, BI, CS)
		- level (str) : Level of class (ie 122, 314)
	Return: 
		- None
	"""

	# mydict = {class_num_1: [aperc, d+fperc, number_of_classes], class_num_2: [...]}
	myDict = {}
	# Loop over the list of classes (i is the class number ie 314)
	for i in class_list:
		class_data = p.parseGradeData(dep, i, None)
		for j in class_data:
			lname = j['instructor'].split(',')[0].strip()
			fname = j['instructor'].split(',')[1].strip()
			full_name = fname + " " + lname

			total_failing = float(j['dprec']) + float(j['fprec'])
			aprec = float(j['aprec'])

			# Teacher name is already in dictionary. Add values to it
			if i in myDict:
				myDict[i][0] += aprec 			# a percentage
				myDict[i][1] += total_failing 	# d/f percentage
				myDict[i][2] += 1 				# number of classes

			# first time this teacher has shown up (count is 1)
			else:
				# check if we want all instructors or just faculty 
				if not allInstrucs and (j['instructor']) in p.getFacultyData(dep):
					# just Faculty
					myDict[i] = [aprec, total_failing, 1]
				elif allInstrucs:
					# all instructors
					myDict[i] = [aprec, total_failing, 1]
	myDict = average_dict(myDict)
	if level != None:
		graph_data(myDict, "Classes", f'All {dep} {level}-level', display_d_f, countClasses)
	else:
		graph_data(myDict, "Classes", f'All {dep} Classes', display_d_f, countClasses)

def instructor_graph(class_name, data, display_d_f, allInstrucs, countClasses):
	"""
	Summary: 
		- Displays graph with all professors who teach a specified class 
		  number where the y-axis are the instructors and x-axis is the 
		  average percentage they give. Graph similar to graph (b) in 
		  Project 1 Document
	Input:
		- class_name (str) : Name of the class
		- data (dict) : Dictionary from the scraper
	Return: 
		- None
	"""
	myDict = {}
	# Loop through data provided by scraper
	for i in data:
		#lname = i['instructor'].split(',')[0].strip()
		lname = i['instructor'].split(',')[0].strip()
		fname = i['instructor'].split(',')[1].strip()
		full_name = fname + " " + lname

		total_failing = float(i['dprec']) + float(i['fprec'])
		aprec = float(i['aprec'])

		# Teacher name is already in dictionary. Add values to it
		if full_name in myDict:
			# we have a teacher who has taught already
			# add to the count of classes taught
			myDict[full_name][2] += 1; 
			myDict[full_name][0] += aprec
			myDict[full_name][1] += total_failing

		# first time this teacher has shown up (count is 1)
		else:
			# check if we want all instructors or just faculty 
			if not allInstrucs and i['instructor'] in p.getFacultyData(''.join([i for i in class_name if not i.isdigit()])):
				# just Faculty
				myDict[full_name] = [aprec, total_failing, 1]
			elif allInstrucs:
				# all instructors
				myDict[full_name] = [aprec, total_failing, 1]

	myDict = average_dict(myDict)
	if allInstrucs:
		graph_data(myDict, "Instructor", f'All {class_name}', display_d_f, countClasses)
	else:
		graph_data(myDict, "Instructor", class_name, display_d_f, countClasses)
	
# ------------------------------------------------------------------
#						CREATE GRAPHS
# ------------------------------------------------------------------
def graph_data(myDict, y_label: str, title:str, display_d_f: bool, countClasses: bool):
	"""
	Summary: 
		- Graphs data using matplotlib
	Input:
		- class_name (str) : Name of the class
		- data (dict) : Dictionary from the scraper
	Return: 
		- Graph
	"""
	# Call helper function to sort dict in decreasing order
	sorted_a = sort_dict_by_value(myDict, key_func=lambda x: x[0])
	sorted_f = sort_dict_by_value(myDict, key_func=lambda x: x[1])

	#create lists, so mathplots is easier		
	a_data = []
	a_per = []
	f_data = []
	f_per = []

	#add how many classes this professors done to name 'a' grades
	for i in sorted_a:
		numClasses = " (" + str(myDict[i][2]) + ")"
		a_data.append(i + (numClasses if countClasses else ''))
		a_per.append(myDict[i][0])
	#add how many classes this professors done to name for 'd/f' grades
	for j in sorted_f:
		numClasses = " (" + str(myDict[i][2]) + ")"
		f_data.append(j + (numClasses if countClasses else ''))
		f_per.append(myDict[j][1])

	# Check if user wanted to display 2 graphs
	if display_d_f:
		fig, ax = plt.subplots()
		ax.barh(f_data, f_per)
		ax.set_xlabel("Percentage of D / F")
		ax.set_ylabel(y_label)
		ax.set_title(title)
		ax.tick_params(axis='y', labelsize=6)
		plt.tight_layout()
		plt.show()
		return
	else:
		# Create one graph
		fig, ax = plt.subplots()
		ax.barh(a_data, a_per)
		ax.set_xlabel("Percentage of A's")
		ax.set_ylabel(y_label)
		ax.set_title(title)
		ax.tick_params(axis='y', labelsize=6)
		plt.show()
	return


# ------------------------------------------------------------------
#						AUXILIARY FUNCTIONS
# ------------------------------------------------------------------
def average_dict(myDict):
	"""
	Summary: 
		- Takes in dictionary with format: {key: [aperc, fperc, total_classes]})
		  and averages the aperc and fperc
	Input:
		- myDict (dict): format {key: [aperc, fperc, total_classes]})
	Return:
		- Averaged aperc and fperc based on total_classes
	"""
	# loop through all elements in myDict
	for i in myDict:
		total_classes = myDict[i][2]
		# Average 'a' score
		if myDict[i][0] != 0 or myDict[i][2] != 0:
			myDict[i][0] = myDict[i][0] / total_classes
		# Average 'd/f' score
		if myDict[i][1] != 0 or myDict[i][2] != 0:
			myDict[i][1] = myDict[i][1] / total_classes
	return myDict


def sort_dict_by_value(d, key_func, reverse=True):
	"""
	Summary: 
		- Sorts dictionary values in order
	Input:
		- d (dict) : Dictionary you want sorted. format {key: [aperc, fperc, total_classes]})
		- key_func (lambda func) : lambda function of item in list you want sorted
		- reverse (bool) : Sort list by increasing/decreasing order
	Return:
		- sorted dictionary
	"""
	return dict(sorted(d.items(), key=lambda item: key_func(item[1]), reverse=reverse))





#main(dep, level, classNum, allInstrucs, list_dept_num, display_d_f, countClasses)

# FUNCTIONAL REQUIREMENTS
# 1a) A single class (such as "Math 111")
# main("BI", None, None, True, True, False, False)

# 1b) A single department (such as "Math")
#main("MATH", None, None, True, False, False)

# 1c) All classes of a particular level within a department (such as "All Math 100-level Classes") 
#	  (This should list instructor names rather than class number)
# main("CIS", "100", None, True, False, False, False)


# 2a) All classes of a particular level within a department (such as "All Math 100-level Classes")
#     (This should list class number rather than instructor name)
# main("CIS", "100", None, False, True, False, False)

# 3a) "All Instructors" vs "Regular Faculty" (all instructors is the default)
		# DONE with allInstrucs argument in main()