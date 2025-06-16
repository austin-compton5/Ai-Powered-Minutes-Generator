from setuptools import setup, find_packages

setup(
    name="automated-notetaker",
    version="0.1.0",
    description="AI-Powered Meeting Minutes Generator",
    author="Austin Compton",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    include_package_data=True,
    install_requires=[],  # We'll point to requirements.txt manually
    python_requires=">=3.8",
)
