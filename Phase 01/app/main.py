from typing import List

from fastapi import FastAPI, status, HTTPException, Depends
import uvicorn
from sqlalchemy.orm import defer

app = FastAPI()




def main():
    print("Hello from phase-01!")
    uvicorn.run(app, host="localhost", port=8000)



if __name__ == "__main__":
    main()
