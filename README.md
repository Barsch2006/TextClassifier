# textClassifier

## trainings data

The modell is basicly trained to classify a string/ a message into one of the following categories:

- greeting
- search (*a question, that can be answered by the internet*)
- question (*a question, that can not be answered by the internet*)
- undefiend (*if the models proba is to low, the message gets the category "undefiend" or if there is a undefiend context*)

Therefor the modell is gets about 20 german sentences/ words/ messages and about 10 english sentences/ words/ messages for each category as trainings data. So 30 sentences/ messages per category, which comes to 120 messages as the basic data-set
