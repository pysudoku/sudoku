class FileFormatError(Exception):
	def __init__(self, extension):
		super().__init__("Invalid file format. '{}' file expected.".format(extension))
		