"""Some functions for my garden plan!"""


def add_by_kind(by_kind: dict[str, list[str]], new_plant_kind: str, new_plant: str) -> None: 
    """Add plant under its kind."""
    if new_plant_kind in by_kind: 
        by_kind [new_plant_kind].append (new_plant)
    else: 
        by_kind [new_plant_kind] = []   
        by_kind [new_plant_kind].append(new_plant)
