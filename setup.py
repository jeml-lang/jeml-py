try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name="jeml",
    version="1.0.1",
    description="A Python Library for JEML (Just Enough Markup Language)",
    long_description="A Python Library for JEML (Just Enough Markup Language)",
    author="Judah Caruso-Rodriguez",
    author_email="judah@tuta.io",
    url="https://github.com/jeml-lang/jeml-py",
    packages=["jeml", "jeml.engine"],
    package_dir={"jeml": "jeml"},
    license="MIT",
    python_requies=">=3.7.3",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python"
    ]
)
