from asyncio import sleep

async def wait_seconds(context):
    await sleep(context['seconds'])