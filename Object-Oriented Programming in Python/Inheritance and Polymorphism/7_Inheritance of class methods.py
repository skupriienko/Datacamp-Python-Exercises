# Original from_str method for reference:
#     @classmethod
#     def from_str(cls, datestr):
#         year, month, day = map(int, datestr.split("-"))
#         return cls(year, month, day)

# Define an EvenBetterDate class and customize from_str
class EvenBetterDate(BetterDate):
    @classmethod
    def from_str(cls, datestr, format="YYYY-MM-DD"):
        if format == "YYYY-MM-DD":
            return BetterDate.from_str(datestr)
        elif format == "DD-MM-YYYY":
            day, month, year = map(int, datestr.split("-"))
            return cls(year, month, day)


# This code should run with no errors
ebd_str = EvenBetterDate.from_str('02-12-2019', format='DD-MM-YYYY')
print(ebd_str.year)
ebd_dt = EvenBetterDate.from_datetime(datetime.today())
print(ebd_dt.year)
