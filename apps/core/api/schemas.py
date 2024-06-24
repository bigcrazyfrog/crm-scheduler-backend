from ninja import Schema


class Message(Schema):
    """Message schema api response."""
    message: str


class DefaultResponse(Schema):
    """Response schema api response."""
    status: str = "success"
    message: str
    error: list[str] = []
