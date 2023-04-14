import os
from functions.delete_dir import delete_dir

fs_path = os.path.dirname(os.path.abspath(__file__))
web_path = os.path.join(fs_path, 'web')
backo_oath = os.path.join(fs_path, 'backoffice')

if os.path.exists(web_path):
    delete_dir(web_path)

if os.path.exists(backo_oath):
    delete_dir(backo_oath)
