def print_name_and_file():
    print(f"Name is {__name__}. File is {__file__}.")

# myproject
# └── mypackage
#     ├── __init__.py
#     └── mymodule.py

zipapp.create_archive(
    # Zip up a project called "myproject"
    "myproject",
    interpreter="/usr/bin/env python",
    # Generate a __main__.py file
    main="mypackage.mymodule:print_name_and_file")

print(subprocess.run([".venv/bin/python", "myproject.pyz"],
                     stdout=-1).stdout.decode())
