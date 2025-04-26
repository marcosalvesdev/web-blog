# Builder stage
FROM python:3.13-alpine@sha256:18159b2be11db91f84b8f8f655cd860f805dbd9e49a583ddaac8ab39bf4fe1a7 AS builder

WORKDIR /app

ARG ENVIRONMENT=production

RUN apk update && apk add --no-cache \
    build-base \
    postgresql-dev

COPY requirements.txt requirements-dev.txt ./

RUN pip install --user --no-cache-dir -r requirements.txt

RUN if [ "$ENVIRONMENT" != "production" ]; then pip3 install --user --no-cache-dir -r requirements-dev.txt; fi

COPY . .

# Runtime stage
FROM python:3.13-alpine@sha256:18159b2be11db91f84b8f8f655cd860f805dbd9e49a583ddaac8ab39bf4fe1a7

WORKDIR /app
COPY --from=builder /root/.local /root/.local
COPY --from=builder /app /app

ENV PATH=/root/.local/bin:$PATH
ENV PYTHONUNBUFFERED=1

COPY run.sh /app/run.sh
RUN chmod +x /app/run.sh

CMD ["/app/run.sh"]
