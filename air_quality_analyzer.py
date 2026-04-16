class AirQualityAnalyzer:
    def __init__(self, air_quality_values):
        self._validate(air_quality_values)
        self.air_quality = air_quality_values
        self.avg_quality = sum(air_quality_values) / len(air_quality_values)

    def _validate(self, values):
        if not values:
            raise ValueError("Air quality list cannot be empty.")

        negative = [v for v in values if v < 0]
        if negative:
            raise ValueError(f"User entered negative values: {negative}. Air quality values must be non-negative.")

        out_of_range = [v for v in values if v > 500]
        if out_of_range:
            raise ValueError(f"Values out of AQI range (0-500): {out_of_range}")

    def quality_of_air(self):
        aqi = self.avg_quality

        if aqi <= 50:
            return "Good", "Air is clean. No health risk."
        elif aqi <= 100:
            return "Moderate", "Acceptable air. Minor risk for sensitive people."
        elif aqi <= 150:
            return "Unhealthy (Sensitive Groups)", "Children, elderly & asthma patients may be affected."
        elif aqi <= 200:
            return "Unhealthy", "Everyone may experience health effects."
        elif aqi <= 300:
            return "Very Unhealthy", "Serious health effects for everyone."
        else:
            return "Hazardous", "Emergency conditions! Affects all people."

    def report(self):
        category, implication = self.quality_of_air()
        print("=" * 80)
        print("        AIR QUALITY INDEX (AQI) REPORT")
        print("=" * 80)
        print(f"  Air Quality Values : {self.air_quality}")
        print(f"  Average AQI        : {self.avg_quality:.2f}")
        print(f"  AQI Category       : {category}")
        print(f"  Health Implication : {implication}")
        print("=" * 80)
if __name__ == "__main__":
    try:
        air_quality = eval(input("Enter air quality values (e.g. [120, 80, 200]): "))
        analyzer = AirQualityAnalyzer(air_quality)
        analyzer.report()

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")