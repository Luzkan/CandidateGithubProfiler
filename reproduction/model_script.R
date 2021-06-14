
# 1. Install required packages

#install.packages("mlr")
#install.packages("e1071")
#install.packages("randomForest")
#install.packages("corrplot")
library(mlr)
library(corrplot)

# 2. Make sure you set the right path to the data csv file
path<-"<YOUR PATH>/modelDataNoLabels.csv"

# 3. Importing data from csv.file
model_data <- read.csv(path,encoding="UTF-8")
model_data$X=NULL


# 4. Displaying matrix of correlations
arrayOfCorrelations <- cor(model_data)
corrplot(arrayOfCorrelations, order = "hclust")

# 5. Adding target columnt to dataset (You can label the data by yourself)
isOk <- c("OK", "OK", "NOTOK", "OK", "NOTOK", "OK", "OK", "OK", "NOTOK", "OK", 
          "OK", "OK", "NOTOK", "NOTOK", "NOTOK", "OK", "NOTOK", "OK", "OK", "OK",
          "OK", "NOTOK","OK", "NOTOK", "NOTOK", "OK")
model_data['isOk'] = isOk

# 6. Defining task
classif_task = makeClassifTask(id = "testowy", data = model_data, target = "isOk")

# 7. Defining repetitive cross validation
rdesc = makeResampleDesc("RepCV", folds=4, reps = 10)

# 8. Learinig and validating model
rf = resample("classif.randomForest", classif_task, rdesc, measures = list(mmce,mcc,f1,acc,kappa))
svm = resample("classif.svm", classif_task, rdesc, measures = list(mmce,mcc,f1,acc,kappa))
knn = resample("classif.knn", classif_task, rdesc, measures = list(mmce,mcc,f1,acc,kappa))

# 9. Displaying results
rf
svm
knn

