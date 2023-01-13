import sys                      # This import file use to copy the path of the package

sys.path.append("/Package1/BasicPackage")          # Path is copied
sys.path.append("/Package1/Base")

import Module1             # Imported the module where the functions are called
import Module2


Module1.mod1()             # Module.function()
Module2.mod2()

