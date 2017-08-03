import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import argparse
import pylab
import sys
import seaborn as sns

def filter_data():
    filename = sys.argv[1]
    filename2 = sys.argv[2]
    size = sys.argv[3]
    names = ['Row', 'Column', 'flour']
    cycles = [i+1 for i in range(40)]
    col_header_list = names + cycles
    data_frame = pd.read_csv(filename, header=None, names = col_header_list, delim_whitespace=True)
    data_frame2 = pd.read_csv(filename2, skiprows=1, header=0, usecols = [0, 1, 2, 3],
                              names = ['Row', 'Column', 'Assay', 'Sample'], sep='\t')
    print data_frame2.shape
    print data_frame.shape
    merged_df = data_frame2.merge(data_frame, on=['Row', 'Column'])
    #merged_df.sort_values("Assay")
    print merged_df.head()
    
    sns.set(style="ticks", font_scale=float(size))
    g1 = sns.factorplot(x="Assay", y=10, hue="Sample", data=merged_df,
                        size = 8, kind="box", palette="muted")
    g1.set_xticklabels(rotation=90)
    
    
    
    #g = sns.FacetGrid(merged_df, col = "Sample", sharex=True) #gridspec_kws={"width_ratios": [5, 3, 3]})
    #g.map(sns.boxplot, 'Assay', 10)
    #g.set_xticklabels(rotation=90)
    plt.savefig(filename[0:-4]+'_+boxplot.png')
    sns.plt.show()
    
    
filter_data()