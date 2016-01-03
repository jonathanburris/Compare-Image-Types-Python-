#!/usr/bin/python

import os
import sys
import urllib
import imghdr
import shutil

extensions = ['.gif', '.jpg']
created_files = []
search_directory = sys.argv[1]

def main():
	print extensions

	for filename in os.listdir(search_directory):
		filepath = os.path.join(search_directory, filename)
		if os.path.isdir(filepath):
			continue

		filename_without_extension, extension = os.path.splitext(filepath)
		if extension in extensions:
			url = urllib.pathname2url(filepath)
			image_type = imghdr.what(filename)
			print filename, extension, image_type

			if image_type != extension[1:]:
				new_filename = filename_without_extension + '.' + image_type
				shutil.copy(filename, new_filename)
				created_files.append(new_filename)

	print 'Created', len(created_files), 'files:'
	print created_files

if __name__ == '__main__':
	main()
