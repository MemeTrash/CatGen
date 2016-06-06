from setuptools import setup


setup(
    name="MemeGeneratorWow",
    version="0.0.0",
    url="https://github.com/YorkZamzar2016/MemeGeneratorWow",
    license="MIT",
    description="Random terrain generator for Python",
    author="Jack Romo",
    author_email="sharrackor@gmail.com",
    platforms="any",
    packages=['randterrainpy'],
    install_requires=[
        "matplotlib>=1.5.1",
        "numpy>=1.6.2"
    ],
    classifiers=[
        "Operating System :: OS Independent",
        "Programming Language :: Python 2.7"
    ]
)
