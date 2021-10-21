from loguru import logger


class BaseAppError(Exception):
    def __init__(self, message: str = "") -> None:
        super().__init__(message)
        self.message = message
        logger.trace("Exception '{}' was raised. {}.", self.__class__.__name__, self.message)

    @property
    def error_code(self) -> int:
        raise NotImplementedError("Error code should be implemented.")

    @property
    def json(self) -> dict:
        raise NotImplementedError("json is not implemented.")


class AppError400(BaseAppError):
    @property
    def error_code(self) -> int:
        return 400


class AppError500(BaseAppError):
    @property
    def error_code(self) -> int:
        return 500


class InvalidDataError(AppError400):
    @property
    def json(self):
        return {"error": "error.data.invalid"}


class UnexpectedError(AppError500):
    @property
    def json(self):
        return {"error": "unexpected"}


class DataExistsError(AppError400):
    @property
    def json(self):
        return {"error": "error.data.exists"}
