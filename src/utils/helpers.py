import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
import logging

logger = logging.getLogger(__name__)

def create_visualization_report(df: pd.DataFrame, target_column: str, output_path: str):
    """Create comprehensive visualization report."""
    
    output_path = Path(output_path)
    output_path.mkdir(parents=True, exist_ok=True)
    
    # Set style
    plt.style.use('seaborn-v0_8')
    sns.set_palette("husl")
    
    # 1. Distribution of target variable
    plt.figure(figsize=(12, 8))
    
    plt.subplot(2, 2, 1)
    df[target_column].hist(bins=50, alpha=0.7)
    plt.title(f'Distribution of {target_column}')
    plt.xlabel(target_column)
    plt.ylabel('Frequency')
    
    # 2. Time series plot (if datetime column exists)
    if 'datetime' in df.columns:
        plt.subplot(2, 2, 2)
        df.set_index('datetime')[target_column].plot()
        plt.title(f'{target_column} Over Time')
        plt.xlabel('Date')
        plt.ylabel(target_column)
    
    # 3. Correlation heatmap
    plt.subplot(2, 2, 3)
    numeric_cols = df.select_dtypes(include=['number']).columns
    correlation_matrix = df[numeric_cols].corr()
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0, square=True)
    plt.title('Feature Correlation Matrix')
    
    # 4. Feature importance (if available)
    plt.subplot(2, 2, 4)
    if 'hour' in df.columns:
        hourly_avg = df.groupby('hour')[target_column].mean()
        hourly_avg.plot(kind='bar')
        plt.title(f'Average {target_column} by Hour')
        plt.xlabel('Hour of Day')
        plt.ylabel(f'Average {target_column}')
        plt.xticks(rotation=45)
    
    plt.tight_layout()
    plt.savefig(output_path / 'traffic_analysis_report.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    logger.info(f"Visualization report saved to {output_path}")

def calculate_traffic_statistics(df: pd.DataFrame) -> dict:
    """Calculate comprehensive traffic statistics."""
    
    stats = {
        'total_records': len(df),
        'date_range': {
            'start': df['datetime'].min() if 'datetime' in df.columns else None,
            'end': df['datetime'].max() if 'datetime' in df.columns else None
        },
        'missing_values': df.isnull().sum().to_dict(),
        'data_types': df.dtypes.to_dict()
    }
    
    # Numeric column statistics
    numeric_cols = df.select_dtypes(include=['number']).columns
    for col in numeric_cols:
        stats[f'{col}_stats'] = {
            'mean': float(df[col].mean()),
            'median': float(df[col].median()),
            'std': float(df[col].std()),
            'min': float(df[col].min()),
            'max': float(df[col].max()),
            'q25': float(df[col].quantile(0.25)),
            'q75': float(df[col].quantile(0.75))
        }
    
    return stats