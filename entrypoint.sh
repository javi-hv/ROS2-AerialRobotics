#!/bin/bash
set -e  # Stop on error

PX4_DIR="/src/aerial_robotics/PX4-Autopilot"
ENTRY_DIR="/src/aerial_robotics"
BUILD_DIR="$PX4_DIR/build"

# Ensure script permissions are set correctly
chmod +x $ENTRY_DIR/entrypoint.sh

# Fix "dubious ownership" error in Git
git config --global --add safe.directory "$PX4_DIR"

# Check if PX4 is already built
if [ ! -d "$BUILD_DIR" ]; then
    echo "PX4 is not built. Building PX4 now..."
    # bash "$PX4_DIR/Tools/setup/ubuntu.sh"
    cd $PX4_DIR
    DONT_RUN=1 make px4_sitl
else
    echo "PX4 is already built. Skipping build process."
fi

# Keep the container running
# tail -f /dev/nul
exec bash