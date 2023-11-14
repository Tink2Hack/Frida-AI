# Copyright (c) 2023, Sellva Manoj D S
# All rights reserved.
#
# This software is licensed under the MIT License.
# See LICENSE.txt for more details.

import os
import subprocess
import re
from termcolor import colored

def decompile_apk(apk_path, output_dir):
    subprocess.run(['jadx', '-d', output_dir, apk_path], check=True)

def mask_package_names(text):
    # Basic masking for privacy reasons
    masked_text = text
    for keyword in keywords_to_find:
        masked_text = masked_text.replace(keyword, '*' * len(keyword))
    return masked_text

def search_keywords(directory, keywords):
    keyword_matches = {}

    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, 'r', errors='ignore') as f:
                lines = f.readlines()
                current_class = None

                for line_number, line in enumerate(lines, start=1):
                    if line.strip().startswith("public class") or line.strip().startswith("class"):
                        current_class = re.search(r'\bclass\s+(\w+)', line)
                        if current_class:
                            current_class = current_class.group(1)

                    for keyword in keywords:
                        if current_class and re.search(r'\b{}\b'.format(re.escape(keyword)), line):
                            if file_path not in keyword_matches:
                                keyword_matches[file_path] = []
                            masked_line = mask_package_names(line)
                            keyword_matches[file_path].append((current_class, line_number, masked_line))

    return keyword_matches

def prompt_user():
    apk_path = input("Enter the path to the APK file: ")
    output_dir = input("Enter the output directory for decompilation: ")
    return apk_path, output_dir

def main():
    global keywords_to_find  # Make keywords_to_find global for access in other functions
    apk_path, output_dir = prompt_user()

    keywords_to_find = [
        'busybox',
        'su',
        'com.noshufou.android.su',
        'com.noshufou.android.su.elite',
        'eu.chainfire.supersu',
        'com.koushikdutta.superuser',
        'com.thirdparty.superuser',
        'com.yellowes.su',
        'com.topjohnwu.magisk',
        'com.kingroot.kinguser',
        'com.kingo.root',
        'com.smedialink.oneclickroot',
        'com.zhiqupk.root.global',
        'com.alephzain.framaroot',
        'com.koushikdutta.rommanager',
        'com.koushikdutta.rommanager.license',
        'com.dimonvideo.luckypatcher',
        'com.chelpus.lackypatch',
        'com.ramdroid.appquarantine',
        'com.ramdroid.appquarantinepro',
        'com.android.vending.billing.InAppBillingService.COIN',
        'com.android.vending.billing.InAppBillingService.LUCK',
        'com.chelpus.luckypatcher',
        'com.blackmartalpha',
        'org.blackmart.market',
        'com.allinone.free',
        'com.repodroid.app',
        'org.creeplays.hack',
        'com.baseappfull.fwd',
        'com.zmapp',
        'com.dv.marketmod.installer',
        'org.mobilism.android',
        'com.android.wp.net.log',
        'com.android.camera.update',
        'cc.madkite.freedom',
        'com.solohsu.android.edxp.manager',
        'org.meowcat.edxposed.manager',
        'com.xmodgame',
        'com.cih.game_cih',
        'com.charles.lpoqasert',
        'catch_.me_.if_.you_.can_',
        'com.devadvance.rootcloak',
        'com.devadvance.rootcloakplus',
        'de.robv.android.xposed.installer',
        'com.saurik.substrate',
        'com.zachspong.temprootremovejb',
        'com.amphoras.hidemyroot',
        'com.amphoras.hidemyrootadfree',
        'com.formyhm.hiderootPremium',
        'com.formyhm.hideroot',
        '/data/local/',
        '/data/local/bin/',
        '/data/local/xbin/',
        '/sbin/',
        '/su/bin/',
        '/system/bin/',
        '/system/bin/.ext/',
        '/system/bin/failsafe/',
        '/system/sd/xbin/',
        '/system/usr/we-need-root/',
        '/system/xbin/',
        '/cache/',
        '/data/',
        '/dev/',
        '/system',
        '/system/bin',
        '/system/sbin',
        '/system/xbin',
        '/vendor/bin',
        '/sbin',
        '/etc'
    ]

    try:
        decompile_apk(apk_path, output_dir)
        keyword_matches = search_keywords(output_dir, keywords_to_find)

        for file_path, matches in keyword_matches.items():
            masked_file_path = mask_package_names(file_path)
            print(f"\nMatches found in file: {colored(masked_file_path, 'yellow')}")
            for class_name, line_number, line in matches:
                masked_line = mask_package_names(line)
                print(f"Class: {class_name}")
                print(f"Line {line_number}: {colored(masked_line, 'red')}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
