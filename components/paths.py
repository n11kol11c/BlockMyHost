import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BUILDER_INI = os.path.join(BASE_DIR, "builder", "build.ini")
BACKUP_DIR = os.path.join(BASE_DIR, "backup")
os.makedirs(BACKUP_DIR, exist_ok=True)
HOSTS_PATH = r"C:\Windows\System32\drivers\etc\hosts"
HOSTS_BACKUP = os.path.join(BACKUP_DIR, "hosts.bak")
