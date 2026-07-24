"""
Holographic Horizon Shield V2 (HHS-V2) - Core Geometric Engine
Author: Jade Siley-Winditt (Phoenixrisingseer)
Description: Provides physical-world mathematical proxy gating using 
             Kepler's Third Law and a Syntactic Damping Coefficient.
"""

import math
import logging
from typing import Dict, Tuple

# Initialize telemetry logging
logger = logging.getLogger("horizon_shield.geometric_engine")

class GeometricEngine:
    def __init__(self, target_threshold: float = 9.62, gamma: float = 2.0):
        """
        Initializes the Core Astrophysical Calculation Engine.
        
        :param target_threshold: Event Horizon Threshold in Solar Masses (M_sun)
        :param gamma: Normalisation scale constant for syntactic damping calibration
        """
        self.THRESHOLD_M_SUN = target_threshold
        self.GAMMA = gamma
        
        # The Orbital Constant (T): Locked to Gaia BH1's companion star orbital period (years)
        self.ORBITAL_CONSTANT_T = 185.59 / 365.25
        
        # Hardcoded structural characters indicative of programming code bases
        self.SYNTAX_CHARS = set("{}[]();._/\\=+:*&%!#<>|\t")

    def calculate_payload_metrics(self, payload: str) -> Dict[str, float]:
        """
        Evaluates the incoming text array payload through the Keplerian proxy engine.
        
        :param payload: The raw input text string from the client request
        :return: Dictionary containing calculated metrics: variance, kappa, a, and mass
        """
        if not payload:
            return {"variance": 0.0, "kappa": 0.0, "scale_factor": 5.0, "a": 1.0, "mass": 0.0}

        total_length = len(payload)
        
        # 1. Structural Token Profiler: Calculate character distribution variance
        char_counts: Dict[str, int] = {}
        syntax_count = 0
        
        for char in payload:
            char_counts[char] = char_counts.get(char, 0) + 1
            if char in self.SYNTAX_CHARS:
                syntax_count += 1

        variance = sum((count / total_length) ** 2 for count in char_counts.values())
        
        # 2. Syntactic Damping Layer (kappa): Caps code density influence at 2.5 maximum
        raw_syntax_ratio = syntax_count / total_length
        kappa = min(2.5, self.GAMMA * raw_syntax_ratio)
        
        # 3. Text Variance Scale Factor Modification
        # High structural code elements lower the scale factor to prevent false positive triggers
        scale_factor = 5.0 / (1.0 + kappa)
        a = 1.0 + (variance * scale_factor)
        
        # 4. Keplerian Core Engine Calculation (M = a³ / T²)
        mass = (a ** 3) / (self.ORBITAL_CONSTANT_T ** 2)
        
        return {
            "variance": variance,
            "kappa": kappa,
            "scale_factor": scale_factor,
            "a": a,
            "mass": mass
        }

    def evaluate_boundary_scan(self, payload: str) -> Tuple[bool, Dict[str, float]]:
        """
        Executes a deterministic perimeter scan on the incoming payload data array.
        
        :param payload: The raw input text string from the client request
        :return: Tuple of (is_breached, metrics)
        """
        metrics = self.calculate_payload_metrics(payload)
        mass = metrics["mass"]
        
        if mass >= self.THRESHOLD_M_SUN:
            logger.warning(
                f"[HORIZON_BREACH] Payload calculated mass {mass:.4f} M_sun "
                f"exceeded threshold of {self.THRESHOLD_M_SUN} M_sun. (kappa: {metrics['kappa']:.2f})"
            )
            return True, metrics
            
        logger.info(
            f"[BOUNDARY_PASSED] Payload mass {mass:.4f} M_sun is within safe limits. "
            f"(kappa: {metrics['kappa']:.2f}, scale_factor: {metrics['scale_factor']:.2f})"
        )
        return False, metrics
