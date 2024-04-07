# streamlit.io link:
# code_04_17_test_score_average.py
# The program aveage test score. It asks the user for the number of students and the number of the average score per student
import streamlit as st
st.title('Average Test Score Calculator')
# Get the number of students
students_num = st.number_input("How many students do you have?", min_value=1, step=1)
# Get the number of test score per students
num_exam = st.number_input("How many exams per student?", min_value=1, step=1)
Total_Score = 0
for student in range(1, students_num + 1):
    st.write(f"## Student {student}'s scores")
    total = 0

    # Repeat calculation for exam
    for test_num in range(1, num_exam + 1):
        test_score = st.number_input(f"Student {student}: What's the test score for exam {test_num}?", min_value=0.0,
                                     max_value=100.0, step=0.1)
        total += test_score

    average_score = total / num_exam
    st.write(f"The average score of Student {student} is {average_score:.2f}")
    Total_Score += total
    # Calculating and displaying the overall average
    Total_student_exams = students_num * num_exam
    Average_score = Total_Score / Total_student_exams
    st.write(f"## Overall average score for all students is {Average_score:.2f}")
# add a print line for which number of exam you are
# add input validation for exam score. each exam score should be in range of 0 to 100
# for extra assignment point
    # add calculation of average of all students
    # add keep going mechanism
    # based on the code, make a streamlit app
    # upload the code to the github and deploy your app using streamlit.io
    # write a streamlit link