from setuptools import find_packages, setup

setup(
    author="Zackary Troop",
    name="wave-reader",
    version="1.0.2",
    url="https://github.com/ztroop/wave-reader-utils",
    license="MIT",
    description="Unofficial package for Airthings Wave communication.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(exclude=["examples", "tests"]),
    install_requires=[
        "Authlib>=0.15.6",
        "bleak>=0.19.5",
        "httpx>=0.18.2",
        "attrs>=21.3.0",
        "python-dateutil>=2.8.2",
    ],
    python_requires=">=3.7.0",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)
