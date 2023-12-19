from setuptools import setup, find_packages

setup(
    name='aranizer',
    version='0.1',
    packages=find_packages(),
    url='https://github.com/omarnj-lab/aranizer',
    license='MIT',
    author='omar najar',
    author_email='onajar@psu.edu.sa',
    description='Aranizer:A Custom Tokenizer for Enhanced Arabic Language Processing',
    install_requires=[
        'transformers',
        'sentence_transformers'
    ],
    include_package_data=True
)
