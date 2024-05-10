# docker build -f Dockerfile -t mrbrandonwalker/openbabel-tool .
FROM condaforge/mambaforge
# NOT mambaforge-pypy3 (openbabel is incompatible with pypy)
RUN mamba install -c conda-forge openbabel
