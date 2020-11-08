print(run(
    # Install project dependencies
    [".venv/bin/python", "-m", "pip", "install", "-r", "requirements.txt"],
    stdout=-1
).stdout.decode())

print(run(
    # Show information on the aardvark package
    [".venv/bin/python", "-m", "pip", "show", "aardvark"], stdout=-1
).stdout.decode())
