import logging

from flask import Flask

from app.log import InterceptHandler

app = Flask("chur-store")

logging.basicConfig(handlers=[InterceptHandler()], level=0)
