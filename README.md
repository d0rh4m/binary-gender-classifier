# binary-gender-classifier

Classifies one as either male or female given body metrics, with three sci-kit classifiers: 

1. Decision Tree Classifier 
2. MLP Classifier 
3. Quadratic Discriminant Analysis 

# Usage

The code prompts for user's gender (male or female), which will be used as the gender_true to calculate the accuracy_score of the three classifiers. It will then prompt for user's height, weight and shoe size - and attempts to guess user's gender. If the classifier gets it right, the code will print "Damn right classifier", else it would print "Not this time classifier" 
