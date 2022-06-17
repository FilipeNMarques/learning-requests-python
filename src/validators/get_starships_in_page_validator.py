from cerberus import Validator

from src.errors import HttpUnprecessableEntitity


def get_starships_validator(request: any):
    """
    Get starship validaor
    :param request:
    :return:
    """
    query_param_validator = Validator(
        {"page": {"type": "string", "allowed": ["1", "2", "3", "4"], "required": True}}
    )

    response = query_param_validator.validate(request.query_params)

    if response is False:
        raise HttpUnprecessableEntitity(query_param_validator.errors)
