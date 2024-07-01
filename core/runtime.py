from core.models import Routine
from ext import funcs
async def sim_routine(routine: Routine):
    for action in routine.actions:
        fn = funcs[action.id]
    
        await fn (
            action.params
        )