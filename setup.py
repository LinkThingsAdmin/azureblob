import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='azureblob',
    version='0.0.1',
    author='Jay van den Bos',
    author_email='jay@linkthings.com',
    description='Package for syncing with Azure Blob',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/LinkThingsAdmin/azureblob',
    project_urls={
        "Bug Tracker": "https://github.com/LinkThingsAdmin/azureblob/issues"
    },
    license='MIT',
    packages=['azureblob'],
    install_requires=['requests'],
)
