from conans import ConanFile, CMake, tools
import os


class FmtConan(ConanFile):
    name = "fmt"
    version = "3.0.0"
    license = "BSD"
    url = "https://github.com/memsharded/conan-fmt"
    build_policy = "missing"
    settings = "os", "arch", "compiler", "build_type"
    options = {"shared": [True, False], "header_only": [True, False],}
    default_options = "shared=False", "header_only=False"

    def config_settings(self):
        if self.options.header_only:
            self.settings.clear()
        else:
            self.build_policy = None

    def source(self):
       self.run("git clone https://github.com/fmtlib/fmt")
       self.run("cd fmt && git checkout 3.0.0")

    def build(self):
        if self.options.header_only:
            return
        cmake = CMake(self.settings)
        shared = "-DBUILD_SHARED_LIBS=ON" if self.options.shared else ""
        shared += " -DFMT_TEST=OFF -DFMT_INSTALL=OFF -DFMT_DOCS=OFF"
        self.run('cmake fmt %s %s' % (cmake.command_line, shared))
        self.run("cmake --build . %s" % cmake.build_config)

    def package(self):
        self.copy("*.h", dst="include/fmt", src="fmt/fmt")
        self.copy("*.h", dst="include/cppformat", src="cppformat")
        if self.options.header_only:
            self.copy("*.cc", dst="include/fmt", src="fmt/fmt")
        else:
            self.copy("*.lib", dst="lib", keep_path=False)
            self.copy("*.dll", dst="bin", keep_path=False)
            self.copy("*.so", dst="lib", keep_path=False)
            self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        if self.options.header_only:
            self.cpp_info.defines.append("FMT_HEADER_ONLY")
        else:
            self.cpp_info.libs.append("fmt")
