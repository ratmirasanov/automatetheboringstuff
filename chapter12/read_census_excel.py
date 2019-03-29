#! python3
# read_census_excel.py -- Tabulates population and number of census tracts for
# each county.

import pprint
import openpyxl


print("Opening workbook...")
WB = openpyxl.load_workbook("./chapter12/censuspopdata.xlsx")
SHEET = WB.get_sheet_by_name("Population by Census Tract")
COUNTY_DATA = {}

print("Reading rows...")

for row in range(2, SHEET.max_row + 1):

    # Each row in the spreadsheet has data for one census tract.
    state = SHEET["B" + str(row)].value
    county = SHEET["C" + str(row)].value
    pop = SHEET["D" + str(row)].value

    # Make sure the key for this state exists.
    COUNTY_DATA.setdefault(state, {})
    # Make sure the key for this county in this state exists.
    COUNTY_DATA[state].setdefault(county, {"tracts": 0, "pop": 0})

    # Each row represents one census tract, so increment by one.
    COUNTY_DATA[state][county]["tracts"] += 1
    # Increase the county pop by the pop in this census tract.
    COUNTY_DATA[state][county]["pop"] += int(pop)

# Open a new text file and write the contents of COUNTY_DATA to it.
print("Writing results...")
RESULT_FILE = open("./chapter12/census2010.py", "w")
RESULT_FILE.write("ALL_DATA = " + pprint.pformat(COUNTY_DATA))
RESULT_FILE.close()
print("Done.")
