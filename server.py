from fastapi import FastAPI
from resource.MYAPI import name_value
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/{name}')
async def root(name):
    value= name_value(name)
    return value