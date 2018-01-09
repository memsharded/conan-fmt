from conan.packager import ConanMultiPackager


if __name__ == "__main__":
    builder = ConanMultiPackager()
    builder.add_common_builds(shared_option_name="fmt:shared")
    
    builds = []
    for settings, options, env_vars, build_requires in builder.builds:
        if settings["compiler"] == "Visual Studio" and settings["compiler.version"] == "10" and settings["arch"] == "x86_64":
            continue
        builds.append([settings, options, env_vars, build_requires])
    builder.builds = builds
    builder.run()