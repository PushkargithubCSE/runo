import os


def detect_project():
    files = os.listdir(".")

    if "package.json" in files:
        print("📦 Detected Node.js project")
        return "node"

    elif "requirements.txt" in files:
        print("🐍 Detected Python project")
        return "python"

    else:
        print("❌ Could not detect project type")
        return None