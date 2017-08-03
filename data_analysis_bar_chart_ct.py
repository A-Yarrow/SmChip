import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import argparse
import pylab
import sys
import seaborn as sns

def filter_data():
 
    filename = sys.argv[1]
    size = sys.argv[2]
    exclude = sys.argv[3]
    data_frame = pd.read_csv(filename, sep='\t')
    data_frame_subset = data_frame[['Sample', 'Assay', 'N', 'Total reps', 'Rejected', 'Ct', 'Ct SD']]
    PC_mask = ~data_frame_subset['Sample'].str.contains(exclude)
    filtered_data = data_frame_subset[PC_mask]
    #filtered_data['Ct'].replace('', 0) #Convert empty strings in failed runs to zero
    
    x = range(len(filtered_data.Ct))
    y = filtered_data.Ct
    std = filtered_data['Ct SD']
    print std
    
    sns.set(style="ticks", font_scale=float(size))
    g1 = sns.factorplot(x="Assay", y='Ct', hue="Sample", data=filtered_data,
                        size = 8, kind="bar", palette="muted")
    g1.set_xticklabels(rotation=90)
    plt.savefig(filename[0:-3]+'_+barplot_'+size+'_Ct.png')
    sns.plt.show()
	
	
filter_data()