# User input gender 
gender = (input("Would you consider yourself a male or a female? :" ))

# Making sure user type the desired input 

while gender not in ("male", "female"):
	gender = input("Please type either male or female: ")		

# User input body metrics
height = int(input("What is your height in cm: "))
weight = int(input("What is your weight in kg: "))
shoe_size = int(input("What is your shoe size in Euro: "))

# Dependencies 
from sklearn import tree
from sklearn import neural_network
from sklearn import discriminant_analysis
from sklearn.metrics import accuracy_score

# Training data: [height, weight, shoe size]
X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40], [190, 90, 47], [175, 64, 39],
     [177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43], [153, 53, 34]]

Y = ['male', 'male', 'female', 'female', 'male', 'male', 'female', 'female', 'female', 'male', 'male', 'female']

# Print user's input geder
print (gender)

# Move user input into data format 
if gender == 'male':
	gender_true = ['male']
else: 
	gender_true = ['female']	

#Classifier 1

clf = tree.DecisionTreeClassifier()

clf = clf.fit(X,Y)

prediction = clf.predict([[height, weight, shoe_size]])

print ("Tree Classifier thinks you are a",prediction)

score = accuracy_score(gender_true, prediction)

if score == 1.0:
		print ("Damn right Tree Classifier")
else: 
		print ("Not this time Tree Classifier")	

#Classifier 2

clf1 =  neural_network.MLPClassifier()

clf1 = clf1.fit(X,Y)

prediction1 = clf1.predict([[height, weight, shoe_size]])

print ("MLP Classifier thinks you are a",prediction1)

score1 = accuracy_score(gender_true, prediction1)

if score1 == 1.0:
		print ("Damn right MLP Classifier")
else: 
		print ("Not this time MLP Classifier")	

#Classifier 3

clf2 =  discriminant_analysis.QuadraticDiscriminantAnalysis()

clf2 = clf2.fit(X,Y)

prediction2 = clf2.predict([[height, weight, shoe_size]])

print ("Quadratic Discriminant thinks you are a",prediction2)

score2 = accuracy_score(gender_true, prediction2)

if score2 == 1.0:
		print ("Damn right Quadratic")
else: 
		print ("Not this time Quadratic")	
