import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import pylab
import sys

def filter_data():
	filename = sys.argv[1]
	data_frame = pd.read_csv(filename, sep='\t')
	data_frame_subset = data_frame[['Sample', 'Assay', 'N', 'Total reps', 'Rejected', 'Ct', 'Ct SD']]
	PC_mask = ~data_frame_subset['Sample'].str.contains('NT')
	filtered_data = data_frame_subset[PC_mask]
	#filtered_data2 = filtered_data[~filtered_data['Sample'].str.contains('Z-Taq')]
	#filtered_data3 = filtered_data2[~filtered_data2['Sample'].str.contains('SpeedStar')]
	sorted_data = filtered_data.sort_values(['Rejected'], axis = 'index', ascending = [False])
	#joined_data = sorted_data.merge(assay_data, on=['Assay'], how='left')
	print sorted_data
	sorted_data.to_csv('sorted_rejects.txt', sep = '\t')
	
	
	cutoff = [7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
	for i in cutoff:
		mask = sorted_data['Rejected'] == i
		data2 = sorted_data[mask]['Assay'].value_counts()
		print 'number of rejects:',i,'\n', data2
	mask_3 = sorted_data['Rejected'] > 7
	data_3 = sorted_data[mask_3]['Assay'].value_counts()
	print data_3
	

	
#make_stacked_bar_chart()
filter_data()