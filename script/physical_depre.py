import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



df=pd.read_csv('C:/Users/nicola.paolucci/Desktop/progetti_github/tech_use_stress/data/Tech_Use_Stress_Wellness.csv')

fisica_depressione=df[["physical_activity_hours_per_week", "weekly_depression_score"]] 
print(fisica_depressione.head(10))

plt.figure(figsize=(8,6))
sns.regplot(
    x='physical_activity_hours_per_week',
    y='weekly_depression_score',
    data=fisica_depressione,
    scatter_kws={'color': 'red','alpha':0.6}
)
plt.xlabel('Ore di attività fisica settimanale')
plt.ylabel('Punteggio settimanale di depressione')
plt.title('Relazione tra attività fisica e depressione (con linea di tendenza)')
plt.grid(True)
plt.show()
