from setuptools import find_packages, setup

setup(
    name="pydantic-mongo-reusables",
    version="0.1.2",
    description=(
        "A collection of Pydantic models that can be reused and extended by anything that are built on top of pydantic."
    ),
    url="https://www.example.com/",
    author="Md Abdur Rakib",
    author_email="<Rakib.1508@outlook.com>",
    packages=find_packages(),
    install_requires=[],
    keywords=["python"],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
    ],
)
