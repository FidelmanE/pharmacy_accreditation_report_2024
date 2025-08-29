import pandas as pd
from google.colab import drive
drive.mount('/content/drive/')
drive.mount("/content/drive/", force_remount=True)
!ls
PrintMARC = pd.read_table('/content/drive/<Insert Filepath>/PrintPharmacy202405.txt', header=0, delimiter='\t', low_memory=False, encoding = 'ISO-8859-1')
list(PrintMARC.columns.values)