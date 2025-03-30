import os
import time
from pathlib import Path

# 🔧 Customize this
DOWNLOADS_FOLDER = str(Path.home() / "Downloads")
DAYS_OLD = 30  # Files older than this will be deleted
TARGET_EXTENSIONS = [".exe", ".msi", ".zip", ".dmg", ".iso", ".7z", ".rar"]

# ⏱ Convert days to seconds
cutoff_time = time.time() - (DAYS_OLD * 86400)

deleted_files = []

for root, dirs, files in os.walk(DOWNLOADS_FOLDER):
    for file in files:
        filepath = os.path.join(root, file)
        ext = os.path.splitext(file)[1].lower()

        if ext in TARGET_EXTENSIONS:
            file_modified = os.path.getmtime(filepath)
            if file_modified < cutoff_time:
                try:
                    os.remove(filepath)
                    deleted_files.append(filepath)
                except Exception as e:
                    print(f"❌ Could not delete {filepath}: {e}")

print(f"\n✅ Deleted {len(deleted_files)} file(s) older than {DAYS_OLD} days:")
for f in deleted_files:
    print(f" - {f}")
