import os
import glob
import pandas as pd 

os.chdir("./All_data")



# Use glob to match the pattern ‘csv’
extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]

# Combine all files in the list
combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames])

# export as CSV
combined_csv.to_csv("combined_csv.csv", index=False)
