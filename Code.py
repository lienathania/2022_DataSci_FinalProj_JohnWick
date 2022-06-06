import pandas as pd
import csv
import matplotlib.pyplot as plt

print("\n")
print("Hello World")

df = pd.read_csv ('JohnWick.csv')

eachMovieKills = df['Movie'].value_counts(sort = False)
print(eachMovieKills)
eachMovieKills.plot.bar(rot = -9)
plt.show()

weaponsUsed = df['Weapon'].value_counts()
print(weaponsUsed)
weaponsUsed.plot.bar(rot = -45)
plt.show()

perMovieWeapon = df.groupby(['Movie','Weapon']).size()
print(perMovieWeapon)

peopleKill = df['Who'].value_counts()
print(peopleKill)
peopleKill.plot.pie(autopct="%1.1f%%",textprops={'fontsize': 16},title=' ')
plt.show()


