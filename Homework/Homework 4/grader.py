import pickle
from sklearn.metrics import mean_squared_error, accuracy_score
from math import sqrt

def grade_1(test_labels_predict):
    file = open('check.pkl', 'rb')
    test_labels = pickle.load(file)
    file.close()
    try:
        grade=0
        test_rmse = sqrt(mean_squared_error(test_labels, test_labels_predict))
        if(test_rmse < 7):
            grade=100
    except:
        return "Answer is not in format as specified in the question"
    return grade

def grade_2(predicted_labels):
    file = open('check_2.pkl', 'rb')
    test_labels = pickle.load(file)
    file.close()
    try:
        grade=0
        acc = accuracy_score(predicted_labels,test_labels)
        if(acc>=0.75):
            grade=100
    except:
        return "Answer is not in format as specified in the question"
    return grade
    