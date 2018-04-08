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

def plot_pie(df,output_file=""):
    """
    plot_pie takes a pandas data series and turns it into a pie chart
    - if the dataseries have a column header, this will become the graph title
    - if output_file is specificed, chart is written to a png file
    """
    #check input
    assert(isinstance(df,pd.core.series.Series))
    assert(isinstance(output_file,str))

    #configure plot
    df.plot.pie(autopct='%.1f%%', pctdistance=0.75)
    plt.xlabel('')
    plt.ylabel('')
    plt.title(df.name)
    plt.axis('equal')
    plt.legend(loc='best')

    #deliver plot
    if output_file:
        plt.savefig(output_file+".png")
    else:
        plt.show()
