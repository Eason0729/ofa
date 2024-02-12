#!/bin/sh
export OTEL_PYTHON_LOGGING_AUTO_INSTRUMENTATION_ENABLED=true
opentelemetry-instrument \
    --traces_exporter otlp_proto_grpc \
    --metrics_exporter otlp_proto_grpc \
    --logs_exporter console,otlp_proto_grpc \
    --service_name dice-server \
    flask run -p 8080