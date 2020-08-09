import pickle
from sklearn.metrics import mean_squared_error, accuracy_score
from math import sqrt
import requests
user_id = open('/home/admin_/nimblebox-comput-server/user.txt').read()

def grader_1(test_labels_predict):
    try:
        global user_id 
        file = open('check.pkl', 'rb')
        test_labels = pickle.load(file)
        file.close()
        grade=0
        test_rmse = sqrt(mean_squared_error(test_labels, test_labels_predict))
        if(test_rmse < 7):
            grade=100
        data = {
        "username": user_id,
        "question_id": "HW4_1",
        "grade": grade
        }
        requests.post("http://10.140.0.92/upload_result", json=data)
    except:
        return "Answer is not in format as specified in the question"
    return "Homework has been submitted successfully"

def grader_2(predicted_labels):
    try:
        global user_id 
        file = open('check_2.pkl', 'rb')
        test_labels = pickle.load(file)
        file.close()
        grade=0
        acc = accuracy_score(predicted_labels,test_labels)
        if(acc>=0.75):
            grade=100
        data = {
        "username": user_id,
        "question_id": "HW4_2",
        "grade": grade
        }
        requests.post("http://10.140.0.92/upload_result", json=data)
    except:
        return "Answer is not in format as specified in the question"
    return "Homework has been submitted successfully"
    