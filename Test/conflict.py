import os
import sys
project_root = os.path.join(os.path.dirname(__file__),"..")
print("PROJECT ROOT: ",project_root)
sys.path.append(project_root)
print(sys.path)
