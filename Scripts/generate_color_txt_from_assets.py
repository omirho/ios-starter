#!/usr/bin/env python

import os, json, argparse

def getHexFromFloatingRGBA(r, g, b, a):
    rgb = (r, g, b, a)
    hex_result = "".join([str(format(int(float(val) * 255.99999999), '02x')).upper() for val in rgb])
    return hex_result

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
                    colors[colorName] = getHexFromFloatingRGBA(rgb["red"], rgb["green"], rgb["blue"], rgb["alpha"])
    return colors

def generateLinesFromColors(colorsDict):
    lines = []
    for color, value in colorsDict.items():
        lines.append("%s : %s" % (color, value))
    return "\n".join(lines)

def writeLinesToFile(filePath, lines):
    f = open(filePath, 'w')
    f.write(lines)
    f.close()

def parseArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', required=True)
    parser.add_argument('-o', '--output')
    return parser.parse_args()

def getAbsolutePath(path):
    return os.path.abspath(os.path.expanduser(path))

def main():
    args = parseArgs()
    colors = {}
    colors = getColorsFromAssetFile(getAbsolutePath(args.input), colors)
    lines = generateLinesFromColors(colors)
    if args.output is not None:
        writeLinesToFile(getAbsolutePath(args.output), lines)
    else:
        print lines

if __name__ == "__main__":
    main()
