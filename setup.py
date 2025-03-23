from setuptools import setup, find_packages

setup(
    name="tu_modelo_de_clientes_ramirez",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "termcolor",
    ],
    author="Darién Ramírez",
    author_email="ianshalaga@gmail.com",
    description="Segundo desafío entregable del curso de Python en modalidad Flex de CoderHouse.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/ianshalaga/TuModeloDeClientesRamirez",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
