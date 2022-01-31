# ACM Research Coding Challenge (Spring 2022)

## [](https://github.com/ACM-Research/-DRAFT-Coding-Challenge-S22#no-collaboration-policy)No Collaboration Policy

**You may not collaborate with anyone on this challenge.**  You  _are_  allowed to use Internet documentation. If you  _do_  use existing code (either from Github, Stack Overflow, or other sources),  **please cite your sources in the README**.

## [](https://github.com/ACM-Research/-DRAFT-Coding-Challenge-S22#submission-procedure)Submission Procedure

Please follow the below instructions on how to submit your answers.

1.  Create a  **public**  fork of this repo and name it  `ACM-Research-Coding-Challenge-S22`. To fork this repo, click the button on the top right and click the "Fork" button.

2.  Clone the fork of the repo to your computer using  `git clone [the URL of your clone]`. You may need to install Git for this (Google it).

3.  Complete the Challenge based on the instructions below.

4.  Submit your solution by filling out this [form](https://acmutd.typeform.com/to/uTpjeA8G).

## Assessment Criteria 

Submissions will be evaluated holistically and based on a combination of effort, validity of approach, analysis, adherence to the prompt, use of outside resources (encouraged), promptness of your submission, and other factors. Your approach and explanation (detailed below) is the most weighted criteria, and partial solutions are accepted. 

## [](https://github.com/ACM-Research/-DRAFT-Coding-Challenge-S22#question-one)Question One

[Binary classification](https://en.wikipedia.org/wiki/Binary_classification) is a type of classification task that labels elements of a set (i.e. dataset) into two different groups. An example of this type of classification would be identifying if people had a specific disease or not based on certain health characteristics. The dataset found in `mushrooms.csv` holds data (22 different characteristics, specifically) about different types of mushrooms, including a mushroom's cap shape, cap surface texture, cap color, bruising, odor, and more. Remember to split the data into test and training sets (you can choose your own percent split). Information about the meaning of the letters under each column can be found within the file `attributelegend.txt`.

**With the file `mushrooms.csv`, use an algorithm of your choice to classify whether a mushroom is poisonous or edible.**

**You may use any programming language you feel most comfortable. We recommend Python because it is the easiest to implement. You're allowed to use any library or API you want to implement this, just document which ones you used in this README file.** Try to complete this as soon as possible.

Regardless if you can or cannot answer the question, provide a short explanation of how you got your solution or how you think it can be solved in your README.md file. However, we highly recommend giving the challenge a try, you just might learn something new!

Explanation for Solution:

I first read the mushroom.csv data as a raw GitHub link using pandas.read_csv to put it into a data frame.  Raw Github link had to be used because the mushroom.csv file was in Github’s display version, meaning no access to the  “raw” actual file.  I then checked if the dataset in the data frame was balanced in terms of having edible or poisonous mushrooms. It is important to have a dataset to be balanced for the model to be accurate. I read if a dataset is unbalanced then the model can be biased for example as one of the many issues that can happen. Even though the dataset was not fully 50% to 50% balanced, as the graph showed the difference was not too large enough for it to be manipulated to be balanced. Seaborn was used to checking if it was balanced or not. I read online that the Seaborn library is useful for data visualizations, which helped in this case with count plot. I ended up checking the data type of elements inside the dataset through the use of dtypes functionality from the pandas.DataFrame library. I found out that all the elements were object data types, which would make it difficult to be used in the models. I wanted to convert them into a data type that could work with my machine learning model. I had to then convert the datatype of the data frame to be category type, which in return allowed me to use LabelEncoder to make the data usable for the machine learning model I was considering. I then assigned the X and Y based on certain features. I ended up splitting the data set with  80% for the training data set and 20% for the testing data set. I ended up using these numbers naturally due to these being the common numbers being used for a split but do know that different numbers can be used for the split. I ended up picking LogisticRegression for my machine learning model to classify, whether the mushrooms would be edible or poisonous. I saw LogisticRegression as a recommended or commonly used model in the Binary Classification Wikipedia link, which made me research it further. When I searched it online, I read that is a popular choice to use when finding the probability between two variables, which in our case would be edible or poisonous. I ended up considering some of the other models mentioned in the Binary Classification Wikipedia link given but ended up sticking with logistic regression due to just how it seemed like a common and good fit given the conditions of the dataset. I ended up 'liblinear' for the solver parameter because the dataset size did not seem to be too large, and the sklearn documentation mentioned how ‘liblinear’ is a wise choice for small datasets. I ended up getting about 95.26 accuracy for the classification in this case.


Sources: 

Reading data: https://stackoverflow.com/questions/14441729/read-a-csv-from-github-into-r
Seaborn doc: https://seaborn.pydata.org/
https://stackabuse.com/seaborn-library-for-data-visualization-in-python-part-1/
Balanced or Unbalanced Dataset info: ​​https://stackoverflow.com/questions/65752715/must-a-dataset-for-a-classifier-be-perfectly-balanced
Sklearn doc: https://scikit-learn.org/stable/
https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html
https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.LabelEncoder.html
Pandas doc: https://pandas.pydata.org/docs/
Logistic Regression research: https://en.wikipedia.org/wiki/Logistic_regression
https://www.geeksforgeeks.org/advantages-and-disadvantages-of-logistic-regression/
Link used to understand encoding: https://www.mygreatlearning.com/blog/label-encoding-in-python/


