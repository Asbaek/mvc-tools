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
        
        
def plot_stack_hist(df,output_file=""):
    """
    df must contain dataframe with the following characteristics:
    - Indexes must be dates
    - Each column is a dataset with integers
    - The values must be mutually exclusive (adding them must give the total)
    - The column name is the label
    - The column named "target" will be plottet as a line if it exist
    output_file will provide name of the png with the graph
    output_file will show graph if not specified
    """
    assert(isinstance(df,pd.core.frame.DataFrame))
    assert(isinstance(output_file,str))
    df.plot.bar(stacked=True)
    plt.show()
    
    
# Data
df = pd.DataFrame({
'col0': ['title1','title2','title3'],
'col1': [1,2,4],
'col2': [2,3,1],
})
df = df.set_index('col0')


#Views
def polar_plot(df,title):
    """Plots spiderweb or radar plot, based on dataframe
       Dataframe must contain the following:
        col0    col1    col2    col3    col4
        title1  x11     x12     x13     x14
        title2  x21     x22     x23     x24
        ...
        each var, will be a corner in the web
        each category, will be set of similar colored dots inside the web.
    """

    # Create coordinate system
    N=len(df)
    ticks = [n/float(N)*2*pi for n in range(N)]
    ticks = np.append(ticks,ticks[0]) #complete the circle
    ax = plt.subplot(111,polar=True)
    ax.set_theta_offset(pi/2)
    ax.set_theta_direction(-1)
    plt.xticks(ticks,list(df.index.values))
    ax.set_rlabel_position(0)
    plt.yticks([1,2,3,4,5], ["1","2","3","4","5"], color="grey", size=7)
    plt.ylim(0,5)
    for column in list(df):
        values = df[column].values
        values = np.append(values,values[0]) #complete the circle
        ax.plot(ticks,values,linewidth=1, linestyle='solid',label=column)
        ax.fill(ticks,values,alpha = 0.25)
    plt.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))
    plt.title(title,fontdict={'fontsize':24})
    plt.show()


def stacked_bars(df,title):
    """ plots stacked bar chart based on dataframe.
        Dataframe must contain the following
        col0    col1    col2    col3    col4
        title1  x11     x12     x13     x14
        title2  x21     x22     x23     x24
        ...
        each var, will be a column in the bar plot
        each bar, will contain the categories stacked 
    """
    df.plot.bar(stacked=True)
    plt.title(title,fontdict={'fontsize':24})
    plt.show()

