import requests
user_id = open('/home/admin_/nimblebox-comput-server/user.txt').read()
def grader_1(out=[]):
    try:
        global user_id       
        correct=0
        if(out[0])=="No Ticket":
            correct+=1
        if(out[1])=="Big Ticket":
            correct+=1
        if(out[2])=="Small Ticket":
            correct+=1
        grade=correct/3.0*100
        data = {
        "username": user_id,
        "question_id": "HW1_1",
        "grade": grade
        }
        requests.post("http://10.140.0.92/upload_result", json=data)
    except:
        return "Answer is not in format as specified in the question"
    return "Homework has been submitted successfully"

def grader_2(out=[]):
    try:
        global user_id
        correct=0
        print(out)
        if(out[0])=="(32, 10, 22)":
            correct+=1
        if(out[1]=="No such triplet found"):
            correct+=1
        grade=correct/2.0*100
        data = {
        "username": user_id,
        "question_id": "HW1_2",
        "grade": grade
        }
        temp = requests.post("http://10.140.0.92/upload_result", json=data)
    except:
        return "Answer is not in format as specified in the question"
    return "Homework has been submitted successfully" 

def grader_3(out=""):
    try:
        global user_id
        ans3="""missing values: 1
    highest number: 7.0
    most common words: something, woop
    occurrences of most common: 3
    numbers: [1.0, 7.0, 2.0]
    words: ['something', 'something', 'n/a', 'wassup', 'woop', 'woop', 'something', 'woop']"""
        grade=0
        if(out==ans3):
            grade=100
        data = {
        "username": user_id,
        "question_id": "HW1_3",
        "grade": grade
        }
        requests.post("http://10.140.0.92/upload_result", json=data)
    except:
        return "Homework has been submitted successfully"