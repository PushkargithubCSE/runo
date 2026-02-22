import argparse
from agent.detector import detect_project
from agent.runner import run_project


def main():
    parser = argparse.ArgumentParser(prog="agent")
    parser.add_argument("command", help="Command to run (run/setup)")
    args = parser.parse_args()

    if args.command == "run":
        project_type = detect_project()
        run_project(project_type)
    else:
        print("❌ Unknown command")


if __name__ == "__main__":
    main()