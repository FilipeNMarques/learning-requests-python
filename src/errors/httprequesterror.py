class HttpRequestError(Exception):
    """
    Custom http error class
    """

    def __init__(self, message: str, status_code: int) -> None:

        super().__init__(message)
        self.message = message
        self.status_code = status_code
