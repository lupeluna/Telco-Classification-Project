# Telco-Classification-Project
______________________

Hello,

Welcome to the README file for my "Telco Churn Classification Project"

Here, you will find my work on working through the pipeline and will also find the data dictionary to help offer more insight to the variables being used.

_______________________

## GOAL:

My goal is to identify and key driver(s) of churn within the TELCO database and develop a classification model to accurately predict the key driver(s) of churn.

______________________



## Planning process

Below you will see the TRELLO pipleline I used which can also be found in this link: [TrelloBoard](https://trello.com/b/Br3Pok0L/telco-churn-classification)

In the process of creating this README file, you can see where I was at at this point below.


![Trello](ScreenShot.png)


___________________________

-  Please use this data dictionary as a reference for the variables used within in the data set.



|   Feature      |  Data Type   | Description    |
| :------------- | :----------: | -----------: |
|  customer_id | object   | unique customer identifier    |
| senior_citizen   | int64 | Whether one is a senior or not|
| tenure_in_months   | int64 | How many months a customer had service|
| total_charges   | int64 | total charges since day 1|
| churn  | object| Yes = Churn, No = Not Churned|
| average_charges  | float64| total_charges / tenure_in_months|
| tenure_in_years   | float64 | tenure_in_months / 12|
| encoded_churn   | int64 | 1 = Churn, 0 = Not Churned|
| no_partner_depend   | int64 | no partner & no dependents|
| phone_lines   | int64 | 1 = has phone lines, 0 = No phone|
| stream_tv_mov   | int64 | has streaming tv & streaming movie|
| online_sec_bckup  | int64 | has online security & online backup|
| female  | uint8| 1 = female, 0 = not female|
| male  | uint8| 1 = male, 0 = not male|
| no_partner  | uint8 | 1 = no partner, 0 = has partner|
| has_partner  | unit8 | 1 = has partner, 0 = no partner|
| dependents_no   | unit8| 1 = no dependents, 0 = has dependents|
| dependents_yes   | unit8| 1 = has dependents, 0 = no dependents|
| device_proctection_no   | uint8 | 1 = no protection, 0 = has protection|
| device_proctection_no_int   | uint8 | 1 = no internet, 0 = has internet|
| device_proctection_yes   | uint8 | 1 = has protection, 0 = no protection|
| tch_support_no   | uint8 | 1 = no tech support, 0 = has tech support|
| tch_support_no_int   | uint8 | 1 = no internet, 0 = has internet|
| tch_support_yes  | uint8 | 1 = has tech support, 0 = no tech support|
| paperless_billing_no   | uint8 | 1 = no paperless billing 0 = has paperless billing|
| paperless_billing_yes   | uint8 | 1 = has paperless billing, 0 = no paperless billing
| monthly_contract   | uint8 | 1 = on monthly contract, 0 = no monthly contract|
| one_yr_contract   | uint8 | 1 = on 1 yr contract, 0 = not on 1 yr contract|
| two_yr_contract   | uint8 | 1 = on 2 yr contract, 0 = not on 2 yr contract|
| has_dsl  | uint8 | 1 = has dsl, 0 = no dsl|
| has_fiber_optic   | uint8 | 1 = has fiber optic, 0 = no fiber optic|
| no_internet   | uint8 | 1 = no internet, 0 = has internet|
| pmt_bank transfer   | uint8 | 1 = pay w/bank transfer, 0 = no bank transfer|
| pmt_cc   | uint8 | 1 = pays w/credit card, 0 = no credit card|
| pmt_electronic_check  | uint8 | 1 = pays w/elec check, 0 = no elec check|
| pmt_mailed_check | uint8 | 1 = pays w/mail check, 0 = no mail check|



-------------------
 
 
#### Initial Hypotheses

> - **Hypothesis 1 -** I rejected the Null Hypothesis; there is a difference.
> - alpha = .05
> - $H_o$: There is no association between service types and churn.  
> - $H_a$: There is an association between service types and churn. 

> - **Hypothesis 2 -** I rejected the Null Hypothesis; there is a difference.
> - alpha = .05
> - $H_0$: $H_o$: There is no association between tenure types and churn.
> - $H_a$: There is an association between tenure types and churn.

<hr style="border-top: 10px groove blueviolet; margin-top: 1px; margin-bottom: 1px"></hr>

### Executive Summary - Conclusions & Next Steps
<hr style="border-top: 10px groove blueviolet; margin-top: 1px; margin-bottom: 1px"></hr>

> - I found that all of the classification models I created, LogisticRegression, DecisionTree, RandomForest, and KNeighbors predicted the species of Iris equally well using the features `sepal_width`, `sepal_length`, `petal_length`, `petal_width`.
> - I chose my DecisionTree model as my best model with a 90% accuracy rate for predicting my target value, species. This model outperformed my baseline score of 33% accuracy, so it has value.
> - Some initial exploration and statistical testing revealed that engineering some new features like petal area or sepal area might help my models predict with even more accuracy, and with more time, I would like to test this hypothesis.

<hr style="border-top: 10px groove blueviolet; margin-top: 1px; margin-bottom: 1px"></hr>

### Pipeline Stages Breakdown

<hr style="border-top: 10px groove blueviolet; margin-top: 1px; margin-bottom: 1px"></hr>

##### **Plan ->** Acquire -> Prepare -> Explore -> Model -> Deliver
- [x] Create README.md with data dictionary, project and business goals, come up with initial hypotheses.
- [x] Acquire data from the Codeup Database and create a function to automate this process. Save the function in an acquire.py file to import into the Final Report Notebook.
- [x] Clean and prepare data for the first iteration through the pipeline, MVP preparation. Create a function to automate the process, store the function in a prepare.py module, and prepare data in Final Report Notebook by importing and using the funtion.
- [x]  Clearly define two hypotheses, set an alpha, run the statistical tests needed, reject or fail to reject the Null Hypothesis, and document findings and takeaways.
- [x] Establish a baseline accuracy and document well.
- [x] Train three different classification models.
- [x] Evaluate models on train and validate datasets.
- [x] Choose the model with that performs the best and evaluate that single model on the test dataset.
- [x] Create csv file with the customer id, the probability of churn, and the model's predictions.
- [x] Document conclusions, takeaways, and next steps in the Final Report Notebook.

___

##### Plan -> :white_check_mark: Acquire ->** Prepare -> Explore -> Model -> Deliver
> - Store functions that are needed to acquire data from the measures and species tables from the iris database on the Codeup data science database server; make sure the acquire.py module contains the necessary imports to run my code.
> - The final function will return a pandas DataFrame.
> - Import the acquire function from the acquire.py module and use it to acquire the data in the Final Report Notebook.
> - Complete some initial data summarization (`.info()`, `.describe()`, `.value_counts()`, ...).
> - Plot distributions of individual variables.
___

##### Plan -> Acquire -> :white_check_mark: Prepare ->** Explore -> Model -> Deliver
> - Store functions needed to prepare the iris data; make sure the module contains the necessary imports to run the code. The final function should do the following:
    - Split the data into train/validate/test.
    - Handle any missing values.
    - Handle erroneous data and/or outliers that need addressing.
    - Encode variables as needed.
    - Create any new features, if made for this project.
> - Import the prepare function from the prepare.py module and use it to prepare the data in the Final Report Notebook.
___

##### Plan -> Acquire -> Prepare -> :white_check_mark:Explore ->** Model -> Deliver
> - Answer key questions, my hypotheses, and figure out the features that can be used in a classification model to best predict the target variable, species. 
> - Run at least 2 statistical tests in data exploration. Document my hypotheses, set an alpha before running the tests, and document the findings well.
> - Create visualizations and run statistical tests that work toward discovering variable relationships (independent with independent and independent with dependent). The goal is to identify features that are related to species (the target), identify any data integrity issues, and understand 'how the data works'. If there appears to be some sort of interaction or correlation, assume there is no causal relationship and brainstorm (and document) ideas on reasons there could be correlation.
> - Summarize my conclusions, provide clear answers to my specific questions, and summarize any takeaways/action plan from the work above.
___

##### Plan -> Acquire -> Prepare -> Explore -> :white_check_mark:Model ->** Deliver
> - Establish a baseline accuracy to determine if having a model is better than no model and train and compare at least 3 different models. Document these steps well.
> - Train (fit, transform, evaluate) multiple models, varying the algorithm and/or hyperparameters you use.
> - Compare evaluation metrics across all the models you train and select the ones you want to evaluate using your validate dataframe.
> - Feature Selection (after initial iteration through pipeline): Are there any variables that seem to provide limited to no additional information? If so, remove them.
> - Based on the evaluation of the models using the train and validate datasets, choose the best model to try with the test data, once.
> - Test the final model on the out-of-sample data (the testing dataset), summarize the performance, interpret and document the results.
___

##### Plan -> Acquire -> Prepare -> Explore -> Model -> :white_check_mark:Deliver**
> - Introduce myself and my project goals at the very beginning of my notebook walkthrough.
> - Summarize my findings at the beginning like I would for an Executive Summary. (Don't throw everything out that I learned from Storytelling) .
> - Walk Codeup Data Science Team through the analysis I did to answer my questions and that lead to my findings. (Visualize relationships and Document takeaways.) 
> - Clearly call out the questions and answers I am analyzing as well as offer insights and recommendations based on my findings.

<hr style="border-top: 10px groove blueviolet; margin-top: 1px; margin-bottom: 1px"></hr>

### Reproduce My Project

<hr style="border-top: 10px groove blueviolet; margin-top: 1px; margin-bottom: 1px"></hr>

You will need your own env file with database credentials along with all the necessary files listed below to run my final project notebook. 
- [x] Read this README.md
- [ ] Download the aquire.py, prepare.py, and final_report.ipynb files into your working directory
- [ ] Add your own env file to your directory. (user, password, host)
- [ ] Run the final_report.ipynb notebook
