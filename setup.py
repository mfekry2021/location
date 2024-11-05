from setuptools import setup, find_packages

setup(
    name='feko-location',  # Name of the package
    version='0.1.1.3',
    packages=find_packages(),
    description='A description of your package',
    author='Your Name',
    author_email='youremail@example.com',
    url='https://github.com/mfekry2021/location',
    install_requires=[
        "requests",
    ],
)
