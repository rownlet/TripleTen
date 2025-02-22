# Data Science Bootcamp Projects

Welcome to the documentation of the projects developed during the Data Science Bootcamp at TripleTen. Throughout the Bootcamp, data analysis, cleansing, transformation and modeling techniques were applied using tools of Data Science and Software Development.

Each project has a detailed description of the context, tools used, development process, results analysis and conclusions.

For those who wish to run the code and validate the results obtained, the repository with the data is available at the following link: 

📂 **Repository in Google Drive:** [Portfolio](https://drive.google.com/drive/folders/1VWdZzKb58ncf8SD0QUKrhCRngkU0ApIK?usp=drive_link)  

---

## Tabla de Contenido

- [Project 1: Data Evaluation and Preparation for Store 1](#project-1-data-evaluation-and-preparation-for-store-1)
- [Project 2: Music Preferences Analysis - "Let Me Hear the Music"](#project-2-music-preferences-analysis---let-me-hear-the-music)
- [Project 3: Order Analysis in Instacart - "Fill That Cart!"](#project-3-order-analysis-in-instacart---fill-that-cart!)
- [Project 4: Telecommunications Rate Analysis - "Which is the Best Rate?"](#project-4-telecommunications-rate-analysis---which-is-the-best-rate?)
- [Project 5: Visual Analysis of Vehicle Data](#project-5-visual-analysis-of-vehicle-data)
- [Project 6: Video Game Sales Analysis for Ice](#project-6-video-game-sales-analysis-for-ice)
- [Project 7: Travel Analysis in Chicago](#project-7-travel-analysis-in-chicago)
- [Project 8: Classification Model for New Megaline Plans](#project-8-classification-model-for-new-megaline-plans)
- [Project 9: Churn Prediction in Beta Bank](#project-9-churn-prediction-in-beta-bank)
- [Project 10: Well Expansion for OilyGiant](#project-10-well-expansion-for-oilygiant)
- [Project 11: Machine Learning Models for Insurance in Sure Tomorrow](#project-11-machine-learning-models-for-insurance-in-sure-tomorrow)
- [Project 12: Used Car Value Prediction](#project-12-used-car-value-prediction)
- [Project 13: Taxi Order Prediction for Sweet Lift](#project-13-taxi-order-prediction-for-sweet-lift)
- [Project 14: Sentiment Analysis of Movie Reviews](#project-14-sentiment-analysis-of-movie-reviews)
- [Project 15: Age Prediction with Convolutional Neural Networks](#project-15-age-prediction-with-convolutional-neural-networks)
- [Final Project: Churn Rate Telecom](#final-project-churn-rate-telecom)

---

## Project 1: Data Evaluation and Preparation for Store 1

### Context
An e-commerce company, **Store 1**, recently started collecting data on its customers. Its ultimate goal is to better understand user behavior and make data-driven decisions to enhance their online experience. As part of the analytics team, the first task is to assess the quality of a sample dataset and prepare it for future analysis.

### Tools and Technologies Used

- `Pandas` for data manipulation and transformation.
- `NumPy` for numerical calculations.
- `Matplotlib / Seaborn` for data visualization (if applicable).
- `Regex` for format corrections in text variables.

### Data Development and Analysis

During the data quality assessment, the following inconsistencies were identified:

1. The **`user_name`** variable contained unnecessary spaces and an underscore between the first and last name, which could cause issues in data standardization.
2. The **`user_age`** variable was stored as a decimal number instead of an integer, which could complicate mathematical operations on age.
3. The **`fav_categories`** list contained uppercase strings, which could affect consistency in the analysis. It was suggested to convert them to lowercase to improve uniformity.

### Conclusions

The data cleaning and normalization process improved the quality of the information for future analyses. Correcting formats in customer names, ages, and preferences ensures better integration of the data into future analytical models.

---

## Project 2: Music Preferences Analysis - "Let Me Hear the Music"

### Context
As a data analyst, the goal of this project is to analyze online music streaming data to identify consumption patterns in two cities: **Springfield** and **Shelbyville**. Through data analysis, the objective is to validate hypotheses about user behavior regarding music playback on different days of the week.

### Tools and Technologies Used

- **`Pandas`** for data manipulation and cleaning.
- **`NumPy`** for numerical calculations.
- **`Matplotlib / Seaborn`** for visualizing patterns and trends in the data.
- **`Statistical methods`** for hypothesis validation.

### Data Development and Analysis
The project was carried out in three main stages:

1. **Data Description**  
   The structure of the dataset (`music_project_en.csv`) was reviewed, and the available variables were analyzed to compare listening patterns.

2. **Data Preprocessing**
   
   Issues in the dataset were corrected, such as:
   - Errors in column headers.
   - Handling of missing values.
   - Removal of duplicates.
   - Conversion of data types to ensure consistency in analysis.

3. **Hypothesis Testing**
   
   The number of songs played on **`Monday`, `Wednesday`, and `Friday`** was compared to determine whether user behavior varied between cities and days of the week.
    
   **Hypothesis Test Conclusion:**
   
   - In **`Springfield`**, Fridays have the highest music playback volume.  
   - In **`Shelbyvill`e**, Wednesdays show the highest playback activity.  
   - Overall, Springfield has a higher volume of music playback compared to Shelbyville.  

### Conclusions
The results confirmed significant differences in music consumption between the two cities. It was observed that playback frequency varies depending on the day of the week and geographic location. This suggests that streaming platforms can optimize their recommendation strategies and promotions based on user behavior in each city.

---

## Project 3: Order Analysis in Instacart - "Fill That Cart!"

### Context

Instacart is a grocery delivery platform that allows customers to place an order and receive it at their doorstep. The objective of this project is to analyze order data to identify purchasing patterns and optimize the user experience on the platform.

The dataset used has been modified to reduce its size and speed up calculations. Additionally, missing values and duplicates were introduced to enhance the data cleaning and preparation experience.

### Tools and Technologies Used

- **`Pandas`** for data manipulation and cleaning.
- **`NumPy`** for numerical calculations.
- **`Matplotlib / Seaborn`** for visualizing patterns and trends in the data.
- **`Statistical methods`** for exploratory data analysis and process optimization.

### Data Development and Analysis

The project was carried out in several key stages:

1. **Data Preprocessing**
   
   - Verification and correction of data types in key columns.
   - Identification and handling of missing values in orders and products.
   - Removal of duplicate values to ensure data integrity.
   - Conversion of categorical and numerical data into appropriate formats.

2. **Purchase Pattern Analysis**
 
   - Evaluation of peak shopping hours and days.
   - Identification of the most popular products and their purchase frequency.
   - Analysis of repeated purchases and customer shopping habits.

3. **Data Validation**
 
   - Review of data quality and detection of possible entry errors.
   - Application of imputations and corrections to affected variables.

### Conclusions

The results confirmed important behavioral patterns in Instacart orders:

- **`Shopping hours`:** Order activity is concentrated at certain hours of the day and specific days of the week.
- **`Popular products`:** Some products have a high repurchase rate, suggesting regular consumption patterns.
- **`Recommendation strategy`:** The analysis of repeated purchases allows for improved recommendations and a more personalized user experience.

These findings can be used by Instacart to optimize product distribution and enhance personalized offers for its customers.

---

## Project 4: Telecommunications Rate Analysis - "Which is the Best Rate?"

### Context

You work as a data analyst for the telecommunications company **`Megaline`**, which offers two prepaid plans: **`Surf`** and **`Ultimate`**. The goal of this project is to determine which of these plans generates more revenue to help the commercial team optimize the advertising budget.

For the analysis, data from 500 customers is available, including information on their call usage, text messages, and Internet consumption throughout 2018.

### Tools and Technologies Used

- **`Pandas`** for data manipulation and cleaning.
- **`NumPy`** for numerical calculations.
- **`Matplotlib / Seaborn`** for visualizing trends in the data.
- **`Statistical tests`** (Student's t-test) to validate income differences between plans.

### Data Development and Analysis

The project was carried out in several key stages:

1. **Data Cleaning and Preprocessing**
   
   - Conversion of dates to `datetime` format to facilitate temporal analysis.
   - Handling of missing values and standardization of data types.
   - Rounding of call durations to align with the company's billing policy.
   - Consolidation of consumption data (calls, messages, and Internet) into a single dataset per user.

2. **Customer Behavior Analysis**
   
   - Exploration of call, message, and data usage by plan type.
   - Identification of consumption patterns and differences between **`Surf`** and **`Ultimate`** plan users.

3. **Revenue Analysis**
   
   - Calculation of monthly revenue per user.
   - Comparison of revenues between plans and geographic regions.
   - Evaluation of the profitability of each plan.

4. **Statistical Tests**
   
   - Application of statistical tests (`Student's t-test`) to determine whether revenue differences between the two plans are statistically significant.
   - Validation of hypotheses regarding usage patterns and plan profitability.

### Conclusions

The results confirmed significant differences in service consumption among **`Surf`** and **`Ultimate`** plan users:

- **`The Ultimate plan generates higher average revenue than the Surf plan`** due to greater data and call usage by its users.
- **`Text message usage has declined`**, suggesting that customers prefer to communicate via mobile data.
- **`Revenue varies by region`**, which can help define more targeted marketing strategies.

These findings can help **`Megaline`** make strategic decisions regarding its pricing structure and advertising campaigns.

---

## Project 5: Visual Analysis of Vehicle Data

### Description

This project is a web application developed with Streamlit that allows users to visualize and analyze data on used vehicles for sale. The application provides an interactive interface to explore different aspects of the data, such as mileage (`odometer`), price (`price`), and other details listed in vehicle advertisements.

### Features

The application includes several features that facilitate data exploration and analysis:

- **`Mileage Histogram`**: Allows users to visualize the distribution of vehicle mileage through a histogram.
- **`Scatter Plot`**: Examines the relationship between different variables such as mileage and price.
- **`Bar and Pie Charts`**: Provides visualizations of the distribution of categorical characteristics such as vehicle condition, fuel type, and more.
- **`Interactivity`**: Users can interact with the application by selecting different options to display graphs.

### Car Brand Visualization

The application displays images of car brands to enhance the interface and better connect with the context of the analysis.

### Usage Instructions

To run this application, follow these steps:

1. Ensure you have Python and Streamlit installed.
2. Clone or download this repository to your local machine.
3. Open a terminal and navigate to the project directory.
4. Run the command `streamlit run app.py`.
5. The application will automatically open in your web browser at `localhost:8501`.

### Requirements

- Python 3
- Streamlit
- Pandas
- Plotly Express

### Run Locally

The application can be run locally for development and testing, allowing adjustments and improvements before a final deployment.

### Application URL

Visit the live application here: [Visual Analysis of Vehicle Data](https://proyecto-5-dr38.onrender.com/)

---

## Project 6: Video Game Sales Analysis for Ice

### Context

You work for the online store **`Ice`**, which sells video games worldwide. Open data is available on user and critic reviews, genres, platforms (e.g., Xbox or PlayStation), and historical game sales. The goal of this project is to **`identify patterns that determine whether a video game will be successful or not`**, allowing the detection of promising titles and the planning of marketing campaigns for 2017.

The dataset includes data from 1980 to 2016, with variables such as **`ESRB rating`**, **`regional sales`**, and **`distribution platforms`**.

### Tools and Technologies Used

- **`Pandas`** for data manipulation and cleaning.
- **`NumPy`** for numerical calculations.
- **`Matplotlib / Seaborn`** for visualizing trends and correlations.
- **`Statistical tests`** to validate hypotheses on the impact of reviews and sales.
- **`Predictive models`** to estimate future sales.

### Data Development and Analysis

The project was carried out in several key stages:

1. **Data Cleaning and Preprocessing**
   
   - Conversion of data types and handling of missing values.
   - Removal of rows with null values in **`genre`** and **`release year`**.
   - Conversion of the **`user_score`** column, replacing "TBD" values with NaN and converting it to **`float`**.
   - Imputation of missing values in **`critic_score`** and **`user_score`** using the mean by genre and platform.

2. **Exploratory Data Analysis**

   - Evaluation of trends in video game releases over the years.
   - Identification of the most profitable platforms and genres in terms of global sales.
   - Analysis of the relationship between user/critic ratings and sales success.

3. **Statistical Tests and Correlations**
   
   - Hypothesis tests were conducted to compare average ratings between platforms and genres.
   - The correlation between reviews and sales was measured to determine the impact of public and critic perception.

4. **Sales Prediction**
   
   - Use of predictive models to estimate the success of new releases in 2017.
   - Evaluation of the influence of key factors such as platform, genre, and ESRB rating.

### Conclusions

The results confirmed several important findings in the video game industry:

- **Next-generation platforms generate higher sales**, with **PS4 and Xbox One** leading the market.
- **Action and Shooter genres dominate in terms of revenue**, followed by RPGs and Sports.
- **Critic reviews have a greater impact on sales than user reviews**, suggesting that obtaining high ratings from experts is key to commercial success.
- **Sales vary significantly by region**, with North America being the most profitable market for Action and Shooter games, while Japan prefers RPGs.

These findings can help **Ice** make better decisions in marketing planning and game selection for future campaigns.

---

## Project 7: Travel Analysis in Chicago

### Context

This project analyzes travel data in **`Chicago`** to identify taxi usage patterns, determine which companies have the highest demand, and evaluate which neighborhoods are the most popular for trip endings. Additionally, it examines how weather conditions affect trip duration.

Two datasets extracted from SQL were used:

- **`project_sql_result_01.csv`**: Contains information on the number of trips per taxi company on November 15 and 16, 2017.
- **`project_sql_result_04.csv`**: Records the average number of trips completed in different Chicago neighborhoods in November 2017.

### Tools and Technologies Used

- **`Pandas`** for data manipulation and cleaning.
- **`NumPy`** for numerical calculations.
- **`Matplotlib / Seaborn`** for visualizing patterns and trends.
- **`SQL`** for extracting data from the travel database.
- **`Statistical tests (Student's t-test)`** to validate hypotheses about the impact of weather on trip duration.

### Data Development and Analysis

The project was carried out in several key stages:

1. **Data Cleaning and Preprocessing**
   
   - Verification of missing values and duplicates.
   - Evaluation of data distribution to identify biases and trends.

2. **Identification of Taxi Companies with the Highest Demand**
   
   - A filter was applied to select only companies with more than **`2,000 trips`** on the analyzed days.
   - The distribution of trips among different companies was analyzed to assess their market share.

3. **Analysis of Neighborhoods with the Highest Demand**
   
   - The **`10 main neighborhoods`** where the highest number of trips ended were identified.
   - Taxi demand was compared across different neighborhoods to better understand usage patterns.

4. **Hypothesis Testing on Weather Impact**
   
   - **`Student's t-test`** was used to determine whether the duration of trips from downtown Chicago to O'Hare Airport changes on **`rainy Saturdays`**.
   - The effect of traffic and weather conditions on trip durations was evaluated.

### Conclusions

The results confirmed several key findings:

- **Leading taxi companies in the market:**
  
  - **`Flash Cab`** has the highest number of trips in Chicago.
  - **`Taxi Affiliation Services`** and **`Medallion Leasing`** also have significant market shares.
  - There is an uneven distribution, suggesting that smaller companies have growth opportunities.

- **Neighborhoods with the highest number of completed trips:**
  
  - **`Loop, River North, and Streeterville`** are the neighborhoods with the highest average trip completions.
  - These neighborhoods are **`key commercial and tourist hubs`**, explaining the high taxi demand.

- **Impact of weather on trips:**
  
  - The average trip duration **`significantly increases on rainy Saturdays`**.
  - Adverse weather conditions increase travel times due to traffic and driving difficulties.

### Optimization Recommendations

- **`Improve infrastructure`**: Implement intelligent traffic management systems and dedicated taxi lanes.
- **`Use technology`**: Equip taxis with advanced navigation systems and optimize mobile taxi booking applications.
- **`Training and coordination`**: Train drivers for handling adverse weather conditions and improve coordination of pickup times.

These findings can help Chicago’s transportation industry enhance taxi efficiency and customer satisfaction.

---

## Project 8: Classification Model for New Megaline Plans

### Context

The mobile company **`Megaline`** aims to optimize the recommendation of its new **`Smart`** and **`Ultra`** plans. Currently, many customers still use legacy plans, so the goal of this project is to develop a **`classification model`** that analyzes customer behavior and recommends the best plan for each user.

Data from customers who have already switched to the new plans was used, enabling the development of a model with an accuracy threshold of at least **`0.75`**.

### Tools and Technologies Used

The following tools were used for data analysis and model development:

- **`Pandas`** for data manipulation and cleaning.
- **`NumPy`** for numerical calculations.
- **`Scikit-learn`** for training and evaluating Machine Learning models.
- **`Matplotlib / Seaborn`** for visualizing patterns and distributions.
- **`GridSearchCV`** for hyperparameter optimization.

### Data Development and Analysis

The project was carried out in several key stages:

1. **Data Preparation**
   
   - Conversion of **`calls`** and **`messages`** data types from `float64` to `int32` to ensure correct interpretation.
   - Splitting the data into **`training (60%)`**, **`validation (20%)`**, and **`test (20%)`** sets.

2. **Training Classification Models**
   
   - **Decision Tree**: The `max_depth` parameter was optimized, achieving the best performance with `max_depth=10` (accuracy: **0.7932**).
   - **Random Forest**: The `n_estimators` and `max_depth` parameters were tuned, reaching **0.8072** accuracy in validation.
   - **Logistic Regression**: Various values of `C` and `solver` were tested, obtaining an accuracy of **0.7201**.

3. **Model Evaluation**
   
   - Models were evaluated on the test set.
   - `Random Forest` achieved the `highest accuracy (82%)`, exceeding the set accuracy threshold.

4. **Sanity Check**
   
   - A **`Dummy Classifier`** was used to predict the most frequent class, serving as a baseline reference to validate the effectiveness of the **`Random Forest`** model.

### Conclusions

The results confirmed that the **`Random Forest`** model is the most efficient for predicting the best plan for Megaline customers:

- **`Random Forest achieved 82% accuracy`**, surpassing the **`0.75`** threshold.
- Hyperparameter optimization significantly improved model performance.
- The model’s validity was confirmed through a sanity check using a Dummy Classifier.

This model will allow **`Megaline`** to optimize plan allocation and enhance the customer experience through personalized recommendations.

---

## Project 9: Churn Prediction in Beta Bank

### Context

Beta Bank faces a significant challenge: each month, an increasing number of its customers are leaving the bank. Management has identified that it is more cost-effective and efficient to focus on retaining existing customers rather than attracting new ones to replace those who leave.

The goal of this project is to develop a **`Machine Learning model`** to predict which customers are most likely to leave the bank. This will allow the company to take proactive measures to retain them and reduce the churn rate.

### Tools and Technologies Used

The following tools were used for data analysis and model development:

- **`Pandas`** for data manipulation and cleaning.
- **`NumPy`** for numerical calculations.
- **`Scikit-learn`** for training and evaluating Machine Learning models.
- **`Matplotlib / Seaborn`** for data visualization and metrics analysis.
- **`Class balancing techniques`**, such as undersampling and oversampling.

### Data Development and Analysis

The project was carried out in several key stages:

1. **Data Loading and Preprocessing**
   
   - Removal of irrelevant columns (`RowNumber`, `CustomerId`, `Surname`).
   - Normalization of numerical features such as `CreditScore`, `Age`, `Balance`, and `EstimatedSalary`.
   - Splitting the data into training and test sets.

2. **Handling Class Imbalance**
   
   - Application of **`undersampling`** and **`oversampling`** techniques to balance the classes.
   - Comparison of models trained with and without data balancing.

3. **Model Training**
   
   - **`Logistic Regression`**: Tested as a baseline model but achieved an **`F1 Score`** of **`0.2916`**, indicating poor performance.
   - **`Random Forest`**: Evaluated with both original and balanced data, achieving an **`F1 Score`** of **`0.62`** and an **`AUC-ROC Score`** of **`0.78`** with oversampling.

4. **Model Evaluation**
   
   - Comparison of `F1 Score` and `AUC-ROC` metrics for each model.
   - **`Random Forest with oversampling`** was the best-performing model, surpassing the **`0.59`** threshold in `F1 Score`.

### Conclusions

The results confirmed that the **`Random Forest with oversampling`** model is the best option for predicting customer retention:

- **`F1 Score of 0.62`**, exceeding the required threshold.
- **`AUC-ROC of 0.78`**, indicating a high ability to distinguish between customers who churn and those who stay.
- Normalization of features and the use of class balancing techniques significantly improved the model’s accuracy.

### Recommendations for Beta Bank

1. **`Implement the Random Forest model with oversampling`** to predict which customers are at risk of churn.
2. **`Continuously monitor the model`** and make adjustments as the bank’s data evolves.
3. **`Design personalized retention strategies`** based on the model’s predictions, offering incentives and service improvements for high-risk customers.

This model will provide **`Beta Bank`** with a powerful tool to reduce churn rates and improve customer retention.

---

## Project 10: Well Expansion for OilyGiant

### Context

The company **`OilyGiant`** aims to expand its operations by opening **`200 new oil wells`**. Given the high development costs and the volatility of the oil market, it is crucial to select optimal locations using geological and economic data analysis.

The project's goal is to **`identify the best regions`** for well drilling, maximizing profits and reducing risks through **`Machine Learning models`**.

### Project Objectives

- **Predict the Volume of Reserves**: Develop a **`linear regression`** model to estimate the oil volume in new wells.
- **Select the Best Wells**: Identify the **`200 wells`** with the highest estimated volume in each region.
- **Evaluate Total Profit**: Calculate the expected profit per region and select the most profitable one.
- **Risk Analysis**: Use **`bootstrapping techniques`** to ensure that the selected regions have a **`loss risk of less than 2.5%`**.

### Tools and Technologies Used

- **`Pandas`** and **`NumPy`** for data manipulation.
- **`Scikit-learn`** for implementing regression models.
- **`Matplotlib / Seaborn`** for pattern visualization.
- **`Bootstrapping`** for investment risk assessment.

### Methodology

The analysis was conducted in several phases:

1. **Data Preparation**
   
   - Loading geological data from three regions (`geo_data_0.csv`, `geo_data_1.csv`, `geo_data_2.csv`).
   - Data exploration and cleaning, removing outliers and unnecessary columns.

2. **Model Training**
 
   - Implementing **`Linear Regressio`n** to predict the volume of reserves.
   - Evaluating model performance in each region using metrics like **`RMSE`**.

3. **Well Selection and Profit Calculation**
 
   - Selecting the **`200 best wells`** per region based on estimated volume.
   - Calculating **`expected profit`**, considering that each unit of oil generates **`$4,500 USD`** in revenue.

4. **Risk Analysis**
 
   - Applying **`bootstrapping`** to estimate confidence intervals and measure profit variability.
   - Determining the region with the **`highest profitability and lowest risk of losses`**.

### Analysis Results

The final calculations showed the following expected profits per region:

- **Region 0**:
  
  - **Average Profit**: $4,035,720
  - **95% Confidence Interval**: [-1,376,900, 9,028,483]
  - **Loss Risk**: **5.9%**

- **Region 1**:
  
  - **Average Profit**: $4,302,083
  - **95% Confidence Interval**: [430,525, 8,473,135]
  - **Loss Risk**: **1.6%** ✅ (Best Option)

- **Region 2**:
  
  - **Average Profit**: $3,842,261
  - **95% Confidence Interval**: [-1,275,898, 9,101,344]
  - **Loss Risk**: **8.0%**

Since **`Region 1`** has the lowest **`loss risk (1.6%)`** and the highest **`average profit`**, it is recommended as the best option for drilling the **`200 new wells`**.

### Conclusions

- The implementation of **`linear regression models`** allowed accurate prediction of reserve volumes.
- **`Risk analysis using bootstrapping`** provided decision-making security.
- **`Region 1`** is the best investment option, combining **`maximum profitability and minimal risk`**.

This analysis will enable **`OilyGiant`** to optimize its investments and maximize returns in its expansion.

---

## Project 11: Machine Learning Models for Sure Tomorrow Insurance

### Context

The insurance company **`Sure Tomorrow`** aims to apply **`Machine Learning models`** to solve four key tasks:

1. **`Finding similar clients`**: This will help company agents with marketing strategies and customer segmentation.
2. **`Predicting the probability of a new client receiving an insurance benefit`**: A predictive model will be evaluated to determine if it outperforms a dummy model.
3. **`Predicting the number of insurance claims for a client`**: A regression model will be used to estimate how often a client may use their insurance.
4. **`Protecting clients’ personal data**: A **data masking mechanism`** will be implemented without affecting the performance of predictive models.

### Tools and Technologies Used

The following tools were used for data analysis and model development:

- **`Pandas`** and **`NumPy`** for data manipulation.
- **`Scikit-learn`** for implementing classification and regression models.
- **`Matplotlib / Seaborn`** for data visualization.
- **`Data obfuscation techniques`** to protect customer privacy.

### Data Development and Analysis

The project was carried out in several phases:

1. **Data Exploration and Preprocessing**
   
   - Data was verified and cleaned, removing null values and categorizing variables.
   - Normalization and standardization techniques were applied to improve model quality.

2. **Training Predictive Models**

   - **Classification Model**: The performance of `Logistic Regression`, `Random Forest`, and `Gradient Boosting` was compared to predict the probability of receiving an insurance claim.
   - **Regression Model**: `Linear Regression` and `Random Forest Regressor` were used to estimate the number of claims a client might file.

3. **Model Evaluation**
   
   - Metrics such as `AUC-ROC`, `precision`, `recall`, and `RMSE` were compared.
   - The `Random Forest` model achieved the best results in both tasks.

4. **Data Protection**
   
   - A **data masking algorithm** was implemented to protect clients' personal information.
   - It was validated that masking did not significantly affect the performance of the Machine Learning models.

### Conclusions

- The **`Random Forest`** model significantly outperformed dummy models in predicting insurance claims.
- Clients’ personal data was successfully protected through *`*data masking techniques`** without compromising model accuracy.
- **`Sure Tomorrow`** can apply these models to enhance marketing strategies and optimize risk management.

This project demonstrates how **`Machine Learning`** can add value to the insurance industry, improving both risk prediction and the protection of sensitive customer information.

---

## Project 12: Used Car Value Prediction

### Context

The used car sales service **`Rusty Bargain`** is developing an application to help customers quickly determine the **`market value`** of their used cars. The application will allow users to access information on technical specifications, equipment versions, and historical prices.

The goal of this project is to develop a **Machine Learning model** that can predict a vehicle's price based on its characteristics.

### Model Requirements

To ensure the model's feasibility, three key requirements must be met:

- **`High accuracy in predicting vehicle value`**.
- **`Fast prediction speed`**, allowing real-time queries in the application.
- **`Optimized training time`**, making future model updates easier.

### Data Used

The dataset contains information about used cars, including:

- **`DateCrawled`**: The date the vehicle profile was downloaded.
- **`VehicleType`**: Type of body style.
- **`RegistrationYear`**: Year of registration.
- **`Gearbox`**: Type of transmission.
- **`Power`**: Horsepower in CV.
- **`Model`**: Vehicle model.
- **`Mileage`**: Mileage in km.
- **`FuelType`**: Type of fuel.
- **`Brand`**: Car brand.
- **`NotRepairedDamage`**: Indicates whether the car has unrepaired damage.
- **`Price`**: Car price (target variable).

### Project Development

1. **Data Cleaning and Preprocessing**
   
   - Removal of outliers and inconsistent data.
   - Conversion of categorical variables into numeric format.
   - Handling of missing values in `NotRepairedDamage`, `FuelType`, and `VehicleType`.
   
2. **Model Training**
   
   - `Linear Regression` as a baseline model.
   - `Decision Trees` and `Random Forest` to improve accuracy.
   - `Gradient Boosting` for further prediction optimization.
   
3. **Evaluation and Comparison**
   
   - `RMSE (Root Mean Squared Error)` metrics were compared for each model.
   - `Training time` and `prediction speed` were measured.

### Results and Conclusions

- **`Random Forest` achieved the best accuracy**, with a low RMSE and an acceptable prediction time.
- **`Gradient Boosting` further improved accuracy**, but its training time was significantly longer.
- **The final model balances `accuracy` and `efficiency`** for implementation in Rusty Bargain's application.

This model will allow **`Rusty Bargain`** to provide accurate estimates of used car prices, improving customer experience and increasing trust in the platform.

---

## Project 13: Taxi Order Prediction for Sweet Lift

### Context

The **`Sweet Lift Taxi`** company has collected historical data on taxi orders at airports. The goal is to predict the number of taxi orders for the next hour to **`attract more drivers during peak hours`** and improve service availability.

To achieve this, a **`Machine Learning model`** will be developed to minimize prediction error and ensure efficient taxi fleet planning.

### Data Used

The dataset is located at `/datasets/taxi.csv` and contains the following information:

- **`timestamp`**: Date and time of the order.
- **`num_orders`**: Number of orders recorded at that moment.

### Project Development

1. **Exploratory Data Analysis and Preprocessing**
   
   - Conversion of the `timestamp` column into a date-time index.
   - Resampling of the data in one-hour intervals to analyze temporal patterns.

2. **Exploratory Data Analysis (EDA)**
   
   - Identification of trends and seasonality in taxi orders.
   - Evaluation of correlations and selection of relevant features.

3. **Training Predictive Models**
   
   - Comparison between `Linear Regression`, `Gradient Boosting` and `Random Forest`.
   - Hyperparameter optimization using `GridSearchCV`.
   
4. **Model Evaluation**
   
   - The main metric is `RMSE`.
   - The final model must achieve an `RMSE below 48` on the test set.

### Results and Conclusions

- `Gradient Boosting` achieved the `best accuracy`, with an `RMSE` of **`43.6`**, surpassing the quality threshold.
- High-demand patterns were identified in the `early morning and afternoon`.
- The model will enable **`Sweet Lift Taxi`** to optimize its service, ensuring taxi availability when it is most needed.

This model will help the company efficiently manage its fleet, reducing passenger wait times and increasing service profitability.

---

## Project 14: Sentiment Analysis of Movie Reviews

### Context

**Film Junky Union**, a cutting-edge community for classic movie enthusiasts, is developing a system to filter and categorize movie reviews. The goal is to train a **Machine Learning model** that can automatically detect negative reviews.

To achieve this, a dataset of **IMDB movie reviews** will be used, where the model must reach an **F1-score of at least 0.85**.

### Data Used

The dataset contains the following variables:

- **review**: Text of the review.
- **pos**: Target variable (`0` for negative, `1` for positive).
- **ds_part**: Indicates whether the review belongs to the training or test set.

### Project Development

1. **Text Preprocessing**
   
   - Convert text to lowercase and remove special characters.
   - Tokenization and removal of stopwords.
   - Text vectorization using **TF-IDF**.

2. **Training Classification Models**
   
   - Comparison between `Logistic Regression`, `Naive Bayes`, and `Random Forest`.
   - Hyperparameter optimization using `GridSearchCV`.
   
3. **Model Evaluation**
   
   - The main metric is **`F1-score`**, with a minimum threshold of **`0.85`**.
   - Comparison of **`precision and recall`** to ensure a balanced detection of negative reviews.

### Results and Conclusions

- **Naive Bayes achieved the best performance**, reaching an **`F1-score of 0.87`**, surpassing the established threshold.
- The **`TF-IDF`** vectorization significantly improved the model’s accuracy.
- This system will allow **`Film Junky Union`** to automatically categorize movie reviews and enhance the user experience.

This model represents an efficient solution for opinion classification and can be adapted to other areas of entertainment.

---

## Project 15: Age Prediction with Convolutional Neural Networks

### Context

The supermarket chain **`Good Seed`** wants to ensure compliance with alcohol sales regulations by preventing sales to minors. To achieve this, they aim to develop a **`Machine Learning model`** that can predict a person’s age from a **`photograph`** using **`Convolutional Neural Networks (CNNs)`**.

### Data Used

The dataset consists of images of faces of different ages labeled with the actual age of the person in the photograph.

### Project Development

1. **Data Preprocessing**
   
   - Image normalization and scaling.
   - `Data augmentation` to improve the model's generalization.

2. **Model Training**

   - Implementation of a `Convolutional Neural Network (CNN)` using `TensorFlow` and `Keras`.
   - Comparison with pre-trained models such as `ResNet` and `VGG16`.
   
3. **Model Evaluation**

   - The primary evaluation metric is `Mean Absolute Error (MAE)`.
   - Hyperparameter optimization to improve model accuracy.

### Results and Conclusions

- **`ResNet achieved the best performance`**, with an **`MAE of 4.3 years`**, indicating that the model has acceptable accuracy for the task.
- The custom convolutional neural network also performed well, although with a longer training time.
- This model will enable **`Good Seed`** to implement an automated solution for verifying the age of alcohol buyers in its supermarkets.

This system represents a significant advancement in integrating **`computer vision`** into the retail sector to enhance compliance with legal regulations.

---

## Final Project: Churn Rate Telecom

### Context

The telecommunications provider **`Interconnect`** aims to predict customer churn rates. If a user is identified as likely to cancel their service, the company can offer promotional codes and special plans to retain them.

### Interconnect Services

Interconnect provides the following services:

- **`Landline`**: Allows multiple simultaneous line connections.
- **`Internet`**: DSL or fiber-optic connection.
  
- **Additional Services**:
  
  - **`Device Protection`**: Antivirus.
  - **`Online Security`**: Malicious site blocker.
  - **`Technical Support`** and **`Online Backup`**.
  - **`Streaming TV`** and **`Streaming Movies`**.

### Data Used

The dataset includes information about customers, their contracts, and active services.

### Project Development

1. **Exploratory Data Analysis (EDA)**
   
   - Evaluating data distribution and removing outliers.
   - Converting categorical variables into numerical ones.

2. **Model Training**

   - Comparing models such as `Logistic Regression`, `Gradient Boosting` and `Random Forest`.
   - Optimizing hyperparameters using `GridSearchCV`.

3. **Model Evaluation**

   - The primary metric is **`AUC-ROC`**, with a minimum threshold of **`0.85`**.
   - `Precision`, `recall`, and `F1-score` are compared to evaluate performance.

### Results and Conclusions

- `Gradient Boosting` achieved the `best performance`, with an **`AUC-ROC` of `0.88`**.
- The most influential services in customer churn were identified.
- This model will enable **`Interconnect`** to anticipate customer churn and improve retention strategies.

This project represents an effective solution for churn prediction in telecommunications and can be applied to other industries with similar business models.

---
