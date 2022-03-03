import glob

from conans import ConanFile, CMake, tools


class PbtoolsConan(ConanFile):
    name = "pbtools"
    license = "MIT"
    author = "Erik Moqvist erik.moqvist@gmail.com"
    url = "https://github.com/eerimoq/pbtools"
    description = "A Google Protocol Buffers C library"
    topics = ("protobuf", )
    settings = ("os", "compiler", "build_type", "arch")
    options = {"shared": [True, False]}
    default_options = {"shared": False}
    generators = "cmake"

    def source(self):
        tools.get(**self.conan_data["sources"][self.version])

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder=f'pbtools-{self.version}/lib')
        cmake.build()
        cmake.install()

    def package(self):
        pass

    def package_info(self):
        self.cpp_info.libs = ["pbtools"]
