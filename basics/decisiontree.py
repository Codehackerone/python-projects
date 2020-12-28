import pandas
# # from sklearn import tree
# # import pydotplus
from sklearn.tree import DecisionTreeClassifier
# # import matplotlib.pyplot as plt
# # import matplotlib.image as pltimg

df = pandas.read_csv("shows.csv")
# To convert from string to numerical data
# UK=0 USA=1 N=2
# YES=1 NO=0
d = {'UK': 0, 'USA': 1, 'N': 2}
df['Nationality'] = df['Nationality'].map(d)
d = {'YES': 1, 'NO': 0}
df['Go'] = df['Go'].map(d)

# features and target column
features = ['Age', 'Experience', 'Rank', 'Nationality']

X = df[features]
y = df['Go']

# Now creating the decision tree
dtree = DecisionTreeClassifier()
dtree = dtree.fit(X, y)
# for image
# # data = tree.export_graphviz(dtree, out_file=None, feature_names=features)
# # graph = pydotplus.graph_from_dot_data(data)
# # graph.write_png('mydecisiontree.png')
# # img = pltimg.imread('mydecisiontree.png')
# # imgplot = plt.imshow(img)
# # plt.show()
# predict values 40 10 7 1
print(dtree.predict([[40, 10, 7, 1]]))
