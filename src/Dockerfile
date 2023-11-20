FROM python:3.11.4-alpine as deps

WORKDIR /opt/build
COPY ./requirements.txt .
# SETTING UP VENV
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
# INSTALL DEPENDENCIES
RUN python -m pip install --upgrade pip
RUN python -m pip install --no-cache-dir -r ./requirements.txt


FROM python:3.11.4-alpine as builder

WORKDIR /app
COPY . /app/src
# VENV CONFIG
COPY --from=deps /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
# RUN APP
CMD ["python", "/app/src/main.py"]
