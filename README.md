# Exodapt Robot Prompt Templates

A library for versioned and standardized prompt templates used throughout the Exodapt robot software packages.

# Installation

PIP installation
```
pip install exodapt-robot-prompt-templates --upgrade
```

Local installation
```
pip install -e .
```

# How to use

Import prompt template functions and use with expected input arguments
```
from exodapt_robot_pt import state_description_pt


state_descr_str = state_description_pt()
```

For local usage for development running the scripts as a module:
```
cd src/
python -m exodapt_robot_pt.state_description_pt
```
