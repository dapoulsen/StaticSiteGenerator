from website import copy_content_to_directory

def main():
    source_dir = "static"
    destination_dir = "public"

    copy_content_to_directory(source_dir, destination_dir)
   

if __name__ == "__main__":
    main()
    
