
import subprocess

def main():
    
    subprocess.run(
        ["python", "mainscript.py", "127.0.0.1", "100", "30"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

if __name__ == "__main__":
    main()

# silent crasher