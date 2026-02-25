import os
import shutil

def copy_content_to_directory(source, destination):
    if os.path.exists(destination):
        print(f"Deleting extisting directory: {destination}")
        shutil.rmtree(destination)
    
    os.mkdir(destination)

    for item in os.listdir(source):
        src_path = os.path.join(source, item)
        dst_path = os.path.join(destination, item)

        if os.path.isfile(src_path):
            shutil.copy(src_path, dst_path)
            print(f"Copied file:{src_path} -> {dst_path}")
        else:
            copy_content_to_directory(src_path, dst_path)