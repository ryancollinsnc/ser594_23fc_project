#### SER594: Machine Learning Evaluation
#### Title: Predictive Analysis of Housing Prices Using Machine Learning 
#### Author: Ryan Collins
#### Date: 11/20/23

## Evaluation Metrics
### Metric 1
**Name:** Mean Squared Error (MSE)

**Choice Justification:** MSE measures the average of the squares of the errors or deviations—that is, the difference between the estimator (the predicted value) and what is estimated (the true value). It is appropriate here to measure the accuracy of our regression models in predicting housing prices.

**Interpretation:** A lower MSE value indicates a model that predicts more closely to the actual data points.

### Metric 2
**Name:** R2 Score

**Choice Justification:** The R2 Score, also known as the coefficient of determination, represents the proportion of the variance in the dependent variable that is predictable from the independent variables. It's a measure of how well the regression predictions approximate the real data points.

**Interpretation:** An R2 score closer to 1 indicates a model that explains a large portion of the variance in the response variable.

## Alternative Models
### Alternative 1
**Construction:** RandomForestRegressor - Utilizes an ensemble of decision trees to improve prediction accuracy and control over-fitting.

**Evaluation:** MSE: 17914324793.951878, R2 Score: 0.8507312217319882

### Alternative 2
**Construction:** LinearRegression - Predicts a linear relationship between the independent and dependent variables.

**Evaluation:** MSE: 114636248819.63701, R2 Score: 0.044808386397451994

### Alternative 3
**Construction:** Lasso - A variation of linear regression that uses shrinkage and variable selection automatically.

**Evaluation:** MSE: 114636255248.88757, R2 Score: 0.04480833282655905

### Alternative 4
**Construction:** Ridge - A technique for analyzing multiple regression data when multicollinearity is present.

**Evaluation:** MSE: 114636249962.7959, R2 Score: 0.044808376872229494

### Alternative 5
**Construction:** DecisionTreeRegressor - Predicts the value of a target variable by learning simple decision rules inferred from the data features.

**Evaluation:** MSE: 23408519104.56266, R2 Score: 0.8049515631769075


## Visualization
### Visual 1
**Analysis:** The set of bar graphs comparing the Mean Squared Error (MSE) and R2 Score of various regression models including RandomForestRegressor, LinearRegression, Lasso, Ridge, and DecisionTreeRegressor. The bar graphs visually illustrate the superior performance of the RandomForestRegressor over the other models, with a significantly lower MSE and a higher R2 Score. This visual comparison underscores the reasons for selecting RandomForestRegressor as the best model for this prediction task, as it not only has the lowest error rate but also the highest explanatory power of the variance in the housing price data.

## Best Model

**Model:** RandomForestRegressor

Ensemble Learning vs Single Model: RandomForestRegressor is an ensemble learning method, meaning it combines the predictions from multiple decision trees to give a more accurate and robust result. In contrast, a DecisionTreeRegressor uses a single decision tree. Ensemble methods like Random Forests typically outperform single decision trees because they reduce the risk of overfitting by averaging the results of many trees.
Overfitting: Decision trees are prone to overfitting, especially with complex data. Overfitting happens when a model learns the training data too well, including its noise and fluctuations, making it less effective at predicting new, unseen data. Random Forest, by averaging multiple trees, mitigates this risk, making it more reliable for practical applications.
Performance Metrics: In this specific case, the RandomForestRegressor has a significantly higher R2 Score (0.8507312217319882) compared to the DecisionTreeRegressor (0.8049515631769075). The R2 Score is a measure of how well the variations in the data are explained by the model. A higher R2 Score means the model can better explain the variation in the data and hence can predict more accurately.
Mean Squared Error (MSE): The MSE for RandomForestRegressor is 17914324793.951878, which is lower than the MSE for DecisionTreeRegressor at 23408519104.56266. MSE measures the average squared difference between the estimated values and the actual value. A lower MSE indicates a model with better accuracy and reliability in prediction.
Generalization: RandomForest models tend to generalize better to new data. Because they aggregate the results of many trees, they are less sensitive to variations and anomalies in the data, leading to better performance on unseen data.
Bias-Variance Tradeoff: Random Forests strike a better balance in the bias-variance tradeoff compared to single decision trees. While decision trees have low bias but high variance, Random Forests reduce variance without substantially increasing bias, leading to overall better predictive performance.
