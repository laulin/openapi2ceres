import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="openapi2ceres",
    version="1.1.0",
    author="Laurent MOULIN",
    author_email="gignops@noemail.com",
    description="Convert OpenAPI YAML file to Ceres files for code generation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/laulin/openapi2ceres",
    packages=["openapi2ceres"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'pyyaml'
    ], 
    scripts=['bin/openapi2ceres'],
)
