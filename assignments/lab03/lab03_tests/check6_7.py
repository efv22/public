#begin import modules
import math
from datascience import *
import numpy as np
# end import modules

#begin msg definitions
default_err_msg = "Something is wrong with your solution.  See if you can figure out what the mistake might be, or ask a neighbor or TA for help!"
type_err_msg = "Your solution is not in the correct format!"
correct_msg = "Your solution is correct!"
okay_msg = "The format of your solution looks okay!"
#end msg definitions


CorrectTable = """ MarketName                                       | city      | State    | y       | x
Caroline Farmers Market | Brooktondale  | New York  | 42.3809  | -76.3934
East Hill Plaza Farmers' Market  | Ithaca | New York | 42.4384 | -76.4664
Ithaca Farmers Market - DeWitt Park | Ithaca | New York | 42.4418  | -76.4988"""

###This function takes tables outlined in the check functions written by the Berkeley Team
###And turns them into datascience.table objects for easy comparison
def string_to_table(TableText):
	FinalTable = Table()
	lines = TableText.split('\n')
	columns = len(lines[0].split("|"))
	for x in range(0,columns):
		ColumnName = lines[0].split("|")[x].strip()
		ArrayForList = []
		for y in lines[1:]:
			z = y.split('|')
			ArrayForList.append(z[x].strip())
			#tupleForArray = tuple(ArrayForList)
		FinalTable = FinalTable.with_columns(ColumnName,np.array(ArrayForList))
	return FinalTable

def CheckTables(Table1,Table2,sortcol = 0,sort = True):
	if sort == True:
		Table1 = Table1.sort(sortcol)
		Table2 = Table2.sort(sortcol)
	ColumnLen = Table1.num_columns
	RowLen =Table1.num_rows
	if (Table1.num_columns == Table2.num_columns) & (Table1.num_rows == Table2.num_rows):
		FinalCheck = True
		for x in range(0,ColumnLen):
			StrArray1 = []
			StrArray2 = []
			for q in range(0,RowLen):
				try:
					StrArray1.append(float(Table1.column(x)[q]))
					StrArray2.append(float(Table2.column(x)[q]))
				except:
					StrArray1.append(str(Table1.column(x)[q].strip()))
					StrArray2.append(str(Table2.column(x)[q].strip()))
			StringArray1 = make_array(StrArray1)
			StringArray2 = make_array(StrArray2)
			try:
				ColumnCheck = np.allclose(StringArray1,StringArray2)
			except:
				ColumnCheck = np.array_equal(StringArray1,StringArray2)
			FinalCheck = FinalCheck & ColumnCheck
		return FinalCheck
	else:
		return False  

def check6_7(tompkins_markets):
	if isinstance(tompkins_markets,Table):
		StudentTable = tompkins_markets.sort(0).take(range(3))
		ATable = string_to_table(CorrectTable)
		if not (CheckTables(StudentTable,ATable,sortcol=0) or (tompkins_markets.num_rows==7)):
			print(default_err_msg)
		else:
			print(correct_msg)
	else:
		print(type_err_msg)
