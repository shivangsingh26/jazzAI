import pkg_resources

with open('requirements.txt') as requirements_file:
    requirements = requirements_file.readlines()

for requirement in requirements:
    requirement = requirement.strip()
    if not requirement or requirement.startswith('#'):
        continue

    try:
        pkg_resources.require(requirement)
        # print(f"{requirement} is installed")
        pass
    except pkg_resources.DistributionNotFound:
        print(f"{requirement} is not installed")
    except pkg_resources.VersionConflict as e:
        print(f"{requirement} version conflict: {e.report()}")
