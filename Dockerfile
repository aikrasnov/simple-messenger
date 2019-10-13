FROM python:3.7

LABEL maintainer="aleksander.krasnoff2013@ya.ru"

RUN mkdir app
COPY . ./app
WORKDIR ./app
RUN pip install --no-cache-dir pipenv && \
    python --version && \
    pipenv install --ignore-pipfile

CMD ["pipenv", "run", "server"]
