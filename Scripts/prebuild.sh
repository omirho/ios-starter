set -e

mkdir -p ${SRCROOT}/Generated/Constants

SCRIPTS_PATH="${SRCROOT}/Scripts"

${SCRIPTS_PATH}/generate_image_constants.sh
${SCRIPTS_PATH}/generate_appkeys.sh
${SCRIPTS_PATH}/generate_color_constants.sh
${SCRIPTS_PATH}/generate_font_constants.sh
${SCRIPTS_PATH}/generate_localization_constants.sh
${SCRIPTS_PATH}/generate_storyboard_constants.sh

if [ "${CONFIGURATION}" != "Release" ]; then
	exit 0
fi

COLOR_FILE_RELATIVE_PATH="./Resources/Colors/Colors.xcassets"
BASE_COLOR_FILE_PATH="${SRCROOT}/${PROJECT_NAME}/${COLOR_FILE_RELATIVE_PATH}"
TARGET_COLOR_FILE_PATH="${SRCROOT}/${TARGET_NAME}/${COLOR_FILE_RELATIVE_PATH}"

if [ ! -f $TARGET_COLOR_FILE_PATH ]; then
    TARGET_COLOR_FILE_PATH=$BASE_COLOR_FILE_PATH
fi

${SCRIPTS_PATH}/replace_named_color_usages.py -c ${TARGET_COLOR_FILE_PATH} -r ${SRCROOT}/${PROJECT_NAME}
