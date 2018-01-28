#!/bin/sh

COLOR_FILE_RELATIVE_PATH = ./Resources/Colors/Colors.xcassets
BASE_COLOR_FILE_PATH = ${SRCROOT}/${PROJECT_NAME}/${COLOR_FILE_RELATIVE_PATH}
TARGET_COLOR_FILE_PATH = ${SRCROOT}/${TARGET_NAME}/${COLOR_FILE_RELATIVE_PATH}
COLOR_TXT_PATH = ${SRCROOT}/${TARGET_NAME}/build/colors.txt
OUTPUT_COLOR_PATH = ${SRCROOT}/Generated/Constants/Colors.swift

if [ ! -f TARGET_COLOR_FILE_PATH ]; then
	TARGET_COLOR_FILE_PATH = BASE_COLOR_FILE_PATH
fi

# Generate txt file from assets file
${SRCROOT}/Scripts/generate_color_txt_from_assets.py -i ${TARGET_COLOR_FILE_PATH} -o ${COLOR_TXT_PATH}

# Generate constants from txt file
${SRCROOT}/Tools/swiftgen/bin/swiftgen colors -t swift4 ${COLOR_TXT_PATH} --output ${OUTPUT_COLOR_PATH}
