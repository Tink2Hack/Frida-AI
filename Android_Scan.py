# Copyright (c) 2023, Sellva Manoj D S
# All rights reserved.
#
# This software is licensed under the MIT License.
# See LICENSE.txt for more details.

import os
import subprocess
import re

def decompile_apk(apk_path, output_dir):
    subprocess.run(['jadx', '-d', output_dir, apk_path], check=True)

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
                            keyword_matches[file_path].append((current_class, line_number, line.strip()))

    return keyword_matches

def main():
    apk_path = 'yourapk file'
    output_dir = '/tmp'
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

    decompile_apk(apk_path, output_dir)
    keyword_matches = search_keywords(output_dir, keywords_to_find)

    for file_path, matches in keyword_matches.items():
        print(f"\nMatches found in file: {file_path}")
        for class_name, line_number, line in matches:
            print(f"Class: {class_name}")
            print(f"Line {line_number}: {line}")

if __name__ == "__main__":
    main()
