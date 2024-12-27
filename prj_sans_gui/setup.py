from setuptools import setup, find_packages

setup(
    name="dev_2",  # Nom de votre package
    version="0.1.0",  # Version actuelle
    packages=find_packages(where="src"),  # Localisation des packages
    package_dir={"": "src"},  
    install_requires=[
        # Dépendances, si nécessaires, spécifiées dans requirements.txt
    ],
    description="dev2_jeux_de_plateau",
    author="Alex",
    author_email="Alexisjacobs@protonmail.com",
    url="https://github.com/Ajkll/DEV-2",  # URL du depot
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
