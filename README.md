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

Below you will see the TRELLO pipleline I used which can also be found in this link: [title](https://trello.com/b/Br3Pok0L/telco-churn-classification)

In the process of creating this README file, you can see where I was at at this point below.


![alt text](ScreenShot.png)



-  Please use this data dictionary as a reference for the variables used within in the data set.



|   Feature      |  Data Type   | Description    |
| :------------- | :----------: | -----------: |
|  customer_id | object   | unique customer identifier    |
| senior_citizen   | int64 | # of months as a customer|
| tenure_in_months   | int64 | Whether one is a senior or not|
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
  <h3><u>Hypothesis and Questions</u></h3>
 - There is a relationship between churn and customers who use fiber optic internet who are single(no dependents), on month to month contracts, have no tech support and pay with electronic check.
 
 - Is there a relationship between churn having fiber optic internet?
 - Is there a relationship between churn and having no tech support?
 - Is there a relationship between churn and being on a monthly contract?
 - Is there a relationship between churn and having no partners and no dependents?
 - Is there a relationship between churn  and paying with an electronic check?
 
