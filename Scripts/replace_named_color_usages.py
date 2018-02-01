#!/usr/bin/env python

import os, json, re, argparse

def getColorsFromAssetFile(filePath, colors):
    for root, dirs, files in os.walk(filePath):
        for dir in dirs:
            if dir.endswith(".colorset"):
                colorName = dir.split(".")[0]
            for file in files:
                if file == "Contents.json":
                    f = open(os.path.join(root, dir, file))
                    jd = json.load(f)
                    rgb = jd["colors"][0]["color"]["components"]
                    colors[colorName] = 'red="{}" green="{}" blue="{}" alpha="{}" colorSpace="calibratedRGB"'.format(rgb["red"], rgb["green"], rgb["blue"], rgb["alpha"])
    return colors

def replaceNamedColorsToRGBInPath(filePath, colors):
	for root, dirs, files in os.walk(filePath):
	    for file in files:
	        if file.endswith((".storyboard", ".xib")):
	            path = os.path.join(root, file)
	            backupPath = path + ".bak"
	            f = open(path)
	            nf = f.read()
	            f.close()

	            bf = open(backupPath, 'w+')
	            bf.write(nf)
	            bf.close()

	            nf = re.sub(r" +<namedColor name=.*\n.*\n +</namedColor>\n", '', nf)
	            nf = re.sub(r" +<capability name=\"Named colors\" minToolsVersion=\".*\n", '', nf)

	            for k, v in colors.items():
	                nf = re.sub(r'name="{}"'.format(k), v, nf)

	            f = open(path, 'w')
	            f.write(nf)
	            f.close()

def parseArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--colorsFile', required=True)
    parser.add_argument('-r', '--replaceDirectory', required=True)
    return parser.parse_args()

def getAbsolutePath(path):
    return os.path.abspath(os.path.expanduser(path))

def main():
	args = parseArgs()
	colors = {}
	colors = getColorsFromAssetFile(getAbsolutePath(args.colorsFile), colors)
	replaceNamedColorsToRGBInPath(getAbsolutePath(args.replaceDirectory), colors)

if __name__ == "__main__":
	main()

