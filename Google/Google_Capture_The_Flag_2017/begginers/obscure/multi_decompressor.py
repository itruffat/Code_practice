import os
import sys
import zipfile
import tarfile
import shutil
import lzma
import bz2
import gzip

def get_files():
	cpath = os.getcwd()
	folder_files = next(os.walk(cpath))[2]
	return folder_files
	
def get_last_file(files):
	biggest = 0
	for cfile in files:
		name, _ = os.path.splitext(cfile)
		name = name[1:]
		if name.isdecimal() and int(name) > biggest:
			biggest = int(name)
	return biggest


class file_decompressor:
	def __init__(self):
		self.change_extention("")

	def change_extention(self,new_extention):
		self.file_extention = new_extention
		
		if self.file_extention == "":
			self.decompressor = None
		elif self.file_extention == ".zip":
			self.decompressor = self.unzip
		elif self.file_extention == ".xz":
			self.decompressor = self.unxz
		elif self.file_extention == ".bz2":
			self.decompressor = self.unbz2
		elif self.file_extention == ".gzip":
			self.decompressor = self.ungzip
		else:
			raise KeyError("No valid file format")
		
	def decompress_files(self):
		#Find newest file
		folder_files = get_files()
		biggest = get_last_file(folder_files)

		#Decompress that file
		file_name = "_{}{}".format(str(biggest), self.file_extention)
		self.decompressor(file_name)

		#Rename the decompressed file
		folder_files2 = get_files()
		new_file = [x for x in folder_files2 if x not in folder_files][0]
		new_name = "_{}{}".format(str(biggest+1), self.file_extention)
		print(new_name)
		os.rename(new_file, new_name)

	def unzip(self,file_name):
		zip_ref = zipfile.ZipFile(file_name, 'r')
		zip_ref.extractall(os.getcwd())
		zip_ref.close()

	def unxz(self,file_name):
		tar_ref = lzma.open(file_name)
		tar_ref_data = tar_ref.read()
		tar_ref.close() 
		extract = open("{}.extract".format(file_name), "wb")
		extract.write(tar_ref_data)
		extract.close()

	def unbz2(self,file_name):
		bz2_ref = bz2.open(file_name)
		bz2_ref_data = bz2_ref.read()
		bz2_ref.close() 
		extract = open("{}.extract".format(file_name), "wb")
		extract.write(bz2_ref_data)
		extract.close()

	def ungzip(self,file_name):
		gzip_ref = gzip.open(file_name)
		gzip_ref_data = gzip_ref.read()
		gzip_ref.close() 
		extract = open("{}.extract".format(file_name), "wb")
		extract.write(gzip_ref_data)
		extract.close()


def main(original_name):
	decompressor = file_decompressor()
	shutil.copyfile(original_name, "_0.zip")
	formats = [".zip",".xz",".bz2",".gzip",".gzip"]
	for n in range((len(formats)-1)):
		decompressor.change_extention(formats[n])
		while True:
			try:
				decompressor.decompress_files()
			except Exception as e:
				break
		biggest = get_last_file(get_files()) 
		if(os.path.exists("_{}{}".format(biggest, formats[n]))):
			shutil.copyfile("_{}{}".format(biggest, formats[n]), "_{}{}".format(biggest+1, formats[n+1]))


main("password.x.a.b.c.d.e.f.g.h.i.j.k.l.m.n.o.p.a.b.c.d.e.f.g.h.i.j.k.l.m.n.o.p.p.o.n.m.l.k.j.i.h.g.f.e.d.c.b.a.a.b.c.d.e.f.g.h.i.j.k.l.m.n.o.p")

