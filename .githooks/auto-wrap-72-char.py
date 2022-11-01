#!/usr/bin/python
#
# Author: Sebastiano Barezzi <barezzisebastiano@gmail.com>
# Version: 1.0
#
# Autowraps commit messages to 72 characters + handles point prefixes
# using my commit style.
#

from argparse import ArgumentParser
from codecs import StreamReaderWriter, open
from pathlib import Path
from sys import stderr
from typing import List

POINT_PREFIXES = [
	'*',
	'-',
]

def wrap_text(message_file: StreamReaderWriter, max_width: int, linesep: str) -> str:
	new_commit_msg: List[str] = []

	first_line_found = False
	second_line_found = False
	# Going through all the lines in the commit message, one line at a time
	for lineno, line in enumerate(message_file):
		# Remove newline
		line = line.rstrip(linesep)

		# Skip comments
		if line.startswith("#"):
			continue

		if not first_line_found and line:
			# Don't wrap the first line
			first_line_found = True
			if len(line) > max_width:
				print(f"Warning: Commit summary is longer than {max_width} characters.",
				      file=stderr)
			new_commit_msg.append(line)
			continue
		elif not second_line_found:
			# Append a newline after the first line
			second_line_found = True
			new_commit_msg.append("")
			if not line:
				continue

		# If line is less than 72 characters, just add it to the new commit message
		if len(line) <= max_width:
			new_commit_msg.append(line)
			continue

		# We have to wrap this line
		new_line: List[str] = []

		# Check if the first part is a point prefix
		needs_padding = any(line.startswith(f"{prefix} ") for prefix in POINT_PREFIXES)

		# Get the first part of the line until we find a non-space character
		# This part will be kept in the new first line
		first_part = ""
		for char in line:
			if char.isspace():
				first_part += char
			else:
				break

		line_split = line[len(first_part):].split()
		if len(line_split) == 0:
			# There are only spaces in the line so append the spaces and go to the next line
			new_commit_msg.append(first_part)
			continue

		# Include the first word regardless of its length
		first_part += line_split.pop(0)
		new_line.append(first_part)

		if needs_padding and len(line_split) >= 1:
			# Include the second word regardless of its length
			new_line.append(line_split.pop(0))

		# Get the rest of the line
		for word in line_split:
			if len(" ".join(new_line)) + len(f" {word}") > max_width:
				new_commit_msg.append(" ".join(new_line))
				new_line.clear()
				if needs_padding:
					new_line.append(" ")

			new_line.append(word)

		new_commit_msg.append(" ".join(new_line))

	return linesep.join(new_commit_msg) + linesep

def main():
	parser = ArgumentParser(description="Wrap commit message to 72 characters")

	parser.add_argument("file", type=Path, help="Commit message file")
	parser.add_argument("-m", "--max-width", type=int, default=72,
	                    help="Maximum width of the commit message")
	parser.add_argument("-l", "--linesep", default='\n', help="Line separator")

	args = parser.parse_args()

	# Process original commit message
	with open(args.file, 'rb', encoding='utf-8') as f:
		formatted_commit_msg = wrap_text(f, args.max_width, args.linesep)

	# Write formatted commit message
	with open(args.file, 'wb', encoding='utf-8') as f:
		f.write(formatted_commit_msg)

if __name__ == '__main__':
	main()
