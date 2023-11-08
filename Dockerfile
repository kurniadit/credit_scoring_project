FROM python:3.10.8-bullseye AS venv
COPY requirement.txt /
RUN pip install \
        --upgrade \
        --root-user-action=ignore \
        pip && \
    pip install \
        --no-cache-dir \
        --upgrade \
        --root-user-action=ignore \
        --target=/opt/venv/ \
        -r requirement.txt

FROM python:3.10.8-bullseye
COPY --from=venv /opt/venv/ /opt/venv/
ENV PYTHONPATH $PYTHONPATH:/opt/venv/
COPY . /app/
WORKDIR /app/
