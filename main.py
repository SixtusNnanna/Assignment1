from fastapi import FastAPI
from uuid import UUID


student_resource = {}

student_data = {
"id":0,
"name":"",
"age":0,
"sex":"",
"height":0.0,

}



app = FastAPI()


@app.get('/')
def home():
    return {'message': 'This is a student resource page'}


@app.post('/student')
def create_student(name:str, age:int, sex:str, height:float):
    new_student = student_data.copy()   # A dictionary of a new student data
    new_student['id'] = str(UUID(int=len(student_resource) + 1))
    new_student['name'] = name
    new_student['age'] = age
    new_student['sex'] = sex
    new_student['height'] = height

    student_resource[new_student['id']] = new_student

    return {'message': 'Student created successfully', "data":new_student}



@app.get('/students')
def get_students():
    return student_resource


@app.get('/students/{id}')
def get_student(id:str):
    student = student_resource.get(id)

    if not student:
        return {'message': 'Student with the stated id  was not found',}
    
    return student


@app.put('/student/{id}/update')
def update_student(id:str, name:str, age:int, sex:str, height:float):
    student = student_resource.get(id)

    if not student:
        return {'message': 'Student with the stated id  was not found',}

    student['name'] = name
    student['age'] = age
    student['sex'] = sex
    student['height'] = height

    return {"message": "student data has been Updated successfully"}



@app.delete('/student/{id}/delete')
def delete_student(id:str):
    student = student_resource.get(id)
    if not student:
        return {'message': 'Student with the stated id  was not found',}

    del student_resource[id]

    return {"message": "student data has been Deleted successfully"}