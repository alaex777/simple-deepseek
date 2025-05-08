from setuptools import setup, find_packages

setup(
    name="simple-deepseek",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests>=2.31.0",
        "aiohttp>=3.9.0",
    ],
    author="Alexander Balashov",
    author_email="alaex77@gmail.com",
    description="A simple async and sync DeepSeek API client",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/alaex77/simple-deepseek",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
