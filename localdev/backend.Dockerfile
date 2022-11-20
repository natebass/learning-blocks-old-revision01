FROM python:3.9-slim-bullseye

ARG UID

RUN test "${UID}" || { echo "Failed to run with UID ${UID}"; exit 1; }
RUN apt update && apt install -y python3-pip curl
RUN pip3 install --upgrade pip
RUN useradd -m -s /bin/bash -u "${UID}" user
USER user
