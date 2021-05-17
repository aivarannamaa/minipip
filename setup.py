import os.path
import sys

from setuptools import find_packages, setup

setupdir = os.path.dirname(__file__)

for line in open(os.path.join(setupdir, "minipip.py")).read().splitlines():
    if line.startswith('__version__'):
        version = line.split('"')[1]
        break
else:
    raise RuntimeError("Unable to find version string.")

requirements = []
for line in open(os.path.join(setupdir, "requirements.txt"), encoding="ASCII"):
    if line.strip() and not line.startswith("#"):
        requirements.append(line)

setup(
    name="minipip",
    version=version,
    description="Tool for installing packages for MicroPython and CircuitPython",
    url="https://github.com/aivarannamaa/minipip",
    author="Aivar Annamaa",
    license="MIT",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: Freeware",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: MacOS",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Software Development",
    ],
    keywords="MicroPython CircuitPython pip upip",
    project_urls={
        "Source code": "https://github.com/aivarannamaa/minipip",
        "Bug tracker": "https://github.com/aivarannamaa/minipip/issues",
    },
    platforms=["Windows", "macOS", "Linux"],
    install_requires=requirements,
    python_requires=">=3.6",
    py_modules=["minipip"],
    entry_points={"console_scripts": ["minipip = minipip:main"]},
)
