"""
Holographic Horizon Shield V2 - Prototype
Minimal working version for testing and CI.
"""

import asyncio
import time
from typing import Tuple


class HolographicHorizonShield:
    """
    Lightweight stand-in for the full Horizon Shield.
    Provides the interface expected by test_shield.py.
    """

    def __init__(self, threshold: float = 9.62):
        self.threshold = threshold

    def calculate_mass(self, prompt: str) -> float:
        """
        Very simple mass estimation based on length and repetition.
        Used by the unit tests.
        """
        if not prompt:
            return 0.0

        # Basic heuristic: longer + more repetitive = higher mass
        length_factor = len(prompt) / 100.0
        unique_ratio = len(set(prompt.split())) / max(len(prompt.split()), 1)
        repetition_penalty = 1.0 / max(unique_ratio, 0.01)

        mass = length_factor * repetition_penalty * 0.15
        return min(mass, 50.0)  # Cap for safety

    async def evaluate_prompt_async(self, prompt: str) -> str:
        """
        Async evaluation used by the tarpit test.
        Returns "SINKHOLED" for high-mass prompts.
        """
        mass = self.calculate_mass(prompt)

        if mass >= self.threshold:
            # Simulate the tarpit delay
            await asyncio.sleep(0.15)
            return "SINKHOLED"

        return "SAFE"

    def full_horizon_scan(self, prompt: str) -> Tuple[bool, str]:
        """
        Synchronous version used by the interactive prototype.
        Returns (is_safe, reason)
        """
        mass = self.calculate_mass(prompt)
        if mass >= self.threshold:
            return False, f"Horizon breach detected (mass={mass:.2f})"
        return True, f"Prompt within safe horizon (mass={mass:.2f})"


# Simple interactive demo (optional)
if __name__ == "__main__":
    print("Holographic Horizon Shield v2 Activated")
    shield = HolographicHorizonShield()

    while True:
        print("\n" + "=" * 60)
        user_prompt = input("\nEnter prompt to scan (or 'quit' to exit): ")
        if user_prompt.lower() == "quit":
            print("Shield powering down... Horizon secure.")
            break

        safe, reason = shield.full_horizon_scan(user_prompt)
        print(f"\nVERDICT: {reason}")
        if not safe:
            print("Malicious input neutralized at the event horizon!")
