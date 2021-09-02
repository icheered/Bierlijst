# Unable to use python:3.8-slim-buster; dependency-injector requires gcc
FROM python:3.9-buster

WORKDIR .

ENV PYTHONPATH=.

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | POETRY_HOME=/opt/poetry python && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry && \
    poetry config virtualenvs.create false

# Copy poetry.lock & pyproject.toml
COPY ./backend/poetry.lock .
COPY ./backend/pyproject.toml .

# Install dependencies
# ARG INSTALL_DEV=false
# RUN bash -c "if [ $INSTALL_DEV == 'true' ] ; then poetry install --no-root ; else poetry install --no-root --no-dev ; fi"
RUN bash -c "poetry install --no-root --no-dev"

# Copy source files
COPY ./backend .

RUN bash -c "ls"
# Start the service
CMD [ "python", "main.py"]