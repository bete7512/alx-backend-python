#!/usr/bin/env python3
""" async generator """
import asyncio
from typing import Generator
import random

async_generator = __import__('0-async_generator').async_generator

async def async_comprehension() -> Generator[float, None, None]:
    """ async generator """
    return [i async for i in async_generator()]