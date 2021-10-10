This repository contains a sample project to illustrate a case of
`-var-list-children`'s bad performance with simple pretty printers.

The sample is based on https://vulkan-tutorial.com/Multisampling Vulkan demo
with minor tweaks.

Steps to reproduce the issue:

- clone this repo and cd into it
- `cmake -DCMAKE_BUILD_TYPE=Debug -Btarget`
- `cd target`
- `cmake --build .`
- `gdb -q -ex "source -v ../gdb-commands"`  

The gdb-commands GDB script basically sets up a simple pretty-printer from printers.py,
sets a breakpoint, launches the executable and calls
-var-list-children that take unexpectedly significant time to execute
despite not doing that much work.
