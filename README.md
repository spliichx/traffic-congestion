# Traffic Congestion Prediction

A machine learning project focused on predicting traffic congestion patterns at intersections across major US cities using GeoTab traffic data.

## Project Overview

This project aims to improve road safety, optimize traffic operations, and identify opportunities for infrastructure improvements by accurately predicting future traffic congestions. The analysis focuses on intersection-level traffic patterns and stop-time predictions.

## 📊 Dataset

The dataset is sourced from **GeoTab** and contains comprehensive traffic congestion information from intersections in major United States cities.

### Features (Independent Variables)

| Variable | Description |
|----------|-------------|
| `IntersectionId` | Unique identifier for each intersection |
| `Latitude` | Geographic latitude of the intersection |
| `Longitude` | Geographic longitude of the intersection |
| `EntryStreetName` | Street name where vehicles enter the intersection |
| `ExitStreetName` | Street name where vehicles exit the intersection |
| `EntryHeading` | Vehicle direction when entering intersection |
| `ExitHeading` | Vehicle direction when exiting intersection |
| `Hour` | Hour of the day (0-23) |
| `Weekend` | Boolean indicator for weekend days |
| `Month` | Month of the year |
| `Path` | Concatenated path: `EntryStreetName_EntryHeading ExitStreetName_ExitHeading` |
| `City` | Name of the city |

### Target Variables

#### Total Time Stopped Metrics
- `TotalTimeStopped_p20/40/50/60/80`: Total stop time at intersection for 20th, 40th, 50th, 60th, and 80th percentiles of vehicles

#### Time From First Stop Metrics  
- `TimeFromFirstStop_p20/40/50/60/80`: Time taken for vehicles to stop again after crossing intersection (by percentile)

#### Distance to First Stop Metrics
- `DistanceToFirstStop_p20/40/50/60/80`: Distance before intersection where vehicles first stopped (by percentile)

### Primary Prediction Targets

The model focuses on predicting these key metrics:
- **Total Time Stopped**: 20th, 50th, 80th percentiles
- **Distance to First Stop**: 20th, 50th, 80th percentiles

## 🔬 Methodology

The project follows a structured machine learning pipeline:

1. **Exploratory Data Analysis (EDA)**
   - Data distribution analysis
   - Feature correlation studies
   - Traffic pattern visualization

2. **Data Preprocessing**
   - Data cleaning and validation
   - Feature engineering
   - Handling missing values
   - Data normalization/scaling

3. **Algorithm Selection**
   - Model comparison and evaluation
   - Hyperparameter tuning
   - Cross-validation

4. **Model Evaluation**
   - Performance metrics assessment
   - Validation on test datasets
   - Result interpretation

## Getting Started

### Prerequisites
```bash
Python 3.7+
Jupyter Notebook
Required libraries (see requirements.txt)
```

### Installation
```bash
git clone https://github.com/yourusername/traffic-congestion-prediction
cd traffic-congestion-prediction
pip install -r requirements.txt
```

### Usage
```bash
jupyter notebook
# Open and run the main analysis notebook
```

## 📈 Expected Outcomes

- Accurate prediction of traffic congestion patterns
- Identification of high-risk intersections
- Insights for traffic optimization strategies
- Data-driven recommendations for infrastructure improvements

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- GeoTab for providing the traffic congestion dataset
- Contributors and maintainers of the project

---

*For questions or suggestions, please open an issue or contact the maintainers.*
