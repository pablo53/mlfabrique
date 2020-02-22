import setuptools

with open("README.md", "r") as freadme:
    long_desc = freadme.read()

setuptools.setup(
    name='nnmodel',
    version='1.0.0',
    author='Paweł A. Ryszawa',
    author_email='pablo53@poczta.onet.eu',
    description='ML Fabrique',
    long_description=long_desc,
    long_description_content_type='text/markdown',
    url='https://github.com/pablo53/mlfabrique/src',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
        "Operating System :: OS Independent"
    ],
    python_requires='>=3.7'
)
