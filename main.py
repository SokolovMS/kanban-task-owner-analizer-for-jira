import logging

import config
import scripts.analyze as analyze
import scripts.parser as parser
from scripts import download, files

logging.root.setLevel(logging.NOTSET)


def fetch_if_needed():
	if not config.do_fetch:
		return

	if config.clear_previous_fetch:
		files.clear_dir(config.issues_rest)
	else:
		files.clear_dir(config.issues_rest_not_final)

	download.fetch_issues()


def parse_if_needed():
	if not config.do_parse:
		return

	if config.clear_previous_parse:
		files.clear_dir(config.issues_parsed)

	parser.parse_everything()


def main():
	fetch_if_needed()
	parse_if_needed()

	analyze.gather_stats()


if __name__ == '__main__':
	main()
	logging.info("Done")
