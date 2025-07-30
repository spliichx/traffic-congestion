import pandas as pd
import numpy as np
from pathlib import Path
import logging
from typing import Tuple, Optional

logger = logging.getLogger(__name__)


class DataLoader:
    """Handle data loading operations for traffic analysis."""

    def __init__(self, config: dict):
        self.config = config
        self.raw_data_path = Path(config["data"]["raw_data_path"])

    def load_traffic_data(self, filename: str) -> pd.DataFrame:
        """Load traffic data from CSV file."""
        try:
            file_path = self.raw_data_path / filename
            df = pd.read_csv(file_path)
            logger.info(f"Loaded data with shape: {df.shape}")
            return df
        except FileNotFoundError:
            logger.error(f"File {filename} not found in {self.raw_data_path}")
            raise
        except Exception as e:
            logger.error(f"Error loading data: {str(e)}")
            raise

    def load_multiple_datasets(self, filenames: list) -> pd.DataFrame:
        """Load and combine multiple traffic datasets."""
        dataframes = []
        for filename in filenames:
            df = self.load_traffic_data(filename)
            dataframes.append(df)

        combined_df = pd.concat(dataframes, ignore_index=True)
        logger.info(f"Combined data shape: {combined_df.shape}")
        return combined_df

    def validate_data_schema(self, df: pd.DataFrame, required_columns: list) -> bool:
        """Validate that the dataframe has required columns."""
        missing_columns = set(required_columns) - set(df.columns)
        if missing_columns:
            logger.error(f"Missing required columns: {missing_columns}")
            return False
        return True
