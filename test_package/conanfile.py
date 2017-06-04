from conans import ConanFile, CMake
import os


channel = os.getenv("CONAN_CHANNEL", "testing")
username = os.getenv("CONAN_USERNAME", "memsharded")
reference = os.getenv("CONAN_REFERENCE", "fmt/3.0.1")


class FmtTestConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    requires = "%s@%s/%s" % (reference, username, channel)
    generators = "cmake"

    def build(self):
        cmake = CMake(self)
        self.run('cmake "%s" %s' % (self.conanfile_directory, cmake.command_line))
        self.run("cmake --build . %s" % cmake.build_config)

    def imports(self):
        self.copy("*.dll", "bin", "bin")
        self.copy("*.dylib", "bin", "lib")

    def test(self):
        os.chdir("bin")
        self.run(".%sexample" % os.sep)
