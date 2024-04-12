#!/bin/bash

# Function to run a process as a daemon in the background
run_daemon() {
  "$@" &  # Run the command in the background
  daemon_pid=$!
  echo "Started process $daemon_pid: $@"  # Log the PID and command for reference
}

# Wait for the model download process (process 1) to complete
wait $(python model_download_70b.py)  # Capture the PID for waiting
echo "Model download complete."

# Start the remaining processes as daemons in parallel
run_daemon python -m fastchat.serve.controller --host 0.0.0.0
run_daemon python -m fastchat.serve.model_worker --model-path meditron-70b --device cuda --host 0.0.0.0 --controller-address http://0.0.0.0:21001
run_daemon python -m fastchat.serve.gradio_web_server --host 0.0.0.0 --share --port 8080
run_daemon python -m fastchat.serve.openai_api_server --host 0.0.0.0 --controller-address http://0.0.0.0:21001 --port 8000

echo "All processes started."