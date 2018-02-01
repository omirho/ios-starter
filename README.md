# ios-starter
A starter project for ios to set up a build process for multiple target apps(white-labeling), handling string constants and more.

# Requirements
* Xcode 9 and above
* python (required for scripts)

# How to run
```
1. Clone repo
2. cd ios-starter
3. pod install
4. Open 'ios-starter.xcworkspace' with Xcode and build/run.
```

# How does it work
[WIP]

# Assumptions
The project and scripts make certain assumptions about the folder structure and project properties. They are listed as below:
* The project name and the main target folder name should be the same. (Used in the scripts)
* Every new target has a new folder (named as "target_name") in the root source directory. (Used in the scripts)
* The folder structure for the "Resources" and "Config" folder remain the same across target folders. (Used in the scripts)


# Small Todos
* ignore generated file changes in source tree
