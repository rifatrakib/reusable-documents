from setuptools import find_packages, setup

setup(
    name="pydantic-mongo-reusables",
    version="0.1",
    description=(
        "A collection of Pydantic models that can be reused and extended by anything that are built on top of pydantic."
    ),
    url="https://www.example.com/",
    author="Md Abdur Rakib",
    author_email="<Rakib.1508@outlook.com>",
    packages=find_packages(),
    install_requires=[
        "pydantic >= 1.10.5",
        "python-dotenv >= 0.10.4",
        "email-validator >= 1.0.3",
        "pydash >= 6.0.2",
        "python-decouple >= 3.7",
    ],
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
