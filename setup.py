from setuptools import setup, find_packages

setup(
    name='easy-openai',
    version='0.0.1',
    description='',
    author='Dongfu Jiang',
    author_email='dongfu.jiang@uwaterloo.ca',
    packages=find_packages(),
    url='https://github.com/jdf-prog/many-image-qa',
    install_requires=[
        "openai",
        "numpy",
        "tiktoken"
    ],
)