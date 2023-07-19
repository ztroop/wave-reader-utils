class Threshold:
    GREEN = "Good"
    YELLOW = "Fair"
    RED = "Poor"
    NONE = "N/A"
    WHITE = "Error"


class TempThreshold:
    RED = "Hot"
    GREEN = "Good"
    BLUE = "Cold"
    WHITE = "Error"


class Temperature(float):
    """Temperature is measured in celsius (°C), fahrenheit (°F) or kelvin (K)."""

    def __new__(cls, value):
        return super(Temperature, cls).__new__(cls, value)

    def __init__(self, value) -> None:
        self.celsius = value
        self.fahrenheit = self.celsius * 9 / 5 + 32
        self.kelvin = self.celsius + 273.15

    def threshold(self) -> str:
        if self.celsius > 50 or self.celsius < -20:
            _threshold = TempThreshold.WHITE
        elif self.celsius >= 25:
            _threshold = TempThreshold.RED
        elif self.celsius < 18:
            _threshold = TempThreshold.BLUE
        else:
            _threshold = TempThreshold.GREEN
        return _threshold


class Radon(float):
    """Radon is measured in becquerels per cubic meter (Bq/m3) or picocuries per litre (pCi/L)."""

    def __new__(cls, value):
        return super(Radon, cls).__new__(cls, value)

    def __init__(self, value) -> None:
        self.becquerels = value
        self.picocuries = self.becquerels / 37

    def threshold(self) -> str:
        if self.becquerels <= 0 or self.becquerels >= 9000:
            _threshold = Threshold.WHITE
        elif self.becquerels >= 150:
            _threshold = Threshold.RED
        elif self.becquerels < 100:
            _threshold = Threshold.GREEN
        else:
            _threshold = Threshold.YELLOW
        return _threshold


class Pressure(float):
    """Pressure is measured in hectopascals (hPa) or kilopascals (kPa)."""

    def __new__(cls, value):
        return super(Pressure, cls).__new__(cls, value)

    def __init__(self, value) -> None:
        self.hectopascals = value
        self.kilopascals = self.hectopascals / 10

    def threshold(self) -> str:
        if self.hectopascals < 800 or self.hectopascals > 1100:
            _threshold = Threshold.WHITE
        else:
            _threshold = Threshold.NONE
        return _threshold


class CO2(float):
    """CO2 is measured in parts per million (ppm) or parts per billion (ppb)."""

    def __new__(cls, value):
        return super(CO2, cls).__new__(cls, value)

    def __init__(self, value) -> None:
        self.parts_per_million = value
        self.parts_per_billion = self.parts_per_million * 1000

    def threshold(self) -> str:
        if self.parts_per_million <= 0 or self.parts_per_million > 30000:
            _threshold = Threshold.WHITE
        elif self.parts_per_million >= 1000:
            _threshold = Threshold.RED
        elif self.parts_per_million < 800:
            _threshold = Threshold.GREEN
        else:
            _threshold = Threshold.YELLOW
        return _threshold


class VOC(float):
    """VOC is measured in parts per billion (ppb) or parts per million (ppm)."""

    def __new__(cls, value):
        return super(VOC, cls).__new__(cls, value)

    def __init__(self, value) -> None:
        self.parts_per_billion = value
        self.parts_per_million = self.parts_per_billion / 1000

    def threshold(self) -> str:
        if self.parts_per_billion <= 0 or self.parts_per_billion >= 30000:
            _threshold = Threshold.WHITE
        elif self.parts_per_billion >= 2000:
            _threshold = Threshold.RED
        elif self.parts_per_billion < 250:
            _threshold = Threshold.GREEN
        else:
            _threshold = Threshold.YELLOW
        return _threshold


class PM(float):
    """Particulate matter is measured in micrograms per cubic meter of air (ug/m3)."""

    def __new__(cls, value):
        return super(PM, cls).__new__(cls, value)

    def __init__(self, value) -> None:
        self.microgram_per_cubic_meter = value

    def threshold(self) -> str:
        if self.microgram_per_cubic_meter <= 0:
            _threshold = Threshold.WHITE
        elif self.microgram_per_cubic_meter >= 25:
            _threshold = Threshold.RED
        elif self.microgram_per_cubic_meter < 10:
            _threshold = Threshold.GREEN
        else:
            _threshold = Threshold.YELLOW
        return _threshold


class Humidity(float):
    """Humidity is measured in relative humidity (%rH)."""

    def __new__(cls, value):
        return super(Humidity, cls).__new__(cls, value)

    def __init__(self, value) -> None:
        self.relative_humidity = value

    def threshold(self) -> str:
        if self.relative_humidity <= 0 or self.relative_humidity > 100:
            _threshold = Threshold.WHITE
        elif self.relative_humidity < 25.0 or self.relative_humidity >= 70.0:
            _threshold = Threshold.RED
        elif (self.relative_humidity < 70.0 and self.relative_humidity >= 60.0) or (
            self.relative_humidity < 30.0 and self.relative_humidity >= 25.0
        ):
            _threshold = Threshold.YELLOW
        else:
            _threshold = Threshold.GREEN
        return _threshold
