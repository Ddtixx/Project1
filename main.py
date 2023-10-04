import pandas as pd
import matplotlib.pyplot as plt


df_inifian = pd.read_csv(r'C:\Users\ddtix\Downloads\Data.csv')

print(df_inifian, ['Date'])

fig,ax= plt.subplots(figsize= (10, 6))
ax.plot(df_inifian['Time'], df_inifian['Date'], '-')
plt.legend(["This is my legend"], fontsize="x-large")
plt.show()
