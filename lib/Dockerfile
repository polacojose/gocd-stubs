FROM python:3.12-slim AS tester

WORKDIR /app

COPY requirements.txt ./
COPY dev-requirements.txt ./

RUN pip install -r requirements.txt
RUN pip install -r dev-requirements.txt

COPY . .

RUN pytest tests -v

#--- 

FROM mcr.microsoft.com/playwright/python:v1.60.0-noble as builder

WORKDIR /app

COPY --from=tester /app/requirements.txt ./requirements.txt

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD fastapi run
