def round_result(digits):
    def decorator(func):
        def wrapper(*args, **kwargs):
            return round(func(*args, **kwargs), digits)
        return wrapper
    return decorator


class SpaceAge:
    earth_seconds_in_year = 31557600
    orbital_periods = {"earth": 365.25,
                       "jupiter": 11.862615,
                       "mars": 1.8808158,
                       "mercury": 0.2408467,
                       "neptune": 164.79132,
                       "saturn": 29.447498,
                       "uranus": 84.016846,
                       "venus": 0.61519726}

    def __init__(self, seconds):
        self.seconds = seconds
        self.earth_years = self.seconds / SpaceAge.earth_seconds_in_year

    @round_result(2)
    def on_earth(self):
        return self.earth_years

    @round_result(2)
    def on_jupiter(self):
        return self.earth_years / SpaceAge.orbital_periods["jupiter"]

    @round_result(2)
    def on_mars(self):
        return self.earth_years / SpaceAge.orbital_periods["mars"]

    @round_result(2)
    def on_mercury(self):
        return self.earth_years / SpaceAge.orbital_periods["mercury"]

    @round_result(2)
    def on_neptune(self):
        return self.earth_years / SpaceAge.orbital_periods["neptune"]

    @round_result(2)
    def on_saturn(self):
        return self.earth_years / SpaceAge.orbital_periods["saturn"]

    @round_result(2)
    def on_uranus(self):
        return self.earth_years / SpaceAge.orbital_periods["uranus"]

    @round_result(2)
    def on_venus(self):
        return self.earth_years / SpaceAge.orbital_periods["venus"]
