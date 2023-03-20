import os
import sys
import subprocess

# Add "infinite-music-discs" to the python PATH so src.version may be imported
build_dir = os.path.dirname(__file__)
sys.path.append(os.path.abspath(os.path.join(build_dir, os.pardir)))

import src.version as version

version_csv = f'{version.MAJOR}, {version.MINOR}, 0, 0'
version_literal = f'{version.MAJOR}.{version.MINOR}.0.0'

# Write a copy of 'version.rc' with the version numbers autopopulated from version.py
with open(os.path.join(build_dir, 'version.rc'), 'r') as v_orig:
    with open(os.path.join(build_dir, 'version.rc.tmp'), 'w') as v_temp:
        for line in v_orig.readlines():
            v_temp.write(line.format(version_csv=version_csv, version_literal=version_literal))

# Run pyinstaller
pyinstaller_cmd = [
    'pyinstaller main.pyw',
    '--onefile',
    '--clean',
    '--noconfirm',
    '--version-file "build/version.rc.tmp"',
    '--add-data "data/*;data"',
    '--name "imd-gui"',
    '--icon "data/jukebox_256.ico"',
    '--distpath "bin"',
    '--workpath "build"'
]

subprocess.run(' '.join(pyinstaller_cmd), check=True)