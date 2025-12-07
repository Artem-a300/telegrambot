import asyncio
import os
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
#import

load_dotenv("security.env")
TOKEN = os.getenv("TOKEN")

async def main():
    print("Бот працює!")
    pass

if __name__ == "__main__":
    asyncio.run(main())
    
    