"""
main.py
"""

import os
import importlib
import sys

# Get the current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Add the current directory to sys.path if it's not already there
if current_dir not in sys.path:
    sys.path.append(current_dir)

# Dictionary to store loaded modules
loaded_modules = {}

# Iterate through all Python files in the directory
def load_all_modules():
    for filename in os.listdir(current_dir):
        if filename.endswith('.py') and filename != 'main.py':
            module_name = filename[:-3]  # Remove '.py' from the filename
            module = importlib.import_module(module_name)
            loaded_modules[module_name] = module
            print(f"Loaded module: {module_name}")
            
            # Add the module's contents to the global namespace
            globals().update(
                {name: getattr(module, name) for name in dir(module) 
                if not name.startswith('_')}
            )

    print("All modules loaded and their contents added to the global namespace.")
    return loaded_modules

# Function to reload a specific module
def reload_module(module_name):
    if module_name in loaded_modules:
        module = importlib.reload(loaded_modules[module_name])
        loaded_modules[module_name] = module
        globals().update(
            {name: getattr(module, name) for name in dir(module) 
             if not name.startswith('_')}
        )
        print(f"Reloaded module: {module_name}")
    else:
        print(f"Module {module_name} not found.")

# Load all modules and get the loaded_modules dictionary
loaded_modules = load_all_modules()

# Make reload_module and loaded_modules accessible in the global scope
globals()['reload_module'] = reload_module
globals()['loaded_modules'] = loaded_modules

print("Use reload_module(module_name, loaded_modules) to reload a specific module.")
