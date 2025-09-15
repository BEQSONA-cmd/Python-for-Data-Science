import datetime


old = datetime.datetime(1970, 1, 1)
now = datetime.datetime.now()

diff = (now - old).total_seconds()

decimal = "{:,.4f}".format(diff)

scientific_notation = format(diff, ".2e")

print("Seconds since January 1, 1970: " +
      decimal + " or " + scientific_notation + " in scientific notation")

month = now.strftime("%b")
day = now.day
year = now.year

print(month, day, year)
