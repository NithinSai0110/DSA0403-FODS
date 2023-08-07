import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

# Step 2: Load the Iris dataset
iris = load_iris()
X, y = iris.data, iris.target

# Step 3: Create a Decision Tree classifier and train it using the Iris dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
classifier = DecisionTreeClassifier()
classifier.fit(X_train, y_train)

# Step 4: Prompt the user to input the sepal length, sepal width, petal length, and petal width of the new flower
sepal_length = float(input("Enter sepal length: "))
sepal_width = float(input("Enter sepal width: "))
petal_length = float(input("Enter petal length: "))
petal_width = float(input("Enter petal width: "))

# Step 5: Use the trained classifier to predict the species of the new flower
new_flower = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
predicted_species = classifier.predict(new_flower)

# Map the predicted species index to actual species names
species_names = iris.target_names[predicted_species]

print("Predicted species:", species_names[0])
