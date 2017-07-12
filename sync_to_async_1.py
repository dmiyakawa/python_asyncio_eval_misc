import asyncio
import time

def hello():
    print('hello inside function')

loop = asyncio.get_event_loop()
try:
    loop.call_later(1, hello)
    print('hello outside function')
    # loop.run_forever()
    loop.run_until_complete(f)
finally:
    loop.close()


    
