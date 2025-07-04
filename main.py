import ascii
import os
import socket
import psutil
import platform

class styles():
    def __init__(self):
        self.reset = "\033[0m"
        self.bold = "\033[1m"
        self.underline = "\033[4m"
        self.red = "\033[31m"
        self.green = "\033[32m"
        self.yellow = "\033[33m"
        self.blue = "\033[34m"
        self.magenta = "\033[35m"
        self.cyan = "\033[36m"
        self.white = "\033[37m"

    def clear(self):
        if platform.system() == "Windows":
            os.system("cls")
        else:
            os.system("clear")

style = styles()

ram_bytes = psutil.virtual_memory().total
ram_mb = ram_bytes / (1024 ** 2)

plat = platform.system()
art = ""
artcolor = style.reset
if "Apple" or "Darwin" in plat:
    art = ascii.apple
    artcolor = style.green
if "Windows" in plat:
    art = ascii.windows
    artcolor = style.blue
elif "Linux" in plat:
    art = ascii.linux
    artcolor = style.yellow
elif "Android" in plat:
    art = ascii.android
    artcolor = style.cyan

hostname = socket.gethostname()
username = os.getlogin()

def main():
    style.clear()

    # Split ASCII art into lines
    art_lines = art.splitlines()

    # Prepare system info lines
    info_lines = [
        f"{style.red}{username}{style.white}@{style.red}{hostname}{style.reset}",
        "-" * (len(username) + len(hostname) + 1),
        f"{style.red}OS:{style.reset} {platform.system()} {platform.version()}",
        f"{style.red}Kernel:{style.reset} {platform.release()}",
        "" * 2,  # Extra line for spacing
        f"{style.red}CPU:{style.reset} {platform.machine()} {platform.processor()}",
        f"{style.red}Installed RAM:{style.reset} {ram_mb:.2f} MB",
    ]

    # Calculate width for ASCII art padding
    art_width = max(len(line) for line in art_lines) if art_lines else 0
    padding = 4  # spaces between art and text

    # Get max number of lines to print
    max_lines = max(len(art_lines), len(info_lines))

    for i in range(max_lines):
        art_line = art_lines[i] if i < len(art_lines) else ""
        info_line = info_lines[i] if i < len(info_lines) else ""
        # Pad art line to fixed width + padding spaces
        print(f"{artcolor}{art_line.ljust(art_width)}{' ' * padding}{style.reset}{info_line}")

if __name__ == "__main__":
    main()
