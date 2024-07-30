from setuptools import setup, find_packages

# Long description from README file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='aranizer',
    version='0.2.3',
    author='RIOTU Lab',
    author_email='riotu@psu.edu.sa',
    description='Aranizer: A Custom Tokenizer for Enhanced Arabic Language Processing',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/riotu-lab/aranizer',
    packages=find_packages(),  # Ensure this line is correct
    install_requires=[
        'transformers>=4.0.0',
        'sentence-transformers>=0.4.0'
    ],
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: Arabic',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Text Processing :: Linguistic',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    license='Apache 2.0',
    include_package_data=True,
    package_data={
        'aranizer': [
            'tokenizers/bpe/*.json',
            'tokenizers/sp/*.model',
        ],
    },
)
