import seaborn as sns
import matplotlib.pyplot as plt
iris = sns.load_dataset('iris')
sns.heatmap(iris.corr(numeric_only=True), annot=True, cmap='summer')
plt.show()
