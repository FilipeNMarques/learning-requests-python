from cerberus import Validator


async def get_starship_information_validator(request: any):
    """get_starship_information_validator _summary_

    _extended_summary_

    Parameters
    ----------
    request : any
        _description_
    """

    body = None

    try:
        body = await request.json()
    except:
        pass

    body_validator = Validator(
        {
            "starship_id": {"type": "string", "required": True},
            "time": {"type": "string", "required": True},
        }
    )

    response = body_validator.validate(body)

    if response is False:
        raise Exception(body_validator.errors)
