
# 01 Introduction to Machine Learning

- **Supervised Learning** 
	- (e.g., Linear Regression, Decision Trees ) 
	- The model is trained on labeled data (input-output pairs)
- **Unsupervised Learning** 
	- (e.g., Clustering, K-Means, PCA)
	- The model identifies patterns or structures in unlabeled data
- **Semi-Supervised Learning** 
	- Falls between supervised and unsupervised learning
	- It uses both labeled and unlabeled data to build a model, which is particularly useful when labeling data is expensive or time-consuming, but a large amount of unlabeled data is readily available
- **Reinforcement Learning** 
	- (e.g., Q-Learning)
	- The model learns through interactions with an environment to maximize a reward signal

### 02 **Model Parameters and Hyperparameters**
- **Model Parameters **
	- These are the internal variables that the model learns from the data during training
	- eg: in a linear regression model, the weights (coefficients) are the parameters
  
- **Hyperparameters** 
	- These are the settings or configurations specified before training
	- They control the learning process and must be tuned
	- eg: learning rate in gradient descent, the number of trees in a random forest, or the number of clusters in K-means

### 03 **Loss Function**
The loss function quantifies how well the model's predictions match the actual data. It measures the error between the predicted output and the true output

- **Mean Squared Error (MSE)** 
	- Used in regression, it measures the average squared difference between the predicted and actual values
- **Cross-Entropy Loss** 
	- Used in classification, it measures the difference between the predicted probability distribution and the actual distribution (labels)

### 04 **Gradient Descent**
Gradient Descent is an optimization algorithm used to minimize the loss function. The basic idea is to update the model parameters in the opposite direction of the gradient of the loss function with respect to the parameters

- **Compute Gradient :** Calculate the gradient of the loss function with respect to each parameter
- **Update Parameters :** Adjust the parameters by moving them slightly in the direction that reduces the loss
- **Learning Rate :** A hyperparameter that controls the size of the step taken during each update

### 05 **Train-Test Split**
Before training the model, the dataset is typically split into
- **Training Set :** Used to train the model
- **Testing Set :** Used to evaluate the model’s performance on unseen data
The train-test split helps to ensure that the model generalizes well to new data and is not simply memorizing the training data

### 06 **Training the Model**
- Training involves feeding the training data to the model and adjusting the parameters based on the loss function and gradient descent
- The training process continues until the model converges (i.e., further training does not significantly reduce the loss)

### 07 **Model Evaluation**
After training, the model is evaluated on the test set using various metrics depending on the task

- **Accuracy**
	- The proportion of correctly predicted labels (used in classification)
- **Precision and Recall**
	- Measures of how many true positives are correctly identified versus false positives (used in classification)
- **F1 Score** 
	- The harmonic mean of precision and recall
- **R-squared** 
	- A statistical measure that represents the proportion of the variance for a dependent variable that's explained by an independent variable (used in regression)
- **Confusion Matrix** 
	- A table used to describe the performance of a classification model

### 08 **Hyperparameter Tuning**
To improve the model's performance, hyperparameters are tuned
- **Grid Search :** Testing all possible combinations of hyperparameters
- **Random Search :** Randomly sampling hyperparameters
- **Bayesian Optimization :** Using a probabilistic model to choose hyperparameters more efficiently

### 09 **Cross-Validation**
- Cross-validation is a technique for assessing how the results of a model will generalize to an independent dataset 
- It involves partitioning the dataset into a set of training and validation sets multiple times, training the model on each training set, and evaluating it on the corresponding validation set

### 10 **Deployment, Monitoring and Maintenance**


# 1. Applications of Machine Learning
- Predictive maintenance
- Fraud detection
- Customer segmentation
- Image recognition
- Natural language processing
- Recommendation systems
- Autonomous vehicles
- Sentiment analysis
- Healthcare diagnostics
- Speech recognition
- Financial forecasting
- Spam detection
- Virtual assistants
- Supply chain optimization
- Personalized marketing etc


# 2. Supervised v/s Unsupervised ML

## Supervised Learning
- A type of machine learning where a model is trained on a labeled dataset
- In this approach, the dataset consists of input-output pairs, where each input (also known as features) is associated with a corresponding output (also known as labels or targets)
- The goal of the model is to learn the mapping from inputs to outputs so that it can accurately predict the output for new, unseen inputs

### Key Concepts in Supervised Learning
1. **Training Data** : The dataset used to train the model. Each example in the dataset includes both the input data (features) and the correct output (label).

2. **Features** : The input variables or attributes used to make predictions. For example, in a dataset predicting house prices, features could include the size of the house, the number of bedrooms, and the location.

3. **Labels** : The output or target variable that the model aims to predict. In the house price example, the label would be the actual price of the house.

4. **Model** : An algorithm that learns from the training data. The model tries to capture the relationship between the features and the labels.

5. **Training** : The process of feeding the model with the training data and allowing it to adjust its internal parameters to minimize the difference between its predictions and the actual labels.

6. **Testing** : After training, the model is evaluated on a separate dataset (the test set) to assess its performance. The test set consists of data that the model has not seen before, helping to ensure that the model generalizes well to new inputs.

7. **Prediction** : Once the model is trained, it can be used to make predictions on new, unseen data by applying the learned mapping from inputs to outputs.

### Types of Supervised Learning
1. **Regression** : When the output variable is continuous, such as predicting a price or temperature. For example, predicting house prices based on various features.

2. **Classification** : When the output variable is categorical, such as predicting whether an email is spam or not (binary classification) or identifying the species of a flower (multi-class classification).

## Applications of Supervised Learning
---
### 1. **Image and Object Recognition**
   - **Facial Recognition**: Identifying or verifying individuals in images or videos based on their facial features.
   - **Object Detection**: Recognizing and locating objects within images, used in autonomous vehicles and security systems.

### 2. **Natural Language Processing (NLP)**
   - **Sentiment Analysis**: Determining the sentiment (positive, negative, or neutral) from text, commonly used in social media monitoring and customer feedback analysis.
   - **Spam Detection**: Classifying emails as spam or not spam based on the content, sender, and other features.
   - **Language Translation**: Translating text from one language to another using models trained on parallel corpora.

### 3. **Medical Diagnosis**
   - **Disease Prediction**: Predicting the likelihood of diseases such as diabetes, cancer, or Alzheimer's disease based on patient data, including symptoms, test results, and medical history.
   - **Medical Imaging**: Classifying medical images (e.g., X-rays, MRIs) to detect conditions like tumors or fractures.

### 4. **Financial Services**
   - **Credit Scoring**: Assessing the creditworthiness of individuals or businesses by predicting the likelihood of default based on historical data.
   - **Fraud Detection**: Identifying fraudulent transactions or activities by analyzing patterns in financial data.

### 5. **Speech Recognition**
   - **Voice Assistants**: Converting spoken language into text and responding to voice commands, as seen in virtual assistants like Siri, Alexa, and Google Assistant.
   - **Transcription Services**: Automatically converting speech from audio files into written text.

### 6. **Recommender Systems**
   - **Product Recommendations**: Suggesting products, movies, or music to users based on their past behavior and preferences, used by platforms like Amazon, Netflix, and Spotify.
   - **Content Filtering**: Personalizing content feeds on social media platforms based on user interactions and preferences.

### 7. **Autonomous Vehicles**
   - **Lane Detection**: Identifying and following lanes on the road to assist in self-driving or advanced driver-assistance systems (ADAS).
   - **Pedestrian and Obstacle Detection**: Detecting pedestrians, other vehicles, and obstacles to ensure safe navigation.

### 8. **Marketing and Customer Relationship Management (CRM)**
   - **Customer Segmentation**: Classifying customers into different segments based on purchasing behavior, demographics, or engagement to target marketing efforts more effectively.
   - **Churn Prediction**: Predicting which customers are likely to leave or stop using a service, allowing companies to take proactive measures to retain them.

### 9. **Predictive Maintenance**
   - **Industrial Equipment Monitoring**: Predicting when equipment is likely to fail based on sensor data, allowing for timely maintenance and reducing downtime in manufacturing and other industries.

### 10. **Agriculture**
   - **Crop Yield Prediction**: Estimating crop yields based on factors like weather conditions, soil quality, and historical data to optimize farming practices.
   - **Pest and Disease Detection**: Identifying signs of pests or diseases in crops using image classification models.

### 11. **Energy Management**
   - **Load Forecasting**: Predicting energy consumption patterns to optimize power grid operations and reduce costs.
   - **Fault Detection**: Identifying faults in power systems or renewable energy installations like solar panels and wind turbines.

### 12. **Human Resources**
   - **Resume Screening**: Automatically filtering and ranking job applicants based on their qualifications and experience.
   - **Employee Performance Prediction**: Predicting employee performance and identifying potential candidates for promotion or additional training.



## Unsupervised Learning

- Unsupervised learning is a type of machine learning where the algorithm is trained on unlabeled data, meaning that the model is given input data without corresponding output labels
- The goal of unsupervised learning is to find hidden patterns, structures, or relationships in the data

### Types of Unsupervised Learning
1. **Clustering**
   - Group similar data points into clusters or groups where data points within the same cluster are more similar to each other than to those in other clusters
     - **K-Means Clustering**
	     - Partitions the data into a predetermined number of clusters by minimizing the variance within each cluster
     - **Hierarchical Clustering** 
	     - Builds a hierarchy of clusters either by starting with individual data points and merging them into larger clusters (agglomerative) or by starting with a single cluster and splitting it into smaller ones (divisive)
     - **DBSCAN (Density-Based Spatial Clustering of Applications with Noise)**
	     - Forms clusters based on the density of data points, which allows it to find clusters of arbitrary shapes and handle noise (outliers)
	 - **Gaussian Mixture Models (GMM)**:
		   - Assumes that the data is generated from a mixture of several Gaussian distributions
		   - Each cluster is represented by a Gaussian distribution, and the algorithm tries to find the parameters of these distributions
		   - GMM is more flexible than K-means because it allows clusters to have different shapes and sizes

2. **Dimensionality Reduction**
   - Reduce the number of features or dimensions in the data while retaining as much of the important information as possible
     - **Principal Component Analysis (PCA)**
	     - Transforms the data into a new set of orthogonal axes (principal components) that capture the maximum variance in the data
     - **t-Distributed Stochastic Neighbor Embedding (t-SNE)**
	     - Reduces the dimensionality of data, particularly useful for visualizing high-dimensional data in 2 or 3 dimensions by preserving the local structure of the data
     - **Autoencoders**
	     - Neural network models that learn to compress the input data into a lower-dimensional representation and then reconstruct it, useful for dimensionality reduction

3. **Association**
   - Discover interesting relationships or associations between different variables in the dataset
     - **Apriori Algorithm**
	     - Finds frequent itemsets in transactional data and derives association rules, commonly used in market basket analysis
     - **Eclat Algorithm**
	     - Similar to Apriori but uses a depth-first search approach to find frequent itemsets
     - **FP-Growth (Frequent Pattern Growth)**
	     - An efficient algorithm that compresses the dataset using a structure called an FP-tree and finds frequent itemsets without candidate generation

4. **Anomaly Detection**
   - Identify rare or unusual data points that do not conform to the general pattern of the data
     - **Isolation Forest**
	     - Detects anomalies by isolating data points in the feature space using random partitions
     - **One-Class SVM**
	     - A variant of Support Vector Machine that tries to separate normal data from anomalies by learning a decision boundary around the normal data
     - **LOF (Local Outlier Factor)**
	     - Identifies anomalies by comparing the local density of data points to that of their neighbors, where points with significantly lower density are considered anomalies

### Applications of Unsupervised Learning
- **Market Basket Analysis**
	- Association rules help in discovering product associations for cross-selling
- **Customer Segmentation**
	- Clustering techniques group customers based on purchasing behavior, enabling targeted marketing
- **Anomaly Detection**
	- Identifying fraudulent activities or system failures
- **Data Compression**
	- Dimensionality reduction methods reduce the complexity of data, useful in image compression and noise reduction
- **Recommendation Systems**
	- Uncovering patterns in user preferences to suggest relevant content



# 3. Important Py-Libraries for ML
1. **Numpy**
2. **Pandas**
3. **Matplotlib**
4. **SciPy**
5. **Scikit-Learn**