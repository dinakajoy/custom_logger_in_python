import os
from datetime import datetime, timezone
from colorama import Fore, Style, init

init(autoreset=True)

LOG_FILE = "logs.txt"
MAX_SIZE_MB = 1

def format_message(level, message):
  timestamp = datetime.now(timezone.utc).isoformat()
  return f"[{timestamp}] [{level.upper()}]: {message}"

def get_color(level):
  return {
    "info": Fore.BLUE,
    "warn": Fore.YELLOW,
    "error": Fore.RED
  }.get(level, "")

def rotate_log_if_needed():
  if os.path.exists(LOG_FILE):
    size_mb = os.path.getsize(LOG_FILE) / (1024 * 1024)
    if size_mb >= MAX_SIZE_MB:
      backup = f"logs_{int(datetime.now(timezone.utc).timestamp())}.txt"
      os.rename(LOG_FILE, backup)

def log(level, message):
  msg = format_message(level, message)

  # Log to console with color
  color = get_color(level)
  print(f"{color}{msg}{Style.RESET_ALL}")

  # Log to file
  rotate_log_if_needed()
  with open(LOG_FILE, "a") as f:
    f.write(msg + "\n")

def info(message):
  log("info", message)

def warn(message):
  log("warn", message)

def error(message):
  log("error", message)
