import store
from fastapi import fastAPI

app = fastAPI()

@app.get('/')
def get_list():
  return [1,2,3]

@app.get('/contact')
def get_list():
  return {"name": 'platzi'}


def run():
  store.get_categories()


if __name__ == "__main__":
  run()