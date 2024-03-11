# docker build -f Dockerfile -t mrbrandonwalker/torch_drug .

FROM condaforge/mambaforge

ENV EXEC_DIR="/opt/executables"
ENV POLUS_LOG="INFO"
RUN mkdir -p ${EXEC_DIR}

# Work directory defined in the base container
WORKDIR ${EXEC_DIR}

COPY pyproject.toml ${EXEC_DIR}
COPY VERSION ${EXEC_DIR}
COPY README.md ${EXEC_DIR}
COPY CHANGELOG.md ${EXEC_DIR}
# need this here because poetry install needs the src directory
COPY src ${EXEC_DIR}/src

# Install needed packages here
RUN pip3 install --upgrade pip
RUN pip3 install poetry
RUN poetry install

RUN pip3 install ${EXEC_DIR} --no-cache-dir
