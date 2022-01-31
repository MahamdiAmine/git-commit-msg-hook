#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import re
import subprocess

_COMMIT_END = "# ------------------------ >8 ------------------------"
_ROLES = """
	# That was close. You almost spoiled the eternal git log!
	#
	# Please follow these rules:
	#
	# SEVEN RULES FOR A GREAT COMMIT MESSAGE
	# ======================================
	# 1. Separate subject from body with a blank line
	# 2. Limit the subject line to 50 characters
	# 3. Capitalize the subject line
	# 4. Do not end the subject line with a period
	# 5. Use the imperative mood in the subject line
	# 6. Wrap the body at 72 characters
	# 7. Use the body to explain what and why vs. how
	☝️️☝️️
"""

def check_commit_message():
	"""
	read sys args and check commit messages
	"""
	# check if it's a smeetz repository to enforce few internel commit messages
	is_smeetz = is_smeetz_repository()

	with open(sys.argv[1], "r") as fp:
		lines = fp.readlines()

		for idx, line in enumerate(lines):
			# we reached the end commit 
			if line.strip() == _COMMIT_END:
				break

			# skip comments
			if line[0] == "#":
				continue

			# force git commit styles, check this link for more details https://cbea.ms/git-commit/
			if not _is_valid_line(idx, line, is_smeetz=is_smeetz):
				print(_ROLES)
				print(" you idiot😕, Can't you just write a propre git commit🤦.")
				if is_smeetz:
					print("check Smeetz roles has to be applied as well")
				sys.exit(1)
	print("✔ Good job! commit is good 👏 👏 👏 👏 ")
	sys.exit(0)


def _is_valid_line(idx, line, is_smeetz):
	"""
	first line should start with Capital letter, no endpoint
	second line has to be a blank line
	other lines has to be wrapped at 72 characters
	plus other checks depending on the repository type (work, personal)
	"""

	if idx == 0:
        # automatic merge commit
		if 'Merge branch ' in line:
			return True

		if not re.match("^[A-Z].{,48}[0-9A-z \t]$", line):
			return False

		# if it's Smeetz repo, it has to start with the ticket's ID 🤷
		if is_smeetz:
			return re.match(r"^(BUD|IBO)-\d{3}", line)
		return True

	elif idx == 1:
		return len(line.strip()) == 0

	return len(line.strip()) <= 72


def is_smeetz_repository():
	"""
	check if it's a smeetz repository
	"""
	try:
		remotes = subprocess.run(['git', 'remote', '-v'], stdout=subprocess.PIPE)
		return "smeetz" in remotes.stdout.decode('utf-8')
	except:
		return False

if __name__ == "__main__":
	check_commit_message()
