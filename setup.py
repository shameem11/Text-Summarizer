import setuptools

name = "text_Summarizer"
version = "0.0.1"
author = "shameem11"
author_email = "shameeemmon.mk@gmail.com"
long_description = "A small example package"

setuptools.setup(
    name=name,
    version=version,
    author=author,
    author_email=author_email,
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        'pandas',
        'numpy',
        'nltk',
        'pyYAML',
        'torch',
        'transformers'
    ]
)
