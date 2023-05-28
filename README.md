# Cancellation Prediction in the Hotel Industry
This project aims to predict whether hotel bookings will be canceled in order to optimize operational planning and minimize financial losses. We utilize various machine learning algorithms such as decision trees (Random Forest), XGBoost, and K-Nearest Neighbors (KNN).

## Project Description
Our goal is to accurately predict whether a hotel booking will be canceled or not. For this purpose, we use historical booking data and consider important factors such as the booking time, room category, and previous cancellations. Our model should be able to predict the cancellation behavior of customers, allowing hotels to improve their operational planning and avoid empty rooms.

## Algorithms Used
Decision Trees with Random Forest: We combine multiple decision trees to make accurate predictions. The Random Forest algorithm takes into account the predictions of all the trees and provides a consistent result.

XGBoost: This algorithm is based on decision trees and optimizes predictions. XGBoost is particularly efficient and provides precise cancellation predictions.

K-Nearest Neighbors (KNN): KNN is based on the observation that similar bookings often have the same class membership. We use KNN to make predictions based on the majority classes of similar bookings.

Further decisions will be made if additional algorithms are needed for evaluation.

## Usage
Install the required dependencies using `pip install -r requirements.txt`.

Execute the "cancellation_prediction.ipynb" notebook to load the dataset, train the model, and generate predictions.

Analyze the prediction results and adjust the algorithm parameters if necessary to achieve better results.

## Contribution
It provides the opportunity to improve cancellation prediction in the hotel industry, thereby optimizing profitability and guest experience.