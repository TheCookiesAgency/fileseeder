import os
import re
import argparse
import sys
from functions.fileseeder import fileseeder
import subprocess

root_path = os.getcwd()
fs_path = os.path.dirname(os.path.abspath(__file__))
md_path = os.path.join(root_path, 'structure.md')
his_path = os.path.join(root_path, 'historial_fs.txt')
rs_path = os.path.join(fs_path, 'functions/read_history.py')

parser = argparse.ArgumentParser()
parser.add_argument('--force', help='Ejecutar una operación forzada', action='store_true')
args = parser.parse_args()

sys.stdout = open(his_path, 'w')

if args.force:
    with open(md_path, 'r') as structure:
        for linea in structure:
            page_match = re.search(r'^# \*\*(\w+)\*\*', linea)
            if page_match:
                camelName = page_match.group(1)
                fileseeder("gpag", camelName, "--d")
                fileseeder("land", camelName, "--d")
                fileseeder("sdoc", camelName, "--d")
                fileseeder("gpag", camelName)
                fileseeder("land", camelName)
                fileseeder("sdoc", camelName)
            template_match = re.search(r'^# (\w+)', linea)
            if template_match:
                camelName = template_match.group(1)
                fileseeder("gtemp", camelName, "--d")
                fileseeder("land", camelName, "--d")
                fileseeder("sdoc", camelName, "--d")
                fileseeder("gtemp", camelName)
                fileseeder("land", camelName)
                fileseeder("sdoc", camelName)
            organism_match = re.search(r'^## (\w+)', linea)
            if organism_match:
                camelName = organism_match.group(1)
                fileseeder("org", camelName, "--d")
                fileseeder("sobj", camelName, "--d")
                fileseeder("org", camelName)
                fileseeder("sobj", camelName)
            molecule_match = re.search(r'^### (\w+)', linea)
            if molecule_match:
                camelName = molecule_match.group(1)
                fileseeder("mol", camelName, "--d")
                fileseeder("mol", camelName)
else:
    with open(md_path, 'r') as structure:
        for linea in structure:
            page_match = re.search(r'^# \*\*(\w+)\*\*', linea)
            if page_match:
                camelName = page_match.group(1)
                fileseeder("gpag", camelName)
                fileseeder("land", camelName)
                fileseeder("sdoc", camelName)
            template_match = re.search(r'^# (\w+)', linea)
            if template_match:
                camelName = template_match.group(1)
                fileseeder("gtemp", camelName)
                fileseeder("land", camelName)
                fileseeder("sdoc", camelName)
            organism_match = re.search(r'^## (\w+)', linea)
            if organism_match:
                camelName = organism_match.group(1)
                fileseeder("org", camelName)
                fileseeder("sobj", camelName)
            molecule_match = re.search(r'^### (\w+)', linea)
            if molecule_match:
                camelName = molecule_match.group(1)
                fileseeder("mol", camelName)

sys.stdout.close()

subprocess.call(["python3", rs_path])