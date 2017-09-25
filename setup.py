from setuptools import setup

setup(
    name="markov_clustering",
    version="0.0.1",
    description="Implementation of the Markov clustering (MCL) algorithm in python.",
    autor="Guy Allard",
    author_email="w.g.allard AT lumc DOT nl",
    url="https://git.lumc.nl/wgallard/markov_clustering.git",
    license="MIT",
    platforms=["linux"],
    packages=["markov_clustering"],
    install_requires=[
        "click",
        "numpy"
    ],
    entry_points={
        #"console_scripts": ['pipe-runner=pipe_runner.command_line:runner']
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Operating System :: Linux",
        "Programming Language :: Python",
        "Topic :: Scientific/Engineering",
        "License :: MIT License",
    ],
    keywords = "bioinformatics clustering"
)
