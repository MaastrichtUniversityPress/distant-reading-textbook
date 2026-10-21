# script to merge multiple txt files for data analysis

## put this script into the folder with your input files
## open it in Jupyter notebook to execute

## define a list of filenames you want to merge
## you can add as many filenames as you like

filenames = ['file1.txt',
             'file2.txt',
             'file3.txt]

## adjust the output file name below and iterate through files
             
with open('my_merged_files.txt', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)

## close file and print notification when done

close(outfile)
print("Done!")
