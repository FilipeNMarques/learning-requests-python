class HttpUnprecessableEntitity(Exception):
    """HttpUnprecessableEntitity _summary_

    _extended_summary_

    Parameters
    ----------
    Exception : _type_
        _description_
    """

    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.message = message
        self.name = "Unprecessable Entity"
        self.status_code = 422
