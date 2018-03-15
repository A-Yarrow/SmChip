import pandas as pd
import matplotlib.pyplot as plt
import sys
import seaborn as sns
import argparse

def filter_data():
    parser = argparse.ArgumentParser(description='Visualize heatmap of ROX or other dye on SmartChip')
    parser.add_argument('-filename', '-f', required=True, help='input file is an exported well file from Wafergen qPCR software' )
    parser.add_argument('-exclude', '-exa', 
                        default=[], action = 'append',
                        help='Assays you do not want to include, usually negative controls.\
                              If assay has a space, surround it in quotes. Example: -ex \'serum albumin\'')
    parser.add_argument('-exclude_sample', '-exs',
                        default=[], action = 'append',
                        help='Samples you do not want to include. use -exs flag for each sample')
    parser.add_argument('-dye', '-d',
                        #default=[], action= 'append',
                        help='dye you want to visualize on chip map ie. Initial: VIC, End: VIC')
    
    args = parser.parse_args()
    sample_exclude_list = args.exclude_sample
    assay_exclude_list = args.exclude
    dye = args.dye
    filename = args.filename
    
    data_frame = pd.read_csv(filename, sep='\t', usecols = ['Row', 'Column', 'Assay', 'Sample', dye])
   
    for i in assay_exclude_list:
        exclude_mask = ~data_frame['Assay'].str.contains(i)
        data_frame = data_frame[exclude_mask]
        
    for i in sample_exclude_list:
        exclude_mask = ~data_frame['Sample'].str.contains(i)
        data_frame = data_frame[exclude_mask]
    data_frame['normalized'] = data_frame[dye].apply(lambda x: x/data_frame[dye].max()) #normalize the data
    return data_frame, filename, dye    
    #print data_frame
    
#filter_data()

def make_plots():
    data_frame, filename, dye = filter_data()
    data_frame.sort_values(by='Assay').to_csv(filename[0:-4]+'_'+'dye'+'.txt', sep='\t')
    df = data_frame[['Row', 'Column', dye]].sort('Row')
    print df
    print dye
    #df2 = pd.DataFrame(data_frame[dye], index= data_frame['Row'], columns=data_frame['Column'])
    #df2 = df2.fillna(0)
    
    #print df2
    
    #Make custom color map for all assays. Set scale for FAM, VIC and ROX
    vmin = None
    vmax = None
    if dye == 'Initial: ROX':
        vmin = 700
        vmax = 2600
    elif dye == 'Initial: VIC':
        vmin = 800
        vmax = 3200
    elif dye == 'Initial: FAM':
        vmin = 1500
        vmax = 9000
     
    plt.scatter(df['Column'], df['Row'], c = df[dye], cmap='bwr')#, vmin=vmin, vmax=vmax) #ROX: vmin = 2600, vmax = 700, VIC: vmin=800, vmax=3200, FAM: vmin=1500, vmax=9000)
    plt.xlim([-10, 80])
    plt.ylim([-10, 80])
    plt.colorbar()
    plt.title(filename[0:-4]+'_'+dye.replace(' ', '').replace(':', '_'))
    plt.gca().invert_yaxis()
    plt.savefig(filename+'_heatmap_'+dye.replace(' ', '').replace(':', '_')+'.png')
    sns.plt.show()

make_plots()
