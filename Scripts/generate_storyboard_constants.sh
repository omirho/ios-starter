#!/bin/sh

STORYBOARD_FOLDER_RELATIVE_PATH="./"
TARGET_STORYBOARD_FOLDER_PATH="${SRCROOT}/${PROJECT_NAME}/${STORYBOARD_FOLDER_RELATIVE_PATH}"
OUTPUT_STORYBOARD_PATH="${SRCROOT}/Generated/Constants/Storyboards.swift"

${SRCROOT}/Tools/swiftgen/bin/swiftgen storyboards -t swift4 $TARGET_STORYBOARD_FOLDER_PATH --param module=${PROJECT_NAME} --param ignoreTargetModule=true --output $OUTPUT_STORYBOARD_PATH
