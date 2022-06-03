from proj07 import process

input_data =  [('4-Jan-02', 'Newark International Airport', 350.0, 'Approved', 350.0), ('2-Feb-02', 'Seattle-Tacoma International', 100.0, 'Settled', 50.0), ('2-Jan-03', 'William P. Hobby', 352.99, 'Settled', 150.0), ('5-Jan-04', 'Ft. Lauderdale-Hollywood International', 550.0, 'Settled', 275.0), ('4-Jan-05', 'William P. Hobby', 2000.0, 'Denied', 0.0), ('5-Jan-05', 'Ft. Lauderdale-Hollywood International', 173.11, 'Approved', 173.11), ('10-Jan-06', 'Phoenix Sky Harbor International', 214.95, 'Settled', 107.48), ('10-Jan-06', 'Houston - George Bush Intercontinental Airport', 995.0, 'Settled', 50.0), ('11-Jan-06', 'Florence Regional', 230.0, 'Canceled', 0.0), ('3-Jan-07', 'Houston - George Bush Intercontinental Airport', 25.0, 'Approved', 25.0), ('4-Jan-08', 'Washington Dulles International', 550.0, 'Settled', 332.35), ('8-Jan-09', 'Orlando International Airport', 371.0, 'Settled', 241.15), ('8-Jan-09', 'Austin-Bergstrom International Airport', 1047.53, 'Settled', 443.46)]
student_data = process(input_data)
instructor_data =  ([2, 1, 1, 2, 2, 1, 1, 2], [2, 1, 1, 1, 2, 1, 1, 2], [0, 0, 0, 1, 0, 0, 0, 0], 12, 199.77727272727273, 2000.0, 'William P. Hobby')
print("Student Data:\n",student_data)
print("Instructor Data:\n",instructor_data)
if student_data == instructor_data:
    print('done')