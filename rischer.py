#!/bin/python

__author__ = "George Exarchakos"
__email__ = "g.exarchakos@tue.nl"
__version__ = "0.0.1"
__copyright__ = "Copyright 2014, The RICH Project"
#__credits__ = ["XYZ"]
#__maintainer__ = "XYZ"
#__license__ = "GPL"
#__status__ = "Production"

import getopt
import sys

from schedule.maestro import Scheduler

def usage():
	print('Command:\trischer.py [-h][-b[-v]]')
	print('Options:')
	print('\t-h,\t--help=\tthis usage message')
	print('\t-b,\t--LBR=\tIPv6 address of Low-Power and Lossy Network Border Router (port:5684 assumed)')
	print('\t-v,\t--visualizer=\tIPv4:port address of the graph visualizer server')

def main(arg_str):
	lbr = None
	visualizer = True

	try:
		if arg_str:
			opts, args = getopt.getopt(arg_str, "hb:v:", ["help", "LBR=", "visualizer="])
		else:
			opts, args = getopt.getopt(sys.argv[1:], "hb:v:", ["help", "LBR=", "visualizer="])
	except getopt.GetoptError as err:
		print(str(err))
		usage()
		return 2

	for o, a in opts:
		if o in ("-b", "--LBR"):
			lbr = a
		elif o in ("-v", "--visualizer"):
			visualizer = a
		elif o in ("-h", "--help"):
			usage()
			return
		else:
			usage()
			return 2

	if lbr is None:
		print("Border router IPv6 must be specified")
		usage()
		return 2

	sch = Scheduler('RICHNET', lbr, 5684, visualizer if visualizer else False)
	sch.start()
	return 0


if __name__ == '__main__':
	x = main(None)
	sys.exit(x)