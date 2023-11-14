# Frida-AI

Root Detection Scanner for Android Applications

Overview
This Python script is designed to help you identify potential security vulnerabilities related to root detection in Android applications. When executed, the script scans an APK file and prints out any source code lines within the application that implement root detection packages.

How to Use

Download the APK File:
Obtain the Android application (APK file) that you want to analyze for root detection.

Download the Script:
Download the provided Python script to your local machine.

Execute the Script:
Run the script, providing the path to the APK file as an input. The script will use jadx to decompile the APK and search for specified keywords related to root detection.

Review the Results:
The script will display the identified source code lines, along with the corresponding class names, where root detection packages are implemented.

Important Note
Ensure that the jadx tool is installed on your system before running the script. You can find jadx installation instructions on the GitHub repository.

Example Command
```
python Android_Scan.py
```
Replace apk_path with the path to your Android application and output_dir with the desired output directory for jadx.
