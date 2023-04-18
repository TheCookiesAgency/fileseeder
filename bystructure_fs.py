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
parser.add_argument('--show', help='Muestra toda la salida', action='store_true')
args = parser.parse_args()

sys.stdout = open(his_path, 'w')

if args.force:
    with open(md_path, 'r') as structure:
        for linea in structure:
            page_match = re.search(r'^# \*\*(\w+)\*\*$', linea)
            if page_match:
                camelName = page_match.group(1)
                fileseeder("gpag", camelName, None, True, False)
                fileseeder("land", camelName, None, True, False)
                fileseeder("sdoc", camelName, None, True, False)
                fileseeder("gpag", camelName, None, False, False)
                fileseeder("land", camelName, None, False, False)
                fileseeder("sdoc", camelName, None, False, False)
            template_match = re.search(r'^# (\w+)$', linea)
            if template_match:
                camelName = template_match.group(1)
                fileseeder("gtemp", camelName, None, True, False)
                fileseeder("land", camelName, None, True, False)
                fileseeder("sdoc", camelName, None, True, False)
                fileseeder("gtemp", camelName, None, False, False)
                fileseeder("land", camelName, None, False, False)
                fileseeder("sdoc", camelName, None, False, False)
            organism_match = re.search(r'^## (\w+)$', linea)
            if organism_match:
                camelName = organism_match.group(1)
                fileseeder("org", camelName, None, True, False)
                fileseeder("sobj", camelName, None, True, False)
                fileseeder("org", camelName, None, False, False)
                fileseeder("sobj", camelName, None, False, False)
            molecule_match = re.search(r'^### (\w+)$', linea)
            if molecule_match:
                camelName = molecule_match.group(1)
                fileseeder("mol", camelName, None, True, False)
                fileseeder("mol", camelName, None, False, False)
            page_match_traduccion = re.search(r'^# \*\*(\w+)\*\* - ', linea)
            if page_match_traduccion:
                camelName = page_match_traduccion.group(1)
                kebabTraduccion = linea.split(' - ')[1]
                fileseeder("gpag", camelName, kebabTraduccion, True, True)
                fileseeder("land", camelName, None, True, True)
                fileseeder("sdoc", camelName, None, True, True)
                fileseeder("gpag", camelName, kebabTraduccion, False, True)
                fileseeder("land", camelName, None, False, True)
                fileseeder("sdoc", camelName, None, False, True)
            template_match_traduccion = re.search(r'^# (\w+) - ', linea)
            if template_match_traduccion:
                camelName = template_match_traduccion.group(1)
                kebabTraduccion = linea.split(' - ')[1]
                fileseeder("gtemp", camelName, kebabTraduccion, True, True)
                fileseeder("land", camelName, None, True, True)
                fileseeder("sdoc", camelName, None, True, True)
                fileseeder("gtemp", camelName, kebabTraduccion, False, True)
                fileseeder("land", camelName, None, False, True)
                fileseeder("sdoc", camelName, None, False, True)
else:
    with open(md_path, 'r') as structure:
        for linea in structure:
            page_match = re.search(r'^# \*\*(\w+)\*\*$', linea)
            if page_match:
                camelName = page_match.group(1)
                fileseeder("gpag", camelName, None, False, False)
                fileseeder("land", camelName, None, False, False)
                fileseeder("sdoc", camelName, None, False, False)
            template_match = re.search(r'^# (\w+)$', linea)
            if template_match:
                camelName = template_match.group(1)
                fileseeder("gtemp", camelName, None, False, False)
                fileseeder("land", camelName, None, False, False)
                fileseeder("sdoc", camelName, None, False, False)
            organism_match = re.search(r'^## (\w+)$', linea)
            if organism_match:
                camelName = organism_match.group(1)
                fileseeder("org", camelName, None, False, False)
                fileseeder("sobj", camelName, None, False, False)
            molecule_match = re.search(r'^### (\w+)$', linea)
            if molecule_match:
                camelName = molecule_match.group(1)
                fileseeder("mol", camelName, None, False, False)
            page_match_traduccion = re.search(r'^# \*\*(\w+)\*\* - ', linea)
            if page_match_traduccion:
                camelName = page_match_traduccion.group(1)
                kebabTraduccion = linea.split(' - ')[1]
                fileseeder("gpag", camelName, kebabTraduccion, False, True)
                fileseeder("land", camelName, None, False, True)
                fileseeder("sdoc", camelName, None, False, True)
            template_match_traduccion = re.search(r'^# (\w+) - ', linea)
            if template_match_traduccion:
                camelName = template_match_traduccion.group(1)
                kebabTraduccion = linea.split(' - ')[1]
                fileseeder("gtemp", camelName, kebabTraduccion, False, True)
                fileseeder("land", camelName, None, False, True)
                fileseeder("sdoc", camelName, None, False, True)

sys.stdout.close()

if args.show:
    subprocess.call(["python3", rs_path , "--show" ])
else:
    subprocess.call(["python3", rs_path ])