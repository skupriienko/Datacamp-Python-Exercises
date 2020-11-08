import os
import glob
import pandas as pd

folder = 'e:\src\data\Summer Olympic medals\Summer Olympic medals'
os.chdir(folder)
extension = 'csv'
#You can use csv as well

all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
combined_csv = pd.concat([pd.read_csv(f, encoding="utf-8", keep_default_na=False) for f in all_filenames])