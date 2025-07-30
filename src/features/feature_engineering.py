import pandas as pd
import numpy as np
from datetime import datetime
import logging

logger = logging.getLogger(__name__)

class FeatureEngineer:
    """Create features for traffic analysis."""
    
    def __init__(self, config: dict):
        self.config = config
        
    def create_time_features(self, df: pd.DataFrame, datetime_column: str) -> pd.DataFrame:
        """Create time-based features."""
        logger.info("Creating time-based features...")
        
        # Convert to datetime if not already
        df[datetime_column] = pd.to_datetime(df[datetime_column])
        
        # Extract time features
        time_features = self.config['features']['time_features']
        
        if 'hour' in time_features:
            df['hour'] = df[datetime_column].dt.hour
        if 'day_of_week' in time_features:
            df['day_of_week'] = df[datetime_column].dt.dayofweek
        if 'month' in time_features:
            df['month'] = df[datetime_column].dt.month
        if 'is_weekend' in time_features:
            df['is_weekend'] = (df[datetime_column].dt.dayofweek >= 5).astype(int)
        
        # Create rush hour indicators
        df['is_morning_rush'] = ((df['hour'] >= 7) & (df['hour'] <= 9)).astype(int)
        df['is_evening_rush'] = ((df['hour'] >= 17) & (df['hour'] <= 19)).astype(int)
        
        logger.info(f"Created time features. New shape: {df.shape}")
        return df
    
    def create_lag_features(self, df: pd.DataFrame, target_column: str) -> pd.DataFrame:
        """Create lag features for time series analysis."""
        logger.info("Creating lag features...")
        
        lag_periods = self.config['features']['lag_features']
        
        # Sort by datetime for proper lag calculation
        df = df.sort_values('datetime')
        
        for lag in lag_periods:
            df[f'{target_column}_lag_{lag}'] = df[target_column].shift(lag)
        
        # Create rolling window features
        for window in [3, 6, 12]:
            df[f'{target_column}_rolling_mean_{window}'] = df[target_column].rolling(window=window).mean()
            df[f'{target_column}_rolling_std_{window}'] = df[target_column].rolling(window=window).std()
        
        # Drop rows with NaN values created by lag/rolling features
        df = df.dropna()
        
        logger.info(f"Created lag features. New shape: {df.shape}")
        return df
    
    def create_traffic_specific_features(self, df: pd.DataFrame) -> pd.DataFrame:
        """Create traffic-specific engineered features."""
        logger.info("Creating traffic-specific features...")
        
        # Traffic density categories
        if 'vehicle_count' in df.columns and 'road_capacity' in df.columns:
            df['traffic_density'] = df['vehicle_count'] / df['road_capacity']
            df['congestion_level'] = pd.cut(
                df['traffic_density'], 
                bins=[0, 0.3, 0.6, 0.8, 1.0, float('inf')],
                labels=['Low', 'Moderate', 'High', 'Severe', 'Gridlock']
            )
        
        # Speed-related features
        if 'average_speed' in df.columns:
            df['speed_category'] = pd.cut(
                df['average_speed'],
                bins=[0, 20, 40, 60, float('inf')],
                labels=['Congested', 'Slow', 'Normal', 'Fast']
            )
        
        # Weather impact on traffic
        if 'weather_condition' in df.columns:
            weather_impact = {
                'Clear': 1.0, 'Cloudy': 1.1, 'Rain': 1.3, 
                'Heavy Rain': 1.5, 'Snow': 1.7, 'Fog': 1.4
            }
            df['weather_impact_factor'] = df['weather_condition'].map(weather_impact).fillna(1.0)
        
        logger.info(f"Created traffic-specific features. New shape: {df.shape}")
        return df