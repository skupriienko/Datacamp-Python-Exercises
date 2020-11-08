# Create an virtual environment
venv.create(".venv")

# Run pip list and obtain a CompletedProcess instance
cp = subprocess.run([".venv/bin/python", "-m", "pip", "list"], stdout=-1)

for line in cp.stdout.decode().split("\n"):
    if "pandas" in line:
        print(line)
