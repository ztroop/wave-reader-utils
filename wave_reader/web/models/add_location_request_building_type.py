from enum import Enum


class AddLocationRequestBuildingType(str, Enum):
    SCHOOL = "SCHOOL"
    RESIDENTIAL = "RESIDENTIAL"
    APARTMENT = "APARTMENT"
    KINDERGARTEN = "KINDERGARTEN"
    HEALTHCENTER = "HEALTHCENTER"
    OFFICE = "OFFICE"
    OTHER = "OTHER"

    def __str__(self) -> str:
        return str(self.value)
