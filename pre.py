
from sklearn.preprocessing import StandardScaler


def scaling():
    sc = StandardScaler()
    d = sc.fit_transform([[34,2,45,4,5]])
    print (d)

scaling()