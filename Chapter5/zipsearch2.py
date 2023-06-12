from Chapter5.zipprocessor import ZipProcessor


class ZipReplace(ZipProcessor):
	def __init__(self, filename, search_string, replace_string):
		super().__init__(filename)
		self.search_string = search_string
		self.replace_string = replace_string

	def process_files(self):
		"""perform a search and replace on all files in the temporary directory"""
		for filename in self.temp_directory.iterdir():
			with filename.open() as file:
				contents = file.read()
			contents = contents.replace(self.search_string, self.replace_string)
			with filename.open("w") as file:
				file.write(contents)
