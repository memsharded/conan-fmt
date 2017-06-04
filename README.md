# conan-fmt
Conan (https://conan.io) package for C++ fmt format library

[![badge](https://img.shields.io/badge/conan.io-fmt%2F3.0.1-green.svg?logo=data:image/png;base64%2CiVBORw0KGgoAAAANSUhEUgAAAA4AAAAOCAMAAAAolt3jAAAA1VBMVEUAAABhlctjlstkl8tlmMtlmMxlmcxmmcxnmsxpnMxpnM1qnc1sn85voM91oM11oc1xotB2oc56pNF6pNJ2ptJ8ptJ8ptN9ptN8p9N5qNJ9p9N9p9R8qtOBqdSAqtOAqtR%2BrNSCrNJ/rdWDrNWCsNWCsNaJs9eLs9iRvNuVvdyVv9yXwd2Zwt6axN6dxt%2Bfx%2BChyeGiyuGjyuCjyuGly%2BGlzOKmzOGozuKoz%2BKqz%2BOq0OOv1OWw1OWw1eWx1eWy1uay1%2Baz1%2Baz1%2Bez2Oe02Oe12ee22ujUGwH3AAAAAXRSTlMAQObYZgAAAAFiS0dEAIgFHUgAAAAJcEhZcwAACxMAAAsTAQCanBgAAAAHdElNRQfgBQkREyOxFIh/AAAAiklEQVQI12NgAAMbOwY4sLZ2NtQ1coVKWNvoc/Eq8XDr2wB5Ig62ekza9vaOqpK2TpoMzOxaFtwqZua2Bm4makIM7OzMAjoaCqYuxooSUqJALjs7o4yVpbowvzSUy87KqSwmxQfnsrPISyFzWeWAXCkpMaBVIC4bmCsOdgiUKwh3JojLgAQ4ZCE0AMm2D29tZwe6AAAAAElFTkSuQmCC)](http://www.conan.io/source/fmt/3.0.1/memsharded/testing)


Using the header-only approach.
Tested and working in 94 different configurations in Windows, Linux and Mac:

[![Build status](https://ci.appveyor.com/api/projects/status/lh9wapq1mx4amc8j?svg=true)](https://ci.appveyor.com/project/memsharded/conan-fmt)
[![Build Status](https://travis-ci.org/memsharded/conan-fmt.svg?branch=testing)](https://travis-ci.org/memsharded/conan-fmt)


## Example

Add it to your requirements in conanfile.txt or conanfile.py:

```
[requires]
fmt/3.0.1@memsharded/testing

[generators]
cmake
```

If you are not using cmake in your project, check other conan generators.

Your example.cpp:

```cpp
#include <iostream>
#include "fmt/format.h"

int main() {
    std::string message = fmt::format("The answer is {}", 42);
    std::cout<<message<<"\n";
}
```

```CMake
project(YourProject)
cmake_minimum_required(VERSION 2.8.12)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

add_executable(example example.cpp)
target_link_libraries(example ${CONAN_LIBS})
```

Then you can use it as:

```bash
$ mkdir build && cd build
$ conan install .. --build=missing (this will use your default conan settings)
$ cmake .. -G "Visual Studio 14 Win64"
$ cmake --build . --config Release
$ bin/example
```

Note that I am using ``--build=missing``. I haven't uploaded binary packages yet, just the recipe,
so the package has to be built from sources.

