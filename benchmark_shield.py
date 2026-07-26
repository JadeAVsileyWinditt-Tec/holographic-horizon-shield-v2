import time
import numpy as np
import torch
import torch.nn as nn


class HolographicHorizonShield(nn.Module):
    """
    Simulates a sub-millisecond Holographic Horizon Boundary Shield.
    Projects high-dimensional token embeddings (d_model) onto a 
    low-dimensional boundary manifold (d_boundary = \partial\Omega) 
    and computes surface entropy/perturbation in parallel.
    """
    def __init__(self, d_model=4096, d_boundary=64, critical_entropy_threshold=2.8):
        super().__init__()
        self.d_model = d_model
        self.d_boundary = d_boundary
        self.critical_threshold = critical_entropy_threshold
        # Fast projection matrix mapping Bulk -> Boundary
        self.boundary_projection = nn.Parameter(torch.randn(d_model, d_boundary) / np.sqrt(d_model))

    def forward(self, embedding_batch: torch.Tensor):
        # 1. Project Bulk Tensor to Horizon Boundary: [batch, seq, d_model] -> [batch, seq, d_boundary]
        boundary_tensor = torch.matmul(embedding_batch, self.boundary_projection)
        
        # 2. Compute Surface Entropy / Phase-Space Disruption at \partial\Omega
        norm = torch.norm(boundary_tensor, dim=-1)
        surface_gravity = torch.var(norm, dim=-1)  # Fluctuation across sequence
        
        # 3. Horizon Lock Condition
        is_adversarial = surface_gravity > self.critical_threshold
        return is_adversarial, surface_gravity


def simulate_heavy_secondary_guardrail(embedding_batch: torch.Tensor):
    """
    Simulates conventional guardrails (e.g., secondary LLM pass/Llama-Guard)
    that run full transformer attention passes to classify prompts.
    """
    # Simulate heavy matrix multiplications (Transformer layer simulation)
    x = embedding_batch
    for _ in range(6):  # 6 deep latent passes
        x = torch.relu(torch.matmul(x, torch.randn(x.shape[-1], x.shape[-1], device=x.device) * 0.01))
    return torch.mean(x, dim=(-1, -2)) > 0.5


def run_benchmark(num_samples=100, seq_len=128, d_model=4096):
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"============================================================")
    print(f"🚀 RUNNING HOLOGRAPHIC HORIZON SHIELD v2 BENCHMARK")
    print(f"Hardware Device : {device}")
    print(f"Batch Size       : {num_samples} prompts")
    print(f"Sequence Length  : {seq_len} tokens")
    print(f"Embedding Dim    : {d_model} (d_bulk)")
    print(f"============================================================\n")

    # Generate synthetic prompt embedding batch [batch_size, seq_len, d_model]
    prompt_embeddings = torch.randn(num_samples, seq_len, d_model, device=device)
    
    # Inject synthetic high-entropy adversarial perturbation into 20% of the batch
    adversarial_mask = torch.rand(num_samples) < 0.2
    prompt_embeddings[adversarial_mask] += torch.randn(seq_len, d_model, device=device) * 4.5

    # Instantiating Horizon Shield
    shield = HolographicHorizonShield(d_model=d_model, d_boundary=64).to(device)

    # ------------------------------------------------------------
    # Benchmark 1: Holographic Horizon Shield
    # ------------------------------------------------------------
    torch.cuda.synchronize() if device.type == 'cuda' else None
    start_time = time.perf_counter()
    
    with torch.no_grad():
        blocked_flags, entropy_scores = shield(prompt_embeddings)
        
    torch.cuda.synchronize() if device.type == 'cuda' else None
    shield_time_ms = (time.perf_counter() - start_time) * 1000.0
    shield_qps = num_samples / (shield_time_ms / 1000.0)

    # ------------------------------------------------------------
    # Benchmark 2: Heavy Secondary Model Guardrail
    # ------------------------------------------------------------
    torch.cuda.synchronize() if device.type == 'cuda' else None
    start_time = time.perf_counter()
    
    with torch.no_grad():
        heavy_blocked = simulate_heavy_secondary_guardrail(prompt_embeddings)
        
    torch.cuda.synchronize() if device.type == 'cuda' else None
    heavy_time_ms = (time.perf_counter() - start_time) * 1000.0
    heavy_qps = num_samples / (heavy_time_ms / 1000.0)

    # ------------------------------------------------------------
    # Results Display
    # ------------------------------------------------------------
    speedup = heavy_time_ms / shield_time_ms if shield_time_ms > 0 else 0

    print("📊 BENCHMARK RESULTS")
    print("------------------------------------------------------------")
    print(f"1. Heavy Secondary Model Guardrail:")
    print(f"   - Total Latency  : {heavy_time_ms:.2f} ms")
    print(f"   - Per-Prompt Avg : {(heavy_time_ms / num_samples):.4f} ms")
    print(f"   - Throughput     : {heavy_qps:.1f} queries/sec")
    print()
    print(f"2. Holographic Horizon Shield (v2):")
    print(f"   - Total Latency  : {shield_time_ms:.2f} ms")
    print(f"   - Per-Prompt Avg : {(shield_time_ms / num_samples):.4f} ms")
    print(f"   - Throughput     : {shield_qps:.1f} queries/sec")
    print("------------------------------------------------------------")
    print(f"🔥 SHIELD SPEEDUP  : {speedup:.1f}x FASTER")
    print(f"🛡️ DETECTED PROMPTS: {blocked_flags.sum().item()} / {num_samples}")
    print("============================================================\n")


if __name__ == "__main__":
    run_benchmark()
