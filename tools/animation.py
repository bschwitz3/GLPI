import sys
import time

class TerminalColors:
    YELLOW = '\033[93m'
    GREEN = '\033[92m'
    RED = '\033[91m'
    END = '\033[0m'

def loading_animation():
    start_time = time.time()
    while not loading_animation.stop:
        sys.stdout.write('\r' + TerminalColors.YELLOW + 'Chargement   ' + TerminalColors.END)
        sys.stdout.flush()
        time.sleep(0.2)
        sys.stdout.write('\r' + TerminalColors.YELLOW + 'Chargement.  ' + TerminalColors.END)
        sys.stdout.flush()
        time.sleep(0.2)
        sys.stdout.write('\r' + TerminalColors.YELLOW + 'Chargement.. ' + TerminalColors.END)
        sys.stdout.flush()
        time.sleep(0.2)
        sys.stdout.write('\r' + TerminalColors.YELLOW + 'Chargement...' + TerminalColors.END)
        sys.stdout.flush()
        time.sleep(0.2)
    sys.stdout.write('\r' + TerminalColors.END + '             ' + TerminalColors.END)
    sys.stdout.flush()