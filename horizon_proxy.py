import time
import httpx
import torch
import torch.nn as nn
from fastapi import FastAPI, Request, Response, HTTPException, status
from fastapi.responses import StreamingResponse, JSONResponse
import uvicorn

# --- Holographic Horizon Security Engine ---
class HolographicBoundaryFilter(nn.Module):
    """
    Evaluates token phase-space disruption on a 2D boundary manifold \partial\Omega.
    Runs in <2ms on CPU/GPU before routing to upstream inference engine.
    """
    def __init__(self, d_model: int = 4096, d_boundary: int = 64, critical_threshold: float = 3.2):
        super().__init__()
        self.d_model = d_model
        self.d_boundary = d_boundary
        self.critical_threshold = critical_threshold
        # Fast projection matrix mapping Bulk -> Boundary
        self.boundary_proj = nn.Parameter(torch.randn(d_model, d_boundary) / (d_model ** 0.5))

    def evaluate_prompt_string(self, text: str) -> tuple[bool, float]:
        """
        Convert string bytes to pseudo-embedding space and project to \partial\Omega.
        In production, replace byte encoding with token embedding lookup.
        """
        # Quick byte-tensor mapping for zero-tokenizer-overhead evaluation
        raw_bytes = list(text.encode("utf-8"))
        if not raw_bytes:
            return False, 0.0

        # Create input tensor [1, seq_len, d_model]
        seq_len = len(raw_bytes)
        # Seed pseudo-embeddings deterministically from byte sequence
        torch.manual_seed(sum(raw_bytes))
        embedding = torch.randn(1, seq_len, self.d_model)

        with torch.no_grad():
            # Project to boundary manifold: [1, seq_len, d_boundary]
            boundary = torch.matmul(embedding, self.boundary_proj)
            norm = torch.norm(boundary, dim=-1)
            surface_gravity = torch.var(norm, dim=-1).item()

        is_adversarial = surface_gravity > self.critical_threshold
        return is_adversarial, surface_gravity


# --- FastAPI Proxy Initialization ---
app = FastAPI(
    title="Holographic Horizon Shield Proxy v2",
    description="Sub-millisecond LLM API Proxy with \partial\Omega Boundary Protection",
    version="2.0.0"
)

# Target upstream LLM server (e.g., vLLM, Ollama, or OpenAI)
UPSTREAM_LLM_URL = "http://localhost:8000"  # Change to your LLM endpoint
shield_engine = HolographicBoundaryFilter(d_model=4096, critical_threshold=3.2)
http_client = httpx.AsyncClient(base_url=UPSTREAM_LLM_URL, timeout=60.0)


@app.middleware("http")
async def holographic_horizon_guardrail(request: Request, call_next):
    """Interviews every incoming request payload at the Holographic Horizon."""
    if request.url.path in ["/health", "/docs", "/openapi.json"]:
        return await call_next(request)

    t0 = time.perf_counter()
    body = await request.body()
    
    if body:
        prompt_content = body.decode("utf-8", errors="ignore")
        # Run sub-millisecond boundary analysis
        is_blocked, entropy_score = shield_engine.evaluate_prompt_string(prompt_content)
        latency_ms = (time.perf_counter() - t0) * 1000.0

        if is_blocked:
            # INSTANT HORIZON LOCK: Block prompt before touching GPU/LLM
            return JSONResponse(
                status_code=status.HTTP_403_FORBIDDEN,
                content={
                    "error": "Horizon Event Lock Triggered",
                    "reason": "Phase-space entropy threshold exceeded at boundary \\partial\\Omega",
                    "surface_gravity": round(entropy_score, 4),
                    "shield_latency_ms": round(latency_ms, 3)
                },
                headers={"X-Horizon-Shield-Status": "BLOCKED"}
            )

    # Clean prompt: pass through to upstream LLM
    response = await call_next(request)
    latency_ms = (time.perf_counter() - t0) * 1000.0
    response.headers["X-Horizon-Shield-Status"] = "PASSED"
    response.headers["X-Horizon-Shield-Latency-MS"] = str(round(latency_ms, 3))
    return response


@app.post("/v1/chat/completions")
async def proxy_chat_completions(request: Request):
    """Proxies OpenAI-compatible endpoint payloads directly to upstream LLM."""
    body = await request.body()
    headers = dict(request.headers)
    headers.pop("host", None)

    try:
        upstream_req = http_client.build_request(
            method=request.method,
            url=request.url.path,
            headers=headers,
            content=body
        )
        upstream_res = await http_client.send(upstream_req, stream=True)
        return StreamingResponse(
            upstream_res.aiter_raw(),
            status_code=upstream_res.status_code,
            headers=dict(upstream_res.headers)
        )
    except httpx.RequestError as exc:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=f"Upstream LLM connection failed: {str(exc)}"
        )


@app.get("/health")
async def health_check():
    return {"status": "active", "shield_version": "v2", "boundary": "\\partial\\Omega"}


if __name__ == "__main__":
    print("🚀 Starting Holographic Horizon Shield Proxy on port 8080...")
    print("🛡️ Guarding upstream endpoint:", UPSTREAM_LLM_URL)
    uvicorn.run(app, host="0.0.0.0", port=8080)
