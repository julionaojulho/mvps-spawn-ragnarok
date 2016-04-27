import pickle
import csv
from models.Mvp import Mvp

mvps_dict = {}
with open('resources/mvps.csv','r') as mvps_csv:
	mvps_read = csv.reader(mvps_csv,delimiter=',')
	for row in mvps_read:
		mvps_dict[(row[0],row[1])] = Mvp(row[0],int(row[2].split('~')[0])
                                        ,row[1])
with open('mvps.db','wb') as handle:
    pickle.dump(mvps_dict, handle)
