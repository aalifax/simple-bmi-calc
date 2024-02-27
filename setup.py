import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="kalkulator_bmi",
    version="0.1",
    author="Aalifa",
    author_email="aalifa.amira@gmail.com",
    description="Paket ini berisi kalkulator yang berfungsi untuk menghitung BMI atau IMT",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/aalifax/simple-bmi-calc",
    project_urls={
        "Website": "https://github.com/aalifax/simple-bmi-calc",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta"
    ],
    # package_dir={"": "src"},
    # packages=setuptools.find_packages(where="src"),
    packages=setuptools.find_packages(),
    python_requires=">=3.7",
)
