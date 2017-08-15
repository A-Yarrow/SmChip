import pandas as pd
import matplotlib.pyplot as plt
import sys
import seaborn as sns
import argparse

def filter_data():
    parser = argparse.ArgumentParser(description='visualize bad wells on SmartChip')
    parser.add_argument('-filename', '-f', required=True, help='input file is an exported well file from Wafergen qPCR software' )
    parser.add_argument('-exclude', '-ex', 
                        default=[], action = 'append',
                        help='delimited list of assays you do not want to include, usually negative controls.\
                              If assay has a space, surround it in quotes. Example: -ex \'serum albumin\'')
    args = parser.parse_args()
    filename = args.filename
    data_frame = pd.read_csv(filename, sep='\t', usecols = ['Row', 'Column', 'Assay', 'Sample', 'Ct'])
    print data_frame.head
    mask = pd.isnull(data_frame['Ct'])
    bad_wells = data_frame[mask] 
    
    #filter out negative control assays
    exclude_list = args.exclude
    #print exclude_list
    #exclude_list = [i for i in exclude.split(',')]
    
    for i in exclude_list:
        exclude_mask = ~data_frame['Assay'].str.contains(i)
        bad_wells = bad_wells[exclude_mask]
        bad_wells_filled = bad_wells.fillna(1)
    
    print bad_wells_filled
    g = sns.FacetGrid(bad_wells_filled, col='Assay', hue='Assay', col_wrap=4,
                      xlim=(-2,79), ylim=(-2,79), size=3)
    g = (g.map(plt.scatter, 'Column', 'Row')).add_legend()
    plt.savefig(filename+'_scatterplot.png')
    #axes = g.axes
    g2 = sns.pairplot(bad_wells_filled, kind='scatter', x_vars='Column',
                      y_vars='Row', hue='Assay', size =5, aspect=1 )
    plt.savefig(filename+'_scatterplot_sharex.png')
    sns.plt.show()
    


filter_data()
    
