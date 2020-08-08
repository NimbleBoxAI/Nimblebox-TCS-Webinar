import pickle
def grade_1(df):
    file = open('check.pkl', 'rb')
    data = pickle.load(file)
    file.close()
    try:
        grade=0
        if(df.equals(data)):
            grade=100
    except:
        return "Answer is not in format as specified in the question"
    return grade
    