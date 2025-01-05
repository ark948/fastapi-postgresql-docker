from fastapi import FastAPI





app = FastAPI()




@app.get('')
@app.get('/')
def root():
    return "root"



@app.get('/test')
def test():
    return {"message": "test successful"}
