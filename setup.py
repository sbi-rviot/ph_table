import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name = 'pretty_html_table',
    version = '0.6.dev0',
    author="Renaud Viot",
    author_email="renaud.viot@simply-bi.com",
    description = 'Make pandas dataframe looking pretty again',
    long_description = long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sbi-rviot/ph_table",
    install_requires = ['pandas'],
    packages=['pretty_html_table'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        ],
    )

