#!/bin/bash

# Install packages using pip
pip install matplotlib tkinter os shutil json

# Check if installation was successful
if [ $? -eq 0 ]; then
  echo "Installation successful"
else
  echo "Installation failed"
fi
