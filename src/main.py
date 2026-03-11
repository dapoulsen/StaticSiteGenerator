import sys
from website import copy_content_to_directory, generate_page, generate_pages_recursive

def main():


    if len(sys.argv) == 1:
        basepath = "/"
    else:
        basepath = sys.argv[1]

    source_dir = "static"
    destination_dir = "docs"

    copy_content_to_directory(source_dir, destination_dir)
   
    generate_pages_recursive("content", "./template.html", "docs", basepath)

if __name__ == "__main__":
    main()
    
