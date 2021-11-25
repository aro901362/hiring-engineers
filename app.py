
from opentelemetry import trace
from opentelemetry.exporter.datadog import (
    DatadogExportSpanProcessor,
    DatadogSpanExporter
)
from opentelemetry.sdk.trace import TracerProvider
trace.set_tracer_provider(TracerProvider())
trace.get_tracer_provider().add_span_processor(
    DatadogExportSpanProcessor(
        DatadogSpanExporter(
            agent_url="http://localhost:8126", service="dd_tracing_example"
        )
    )
)
tracer = trace.get_tracer(__name__)

with tracer.start_as_current_span("span_1"):
    with tracer.start_as_current_span("span_2"):
        with tracer.start_as_current_span("span_3"):
            print("Hello world from OpenTelemetry Python!")