#!/bin/sh

FONT_FOLDER_RELATIVE_PATH="./Resources/Fonts/"
TARGET_FONT_FOLDER_PATH="${SRCROOT}/${PROJECT_NAME}/${FONT_FOLDER_RELATIVE_PATH}"
OUTPUT_FONT_PATH="${SRCROOT}/Generated/Constants/Fonts.swift"

${SRCROOT}/Tools/swiftgen/bin/swiftgen fonts -t swift4 $TARGET_FONT_FOLDER_PATH --output $OUTPUT_FONT_PATH
