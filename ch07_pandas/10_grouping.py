"""
     10_grouping.py:

    The following reads from a data file (csv) using read_csv() and establishes columns
    afterwards.

    It illustrates grouping of records by state using groupby() and extracting
    specified records from each group using nth().

    size() provides the sizes of each group.



     Data from the file:
     Bob Green,          4517 Elm St. Riverside,                 NJ, 08075,301,356-8921,bob@abc.com,            ABC Inc.,                       President
     Violet Smith,       220 E. Main Ave Philadelphia,           PA, 09119,202,421-9008,ssmithj@hypex.org,      FakeCo Inc.,                    Janitor
     John Brown,         231 Oak Blvd. Black Hills,              SD, 82101,719,303-1219,vivoj@wandergem.com,    Wandergem LLC,                  Sr. Analyst
     Ed Blumenthal,      3012 Briarwood Ln. Denver,              CO, 80101,719,422-8091,ep20002@gmail.com,      Hanibow & Delite,               Programmer
     Rosey Englund,      1818 Mockingbird Ln. Aurora,            CO, 82101,719,286-1920,ke7001@yahoo.com,       Wadlow Inc.,                    Administrative Lead
     Tori Gray,          2218 Masengild Ave.,                    NJ, 08075,301,338-6571,tjames@acme.com,        Acme Inc.,                      Inventor
     Lisa Black,         89 Prince Dr. Philadelphia,             PA, 09119,202,419-0650,victors89@glaser.org,   Glaser Properties LLC.,         Manager
     Tom Redford,        2323 Nicholas St. Newark,               NJ, 07101,862,227-8022,tom.redford@gmail.com,  Illustrative Studio Systems,    Graphics Engineer
     Sally White,        3345 Spruce Cir. Harrisburg,            PA, 17105,717,429-1217,swhope@ggworth.com,     Bond Appliances,                Administrative Specialist
     Goldy Simpson,      4430 Mountainside Creek Rd Custer,      SD, 57730,605,689-3131,simpson@yahoo.com,      Crater Construction,            Owner
     O. Range,           1703 Treeline Dr. Denver,               CO, 80101,719,429-1356,ffnine27@hotmail.com,   n/a,                            Retired
     Sil Verna,          557 Pine Ave Aurora                     CO, 82101,719,286-1920,sil@yahoo.com,          Music Enthusiasts,              Salesperson
     Pinky Tuscadero,    601 Sapling Blvd.,                      NJ, 08501,609,227-6001,pinky@freedom.net,      Self-employed,                  Vocal Artist
     Hazel Sanford,      27 Musket Dr. Pittsburg,                PA, 15201,412,389-7711,hazel@outlook.com,      Bourne Legal Associates,        Paralegal
"""
import pandas as pd
contacts = pd.read_csv('contacts2.dat', header=None,
                       names=['name', 'address', 'state', 'zip', 'area_code', 'phone', 'email', 'company', 'position'],
                       converters={'state': lambda txt: txt.strip()})

print(contacts.head(3))

bystate = contacts.groupby('state')

print(bystate.groups)                           # {'SD': [2, 9], 'PA': [1, 6, 8, 13], 'NJ': [0, 5, 7, 12], 'CO': [3, 4, 10, 11]}

print(bystate.nth(1))                                                            # address   ...       zip
                                                # state                                      ...
                                                #  CO          1818 Mockingbird Ln. Aurora   ...     82101
                                                #  NJ                  2218 Masengild Ave.   ...     08075
                                                #  PA           89 Prince Dr. Philadelphia   ...     09119
                                                #  SD    4430 Mountainside Creek Rd Custer   ...     57730

print(bystate.nth(1)['name'])                   # state
                                                # CO    Rosey Englund
                                                # NJ        Tori Gray
                                                # PA       Lisa Black
                                                # SD    Goldy Simpson
                                                # Name: name, dtype: object


print(bystate.size())                           # state
                                                # CO    4
                                                # NJ    4
                                                # PA    4
                                                # SD    2
                                                # dtype: int64


print(bystate.indices)                          # {' NJ': array([ 0,  5,  7, 12], dtype=int64), ' CO': array([ 3,  4, 10, 11], dtype=int64), ' PA': array([ 1,  6,  8, 13], dtype=int64), ' SD': array([2, 9], dtype=int64)}


print(bystate.first())                          #                 name                       address     zip area_code  phone                email            company     position
                                                # state
                                                #  CO    Ed Blumenthal     3012 Briarwood Ln. Denver   80101       719  422-8091    ep20002@gmail.com   Hanibow & Delite   Programmer
                                                #  NJ        Bob Green        4517 Elm St. Riverside   08075       301  356-8921          bob@abc.com           ABC Inc.    President
                                                #  PA     Violet Smith  220 E. Main Ave Philadelphia   09119       202  421-9008    ssmithj@hypex.org        FakeCo Inc.      Janitor
                                                #  SD       John Brown     231 Oak Blvd. Black Hills   82101       719  303-1219  vivoj@wandergem.com      Wandergem LLC  Sr. Analyst

print(bystate.get_group('CO'))                  #                         address area_code   ...               position     zip
                                                # 3     3012 Briarwood Ln. Denver       719   ...             Programmer   80101
                                                # 4   1818 Mockingbird Ln. Aurora       719   ...    Administrative Lead   82101
                                                # 10     1703 Treeline Dr. Denver       719   ...                Retired   80101
                                                # 11          557 Pine Ave Aurora       719   ...            Salesperson   82101

colorado = bystate.get_group('CO')
print(colorado[colorado['zip'] == 82101])