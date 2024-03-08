import os

LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()

CUSTOM_LOGGERS = [
    "uvicorn",
    "uvicorn.error",
    "uvicorn.access",
]
