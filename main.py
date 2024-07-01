import asyncio
import os

from core import runtime
from core.models import ScheduleJSON, OrchestrationJSON


ORCHESTRATION_JSON_FILE = os.path.join("config", "orchestration.json")
SCHEDULE_JSON_FILE = os.path.join("config", "schedule.json")

async def main():
    # Validate the JSONs
    with open(ORCHESTRATION_JSON_FILE, 'r') as f_orc, open(SCHEDULE_JSON_FILE, 'r') as f_sch:
        try:
            ORCHESTRATION, SCHEDULE = OrchestrationJSON.model_validate_json(f_orc.read()), ScheduleJSON.model_validate_json(f_sch.read())
        
        except Exception as e:
            print(f"Configuration error! {e}")
            exit()

    # Run one routine
    # TODO change
    # r = ORCHESTRATION.routines[0]
    # await runtime.sim_routine(r)


asyncio.run(main())
