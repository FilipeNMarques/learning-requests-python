from typing import Type, Dict

from src.errors import HttpRequestError, HttpUnprecessableEntitity


def handle_error(error: Type[Exception]) -> Dict:
    """handle_error _summary_

    _extended_summary_

    Parameters
    ----------
    error : Type[Exception]
        _description_

    Returns
    -------
    Dict
        _description_
    """

    if isinstance(error, HttpRequestError):
        return {"data": {"error": error.message}, "status_code": error.status_code}
    elif isinstance(error, HttpUnprecessableEntitity):
        return {"data": {"error": error.message}, "status_code": error.status_code}
    else:
        return {"data": {"error": str(error)}, "status_code": 500}
