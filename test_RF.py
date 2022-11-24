#just for testing edit
from sklearn.datasets import make_classification
import numpy as np
from sklearn.impute import SimpleImputer as Imputer
from sklearn.ensemble import RandomForestClassifier
from RF import RandomForestClassifier as PRF
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import warnings
import matplotlib.pyplot as plt

warnings.filterwarnings("ignore")

def insert_nans(X_train, X_test, nan_frac):
    X_train_w_nans = X_train.copy()
    X_test_w_nans = X_test.copy()

    n_train = X_train.shape[0]
    n_test = X_test.shape[0]
    nf = X_train.shape[1]

    nof_nans = int(np.prod(X_train.shape) * nan_frac)
    for i in range(nof_nans):
        o = np.random.choice(n_train)
        f = np.random.choice(nf)
        X_train_w_nans[o, f] = np.nan

    nof_nans = int(np.prod(X_test.shape) * nan_frac)
    for i in range(nof_nans):
        o = np.random.choice(n_test)
        f = np.random.choice(nf)
        X_test_w_nans[o, f] = np.nan

    imp = Imputer(missing_values=np.nan, strategy='median')
    X_train_w_nans_imp = imp.fit_transform(X_train_w_nans)
    X_test_w_nans_imp = imp.fit_transform(X_test_w_nans)

    return X_train_w_nans, X_test_w_nans, X_train_w_nans_imp, X_test_w_nans_imp


X, y = make_classification(n_samples = 1000)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


fr = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7]

prf_list = []
rf_list = []

for f in fr:
    X_train_w_nans, X_test_w_nans, X_train_w_nans_imp, X_test_w_nans_imp = insert_nans(X_train, X_test, f)

    prf = PRF()
    prf.fit(X_train_w_nans, y_train)
    prf_predict = prf.predict(X_test_w_nans)

    rf = RandomForestClassifier(n_estimators=10)
    rf.fit(X_train_w_nans_imp, y_train)
    rf_predict = rf.predict(X_test_w_nans_imp)

    prf_score = accuracy_score(y_test, prf_predict)
    rf_score = accuracy_score(y_test, rf_predict)

    prf_list.append(prf_score)
    rf_list.append(rf_score)



plt.plot(list(range(len(fr))), prf_list, label = 'PRF')
plt.plot(list(range(len(fr))), rf_list, label = 'RF')

plt.grid()
plt.legend()
plt.show()

