#!/bin/bash
cd /app/projects/pycookbook
source venv/bin/activate
jupyter lab --notebook-dir=/app/projects/pycookbook --ip=0.0.0.0
