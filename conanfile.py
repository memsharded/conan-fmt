from conans import ConanFile, CMake, tools
import os


class FmtConan(ConanFile):
    name = "fmt"
    version = "3.0.0"
    license = "BSD"
    url = "https://github.com/memsharded/conan-fmt"
    build_policy = "missing"

    def source(self):
       self.run("git clone https://github.com/fmtlib/fmt")
       self.run("cd fmt && git checkout 3.0.0")

    def package(self):
        self.copy("*.h", dst="include/fmt", src="fmt/fmt")
        self.copy("*.h", dst="include/cppformat", src="cppformat")
        self.copy("*.cc", dst="include/fmt", src="fmt/fmt")
        self.copy("*.h", dst="include/cppformat", src="cppformat")

    def package_info(self):
        self.cpp_info.defines.append("FMT_HEADER_ONLY")

