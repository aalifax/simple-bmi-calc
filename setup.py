import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="kalkulator_bmi",
    version="0.1",
    author="Muhammad Iqbal",
    author_email="miqbal020@hotmail.com",
    description="Paket ini berisi kalkulator yang berfungsi untuk menghitung BMI atau IMT",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Miqbal20/kalkulator_bmi",
    project_urls={
        "Website": "https://replit.com/@miqbal20",
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