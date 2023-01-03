from fastapi import FastAPI, Query
from random import randint

app = FastAPI()

ferrari = [{'brand': 'ferrari',
            'model': '812',
            'horsepower': '789'},

           {'brand': 'ferrari',
            'model': 'test1',
            'horsepower': '800'},

           {'brand': 'ferrari',
            'model': 'test2',
            'horsepower': '900'},

           {'brand': 'ferrari',
            'model': 'test4',
            'horsepower': '900'},

           {'brand': 'ferrari',
            'model': 'test5',
            'horsepower': '900'},


           {'brand': 'ferrari',
            'model': 'test6',
            'horsepower': '900'},


           {'brand': 'ferrari',
            'model': 'test7',
            'horsepower': '900'}
           ]

@app.get("/car/ferrari") #mss met while loop
async def get_car(number: int = Query(default=2, le=len(ferrari), description="This parameter is for determining how many ferrari's you want to see, the default value is 2")):
    cars = []
    for i in range(number):
        new_car = ferrari[randint(0, len(ferrari) - 1)]
        cars.append(new_car)
    return {"ferrari's": cars}
