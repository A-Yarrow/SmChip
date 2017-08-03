import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm
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
	#return filtered_data
	#return data_frame_subset
    print data_frame_subset['Assay']
    sns.set(style="ticks", font_scale=float(size))
    g1 = sns.factorplot(x="Assay", y="N", hue="Sample", data=filtered_data,
                   size=8, kind="bar", palette="muted")
    g1.set_xticklabels(rotation=90)
    g1.despine(left=True)
    plt.savefig(filename[0:-4]+'_calls_barplot_'+size+'_.png')
    sns.plt.show()
	
	
filter_data()

"""
def main():
	filename = sys.argv[1]
	filtered_data = filter_data(filename)
	table = pd.pivot_table(filtered_data, index = ['Sample'], columns = ['Assay'], values= ['N'])
	my_colors = ['#b3b3ff', '#99ebff', '#c2d6d6', '#9fdf9f', '#ffffb3', '#d6d6c2', '#ffd480', '#ffbf80',
				 '#80ffff', '#4d4dff', '#ff99ff', '#bfff80', '#cccccc', '#99ffcc', '#b3ccff', '#6666ff',]
	

	
	
	
	
	fig1 = plt.figure()
	ax = table.plot(kind='bar', color=my_colors)
	plt.legend(loc ='right', bbox_to_anchor=(1.0, 0.625))
	fig1.set_size_inches(7, 3)
	fig1.savefig('x1', dpi=300)
	plt.show()
	
	
#make bar_chart()
if __name__ == "__main__":
    main()
"""