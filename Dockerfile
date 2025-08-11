# Builder stage
FROM python:3.13-alpine3.22@sha256:37b14db89f587f9eaa890e4a442a3fe55db452b69cca1403cc730bd0fbdc8aaf AS builder

WORKDIR /app

ARG ENVIRONMENT=production

RUN apk update && apk upgrade --no-cache && apk add --no-cache \
    build-base \
    postgresql-dev

RUN pip install --upgrade pip setuptools --no-cache-dir

COPY requirements.txt requirements-dev.txt ./

RUN pip install --user --no-cache-dir -r requirements.txt --no-deps

RUN if [ "$ENVIRONMENT" != "production" ]; then pip3 install --user --no-cache-dir -r requirements-dev.txt --no-deps; fi

COPY . .

# Runtime stage
FROM python:3.13-alpine3.22@sha256:37b14db89f587f9eaa890e4a442a3fe55db452b69cca1403cc730bd0fbdc8aaf

WORKDIR /app
COPY --from=builder /root/.local /root/.local
COPY --from=builder /app /app

ENV PATH=/root/.local/bin:$PATH
ENV PYTHONUNBUFFERED=1

COPY run.sh /app/run.sh
RUN chmod +x /app/run.sh

CMD ["/app/run.sh"]
