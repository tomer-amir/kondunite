from setuptools import setup, find_packages

__version__ = '0.1.12'

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="kondunite",
    description="Kubernetes Conditional Manifests Unifier",
    long_description=long_description,
    long_description_content_type="text/markdown",
    version=__version__,
    author='ReallyLiri',
    url='https://github.com/ReallyLiri/kondunite',
    author_email='reallyliri@gmail.com',
    keywords='k8s kubernetes kustomize yaml yml manifest gke repl replicated',
    py_modules=['kondunite'],
    install_requires=[
        'Click',
        'ruamel.yaml',
        'toposort',
    ],
    python_requires='>=3.6',
    packages=find_packages(),
    entry_points='''
        [console_scripts]
        kondunite=kondunite:cli
    ''',
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
