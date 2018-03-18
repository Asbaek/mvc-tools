import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

def plot_heatmap(df,total_rows,figure_output_file):
    fontsize=18
    rc={'font.size': fontsize, 'axes.labelsize': fontsize, 'legend.fontsize': fontsize,
    'axes.titlesize': fontsize, 'xtick.labelsize': fontsize, 'ytick.labelsize': fontsize}
    sns.set(rc=rc)
    fig = plt.figure()
    ax1 = fig.add_axes([0.8,0.0,0.20,0.8])
    ax = sns.heatmap(df,annot=True, linewidths=2.0,fmt="g",ax=ax1,cbar=False)
    for t in ax.texts:
        current_text = t.get_text()
        t.set_text(current_text+" ({0:.1f} %)".format(int(current_text)/total_rows*100))
    plt.yticks(rotation=0)
    ax.xaxis.tick_top()
    ax.xaxis.set_label_position('top')
    plt.savefig(figure_output_file)
    #plt.show()
