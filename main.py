from fastapi import FastAPI





app = FastAPI()




@app.get('')
@app.get('/')
def root():
    return "root"



@app.get('/test')
def test():
    return {"message": "test successful"}



@app.get('/test2')
def test2():
    return "Yes this is test 2"



@app.get('/test3')
def test3():
    return "test 3"
