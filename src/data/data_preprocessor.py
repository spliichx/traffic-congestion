import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split
import logging
from typing import Tuple

logger = logging.getLogger(__name__)

class DataPreprocessor:
    """Handle data preprocessing for traffic analysis."""
    
    def __init__(self, config: dict):
        self.config = config
        self.scaler = StandardScaler()
        self.label_encoders = {}
        
    def clean_data(self, df: pd.DataFrame) -> pd.DataFrame:
        """Clean the traffic data."""
        logger.info("Starting data cleaning...")
        
        # Remove duplicates
        initial_shape = df.shape
        df = df.drop_duplicates()
        logger.info(f"Removed {initial_shape[0] - df.shape[0]} duplicate rows")
        
        # Handle missing values
        missing_counts = df.isnull().sum()
        if missing_counts.sum() > 0:
            logger.info(f"Missing values found: {missing_counts[missing_counts > 0].to_dict()}")
            
            # Strategy for handling missing values
            for column in df.columns:
                if df[column].dtype in ['int64', 'float64']:
                    df[column].fillna(df[column].median(), inplace=True)
                else:
                    df[column].fillna(df[column].mode()[0], inplace=True)
        
        # Remove outliers using IQR method
        numeric_columns = df.select_dtypes(include=[np.number]).columns
        for column in numeric_columns:
            Q1 = df[column].quantile(0.25)
            Q3 = df[column].quantile(0.75)
            IQR = Q3 - Q1
            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR
            
            outliers = ((df[column] < lower_bound) | (df[column] > upper_bound)).sum()
            if outliers > 0:
                logger.info(f"Removing {outliers} outliers from {column}")
                df = df[(df[column] >= lower_bound) & (df[column] <= upper_bound)]
        
        logger.info(f"Data cleaning completed. Final shape: {df.shape}")
        return df
    
    def encode_categorical_features(self, df: pd.DataFrame) -> pd.DataFrame:
        """Encode categorical features."""
        categorical_columns = df.select_dtypes(include=['object']).columns
        
        for column in categorical_columns:
            if column not in self.label_encoders:
                self.label_encoders[column] = LabelEncoder()
                df[column] = self.label_encoders[column].fit_transform(df[column])
            else:
                df[column] = self.label_encoders[column].transform(df[column])
        
        return df
    
    def split_data(self, df: pd.DataFrame, target_column: str) -> Tuple[pd.DataFrame, pd.DataFrame, pd.Series, pd.Series]:
        """Split data into training and testing sets."""
        X = df.drop(columns=[target_column])
        y = df[target_column]
        
        test_size = self.config['data']['test_size']
        random_state = self.config['data']['random_state']
        
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=test_size, random_state=random_state, stratify=y if y.dtype == 'object' else None
        )
        
        logger.info(f"Data split - Train: {X_train.shape}, Test: {X_test.shape}")
        return X_train, X_test, y_train, y_test
    
    def scale_features(self, X_train: pd.DataFrame, X_test: pd.DataFrame) -> Tuple[pd.DataFrame, pd.DataFrame]:
        """Scale numerical features."""
        X_train_scaled = pd.DataFrame(
            self.scaler.fit_transform(X_train),
            columns=X_train.columns,
            index=X_train.index
        )
        
        X_test_scaled = pd.DataFrame(
            self.scaler.transform(X_test),
            columns=X_test.columns,
            index=X_test.index
        )
        
        return X_train_scaled, X_test_scaled