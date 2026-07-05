from loguru import logger

logger.add(
    "logs/cortex.log",
    rotation="5 MB",
    retention=10,
    level="INFO"
)

logger.info("Logger Initialized")