import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv('C:/Users/nicola.paolucci/Desktop/progetti_github/tech_use_stress/data/Tech_Use_Stress_Wellness.csv')


# creiamo categorie per età
conditions = [
    (df['age'] < 26),
    (df['age'] >= 26) & (df['age'] < 50),
    (df['age'] >= 50)
]

choices = ['giovane', 'adulto', 'anziano']

 #mi sono aiutato con AI, volevo ricreare una Case when con Python per cui le età fossero suddivise con testo
df['age_category'] = np.select(conditions, choices, default='non definito')

#qui faccio la media di queste colonne raggruppando per categoria di età
age_grouped = df.groupby('age_category')[[
    'daily_screen_time_hours',
    'sleep_duration_hours',
    'mental_health_score',
    'stress_level'
]].mean()

print(age_grouped)

age_grouped.plot(kind='bar', figsize=(10,6))
plt.title('Media di variabili per categoria di età')
plt.xlabel('Categoria di età')
plt.ylabel('Valore medio')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()



#voglio provare a fare una funzione tipo case when 

# def eta_esplicita(x):
#     if x<=26:
#         return "Giovane"
#     elif x<=50:
#         return "Adulto"
#     else:
#         return "Anziano"
    
# df["age_cat"]=df['age'].apply(eta_esplicita)