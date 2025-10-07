import pandas as pd
import matplotlib.pyplot as plt


df=pd.read_csv('C:/Users/nicola.paolucci/Desktop/progetti_github/tech_use_stress/data/Tech_Use_Stress_Wellness.csv')

ore_ansia= df[['daily_screen_time_hours','weekly_anxiety_score']] #creo un dataframe con le colonne che mi interessano, ossia ore di telefono e score settimanael
print(ore_ansia) 

plt.figure(figsize=(8,6)) 
plt.scatter(ore_ansia['daily_screen_time_hours'], ore_ansia['weekly_anxiety_score'], alpha=0.6) #grafico scatter
plt.xlabel('Ore di uso degli schermi')
plt.ylabel('Punteggio settimanale di ansia')
plt.title('Relazione tra screen time e ansia')
plt.grid(True)
plt.show()