import pyperclip
import re
# import asyncio

# async def other_function(text):
    # text = re.sub(r'.\t', '', text)
    # pyperclip.copy(text)

# async def main():
    # task = asyncio.create_task(pyperclip.waitForPaste())
    # text = await task
    # await other_function(text)
    

while (True):
    # asyncio.run(main())
    try:
        text = pyperclip.waitForNewPaste()
        print(text)
        text = re.sub(r'.\t', '', text)
        pyperclip.copy(text)
    except:
        pass