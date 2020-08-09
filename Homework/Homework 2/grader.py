import requests
user_id = open('/home/admin_/nimblebox-comput-server/user.txt').read()

def grader_1(ans=0):
    try:
        global user_id 
        ans = round(ans,3)
        grade=0
        if(ans == 0.016):
            grade=100
        data = {
            "username": user_id,
            "question_id": "HW2_1",
            "grade": grade
            }
        requests.post("http://10.140.0.92/upload_result", json=data)
    except:
        return "Answer is not in format as specified in the question"
    return "Homework has been submitted successfully"