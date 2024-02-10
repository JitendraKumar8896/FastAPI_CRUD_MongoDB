def individual_serial(fastDemo) -> dict:
    return {
        "id": str(fastDemo["_id"]),
        "name": fastDemo["name"],
        "desc": fastDemo["desc"],
        "complete": fastDemo["complete"]
    }


def list_serial(fastDemos) -> list:
    return [individual_serial(fastDemo) for fastDemo in fastDemos]
