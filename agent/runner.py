import subprocess
import json
import os


def run_project(project_type):
    if project_type == "node":
        run_node()

    elif project_type == "python":
        run_python()

    else:
        print("❌ Unsupported project type")


# ---------------- NODE ---------------- #

def run_node():
    print("🚀 Setting up Node project...")

    run_cmd("npm install")

    print("▶ Running project...")

    # try npm start
    run_cmd("npm start")


# ---------------- PYTHON ---------------- #

def run_python():
    print("🚀 Setting up Python project...")

    if os.path.exists("requirements.txt"):
        run_cmd("pip install -r requirements.txt")

    print("▶ Running project...")

    if os.path.exists("main.py"):
        run_cmd("python main.py")

    elif os.path.exists("app.py"):
        run_cmd("python app.py")

    else:
        print("❌ No entry file found (main.py/app.py)")


# ---------------- UTILITY ---------------- #

def run_cmd(cmd):
    try:
        subprocess.run(cmd, shell=True, check=True)
    except subprocess.CalledProcessError:
        print(f"❌ Failed: {cmd}")