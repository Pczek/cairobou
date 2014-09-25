#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import math
import cairo
import optparse
import logging


# globale variables
g_options = False # command line options
g_images = False # images to process

# constants
INCH = 72 # 72 pixels (p) = 1 inch (in)
MM = INCH / 25.4 # 25.4 milimeters (mm) = 1 in
CM = INCH / 2.54 # 2.54 centimetes (cm) = 1 in
A4_WIDTH, A4_HEIGHT = INCH * 8.3, INCH * 11.7 # DIN A4 Paper is 297mm heigh and 210mm wide

def main():
	# SetUp OptionParser
	usage = "usage: %prog [options] images*"
	parser = optparse.OptionParser(usage = usage)
	parser.add_option("-o", "--out", dest="out", type="string",
					help="specify output file", default="cairobou.pdf")

	parser.add_option("-v", "--verbose", action="store_true",
					help="print status messages to stdout", default=False)
	parser.add_option("-d", "--debug", action="store_true",
					help="print status and debug messages to stdout", default=False)
	global g_options
	global g_images
	(g_options, g_images) = parser.parse_args()

	# checking if enough images are specified
	if(len(g_images)<1):
		parser.error("At least one image has to be specified!")
		return 1

	# defining output
	if(g_options.debug):
		logging.basicConfig(format='%(message)s', level="DEBUG")
		# Printing Options for Debugging
		for option in parser.option_list:
			if(option.dest != None):
				logging.debug("%s = %s", option, getattr(g_options, option.dest))
		logging.debug("Processing %d image(s):", len(g_images))
		for image in g_images:
			logging.debug("\t%s",str(image))
	elif(g_options.verbose):
		logging.basicConfig(format='%(message)s', level="INFO")

	return 0

if __name__ == "__main__":
    sys.exit(main())
