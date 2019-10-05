import matplotlib.pyplot as plt
import pandas as pd
import os

current_directory = os.getcwd()
def Plot(csv):

    df = pd.read_csv(csv, encoding='utf-8')
    cols = list(df.columns)
    cols[0:] = 'price', 'change', 'time'
    print(cols)
    df.columns = cols
    plt.plot(df["time"], df["price"], df["change"],'ro--')
    
    script_dir = os.path.dirname(__file__)
    results_dir = os.path.join(script_dir, 'TheScreenshots/')
    sample_file_name = "Quote.png"

    if not os.path.isdir(results_dir):
        os.makedirs(results_dir)

    plt.savefig(results_dir + sample_file_name)
    plt.show()
