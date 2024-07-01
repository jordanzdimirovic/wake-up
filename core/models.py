from pydantic import BaseModel

# Orchestration (file)

class Action(BaseModel):
    id: str
    params: dict[str, object]    


class Routine(BaseModel):
    name: str
    actions: list[Action]


class OrchestrationJSON(BaseModel):
    routines: list[Routine]


###

# Options (file)

class ScheduledItem(BaseModel):
    time: str
    routine: str


class ScheduleJSON(BaseModel):
    weekday: ScheduledItem
    weekend: ScheduledItem

###