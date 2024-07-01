from kasa import Discover, Device

async def switch_state(context):
    devices = await Discover.discover()
    for d in devices.values():
        if d.alias.lower().strip() == context["switch_name"].lower().strip():
            await d.set_state(context["switch_state"])
