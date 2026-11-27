dog = {
    'name': 'John',
    'color': 'white',
    'breed': 'British',
    'age': '3',
    'legs': 'long'
}
student = {
    'first_name': 'Akhil',
    'last_name': 'Maccha',
    'marital_status': 'Single',
    'age': 23,
    'country': 'India',
    'skills' : ['JavaScript', 'React', 'Node', 'MongoDB', 'Python']
    }

print(len(student))
print(student['skills'])
print(type(student['skills']))

student['skills'].append('AIML')
student['skills'].append('Robotics')
print(student['skills'])

print(student.keys())
print(student.values())
print(student.items())

student.pop('age')
print(student)

del dog
print(dog)
