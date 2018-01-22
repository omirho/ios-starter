#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, json

print os.getcwd()

colorDict = {}

# read all colorset
for root, dirs, files in os.walk("./"):
    for d in dirs:
        if d.endswith(".colorset"):
            colorK = d.split(".")[0]
            print "found " + colorK
            for file in files:
                if file == "Contents.json":
                    f = open(os.path.join(root, d, file))
                    jd = json.load(f)
                    rgb = jd["colors"][0]["color"]["components"]
                    colorDict[colorK] = 'red="{}" green="{}" blue="{}" alpha="{}" colorSpace="calibratedRGB"'.format(rgb["red"], rgb["green"], rgb["blue"], rgb["alpha"])

print ""
import re

# replacing
for root, dirs, files in os.walk("./"):
    for file in files:
        if file.endswith((".storyboard", ".xib")):
            path = os.path.join(root, file)
            print "Replacing namedColor in " + path
            f = open(path)
            nf = f.read()
            f.close()

            nf = re.sub(r" +<namedColor name=.*\n.*\n +</namedColor>\n", '', nf)
            nf = re.sub(r" +<capability name=\"Named colors\" minToolsVersion=\".*\n", '', nf)

            for k, v in colorDict.items():
                nf = re.sub(r'name="{}"'.format(k), v, nf)

            f = open(path, 'w')
            f.write(nf)
            f.close()

# Usage:
# if [ "${CONFIGURATION}" = "Release" ]; then
#    python NamedColors2RGB.py
#fi

