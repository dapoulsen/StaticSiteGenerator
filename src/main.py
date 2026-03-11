from website import copy_content_to_directory, generate_page, generate_pages_recursive

def main():
    source_dir = "static"
    destination_dir = "public"

    copy_content_to_directory(source_dir, destination_dir)
   
    generate_pages_recursive("./content/", "./template.html", "./public/")

if __name__ == "__main__":
    main()
    
