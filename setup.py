import setuptools

NAME = "fy-end-tools"
AUTHOR = "Rudy Williams"
AUTHOR_EMAIL = "rudysw05@knights.ucf.edu"
SHORT_DESCRIPTION = "A package for end of year analysis at CYS"
URL = "https://github.com/RudyWilliams/fy-end-tools"

with open("fy_end_tools/VERSION") as v:
    VERSION = v.read().strip()


def list_reqs(fname="requirements.txt"):
    with open(fname) as f:
        return f.read().splitlines()


setuptools.setup(
    name=NAME,
    version=VERSION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    description=SHORT_DESCRIPTION,
    url=URL,
    packages=setuptools.find_packages(),
    entry_points={"console_scripts": ["fy_end_tools=fy_end_tools.cli.runner:run_cli"]},
    install_requires=list_reqs(),
    include_package_data=True,
    python_requires=">=3.7",
)
