import os
import shutil
from textnode import TextNode, TextType

STATIC_DIR = "static"
PUBLIC_DIR = "public"

def copy_dir(src_name: str, dst_name: str) -> None:
    for file_name in os.listdir(src_name):
        src_path = os.path.join(src_name, file_name)
        dst_path = os.path.join(dst_name, file_name)

        if os.path.isfile(src_path):
            print(f"Copying file {src_path}")
            shutil.copy(src_path, dst_path)
        else:
            os.mkdir(dst_path)
            print(f"Copying dir {src_path}")
            copy_dir(src_path, dst_path)

def main():
    if not os.path.exists(STATIC_DIR):
        raise FileNotFoundError(f"{STATIC_DIR} does not exist")

    if os.path.exists(PUBLIC_DIR):
        shutil.rmtree(PUBLIC_DIR)
    os.mkdir(PUBLIC_DIR)

    copy_dir(STATIC_DIR, PUBLIC_DIR)

main()
