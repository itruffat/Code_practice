import os
import zipfile

def unzip(file_name):
		zip_ref = zipfile.ZipFile(file_name, 'r')
		zip_ref.extractall(os.getcwd())
		zip_ref.close()

def filter_binary(file_name, data_filter):
		with open(file_name, "rb") as file_ref:
			file_ref_data = file_ref.read()
		with  open("{}.filtered".format(file_name), "wb") as  filtered_data:
			filtered_data.write(data_filter(file_ref_data))

def skip_everything_before_40_nulls(data):
	zero_count = 0
	for x in range(len(data)):
		if data[x] == 0:
			zero_count += 1
		elif zero_count < 40:
			zero_count = 0
		else:
			break
	return data[x:]		
		
filter_binary("foo.ico", skip_everything_before_40_nulls)
unzip("foo.ico.filtered")

