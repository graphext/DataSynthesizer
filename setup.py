from setuptools import setup, find_packages

setup(
    name='datasynth',
    version='0.1.0',
    url='https://github.com/graphext/DataSynthesizer.git',
    author='Graphext',
    author_email='thomas@graphext.com',
    description='A fork of https://github.com/DataResponsibly/DataSynthesizer installable with pip.',
    packages=find_packages(),
    install_requires=[
        "numpy",
        "pandas",
        "scipy",
        "scikit-learn"
    ],
)
