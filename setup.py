from setuptools import find_packages, setup

setup(
    author='Zackary Troop',
    name='wave-reader',
    version='0.0.2',
    url='https://github.com/ztroop/wave-reader-utils',
    license='MIT',
    description='A unofficial package for Airthings Wave communication.',
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(exclude=['examples', 'tests']),
    install_requires=['bleak>=0.10.0'],
    python_requires='>=3.7.*',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ]
)
