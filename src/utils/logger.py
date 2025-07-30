import logging
import sys
from pathlib import Path

def setup_logger(config: dict, name: str = 'traffic_analysis') -> logging.Logger:
    """Set up logging configuration."""
    
    # Create logs directory if it doesn't exist
    log_dir = Path('logs')
    log_dir.mkdir(exist_ok=True)
    
    # Configure logging
    logging.basicConfig(
        level=getattr(logging, config['logging']['level']),
        format=config['logging']['format'],
        handlers=[
            logging.FileHandler(log_dir / 'traffic_analysis.log'),
            logging.StreamHandler(sys.stdout)
        ]
    )
    
    logger = logging.getLogger(name)
    return logger