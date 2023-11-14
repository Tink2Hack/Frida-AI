# Copyright (c) 2023, Sellva Manoj D S
# All rights reserved.
#
# This software is licensed under the MIT License.
# See LICENSE.txt for more details.

import zipfile
import os

def extract_ipa(ipa_path, extract_path):
    with zipfile.ZipFile(ipa_path, 'r') as zip_ref:
        zip_ref.extractall(extract_path)

def scan_for_constants(extract_path, constants):
    for root, dirs, files in os.walk(extract_path):
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, 'r', errors='ignore') as f:
                content = f.read()
                for constant in constants:
                    if constant in content:
                        print(f"Constant '{constant}' found in: {file_path}")

def main():
    # Replace with the path to your IPA file
    ipa_path = "your_IPA_file"

    # Replace with the path where you want to extract the contents
    extract_path = "your_directory_Path"

    # Constants to search for
    constants_to_find = [
        "/Applications/Cydia.app",
        "/Applications/FakeCarrier.app",
        "/Applications/Icy.app",
        "/Applications/IntelliScreen.app",
        "/Applications/MxTube.app",
        "/Applications/RockApp.app",
        "/Applications/SBSetttings.app",
        "/Applications/WinterBoard.app",
        "/Applications/blackra1n.app",
        "/Applications/Terminal.app",
        "/Applications/Pirni.app",
        "/Applications/iFile.app",
        "/Applications/iProtect.app",
        "/Applications/Backgrounder.app",
        "/Applications/biteSMS.app",
        "/Library/MobileSubstrate/DynamicLibraries/LiveClock.plist",
        "/Library/MobileSubstrate/DynamicLibraries/Veency.plist",
        "/Library/MobileSubstrate/DynamicLibraries/SBSettings.dylib",
        "/Library/MobileSubstrate/DynamicLibraries/SBSettings.plist",
        "/Library/MobileSubstrate/MobileSubstrate.dylib",
        "/System/Library/LaunchDaemons/com.ikey.bbot.plist",
        "/System/Library/LaunchDaemons/com.saurik.Cy@dia.Startup.plist",
        "/System/Library/LaunchDaemons/com.saurik.Cydia.Startup.plist",
        "/System/Library/LaunchDaemons/com.bigboss.sbsettingsd.plist",
        "/System/Library/PreferenceBundles/CydiaSettings.bundle",
        "/bin/bash",
        "/bin/sh",
        "/etc/apt",
        "/etc/ssh/sshd_config",
        "/etc/profile.d/terminal.sh",
        "/private/var/stash",
        "/private/var/tmp/cydia.log",
        "/private/var/lib/apt",
        "/private/var/root/Media/Cydia",
        "/private/var/lib/cydia",
        "/private/var/mobile/Library/SBSettings/Themes",
        "/private/var/lib/dpkg/info/cydia-sources.list",
        "/private/var/lib/dpkg/info/cydia.list",
        "/private/etc/profile.d/terminal.sh",
        "/usr/lib/libsubstitute.dylib",
        "/usr/lib/substrate",
        "/usr/lib/libhooker.dylib",
        "/usr/bin/cycript",
        "/usr/bin/ssh",
        "/usr/bin/sshd",
        "/usr/libexec/sftp-server",
        "/usr/libexec/ssh-keysign",
        "/usr/libexec/cydia",
        "/usr/sbin/sshd",
        "/var/cache/apt",
        "/var/lib/cydia",
        "/var/log/syslog",
        "/var/tmp/cydia.log",
        "/private/var/lib/apt"
    ]

    # Extract the IPA file
    extract_ipa(ipa_path, extract_path)

    # Scan for constants in the extracted files
    scan_for_constants(extract_path, constants_to_find)

if __name__ == "__main__":
    main()
