Collection of scripts for visualizing  WgnSmChip high throughput qPCR data
The seaborn module must be installed before running

data_analysis_bar_chart_ct.py
plots CT values in groups for each assay.
Usage: Python data_analysis_bar_chart_ct.py arg1 arg2 arg3
arg1 = filename
arg2 = size of plot
arg3 = keyword in data to be excluded if any.

bad_wells.py
Takes an exported wells file as input. Maps the non-calls to a scatter plot.
Usage: Python bad_wells.py -f <filename> -ex <Sample names to exclude from analysis>
       You can enter as many sample names to exclude as you like by repeating the -ex flag
  example: python bad_wells.py -f wells.txt -ex dumb_assay1 -ex dumb_assay2
