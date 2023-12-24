# cookiecutter 

## Features
Python 3.10+
Git integration
Python preset functions
## Requirements
Anaconda >= 4.x
git >= 2.x
Cookiecutter Python package >= 2.5.0:
You could install cookiecutter depending on how you manage your Python packages (pip or conda), follow the code below:

pip:
```sh
pip install cookiecutter
```
conda:
```sh
conda install -c conda-forge cookiecutter
```
## Directories Distribution
```sh
.
├── README.md
├── cookiecutter.json
├── environment.yml
├── hooks
│   ├── post_gen_project.py
│   └── pre_gen_project.py
└── {{ cookiecutter.project_slug }}
    ├── README.md
    ├── data
    │   ├── processed
    │   └── raw
    ├── environment.yml
    └── notebooks
        └── 0.0-{{ cookiecutter.project_slug }}-introduction.ipynb
```

## Usage
In the directory that you create for the project, execute in terminal:

```sh
cookiecutter https://github.com/bry4nvq/cookiecutter-personal
```
## Credits
This project was made it in base of:

[Platzi](https://platzi.com/new-home/) Configuración Profesional de Entorno de Trabajo para Ciencia de Datos course by [Jesús Vélez Santiago](https://github.com/jvelezmagic)

[Cookiecutter Data Science](https://github.com/drivendata/cookiecutter-data-science) repository by [Driven Data](https://github.com/drivendata)