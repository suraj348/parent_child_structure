import pandas as pd
import json

#==============================================================================
def get_unique_name(df):
	unique= df.unique()
	unique = [r for r in unique if r!='']
	return unique

#==============================================================================
def get_nestDetails(df,ind):
	list_ = []
	unique_name = get_unique_name(df[ind])
	unique_id = get_unique_name(df[ind+1])
	unique_link = get_unique_name(df[ind+2])

	for index,data in enumerate(unique_name):
		df_temp = df[df[ind]==data]
		
		childrLst=[]
		if len(df_temp.columns) > ind+3:
			childrLst = get_nestDetails(df_temp,ind+3)
		list_.append({
			"lable":data,
			"id":unique_id[index],
			"link":unique_link[index],
			"children":childrLst
		})

	return list_

#==============================================================================
def main(file_name):

	df = pd.read_csv(file_name,header = None,skiprows=1)
	df = df.fillna('')

	final_data = []
	unique_base_url = get_unique_name(df[0])

	for base_url in unique_base_url:
		df_temp = df[df[0]==base_url]

		childrens = get_nestDetails(df_temp,1)

		final_data.append({
				"base_url":base_url,
				"children":childrens
			})
	return json.dumps(final_data)

#==============================================================================
final_data = main('data.csv')
print(final_data)
