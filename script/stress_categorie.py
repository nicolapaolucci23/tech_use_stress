import pandas as pd

df=pd.read_csv('C:/Users/nicola.paolucci/Desktop/progetti_github/tech_use_stress/data/Tech_Use_Stress_Wellness.csv')
#rint(df.head(10))

def stress_categorization(a):    #direi che se stress sotto 5 di media è basso, tra 5 e 8 medio, sopra 8 è alto, 
   if a<= 5.0:
      return "Low stress level"  # la media è stata calcolata sul notebook info_on_age dove facevo la media raggruppando per eta
   elif a<=8.0:
      return "Medium stress level"
   else:
      return "High stress level"                             
                                 
df["stress_category"]=df["stress_level"].apply(stress_categorization)

raggruppa=df.groupby('stress_category')[[
    'daily_screen_time_hours',
    'sleep_duration_hours',
    'mental_health_score',
    'stress_level'
]].mean()

print(raggruppa)

import matplotlib.pyplot as plt

raggruppa.plot(kind='bar', figsize=(10,6))
plt.title('Media delle variabili per categoria di stress')
plt.xlabel('Categoria di stress')
plt.ylabel('Valore medio')
plt.xticks(rotation=15)
plt.tight_layout()
plt.show()
