from unittest import TestCase

from wave_reader import measure


class TestTemperature(TestCase):
    def test_temperature(self):
        temp = measure.Temperature(26.0)

        self.assertEqual(temp, 26.0)
        self.assertEqual(temp.celsius, 26.0)
        self.assertEqual(temp.fahrenheit, 78.8)

    def test_threshold(self):
        hot_temp = measure.Temperature(30.0).threshold()
        cold_temp = measure.Temperature(10.0).threshold()
        good_temp = measure.Temperature(21).threshold()

        self.assertEqual(hot_temp, measure.TempThreshold.RED)
        self.assertEqual(cold_temp, measure.TempThreshold.BLUE)
        self.assertEqual(good_temp, measure.TempThreshold.GREEN)


class TestRadon(TestCase):
    def test_radon(self):
        r = measure.Radon(50.0)

        self.assertEqual(r, 50.0)
        self.assertEqual(r, r.becquerels)
        self.assertEqual(round(r.picocuries, 2), 1.35)

    def test_threshold(self):
        good = measure.Radon(25.0).threshold()
        fair = measure.Radon(100.0).threshold()
        poor = measure.Radon(150.0).threshold()

        self.assertEqual(good, measure.Threshold.GREEN)
        self.assertEqual(fair, measure.Threshold.YELLOW)
        self.assertEqual(poor, measure.Threshold.RED)


class TestPressure(TestCase):
    def test_pressure(self):
        p = measure.Pressure(900.0)

        self.assertEqual(p, 900.0)
        self.assertEqual(p.hectopascals, 900.0)
        self.assertEqual(p.kilopascals, 90)

        self.assertEqual(p.threshold(), measure.Threshold.NONE)


class TestCO2(TestCase):
    def test_co2(self):
        co2 = measure.CO2(500.0)

        self.assertEqual(co2, 500.0)
        self.assertEqual(co2.parts_per_million, 500.0)
        self.assertEqual(co2.parts_per_billion, 500000.0)

    def test_threshold(self):
        good = measure.CO2(799).threshold()
        fair = measure.CO2(950).threshold()
        poor = measure.CO2(1000).threshold()

        self.assertEqual(good, measure.Threshold.GREEN)
        self.assertEqual(fair, measure.Threshold.YELLOW)
        self.assertEqual(poor, measure.Threshold.RED)


class TestVOC(TestCase):
    def test_voc(self):
        voc = measure.VOC(200.0)

        self.assertEqual(voc, 200.0)
        self.assertEqual(voc.parts_per_billion, 200.0)
        self.assertEqual(voc.parts_per_million, 0.2)

    def test_threshold(self):
        good = measure.VOC(249).threshold()
        fair = measure.VOC(500).threshold()
        poor = measure.VOC(2000.0).threshold()

        self.assertEqual(good, measure.Threshold.GREEN)
        self.assertEqual(fair, measure.Threshold.YELLOW)
        self.assertEqual(poor, measure.Threshold.RED)


class TestPM(TestCase):
    def test_pm(self):
        pm = measure.PM(5)

        self.assertEqual(pm, 5)
        self.assertEqual(pm.microgram_per_cubic_meter, 5)

    def test_threshold(self):
        good = measure.PM(9).threshold()
        fair = measure.PM(20).threshold()
        poor = measure.PM(25).threshold()

        self.assertEqual(good, measure.Threshold.GREEN)
        self.assertEqual(fair, measure.Threshold.YELLOW)
        self.assertEqual(poor, measure.Threshold.RED)


class TestHumidity(TestCase):
    def test_humidity(self):
        h = measure.Humidity(30.0)

        self.assertEqual(h, 30.0)
        self.assertEqual(h.relative_humidity, 30.0)

    def test_threshold(self):
        too_dry = measure.Humidity(10.0).threshold()
        too_wet = measure.Humidity(70.0).threshold()
        fair = measure.Humidity(60.0).threshold()
        good = measure.Humidity(40.0).threshold()

        self.assertEqual(too_dry, measure.Threshold.RED)
        self.assertEqual(too_wet, measure.Threshold.RED)
        self.assertEqual(fair, measure.Threshold.YELLOW)
        self.assertEqual(good, measure.Threshold.GREEN)
