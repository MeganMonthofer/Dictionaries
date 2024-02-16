#

student = {'name':'Megan Monthofer',
           'age':21,
           'major':'MIS',
           'hobbies':['pickleball', 'chess', 'volunteering']}

student['State'] = 'Texas'

student['age'] += 1

for k, v in student.items():
    if(k == 'hobbies'):                             # properly formats hobbies
        print(f'Your {k} are ', end = '') 
        j = 0
        for i in student['hobbies']:
            if j == len(student['hobbies']) - 1:    # properly prints last element in hobbies
                print(f'and {i}')
            else:
                print(f'{i}', end = ', ')           # prints elements in hobbies
            j += 1
    else:
        print(f'Your {k} is {v}')                   # prints elements in student

