# Stock Price Analysis and Prediction 🚀

## 📈 Project Overview  
The **Tesla Stock Price Analysis and Prediction** project is a comprehensive approach to understanding and forecasting Tesla's stock price movements. By utilizing machine learning models and in-depth data analysis, the project aims to assist traders, analysts, and financial enthusiasts in making informed decisions.  

## 🎯 Objectives  
- **Analyze Tesla's stock data** using exploratory and statistical techniques.  
- **Feature engineering** to extract meaningful insights from historical stock prices.  
- **Predict price movements** with high accuracy using machine learning models.  
- **Provide interpretative insights** through visualizations and evaluation metrics.  

## 📂 Project Structure  

- **`data/`**: Contains the historical stock data in CSV format.  
- **`notebooks/`**: Includes Jupyter notebooks for data preprocessing, exploratory data analysis, and model training.   
- **`requirements.txt`**: Specifies the required Python libraries for the project.  
- **`README.md`**: Documentation providing an overview and usage guide for the project.  

## 🛠️ Approach  

1. **Data Preprocessing**:  
   - Converted `Date` into datetime format and extracted `day`, `month`, and `year`.  
   - Engineered new features like `open-close`, `low-high`, and `is_quarter_end`.  
   - Handled missing values and scaled the dataset using `StandardScaler`.  

2. **Exploratory Data Analysis**:  
   - Visualized closing price trends over time.  
   - Created distribution plots for stock price variables.  
   - Examined correlations between features to identify relationships.  

3. **Modeling**:  
   - Implemented and evaluated three machine learning models:  
     - **Linear Regression**: For predicting continuous values of stock price changes.  
     - **Support Vector Classifier (SVC)**: To classify upward or downward movement.  
     - **XGBoost Classifier**: A powerful gradient-boosting model for enhanced accuracy.  
   - Evaluated models using metrics like accuracy and ROC-AUC score.  

4. **Visualization**:  
   - Plotted learning curves for model accuracy and loss.  
   - Generated confusion matrices to assess class-wise performance.  

## 📊 Results  

- **Classification Metrics**: Each model’s performance is assessed using precision, recall, F1-score, and accuracy.  
- **Visualization Insights**: Line charts, histograms, and box plots provide a clear view of stock trends.  

## 📈 Dataset  

The dataset contains Tesla stock prices with the following attributes:  
- **Date**: Trading date (MM/DD/YYYY format).  
- **Open, High, Low, Close**: Prices at different points during the trading day.  
- **Adj Close**: Adjusted closing price accounting for dividends and splits.  
- **Volume**: Number of shares traded.  

## 🚀 Getting Started  

### Requirements  
Install the required libraries using:  

pip install -r requirements.txt

### Running the Project  
1. Clone the repository:  
2. Place the dataset in the `data/` directory.  
3. Open `notebooks/analysis.ipynb` in Jupyter Notebook to execute the analysis pipeline.  

### Testing the Models  
To test a new set of stock prices, place the CSV file in the `data/` directory and modify the `load_data()` function to include the file path.  

## 📈 Visualization Highlights  

- **Closing Price Trends**: A line plot showing the movement of Tesla's closing prices over time.  
- **Feature Distributions**: Histograms and density plots for engineered features.  
- **Correlation Heatmap**: Visualizing relationships between numerical features.  

## 🤖 Troubleshooting  

- **Deprecation Warnings**: If you encounter `distplot` warnings, update the code to use `histplot` or `displot` as recommended.  
- **File Errors**: Ensure the dataset matches the expected structure.  
- **Model Performance**: If models underperform, experiment with hyperparameter tuning or additional features.  

## 📜 Results  

Detailed model evaluation, classification reports, and learning curves are available in the `notebooks/analysis.ipynb` file.  

Happy Predicting! 🚀  
