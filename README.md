# Lazy Optimization Planner

This is our project in automated planning (apl), we modified existing code of
fast-downward planner, for more info take a look on [LazyOptimizationPlanner.pdf](https://github.com/louiscyphre/apl/blob/master/LazyOptimizationPlanner.pdf) 
in project tree. 
## License 

The following directories are not part of Lazy Optimization Planner as covered by this license:

    ./fast-downward/src/search/ext

For the rest, the following license applies: [GPL-3.0](https://www.gnu.org/licenses/gpl-3.0.en.html)

## Overview

This planner is based on fast-downward planner (http://www.fast-downward.org),
revision b850cf57c2f2

### Building on Linux:

~~~ sh
sudo apt-get install cmake g++ g++-multilib make python
cd fast-downward
./build.py
~~~


### Building on Windows:

If your compiler doesn't find flex or bison, your include directories might be in a non-standard location. In this case you probably have to specify where to look for includes and libraries in VAL's Makefile (probably /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr). 

For more info: 

[Obtaining And Running FastDownward](http://www.fast-downward.org/ObtainingAndRunningFastDownward)

## Important note

Remember that code in this repository is modified fast-downward, so if you 
planning to use it or compare, remember to obtain source from here. Any changes
in fast-downward project that where made after obtaining the code by us, possibly
will not appear here, so instructions might be for a different planner after original fast-downward will change.


## Validating plans

You can validate the found plans by passing --validate to the planner.

### Building VAL on Linux: 

~~~ sh
sudo apt-get install g++ make flex bison
git clone https://github.com/KCL-Planning/VAL.git
cd VAL
make clean  # Remove old build artifacts and binaries.
make
# Add "validate" binary to a directory on your PATH.
~~~


### Building VAL on Windows:

If your compiler doesn't find flex or bison, your include directories might be in a non-standard location. In this case you probably have to specify where to look for includes and libraries in VAL's Makefile (probably /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr). 


### Additional dependencies on Mac OS X

As of this writing, the planner appears to run without problems on Mac OS X. However, we do not promise full support. 

### Dependencies on Windows

On Windows, you should install Visual Studio (we tested with the free [VS 2013 Express Community Edition](https://www.visualstudio.com/en-us/downloads/download-visual-studio-vs.aspx)), [Python](https://www.python.org/downloads/windows/), and [CMake](http://www.cmake.org/download/). If you use Visual Studio 2015, make sure to install the C++ compiler. The compiler is not installed by default, but the IDE will prompt you to install it when you create a new C++ project. 

## Running the planner


### Running with our configuration, that rely on the code that we added:
~~~ sh
./run domain.pddl problem.pddl
~~~

This will run planner with 30m limit on overall time, and overall memory limit 2G.
For more info look [LazyOptimizationPlanner.pdf](https://github.com/louiscyphre/apl/blob/master/LazyOptimizationPlanner.pdf) inside the project.


