from typing import Optional

from app.errors import InvalidDataError


def validate_add_data(data: Optional[dict]) -> None:
    if data is None:
        raise InvalidDataError()
