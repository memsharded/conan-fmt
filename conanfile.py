from conans import ConanFile, CMake, tools
import os


class FmtConan(ConanFile):
    name = "fmt"
    version = "3.0.0"
    license = "BSD"
    url = "https://github.com/memsharded/conan-fmt"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"
    build_policy = "missing"

    def source(self):
       self.run("git clone https://github.com/fmtlib/fmt")
       self.run("cd fmt && git checkout 3.0.0")
       # This small hack might be useful to guarantee proper /MT /MD linkage in MSVC
       # if the packaged project doesn't have variables to set it properly
       tools.replace_in_file("fmt/CMakeLists.txt", "project(FMT)", '''project(FMT)
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()''')

    def build(self):
        cmake = CMake(self.settings)
        shared = "-DBUILD_SHARED_LIBS=ON" if self.options.shared else ""
        shared += " -DFMT_TEST=OFF -DFMT_INSTALL=OFF -DFMT_DOCS=OFF"
        self.run('cmake fmt %s %s' % (cmake.command_line, shared))
        self.run("cmake --build . %s" % cmake.build_config)

    def package(self):
        self.copy("*.h", dst="include/fmt", src="fmt/fmt")
        self.copy("*.h", dst="include/cppformat", src="cppformat")
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["fmt"]
