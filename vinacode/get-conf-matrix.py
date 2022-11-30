import seaborn as sn
import pandas as pd
import matplotlib.pyplot as plt

array = [[98,1],
         [2,19],]

df_cm = pd.DataFrame(array, ('1', '0'), ('1', '0'))
# plt.figure(figsize=(10,7))
sn.set(font_scale=2) # for label size
sn.heatmap(df_cm, annot=True, annot_kws={"size": 48}) # font size

plt.show()