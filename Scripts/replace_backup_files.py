#!/usr/bin/env python

import os, argparse

def replaceBackupFiles(filePath):
	for root, dirs, files in os.walk(filePath):
	    for file in files:
	        if file.endswith(".bak"):
	            backupPath = os.path.join(root, file)
	            path = backupPath[:-4]

	            bf = open(backupPath)
	            nf = bf.read()
	            bf.close()

	            f = open(path, 'w')
	            f.write(nf)
	            f.close()

	            os.remove(backupPath)

def parseArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument('-r', '--replaceDirectory', required=True)
    return parser.parse_args()

def getAbsolutePath(path):
    return os.path.abspath(os.path.expanduser(path))

def main():
	args = parseArgs()
	replaceBackupFiles(getAbsolutePath(args.replaceDirectory))

if __name__ == "__main__":
	main()
