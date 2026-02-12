import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score,roc_curve
from sklearn.pipeline import Pipeline

import matplotlib.pyplot as plt
from sklearn.model_selection import cross_val_score

df = pd.read_csv("leads_cleaned.csv")


df['Converted'] = df['Converted'].astype(str).str.strip().str.lower()

df['Converted'] = df['Converted'].map({
    'yes': 1, 'no': 0,
    '1': 1, '0': 0,
    'true': 1, 'false': 0
})

df = df.dropna(subset=['Converted'])#It removes all rows where the Converted column is NaN.





X = df.drop('Converted', axis=1)# axis =1 represents column
y = df['Converted']


X = pd.get_dummies(X, drop_first=True)

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.3,
    random_state=42,
    stratify=y
)
X=X.astype(int)

from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

log_reg = LogisticRegression(max_iter=1000)

log_reg.fit(X_train_scaled, y_train)

y_pred = log_reg.predict(X_test_scaled)
print("Accuracy:", accuracy_score(y_test, y_pred))
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))
y_prob = log_reg.predict_proba(X_test_scaled)[:,1]
print("ROC-AUC:", roc_auc_score(y_test, y_prob))
auc_score = roc_auc_score(y_test, y_prob)
fpr, tpr, thresholds = roc_curve(y_test, y_prob)
plt.figure()
plt.plot(fpr, tpr, label=f"Logistic Regression (AUC = {auc_score:.3f})")
plt.plot([0,1], [0,1], linestyle='--')  # random classifier
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve")
plt.legend()
plt.show()

pipe = Pipeline([
    ('scaler', StandardScaler()),
    ('model', LogisticRegression(max_iter=1000))
])

cv_scores = cross_val_score(
    pipe,
    X,
    y,
    cv=5,
    scoring='roc_auc'
)

print("Logistic Regression CV ROC-AUC Scores:", cv_scores)
print("Mean CV ROC-AUC:", cv_scores.mean())


#Decision Tree
from sklearn.tree import DecisionTreeClassifier
clf=DecisionTreeClassifier(criterion="entropy",max_depth=5,random_state=42)
clf.fit(X_train,y_train)
y_pred = clf.predict(X_test)

print("Test Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

y_prob_dt = clf.predict_proba(X_test)[:,1]

fpr_dt, tpr_dt, _ = roc_curve(y_test, y_prob_dt)
auc_dt = roc_auc_score(y_test, y_prob_dt)

plt.plot(fpr_dt, tpr_dt, label=f"Decision Tree (AUC = {auc_dt:.3f})")


dt = DecisionTreeClassifier(max_depth=5, random_state=42)

cv_scores_dt = cross_val_score(
    dt,
    X,
    y,
    cv=5,
    scoring='roc_auc'
)

print("Decision Tree CV ROC-AUC Scores:", cv_scores_dt)
print("Mean CV ROC-AUC:", cv_scores_dt.mean())


#random forest
from sklearn.ensemble import RandomForestClassifier
rf = RandomForestClassifier(n_estimators=1000,criterion="gini",random_state=42)
rf.fit(X_train,y_train)
y_pred = rf.predict(X_test)

print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))
y_prob_rf = rf.predict_proba(X_test)[:,1]
fpr_rf, tpr_rf, _ = roc_curve(y_test, y_prob_rf)
auc_rf = roc_auc_score(y_test, y_prob_rf)
plt.plot(fpr_rf, tpr_rf, label=f"Random Forest (AUC = {auc_rf:.3f})")


#random forest
from sklearn.ensemble import RandomForestClassifier
rf = RandomForestClassifier(n_estimators=1000,criterion="gini",random_state=42)
rf.fit(X_train,y_train)
y_pred = rf.predict(X_test)
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))
y_prob_rf = rf.predict_proba(X_test)[:,1]
fpr_rf, tpr_rf, _ = roc_curve(y_test, y_prob_rf)
auc_rf = roc_auc_score(y_test, y_prob_rf)
plt.plot(fpr_rf, tpr_rf, label=f"Random Forest (AUC = {auc_rf:.3f})")

rf = RandomForestClassifier(n_estimators=1000, random_state=42)

cv_scores_rf = cross_val_score(
    rf,
    X,
    y,
    cv=5,
    scoring='roc_auc'
)

print("Random Forest CV ROC-AUC Scores:", cv_scores_rf)
print("Mean CV ROC-AUC:", cv_scores_rf.mean())


import pandas as pd
import matplotlib.pyplot as plt


rf.fit(X_train, y_train)


feature_importance = pd.DataFrame({
    'Feature': X.columns,
    'Importance': rf.feature_importances_
})


feature_importance = feature_importance.sort_values(
    by='Importance',
    ascending=False
)


top_features = feature_importance.head(10)


plt.figure(figsize=(8,6))
plt.barh(top_features['Feature'], top_features['Importance'])
plt.gca().invert_yaxis()   
plt.xlabel("Importance Score")
plt.title("Top 10 Important Features - Random Forest")
plt.show()


#SVM
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, roc_auc_score

svm_clf = SVC(
    kernel="rbf",
    C=10,
    gamma="scale",
    probability=True

)

svm_clf.fit(X_train_scaled, y_train)

# Predictions
y_pred = svm_clf.predict(X_test_scaled)
print("Accuracy:", accuracy_score(y_test, y_pred))


y_prob_svm = svm_clf.predict_proba(X_test_scaled)[:, 1]
print("ROC-AUC:", roc_auc_score(y_test, y_prob_svm))
fpr_svm, tpr_svm, _ = roc_curve(y_test, y_prob_svm)
auc_svm = roc_auc_score(y_test, y_prob_svm)

plt.plot(fpr_svm, tpr_svm, label=f"SVM (AUC = {auc_svm:.3f})")


svm_model = Pipeline([
    ('scaler', StandardScaler()),
    ('svm', SVC(kernel='rbf', C=10, gamma='scale', probability=True))
])

cv_scores_svm = cross_val_score(
    svm_model,
    X,
    y,
    cv=5,
    scoring='roc_auc'
)

print("SVM CV ROC-AUC Scores:", cv_scores_svm)
print("Mean CV ROC-AUC:", cv_scores_svm.mean())

#roc-curve
plt.figure(figsize=(7,6))

plt.plot(fpr, tpr, label=f"Logistic Regression (AUC = {auc_score:.3f})")
plt.plot(fpr_dt, tpr_dt, label=f"Decision Tree (AUC = {auc_dt:.3f})")
plt.plot(fpr_rf, tpr_rf, label=f"Random Forest (AUC = {auc_rf:.3f})")
plt.plot(fpr_svm, tpr_svm, label=f"SVM (AUC = {auc_svm:.3f})")

plt.plot([0,1], [0,1], linestyle="--", color="black")
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve Comparison")
plt.legend()
plt.show()