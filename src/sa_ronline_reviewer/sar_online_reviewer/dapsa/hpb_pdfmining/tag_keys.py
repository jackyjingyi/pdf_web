import os
import logging
BEGIN_KEYS = [
    'Parts Inventory',
]

END_KEYS = {
    'positive': [

    ],
    'negative': [

    ]
}

SKIP_KEYS = [
    'General Terms and Conditions of Business of TÜV Rheinland in Greater China \n',
]

INFO_KEYS = {
    'report_number': ['PrüfberichtNr Test Report No', 'PrüfberichtNr Test Report  No', 'Test Report No', 'Prüfbericht-Nr.:'],
    'protocol': ['Prüfgrundlage Test specification', 'Test specification'],
    'vendor_name': ['Vender Name'],
    'factory_name': ['Factory Name', 'Factory  Name'],
    'lab': ['TUV Rheinland', 'TÜV Rheinland'],
}

DATE_PATTERN = {
    'mm/dd/yyyy': "([1-9]|1[0-9]|2[0-9]|3[0-1])(.|-)(0[1-9]|1[0-2])(.|-|)(20[0-9][0-9])",
    'dd/mm/yyyy': "([1-9]|1[0-9]|2[0-9]|3[0-1])(.|-)([1-9]|1[0-2])(.|-|)(20[0-9][0-9])",
    'yyyy/mm/dd': "([0-9]{4})(-|/|.)(0[1-9]|1[0-2])(-|/|.)(0[1-9]|[1-2][0-9]|3[0-1])",
    'oo/dd/yyyy': "([a-zA-z]{3})(-|/|.)([1-9]|1[0-9]|2[0-9]|3[0-1])(-|/|.)([0-9]{4})",
}

FAILURE_SUMMARY = [
    'details of failure', 'failure summary',
]

FAILURE_KEYS = [
    'fail'
]

MONTH = {
    'Jan': 1,
    'Feb': 2,
    'Mar': 3,
    'Apr': 4,
    'May': 5,
    'Jun': 6,
    'Jul': 7,
    'Aug': 8,
    'Sep': 9,
    'Oct': 10,
    'Nov': 11,
    'Dec': 12,
}

PROTOCOLS = os.path.join(os.getcwd(), 'hpb_pdfmining/documents/protocols/tt1/')

LAB_INFO = {
    'TUV': {},
    'ITS': {},
    'BV': {},
}

BASIC_INFO = [
    {
        'item': 'report number',
        'keywords': ['Test Report No.:', 'Number:'],
        'force': None,
        'regex': [r'\w+'],
        'bbox':(1, 2, 3, 4)  # top 30 % of the page
    },
    {
        'item': 'protocol',
        'keywords': ['ax'],
        'force': ['PL_LUGGAGE',
                  'PL_Mattress_Crib_Infant',
                  'PL_Mattress_Pads',
                  'PL_MATTRESSES',
                  'PL_MOTOR_VEHICLE_CHARGED_DEVICES',
                  'PL_Non_Powered_Scooters_Child',
                  'PL_OFFICE_CHAIRS',
                  'PL_OFFICE_DESKS',
                  'PL_OFFICE_PRODUCTS_GENERAL_USE',
                  'PL_OUTDOOR_GRILL_MATS',
                  'PL_Bathseats_Infant',
                  'PL_OUTDOOR_HEATER_ELECTRIC',
                  'PL_OUTDOOR_HEATER_GAS',
                  'PL_OUTDOOR_POOL_GENERAL_USE',
                  'PL_OUTDOOR_POOL_MOTOR_OPERATED',
                  'PL_OUTDOOR_SEATING',
                  'PL_Outdoor_Tables',
                  'PL_PAPER_PRODUCTS',
                  'PL_PAPER_SHREDDERS',
                  'PL_PET_BEDS',
                  'PL_PET_FOOD_CONTACT',
                  'PL_Bathtubs_Infant',
                  'PL_PETS_GENERAL_USE',
                  'PL_PHONE_CHARGING_CABLES',
                  'PL_Playpens_Play_yards_Infant',
                  'PL_Portable_Bed_Rails_Child',
                  'PL_Rear_Mounted_Bicycle_Seats_Child',
                  'PL_Rockers_Infant',
                  'PL_Slings_Infant',
                  'PL_SPORTS_GENERAL_USE',
                  'PL_Stationary_Activity_Centers_Infant',
                  'PL_STORAGE_FURNITURES',
                  'PL_BATS_AND_RACQUETS',
                  'PL_Swings_Infant',
                  'PL_Teethers_Soothers_Filled_Infant',
                  'PL_TENTS',
                  'PL_TEXTILES_CHILD',
                  'PL_TEXTILES_GENERAL_USE',
                  'PL_TEXTILES_GENERAL_USE',
                  'PL_Toys_Child',
                  'PL_Toys_General_Use',
                  'PL_Tricycles_Child',
                  'PL_TV_ANTENNAS',
                  'PL_Walkers_Infant',
                  'PL_Beds_Toddler',
                  'PL_WEIGHTS',
                  'PL_WIRELESS_DEVICES',
                  'PL_WRITING_UTENSILS',
                  'PL_SAFES_AND_LOCKS',
                  'PL_binoculars_and_microscopes',
                  'PL_WATER_PLUMBING',
                  'PL_Chemical_Cleaners_and_Polishes',
                  'PL_car_battery_chargers',
                  'PL_Musical_Instruments',
                  'PL_auto_batteries',
                  'PL_Bicycle_Trailers_Child',
                  'PL_Sports_Protective_Equipments',
                  'PL_FIREARMS_SAFE',
                  'PL_MOTOR_OIL',
                  'PL_Heated_Car_Seat_Cushion',
                  'PL_WATER_HOSE',
                  'PL_WELDING_BRUSHES',
                  'PL_PPE_Gloves',
                  'PL_WELDING_GOGGLES_AND_REPLACEMENT_LENS',
                  'PL_AIR_FILTERS',
                  'PL_Bicycles_Child',
                  'PL_AIR_FITTINGS_AND_ATTACHMENTS',
                  'PL_AIR_GAUGES',
                  'PL_AIR_HOSES',
                  'PL_AIR_TOOLS_AND_ACCESSORIES',
                  'PL_DIGITAL_TIRE_GAUGE',
                  'PL_FLINT_STRIKER',
                  'PL_HAND_TOOLS',
                  'PL_MIG_TIPS_AND_ACCESSORIES',
                  'PL_MISC._STORAGE',
                  'RINGS',
                  'PL_Bicycles_General_Use',
                  'PL_SPRAY_GUNS_NOZZLES_AND_ACCESSORIES',
                  'PL_SURFACE_CLEANER',
                  'PL_3D_PRINTER_FILAMENT_V3',
                  'PL_Activity_Table',
                  'PL_AIR_CONDITIONER_COOLER',
                  'PL_Air',
                  'PL_Clothes',
                  'PL_Clothes',
                  'PL_CONSUMER_SOLAR_PANEL',
                  'PL_Digital',
                  'PL_Booster_Seats_Infant',
                  'PL_Dishwasher',
                  'PL_EMERGENCY_LIGHTING',
                  'PL_EXERCISE_EQUIPMENTS',
                  'PL_Gymnastic',
                  'PL_HAMMOCK',
                  'PL_INKJET_CARTRIDGE_TONER',
                  'PL_Junior',
                  'PL_LIGHT_SWITCHES',
                  'PL_Mercury',
                  'PL_PPE',
                  'PL_Bouncers_Jumpers_Infant',
                  'PL_Roof',
                  'PL_SLEEPING_BAG',
                  'PL_Spill',
                  'PL_TELEVISION_MONITORS_PROJECTORS',
                  'PL_WATER_FILTERS',
                  'PL_Wiper',
                  'PL_HEATED_AIRER',
                  'PL_DEHUMIDIFIER',
                  'PL_HUMIDIFIER',
                  'PL_STEAM_MOPS',
                  'PL_Candle_Holders',
                  'PL_ADHESIVES_GLUES_HOME_IMPROVEMENT',
                  'PL_STEAM_IRONS',
                  'PL_GLOW',
                  'PL_CAR_DEHUMIDIFIER',
                  'PL_MEASUREMENT_DEVICES',
                  'PL_COMMERCIAL_PUMP',
                  'PL_PET_LITTER',
                  'PL_AIR_BEDS',
                  'PL_STRAPS_ROPES_TIE',
                  'PL_WATER_PUMPS',
                  'PL_VACUUM_PUMPS',
                  'PL_Candles',
                  'PL_POWERED_PAINT_SPRAYER',
                  'PL_FIRE_PITS',
                  'PL_IT_STORAGE_DEVICES',
                  'PL_OUTDOOR_PLAYGROUND_EQUIPMENT',
                  'PL_COSMETIC_ACCESSORIES',
                  'PL_PERSONAL_PROTECTIVE_EQUIPMENT',
                  'PL_Car_Seats_and_Booster_Seats_Child',
                  'PL_CARPETS_RUGS',
                  'PL_Carriages_Strollers_Infant',
                  'PL_Carriers_Framed_Infant',
                  'PL_Carriers_Soft_sided_Infant',
                  'PL_CE_GENERAL_USE',
                  'PL_Changing_Pads_Infant',
                  'PL_Changing_Tables_Infant',
                  'PL_ADULT_BEDS',
                  'PL_CHARCOAL_BBQ',
                  'PL_CHILDREN_HEADPHONES',
                  'PL_CHRISTMAS_LIGHTS',
                  'PL_Constant_Air_Inflatables_Child',
                  'PL_CONSUMER_AUDIO_VIDEO_EQUIPMENTS',
                  'PL_CONSUMER_ELECTRICAL_PRODUCTS',
                  'PL_CONSUMER_FANS_VENTILATION',
                  'PL_CONSUMER_FLASHLIGHTS',
                  'PL_CONSUMER_ELECTRIC_PERSONAL_GROOMING',
                  'PL_CONSUMER_HAIR_DRYERS',
                  'PL_ART_SUPPLIES',
                  'PL_CONSUMER_HEADLAMPS',
                  'PL_CONSUMER_HEATING_DEVICES',
                  'PL_CONSUMER_IT_EQUIPMENTS',
                  'PL_CONSUMER_MOTOR_OPERATED_DEVICES',
                  'PL_Consumer_Non_Rechargeable_Batteries',
                  'PL_CONSUMER_POWER_ADAPTORS',
                  'PL_CONSUMER_POWER_OUTLETS',
                  'PL_CONSUMER_POWER_REFRIGERATORS',
                  'PL_CONSUMER_POWER_ROOM_HEATERS',
                  'PL_CONSUMER_POWER_TOOLS',
                  'PL_AUDIO_VIDEO_CABLES',
                  'PL_CONSUMER_POWER_WATER_HEATERS',
                  'PL_Consumer_Rechargeable_Batteries',
                  'PL_CONSUMER_VACUUM_CLEANERS',
                  'PL_CONSUMER_VACUUM_SEALERS',
                  'PL_Corded_Window_Coverings',
                  'PL_Cribs_Full_Sized_Infant',
                  'PL_CURTAINS',
                  'PL_EMC_DEVICES',
                  'PL_ETHERNET_PATCH_CABLES',
                  'PL_AUTO_BATTERY_BOOSTER_CABLES',
                  'PL_EXERCISE_MATS',
                  'PL_Expansion_Gates_Enclosures_Infant',
                  'PL_EXTENSION_POWER_CORDS',
                  'PL_Eyewear_Safety',
                  'PL_Feeding_Bottle_Nipples_Infant',
                  'PL_FUN_KARTS_CHILD',
                  'PL_Furniture_Upholstered_Child',
                  'PL_HEADLIGHTS',
                  'PL_HEADPHONES_GENERAL_USE',
                  'PL_AUTO_GENERAL_USE',
                  'PL_Helmets_Bicycle',
                  'PL_Helmets_Bicycle_Child',
                  'PL_Helmets_Motorcycle_Child',
                  'PL_Helmets_Motorcycle_General_Use',
                  'PL_Helmets_Safety',
                  'PL_Helmets_Sports_Protective',
                  'PL_High_Chairs_Infant',
                  'PL_HIGH_POWERED_MAGNET_SETS',
                  'PL_HOME_GENERAL_USE',
                  'PL_HOME_IMPROVEMENT_GENERAL_USE',
                  'PL_AUTOMOTIVE_POWER_ADAPTORS',
                  'PL_HOME_IMPROVEMENT_WEIGHT_BEARING',
                  'PL_Hook_on_Chairs_Infant',
                  'PL_Inclined_Sleepers_Infant',
                  'PL_INDOOR_SEATING',
                  'PL_INDOOR_TABLE',
                  'PL_Jewelry_Child',
                  'PL_Jewelry_General_Use',
                  'PL_KETTLES',
                  'PL_KITCHEN_GENERAL_USE',
                  'PL_BABY_MONITORS',
                  'PL_LAMPS_LUMINAIRES',
                  'PL_Lawn_Garden_Appliance_Electrical_Use',
                  'PL_Lawn_Garden_Appliance_Gas_Fired_Use',
                  'PL_Lawn_Garden_General_Use',
                  'PL_Lawn_Garden_Lighting_Electrical_Use',
                  'PL_Lawn_Garden_Tool_Electrical_Use',
                  'PL_Lawn_Garden_Tool_Petrol_Power_Use',
                  'PL_LAWNMOWERS',
                  'PL_LIGHTBULBS',
                  'PL_BALLS',
                  'PL_AUTO_RACKS', ],
    },
    {
        'item': 'vendor',
        'keywords': ['vendor#'],
    },
    {
        'item': 'factory',
        'keywords': ['factory#'],
    },
    {
        'item': 'lab',
        'keywords': ['TUV Rheinland', 'TÜV Rheinland'],
    },
    {
        'item': 'start',
        'keywords': [''],
    }
]


class BasicDict:
    data = BASIC_INFO
    keys = [i['item'] for i in data]

    def __init__(self, idx=0, key=None):
        if key:
            idx = BasicDict.keys.index(key)
        self.item = BasicDict.data[idx]['item']
        self.keywords = BasicDict.data[idx]['keywords']
        try:
            self.force = BasicDict.data[idx]['force']
        except KeyError:
            logging.warning("No force items for {%s}" % self.item)
            self.force = None

        try:
            self.regex = BasicDict.data[idx]['regex']
        except KeyError:
            logging.warning("No regex items for {%s}" % self.item)
            self.regex = None

        try:
            self.bbox = BasicDict.data[idx]['bbox']
        except:
            logging.warning("No bbox items for {%s}" % self.item)
            self.bbox = None

    def __iter__(self):
        # simple check
        for key, value in self.__dict__.items():
            print(key, value)


PATH = {
    'path': os.path.join(os.getcwd(), 'hpb_pdfmining/documents/reports/'),
    'sub_path': {4: '4columns/', 5: '56columns/', 6: '56columns/', 'cornerstone': 'others/', 'check': 'check/'},
}
# all country combinations in all tuv protocols
COUNTRY_LIST = ['US, CA', 'EU', 'United States/ Canada', 'United States; Mexico; Canada; European Union, Japan, India',
                'United States; Mexico; India; Canada; Japan; European Union; China', 'EU,US,CAN',
                'United States; Mexico; Canada; Japan; European, India', 'US', 'United States;',
                'France; Germany; Italy; Spain; United Kingdom',
                'United States; Mexico; Canada; Japan; European Union; India; Turkey',
                'United States; Mexico; Canada; Japan; European Union; India;', 'European Union', 'EU,US,CA',
                'United States; Mexico; Canada; Japan; European Union; India;  Turkey',
                'United States; Mexico; Canada; Japan; European Union; India',
                'United States; Mexico; Canada; Japan; European Union; India; Singapore, Australia', 'Canada', 'GE',
                'United States; Mexico; Canada; Japan; European Union; India; ,',
                'United States; Canada; European Union, Mexico, Japan, India', 'US, CA, JP, EU, IN',
                'United States (California market only)', 'EU, IN, US', 'FR', 'United States',
                'United States; Mexico; Canada;',
                'United States; Mexico; Canada; Japan; European Union; India; China, Turkey', 'DE',
                'United States; Mexico; Canada; Japan; European Union; India; , Turkey', 'US, CA, MX',
                'Canada; European Union', 'United Kingdom',
                'United States; Mexico; Canada; Japan; European Union; India; China;Turkey',
                'CA, CN, EU, IN, JP, MX, US', 'EU, CA, US, JP, MX, IN', 'United States; Canada',
                'United States-California', 'US,CAN,MX', 'United States; Mexico; Canada; ; European Union; India;',
                'Canada; European Union; Japan; Mexico; United States', 'United States; Mexico; Canada; European Union',
                'England', 'United States; Mexico; Canada; Japan; European Union;',
                'United States; Mexico; Canada, European union, India, Japan',
                'United States; Mexico; Canada; Japan; European Union; India; ; Turkey',
                'United States; Mexico; Canada; Japan; European Union; India; china',
                'Canada; European Union; India; Mexico; Japan; United States',
                'Canada; European Union; Japan; United States', 'CA, US, MX, JP',
                'Mexico, Japan, India, Canada, European Union', 'IT', 'All',
                'United States; Mexico; Canada; Japan; European Union; India; ;',
                'United States; Mexico; Canada; Japan; European Union; China', 'Germany', 'European Union, Turkey',
                'CA', 'UK', 'EU, JP, MX, US', 'United States; Mexico; Canada;  European Union;', 'EU, IN, JP', 'EU, IN',
                'EU/JP/MX', 'United States; Mexico; India; Canada; Japan; European Union;',
                'United States, Canada, Mexico', 'United States; Canada; Japan; European Union;', 'US/CA',
                'United States; Mexico; Canada; Japan; European Union; India,', 'EU, JP, MX', 'US/Canada',
                'United States; Mexico; Canada; Japan; European Union; India; china; Turkey',
                'United States (California)', 'European Union,', 'United States; Canada; European Union; UK',
                'United States; Mexico; Canada; Japan; European Union; India; China;',
                'United States; Mexico; Canada; Japan; European Union;India; Turkey', 'Italy',
                'Canada (British Columbia)', 'Canada; European Union; India; Japan; Mexico; United States',
                'Canada; China; European Union; India; Japan; Mexico; United States', 'Canada; Mexico; United States']


COUNTRY_DICT = {'US, CA': ['CA', 'US'], 'EU': ['UK', 'DE', 'FR', 'IT', 'ES'], 'United States/ Canada': ['CA', 'US'],
                'United States; Mexico; Canada; European Union, Japan, India': ['UK', 'DE', 'FR', 'IT', 'ES', 'CA',
                                                                                'US'],
                'United States; Mexico; India; Canada; Japan; European Union; China': ['UK', 'DE', 'FR', 'IT', 'ES',
                                                                                       'CA', 'US'],
                'EU,US,CAN': ['UK', 'DE', 'FR', 'IT', 'ES', 'CA', 'US'],
                'United States; Mexico; Canada; Japan; European, India': ['UK', 'DE', 'FR', 'IT', 'ES', 'CA', 'US'],
                'US': ['US'], 'United States;': ['US'],
                'France; Germany; Italy; Spain; United Kingdom': ['UK', 'DE', 'FR', 'IT', 'ES'],
                'United States; Mexico; Canada; Japan; European Union; India; Turkey': ['UK', 'DE', 'FR', 'IT', 'ES',
                                                                                        'CA', 'US'],
                'United States; Mexico; Canada; Japan; European Union; India;': ['UK', 'DE', 'FR', 'IT', 'ES', 'CA',
                                                                                 'US'],
                'European Union': ['UK', 'DE', 'FR', 'IT', 'ES'],
                'EU,US,CA': ['UK', 'DE', 'FR', 'IT', 'ES', 'CA', 'US'],
                'United States; Mexico; Canada; Japan; European Union; India;  Turkey': ['UK', 'DE', 'FR', 'IT', 'ES',
                                                                                         'CA', 'US'],
                'United States; Mexico; Canada; Japan; European Union; India': ['UK', 'DE', 'FR', 'IT', 'ES', 'CA',
                                                                                'US'],
                'United States; Mexico; Canada; Japan; European Union; India; Singapore, Australia': ['UK', 'DE', 'FR',
                                                                                                      'IT', 'ES', 'CA',
                                                                                                      'US'],
                'Canada': ['CA'], 'GE': ['DE'],
                'United States; Mexico; Canada; Japan; European Union; India; ,': ['UK', 'DE', 'FR', 'IT', 'ES', 'CA',
                                                                                   'US'],
                'United States; Canada; European Union, Mexico, Japan, India': ['UK', 'DE', 'FR', 'IT', 'ES', 'CA',
                                                                                'US'],
                'US, CA, JP, EU, IN': ['UK', 'DE', 'FR', 'IT', 'ES', 'CA', 'US'],
                'United States (California market only)': ['US'], 'EU, IN, US': ['UK', 'DE', 'FR', 'IT', 'ES', 'US'],
                'FR': ['FR'], 'United States': ['US'], 'United States; Mexico; Canada;': ['CA', 'US'],
                'United States; Mexico; Canada; Japan; European Union; India; China, Turkey': ['UK', 'DE', 'FR', 'IT',
                                                                                               'ES', 'CA', 'US'],
                'DE': ['DE'],
                'United States; Mexico; Canada; Japan; European Union; India; , Turkey': ['UK', 'DE', 'FR', 'IT', 'ES',
                                                                                          'CA', 'US'],
                'US, CA, MX': ['CA', 'US'], 'Canada; European Union': ['UK', 'DE', 'FR', 'IT', 'ES', 'CA'],
                'United Kingdom': ['UK'],
                'United States; Mexico; Canada; Japan; European Union; India; China;Turkey': ['UK', 'DE', 'FR', 'IT',
                                                                                              'ES', 'CA', 'US'],
                'CA, CN, EU, IN, JP, MX, US': ['UK', 'DE', 'FR', 'IT', 'ES', 'CA', 'US'],
                'EU, CA, US, JP, MX, IN': ['UK', 'DE', 'FR', 'IT', 'ES', 'CA', 'US'],
                'United States; Canada': ['CA', 'US'], 'United States-California': ['US'], 'US,CAN,MX': ['CA', 'US'],
                'United States; Mexico; Canada; ; European Union; India;': ['UK', 'DE', 'FR', 'IT', 'ES', 'CA', 'US'],
                'Canada; European Union; Japan; Mexico; United States': ['UK', 'DE', 'FR', 'IT', 'ES', 'CA', 'US'],
                'United States; Mexico; Canada; European Union': ['UK', 'DE', 'FR', 'IT', 'ES', 'CA', 'US'],
                'England': ['UK'],
                'United States; Mexico; Canada; Japan; European Union;': ['UK', 'DE', 'FR', 'IT', 'ES', 'CA', 'US'],
                'United States; Mexico; Canada, European union, India, Japan': ['UK', 'DE', 'FR', 'IT', 'ES', 'CA',
                                                                                'US'],
                'United States; Mexico; Canada; Japan; European Union; India; ; Turkey': ['UK', 'DE', 'FR', 'IT', 'ES',
                                                                                          'CA', 'US'],
                'United States; Mexico; Canada; Japan; European Union; India; china': ['UK', 'DE', 'FR', 'IT', 'ES',
                                                                                       'CA', 'US'],
                'Canada; European Union; India; Mexico; Japan; United States': ['UK', 'DE', 'FR', 'IT', 'ES', 'CA',
                                                                                'US'],
                'Canada; European Union; Japan; United States': ['UK', 'DE', 'FR', 'IT', 'ES', 'CA', 'US'],
                'CA, US, MX, JP': ['CA', 'US'],
                'Mexico, Japan, India, Canada, European Union': ['UK', 'DE', 'FR', 'IT', 'ES', 'CA', 'US'],
                'IT': ['IT'], 'All': ['UK', 'DE', 'FR', 'IT', 'ES', 'CA', 'US'],
                'United States; Mexico; Canada; Japan; European Union; India; ;': ['UK', 'DE', 'FR', 'IT', 'ES', 'CA',
                                                                                   'US'],
                'United States; Mexico; Canada; Japan; European Union; China': ['UK', 'DE', 'FR', 'IT', 'ES', 'CA',
                                                                                'US'], 'Germany': ['DE'],
                'European Union, Turkey': ['UK', 'DE', 'FR', 'IT', 'ES'], 'CA': ['CA'], 'UK': ['UK'],
                'EU, JP, MX, US': ['UK', 'DE', 'FR', 'IT', 'ES', 'US'],
                'United States; Mexico; Canada;  European Union;': ['UK', 'DE', 'FR', 'IT', 'ES', 'CA', 'US'],
                'EU, IN, JP': ['UK', 'DE', 'FR', 'IT', 'ES'], 'EU, IN': ['UK', 'DE', 'FR', 'IT', 'ES'],
                'EU/JP/MX': ['UK', 'DE', 'FR', 'IT', 'ES'],
                'United States; Mexico; India; Canada; Japan; European Union;': ['UK', 'DE', 'FR', 'IT', 'ES', 'CA',
                                                                                 'US'],
                'United States, Canada, Mexico': ['CA', 'US'],
                'United States; Canada; Japan; European Union;': ['UK', 'DE', 'FR', 'IT', 'ES', 'CA', 'US'],
                'US/CA': ['CA', 'US'],
                'United States; Mexico; Canada; Japan; European Union; India,': ['UK', 'DE', 'FR', 'IT', 'ES', 'CA',
                                                                                 'US'],
                'EU, JP, MX': ['UK', 'DE', 'FR', 'IT', 'ES'], 'US/Canada': ['CA', 'US'],
                'United States; Mexico; Canada; Japan; European Union; India; china; Turkey': ['UK', 'DE', 'FR', 'IT',
                                                                                               'ES', 'CA', 'US'],
                'United States (California)': ['US'], 'European Union,': ['UK', 'DE', 'FR', 'IT', 'ES'],
                'United States; Canada; European Union; UK': ['UK', 'DE', 'FR', 'IT', 'ES', 'CA', 'US'],
                'United States; Mexico; Canada; Japan; European Union; India; China;': ['UK', 'DE', 'FR', 'IT', 'ES',
                                                                                        'CA', 'US'],
                'United States; Mexico; Canada; Japan; European Union;India; Turkey': ['UK', 'DE', 'FR', 'IT', 'ES',
                                                                                       'CA', 'US'], 'Italy': ['IT'],
                'Canada (British Columbia)': ['CA'],
                'Canada; European Union; India; Japan; Mexico; United States': ['UK', 'DE', 'FR', 'IT', 'ES', 'CA',
                                                                                'US'],
                'Canada; China; European Union; India; Japan; Mexico; United States': ['UK', 'DE', 'FR', 'IT', 'ES',
                                                                                       'CA', 'US'],
                'Canada; Mexico; United States': ['CA', 'US']}

if __name__ == '__main__':

    import re

    date = 'this is date 23/10/2019, 10.23.2019, 2019/10.23,sas '
    xref = "this is k Prüfgrundlage Test specification 16.01.2019"
    x = re.findall(
        "([1-9]|1[0-9]|2[0-9]|3[0-1])(.|-)(0[1-9]|1[0-2])(.|-|)(20[0-9][0-9])", xref)
    print(x)
    y = re.findall(
        "([0-9]{4})(-|/|.)(0[1-9]|1[0-2])(-|/|.)(0[1-9]|[1-2][0-9]|3[0-1])", xref)
    print(y)
    z = re.findall(
        "([1-9]|1[0-9]|2[0-9]|3[0-1])(.|-)([1-9]|1[0-2])(.|-|)(20[0-9][0-9])", xref)
    print(z)
