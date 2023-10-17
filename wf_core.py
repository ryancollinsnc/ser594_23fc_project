import subprocess
import sys

def run_script(script_name):
    try:
        output = subprocess.check_output([sys.executable, script_name])
        print(f"Output from {script_name}: {output.decode()}")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while executing {script_name}: {e}")

run_script("wf_dataprocessing.py")

run_script("wf_visualization.py")
