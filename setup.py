from pathlib import Path
from setuptools import setup, find_packages

HERE = Path(__file__).parent
README = (HERE / 'README.md').read_text(encoding="utf8")

setup(
    name = 'bubbleprint',
    version = '0.0.1',
    author = 'Brian K. Blaylock',
    author_email = "blaylockbk@gmail.com",
    description = "Give your print statements personality",
    long_description = README,
    long_description_content_type = 'text/markdown',
    project_urls = {
        'Source Code': 'https://github.com/blaylockbk/BubblePrint',
    },
    license = "MIT",
    packages = find_packages(),
    package_data = {
        "": ['*.cfg'],
    },
    python_requires=">=3.8",
    install_requires = [],
    keywords = ['python', 'print'],
    classifiers = [
        "Programming Language :: Python",
    ],
    zip_safe = False,
)

###############################################################################
## Brian's Note: How to upload a new version to PyPI
## -------------------------------------------------
# Created a new conda environment with twine
# conda create -n pypi python=3 twine pip -c conda-forge
'''
conda activate pypi
cd BubblePrint
python setup.py sdist bdist_wheel
twine check dist/*

# PyPI
twine upload --skip-existing dist/*

# Test PyPI
twine upload --skip-existing --repository-url https://test.pypi.org/legacy/ dist/*
'''
