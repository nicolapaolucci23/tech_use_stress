import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('C:/Users/nicola.paolucci/Desktop/progetti_github/tech_use_stress/data/Tech_Use_Stress_Wellness.csv')
print(df.columns)

caffe=df[["sleep_quality", "caffeine_intake_mg_per_day"]]
#print(caffe[["sleep_quality", "caffeine_intake_mg_per_day"]].dtypes)

#print(caffe)

plt.figure(figsize=(8,6)) 
plt.scatter(caffe['sleep_quality'], caffe['caffeine_intake_mg_per_day'],alpha=0.6) #grafico scatter
plt.ylabel('caffeina in milligrammi')
plt.xlabel('qualita del sonno')
plt.title('Relazione tra intake di caffeina e qualità del sonno')
plt.grid(True)
plt.show()






