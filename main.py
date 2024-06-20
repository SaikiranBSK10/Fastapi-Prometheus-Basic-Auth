from fastapi import FastAPI
from starlette_exporter import PrometheusMiddleware, handle_metrics

app = FastAPI()

# Add middleware to expose metrics
app.add_middleware(PrometheusMiddleware)
app.add_route("/metrics", handle_metrics)

@app.get("/")
def read_root():
    return {"Hello": "World"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
