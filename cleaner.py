import os
from functions.delete_dir import delete_dir

fs_path = os.path.dirname(os.path.abspath(__file__))
web_path = os.path.join(fs_path, 'web')
backo_path = os.path.join(fs_path, 'backoffice')

if os.path.exists(web_path):
    delete_dir(web_path)

if os.path.exists(backo_path):
    delete_dir(backo_path)
