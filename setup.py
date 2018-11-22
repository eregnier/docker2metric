from setuptools import setup, find_packages
import docker2metric

setup(
    name='docker2metric',
    version=docker2metric.__version__,
    author="Eric Régnier",
    author_email="utopman@gmail.com",
    packages=find_packages(),
    description="Host's docker metrics to json",
    long_description=open('README.md').read(),
    include_package_data=False,
    url='http://github.com/eregnier/docker2metric',
    classifiers=[
        "Programming Language :: Python",
        "Development Status :: 1 - Planning",
        "License :: MIT",
        "Natural Language :: French",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.5",
        "Topic :: System metrics",
    ],
    license="MIT",
)
