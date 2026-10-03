"""
logger.py
"""

import structlog
import logging
import sys
import os

def configure_logger(log_file_dir: str, log_file_name: str = "app.log"):
    """
    Configure structlog logger
    
    Args:
        log_file_dir: Log file directory
        log_file_name: Log file name, default is "app.log"
    """
    log_file_path = os.path.join(log_file_dir, log_file_name)
    os.makedirs(log_file_dir, exist_ok=True)
    
    logging.basicConfig(
        format="%(message)s",
        stream=sys.stdout,
        level=logging.INFO,
    )
    
    structlog.configure(
        processors=[
            structlog.stdlib.add_logger_name,
            structlog.stdlib.add_log_level,
            structlog.stdlib.PositionalArgumentsFormatter(),
            structlog.processors.TimeStamper(fmt="%Y-%m-%d %H:%M:%S"),
            structlog.processors.StackInfoRenderer(),
            structlog.processors.format_exc_info,
            structlog.processors.UnicodeDecoder(),
            structlog.stdlib.render_to_log_kwargs,
        ],
        context_class=dict,
        logger_factory=structlog.stdlib.LoggerFactory(),
        wrapper_class=structlog.stdlib.BoundLogger,
        cache_logger_on_first_use=True,
    )
    
    file_handler = logging.FileHandler(log_file_path, encoding='utf-8')
    file_handler.setFormatter(logging.Formatter(
        fmt="%(asctime)s [%(name)s] %(levelname)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    ))
    
    root_logger = logging.getLogger()
    root_logger.addHandler(file_handler)
    
    return structlog.get_logger()

def get_logger(name: str):
    """
    Get structlog logger with specific name or module name as context
    
    Args:
        name: Logger name (usually module name)
        
    Returns:
        structlog logger instance
    """
    return structlog.get_logger(name)