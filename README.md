# Salary Recommender System Web Application  (FLASK Front End Interface)

Web application written in Python using `flask` and deployed on Heroku.
This is a project for NUS Capstone and deployed by Zac & his team. 
http://salaryapp123-05a352c77bf6.herokuapp.com/

1. Data Preparation:
18,960 rows data was extracted from different job portals such as MyCareerFuture, Indeed & Jobstreet using various tools (such as RPA, Python Script & third party tools)

2. Data Prep:
Data was cleaned using Regex, replacement & transformation. NLP & Rule-based filtering for texts. We also fractionized different useful skills & keywords from JD before One Hot Encoding.

3. Data Modeling 1:
Supervised training with expert labelling using SVM to classify unrelated texts & job requirements texts. Classify job titles using 950 expert labelled samples with cleaned JD.

4. Modeling 2:
Explore more than 5 different classification models. Hyper-parameter tuning using GridSearchCV.

5. Fine Tuning:
Updated >100 words stop-word & keep-word dictionary using estimated log probability.

7. Deployment:
Offline trained model extracted using Pickle & push to Heroku. 
