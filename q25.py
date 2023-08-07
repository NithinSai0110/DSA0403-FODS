from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

def get_user_input():
 
    print("Enter the dimensions of the new flower:")
    sepal_length = float(input("Sepal Length: "))
    sepal_width = float(input("Sepal Width: "))
    petal_length = float(input("Petal Length: "))
    petal_width = float(input("Petal Width: "))
    return [[sepal_length, sepal_width, petal_length, petal_width]]

def main():

    iris = load_iris()
    X = iris.data
    y = iris.target
    
    new_flower = get_user_input()

    dt_classifier = DecisionTreeClassifier()
    dt_classifier.fit(X, y)

    prediction = dt_classifier.predict(new_flower)

    species_mapping = {
        0: "setosa",
        1: "versicolor",
        2: "virginica"
    }

    print(f"The species of the new flower is: {species_mapping[prediction[0]]}")

if __name__ == "__main__":
    main()
