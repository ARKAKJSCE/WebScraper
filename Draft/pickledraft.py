import matplotlib.pyplot as plt
import pandas as pd
import pathlib
import os

df = pd.read_csv('2Apple.csv')
cols = list(df.columns)
cols[0:] = 'price', 'change', 'time'
print(cols)
df.columns = cols
plt.plot(df["time"], df["price"], df["change"],'ro--')


new_dir = pathlib.Path('C:/Users/Dell/Desktop/Python Projects/Python internship/Scraping', 'ThePicsFolder')
new_dir.mkdir(parents=True, exist_ok=True)
new_file = new_dir / 'howdy.png'
os.chdir(r"C:\\Users\\Dell\\Desktop\\Python Projects\\Python internship\\Scraping\\ThePicsFolder") 
plt.savefig('howdy.png')
os.chdir(r"C:\\Users\\Dell\\Desktop\\Python Projects\\Python internship\\Scraping") 

plt.show()


# fig_handle = plt.plot(df["time"], df["price"], df["change"],'ro--')
# with open('sinus.pickle', 'wb') as f: # should be 'wb' rather than 'w'
#     pickle.dump(fig_handle, f) 
# fig_handle = pickle.load(open('sinus.pickle','rb'))
# for a in fig_handle : 
#     a.show()