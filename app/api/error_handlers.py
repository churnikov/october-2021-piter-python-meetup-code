from flask import jsonify
from loguru import logger

from ..errors import BaseAppError, UnexpectedError
from .main import app


@app.errorhandler(BaseAppError)
def handle_app_error(e: BaseAppError):
    return jsonify(e.json), e.error_code


@app.errorhandler(Exception)
def handle_exception(e: Exception):
    logger.exception(f"Unexpected error occurred '{e}'")
    unexpected_error = UnexpectedError()
    return jsonify(unexpected_error.json), unexpected_error.error_code
