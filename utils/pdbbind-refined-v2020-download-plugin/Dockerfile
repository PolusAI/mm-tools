FROM condaforge/mambaforge

ENV EXEC_DIR="/opt/executables"
ENV POLUS_LOG="INFO"
RUN mkdir -p ${EXEC_DIR}

RUN wget --no-clobber https://pdbbind.oss-cn-hangzhou.aliyuncs.com/download/PDBbind_v2020_refined.tar.gz
RUN tar -xvf PDBbind_v2020_refined.tar.gz
