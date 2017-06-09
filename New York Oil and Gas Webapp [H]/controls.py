# flake8: noqa

# In[]:
# Controls for webapp
COUNTIES = {
    '001': 'Albany',
    '003': 'Allegany',
    '005': 'Bronx',
    '007': 'Broome',
    '009': 'Cattaraugus',
    '011': 'Cayuga',
    '013': 'Chautauqua',
    '015': 'Chemung',
    '017': 'Chenango',
    '019': 'Clinton',
    '021': 'Columbia',
    '023': 'Cortland',
    '025': 'Delaware',
    '027': 'Dutchess',
    '029': 'Erie',
    '031': 'Essex',
    '033': 'Franklin',
    '035': 'Fulton',
    '037': 'Genesee',
    '039': 'Greene',
    '041': 'Hamilton',
    '043': 'Herkimer',
    '045': 'Jefferson',
    '047': 'Kings',
    '049': 'Lewis',
    '051': 'Livingston',
    '053': 'Madison',
    '055': 'Monroe',
    '057': 'Montgomery',
    '059': 'Nassau',
    '061': 'New York',
    '063': 'Niagara',
    '065': 'Oneida',
    '067': 'Onondaga',
    '069': 'Ontario',
    '071': 'Orange',
    '073': 'Orleans',
    '075': 'Oswego',
    '077': 'Otsego',
    '079': 'Putnam',
    '081': 'Queens',
    '083': 'Rensselaer',
    '085': 'Richmond',
    '087': 'Rockland',
    '089': 'St. Lawrence',
    '091': 'Saratoga',
    '093': 'Schenectady',
    '095': 'Schoharie',
    '097': 'Schuyler',
    '099': 'Seneca',
    '101': 'Steuben',
    '103': 'Suffolk',
    '105': 'Sullivan',
    '107': 'Tioga',
    '109': 'Tompkins',
    '111': 'Ulster',
    '113': 'Warren',
    '115': 'Washington',
    '117': 'Wayne',
    '119': 'Westchester',
    '121': 'Wyoming',
    '123': 'Yates'
 }

WELL_STATUSES = dict(
    AC = 'Active',
    AR = 'Application Received to Drill/Plug/Convert',
    CA = 'Cancelled',
    DC = 'Drilling Completed',
    DD = 'Drilled Deeper',
    DG = 'Drilling in Progress',
    EX = 'Expired Permit',
    IN = 'Inactive',
    NR = 'Not Reported on AWR',
    PA = 'Plugged and Abandoned',
    PI = 'Permit Issued',
    PB = 'Plugged Back',
    PM = 'Plugged Back Multilateral',
    RE = 'Refunded Fee',
    RW = 'Released - Water Well',
    SI = 'Shut-In',
    TA = 'Temporarily Abandoned',
    TR = 'Transferred Permit',
    UN = 'Unknown',
    UL = 'Unknown Located',
    UM = 'Unknown Not Found',
    VP = 'Voided Permit',
)

WELL_TYPES = dict(
     BR = 'Brine',
     Confidential = 'Confidential',
     DH = 'Dry Hole',
     DS = 'Disposal',
     DW = 'Dry Wildcat',
     GD = 'Gas Development',
     GE = 'Gas Extension',
     GW = 'Gas Wildcat',
     IG = 'Gas Injection',
     IW = 'Oil Injection',
     LP = 'Liquefied Petroleum Gas Storage',
     MB = 'Monitoring Brine',
     MM = 'Monitoring Miscellaneous',
     MS = 'Monitoring Storage',
     NL = 'Not Listed',
     OB = 'Observation Well',
     OD = 'Oil Development',
     OE = 'Oil Extension',
     OW = 'Oil Wildcat',
     SG = 'Stratigraphic',
     ST = 'Storage',
     TH = 'Geothermal',
     UN = 'Unknown',
)
