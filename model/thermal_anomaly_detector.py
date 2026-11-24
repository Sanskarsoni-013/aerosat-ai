"""
Thermal Infrared Anomaly & Wildfire Detection Model
Analyzes brightness temperature gradients in multispectral bands (3.9µm and 11µm)
to isolate active fire perimeters, compute Fire Radiative Power (FRP), and assess spread risk.
"""

import numpy as np

class ThermalAnomalyDetector:
    def __init__(self, temp_threshold_kelvin=320.0, bg_delta_threshold=15.0):
        self.temp_threshold_kelvin = temp_threshold_kelvin
        self.bg_delta_threshold = bg_delta_threshold

    def compute_fire_radiative_power(self, fire_pixels_kelvin, bg_mean_kelvin, pixel_area_m2=14400.0):
        """
        Estimates Fire Radiative Power (FRP) in Megawatts (MW) using the Wooster Stefan-Boltzmann formulation:
        FRP = (A_pixel * sigma) / a * (T_fire^4 - T_bg^4)
        """
        sigma = 5.670374e-8  # W/(m^2 K^4)
        power_watts = pixel_area_m2 * sigma * (np.power(fire_pixels_kelvin, 4) - np.power(bg_mean_kelvin, 4))
        total_mw = np.sum(power_watts) / 1e6
        return max(0.0, float(total_mw))

    def detect_thermal_anomalies(self, thermal_matrix_kelvin):
        """
        Performs contextual anomaly detection over thermal infrared imagery.
        """
        bg_mean = np.mean(thermal_matrix_kelvin)
        bg_std = np.std(thermal_matrix_kelvin)

        # Contextual threshold: T > threshold AND T > (bg_mean + 3 * bg_std)
        fire_mask = (thermal_matrix_kelvin >= self.temp_threshold_kelvin) & \
                    (thermal_matrix_kelvin >= (bg_mean + 2.5 * bg_std))

        fire_pixel_count = int(np.sum(fire_mask))
        frp_megawatts = 0.0

        if fire_pixel_count > 0:
            fire_temps = thermal_matrix_kelvin[fire_mask]
            frp_megawatts = self.compute_fire_radiative_power(fire_temps, bg_mean)

        confidence_score = min(1.0, (fire_pixel_count / 100.0) + (frp_megawatts / 500.0)) if fire_pixel_count else 0.0

        return {
            "total_pixels_analyzed": int(thermal_matrix_kelvin.size),
            "active_fire_pixels": fire_pixel_count,
            "fire_radiative_power_mw": round(frp_megawatts, 2),
            "background_temp_kelvin": round(float(bg_mean), 1),
            "max_detected_temp_kelvin": round(float(np.max(thermal_matrix_kelvin)), 1),
            "anomaly_confidence": round(confidence_score, 3),
            "threat_level": "CRITICAL" if frp_megawatts > 100 else ("HIGH" if fire_pixel_count > 10 else "NORMAL")
        }

if __name__ == "__main__":
    # Test simulation
    np.random.seed(42)
    # Background terrain 295K (~22°C), with active wildfire hotspot at 380K (~107°C)
    sim_thermal = np.random.normal(295.0, 3.5, (100, 100))
    sim_thermal[45:52, 48:55] += np.random.uniform(70.0, 110.0, (7, 7))

    detector = ThermalAnomalyDetector()
    results = detector.detect_thermal_anomalies(sim_thermal)

    print("=" * 60)
    print("AeroSat AI - Thermal Infrared Wildfire Analysis")
    print("=" * 60)
    for k, v in results.items():
        print(f" {k:<28}: {v}")
    print("=" * 60)
