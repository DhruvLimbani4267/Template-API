import uvicorn
from fastapi import FastAPI
from templates import temps,temps_list
app = FastAPI()

@app.get("/templates/{template_name}")
def get_template(template_name: str):
    strg = temps[template_name]
    return strg

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)