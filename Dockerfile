# Builder stage
FROM python:3.13-alpine@sha256:452682e4648deafe431ad2f2391d726d7c52f0ff291be8bd4074b10379bb89ff AS builder

WORKDIR /app

ARG ENVIRONMENT=production

RUN apk update && apk add --no-cache \
    build-base \
    postgresql-dev

COPY requirements.txt requirements-dev.txt ./

RUN pip install --user --no-cache-dir -r requirements.txt --no-deps

RUN if [ "$ENVIRONMENT" != "production" ]; then pip3 install --user --no-cache-dir -r requirements-dev.txt --no-deps; fi

COPY . .

# Runtime stage
FROM python:3.13-alpine@sha256:452682e4648deafe431ad2f2391d726d7c52f0ff291be8bd4074b10379bb89ff

WORKDIR /app
COPY --from=builder /root/.local /root/.local
COPY --from=builder /app /app

ENV PATH=/root/.local/bin:$PATH
ENV PYTHONUNBUFFERED=1

COPY run.sh /app/run.sh
RUN chmod +x /app/run.sh

CMD ["/app/run.sh"]
