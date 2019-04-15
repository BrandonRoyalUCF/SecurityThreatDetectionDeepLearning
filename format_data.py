import numpy as np 

class DataSample(object):

    def __init__(self, data_row):
        self.data_row = data_row

        self.MachineIdentifier = None
        self.ProductName = None
        self.EngineVersion = None
        self.AppVersion = None
        self.AvSigVersion = None
        self.IsBeta = None
        self.RtpStateBitfield = None
        self.IsSxsPassiveMode = None
        self.DefaultBrowsersIdentifier = None
        self.AVProductStatesIdentifier = None
        self.AVProductsInstalled = None
        self.AVProductsEnabled = None
        self.HasTpm = None
        self.CountryIdentifier = None
        self.CityIdentifier = None
        self.OrganizationIdentifier = None
        self.GeoNameIdentifier = None
        self.LocaleEnglishNameIdentifier = None
        self.Platform = None
        self.Processor = None
        self.OsVer = None
        self.OsBuild = None
        self.OsSuite = None
        self.OsPlatformSubRelease = None
        self.OsBuildLab = None
        self.SkuEdition = None
        self.IsProtected = None
        self.AutoSampleOptIn = None
        self.PuaMode = None
        self.SMode = None
        self.IeVerIdentifier = None
        self.SmartScreen = None
        self.Firewall = None
        self.UacLuaenable = None
        self.Census_MDC2FormFactor = None
        self.Census_DeviceFamily = None
        self.Census_OEMNameIdentifier = None
        self.Census_OEMModelIdentifier = None
        self.Census_ProcessorCoreCount = None
        self.Census_ProcessorManufacturerIdentifier = None
        self.Census_ProcessorModelIdentifier = None
        self.Census_ProcessorClass = None
        self.Census_PrimaryDiskTotalCapacity = None
        self.Census_PrimaryDiskTypeName = None
        self.Census_SystemVolumeTotalCapacity = None
        self.Census_HasOpticalDiskDrive = None
        self.Census_TotalPhysicalRAM = None
        self.Census_ChassisTypeName = None
        self.Census_InternalPrimaryDiagonalDisplaySizeInInches = None
        self.Census_InternalPrimaryDisplayResolutionHorizontal = None
        self.Census_InternalPrimaryDisplayResolutionVertical = None
        self.Census_PowerPlatformRoleName = None
        self.Census_InternalBatteryType = None
        self.Census_InternalBatteryNumberOfCharges = None
        self.Census_OSVersion = None
        self.Census_OSArchitecture = None
        self.Census_OSBranch = None
        self.Census_OSBuildNumber = None
        self.Census_OSBuildRevision = None
        self.Census_OSEdition = None
        self.Census_OSSkuName = None
        self.Census_OSInstallTypeName = None
        self.Census_OSInstallLanguageIdentifier = None
        self.Census_OSUILocaleIdentifier = None
        self.Census_OSWUAutoUpdateOptionsName = None
        self.Census_IsPortableOperatingSystem = None
        self.Census_GenuineStateName = None
        self.Census_ActivationChannel = None
        self.Census_IsFlightingInternal = None
        self.Census_IsFlightsDisabled = None
        self.Census_FlightRing = None
        self.Census_ThresholdOptIn = None
        self.Census_FirmwareManufacturerIdentifier = None
        self.Census_FirmwareVersionIdentifier = None
        self.Census_IsSecureBootEnabled = None
        self.Census_IsWIMBootEnabled = None
        self.Census_IsVirtualDevice = None
        self.Census_IsTouchEnabled = None
        self.Census_IsPenCapable = None
        self.Census_IsAlwaysOnAlwaysConnectedCapable = None
        self.Wdft_IsGamer = None
        self.Wdft_RegionIdentifier = None
        self.HasDetections = None

        self.setup_data_object()

    def setup_data_object(self):

        if(self.data_row is None):
            raise Exception('There is no data in the data_row.')

        self.MachineIdentifier = self.data_row[0]
        self.ProductName = self.data_row[1]
        self.EngineVersion = self.data_row[2]
        self.AppVersion = self.data_row[3]
        self.AvSigVersion = self.data_row[4]
        self.IsBeta = self.data_row[5] if self.data_row[5] != '' else -1
        self.RtpStateBitfield = self.data_row[6] if self.data_row[6] != '' else -1
        self.IsSxsPassiveMode = self.data_row[7]
        self.DefaultBrowsersIdentifier = self.data_row[8] if self.data_row[8] != '' else -1
        self.AVProductStatesIdentifier = self.data_row[9] if self.data_row[9] != '' else -1
        self.AVProductsInstalled = self.data_row[10] if self.data_row[10] != '' else -1
        self.AVProductsEnabled = self.data_row[11] if self.data_row[11] != '' else -1
        self.HasTpm = self.data_row[12]
        self.CountryIdentifier = self.data_row[13] if self.data_row[13] != '' else -1
        self.CityIdentifier = self.data_row[14] if self.data_row[14] != '' else -1
        self.OrganizationIdentifier = self.data_row[15] if self.data_row[15] != '' else -1
        self.GeoNameIdentifier = self.data_row[16] if self.data_row[16] != '' else -1
        self.LocaleEnglishNameIdentifier = self.data_row[17] if self.data_row[17] != '' else -1
        self.Platform = self.data_row[18]
        self.Processor = self.data_row[19]
        self.OsVer = self.data_row[20]
        self.OsBuild = self.data_row[21]
        self.OsSuite = self.data_row[22]
        self.OsPlatformSubRelease = self.data_row[23]
        self.OsBuildLab = self.data_row[24]
        self.SkuEdition = self.data_row[25]
        self.IsProtected = self.data_row[26] if self.data_row[26] != '' else -1
        self.AutoSampleOptIn = self.data_row[27]
        self.PuaMode = self.data_row[28]
        self.SMode = self.data_row[29] if self.data_row[29] != '' else -1
        self.IeVerIdentifier = self.data_row[30] if self.data_row[30] != '' else -1
        self.SmartScreen = self.data_row[31] if self.data_row[31] != '' else -1
        self.Firewall = self.data_row[32] if self.data_row[32] != '' else -1
        self.UacLuaenable = self.data_row[33] if self.data_row[33] != '' else -1
        self.Census_MDC2FormFactor = self.data_row[34]
        self.Census_DeviceFamily = self.data_row[35]
        self.Census_OEMNameIdentifier = self.data_row[36] if self.data_row[36] != '' else -1
        self.Census_OEMModelIdentifier = self.data_row[37] if self.data_row[37] != '' else -1
        self.Census_ProcessorCoreCount = self.data_row[38] if self.data_row[38] != '' else -1
        self.Census_ProcessorManufacturerIdentifier = self.data_row[39] if self.data_row[39] != '' else -1
        self.Census_ProcessorModelIdentifier = self.data_row[40] if self.data_row[40] != '' else -1
        self.Census_ProcessorClass = self.data_row[41]
        self.Census_PrimaryDiskTotalCapacity = self.data_row[42] if self.data_row[42] != '' else -1
        self.Census_PrimaryDiskTypeName = self.data_row[43]
        self.Census_SystemVolumeTotalCapacity = self.data_row[44] if self.data_row[44] != '' else -1
        self.Census_HasOpticalDiskDrive = self.data_row[45] if self.data_row[45] != '' else -1
        self.Census_TotalPhysicalRAM = self.data_row[46] if self.data_row[46] != '' else -1
        self.Census_ChassisTypeName = self.data_row[47]
        self.Census_InternalPrimaryDiagonalDisplaySizeInInches = self.data_row[48] if self.data_row[48] != '' else -1
        self.Census_InternalPrimaryDisplayResolutionHorizontal = self.data_row[49] if self.data_row[49] != '' else -1
        self.Census_InternalPrimaryDisplayResolutionVertical = self.data_row[50] if self.data_row[50] != '' else -1
        self.Census_PowerPlatformRoleName = self.data_row[51]
        self.Census_InternalBatteryType = self.data_row[52]
        self.Census_InternalBatteryNumberOfCharges = self.data_row[53] if self.data_row[53] != '' else -1
        self.Census_OSVersion = self.data_row[54]
        self.Census_OSArchitecture = self.data_row[55]
        self.Census_OSBranch = self.data_row[56]
        self.Census_OSBuildNumber = self.data_row[57]
        self.Census_OSBuildRevision = self.data_row[58]
        self.Census_OSEdition = self.data_row[59]
        self.Census_OSSkuName = self.data_row[60]
        self.Census_OSInstallTypeName = self.data_row[61]
        self.Census_OSInstallLanguageIdentifier = self.data_row[62] if self.data_row[62] != '' else -1
        self.Census_OSUILocaleIdentifier = self.data_row[63] if self.data_row[63] != '' else -1
        self.Census_OSWUAutoUpdateOptionsName = self.data_row[64]
        self.Census_IsPortableOperatingSystem = self.data_row[65]
        self.Census_GenuineStateName = self.data_row[66]
        self.Census_ActivationChannel = self.data_row[67]
        self.Census_IsFlightingInternal = self.data_row[68] if self.data_row[68] != '' else -1
        self.Census_IsFlightsDisabled = self.data_row[69] if self.data_row[69] != '' else -1
        self.Census_FlightRing = self.data_row[70]
        self.Census_ThresholdOptIn = self.data_row[71] if self.data_row[71] != '' else -1
        self.Census_FirmwareManufacturerIdentifier = self.data_row[72] if self.data_row[72] != '' else -1
        self.Census_FirmwareVersionIdentifier = self.data_row[73] if self.data_row[73] != '' else -1
        self.Census_IsSecureBootEnabled = self.data_row[74] if self.data_row[74] != '' else -1
        self.Census_IsWIMBootEnabled = self.data_row[75] if self.data_row[75] != '' else -1
        self.Census_IsVirtualDevice = self.data_row[76] if self.data_row[76] != '' else -1
        self.Census_IsTouchEnabled = self.data_row[77] if self.data_row[77] != '' else -1
        self.Census_IsPenCapable = self.data_row[78] if self.data_row[78] != '' else -1
        self.Census_IsAlwaysOnAlwaysConnectedCapable = self.data_row[79] if self.data_row[79] != '' else -1
        self.Wdft_IsGamer = self.data_row[80] if self.data_row[80] != '' else -1
        self.Wdft_RegionIdentifier = self.data_row[81] if self.data_row[81] != '' else -1
        self.HasDetections = self.data_row[82]

        

'''
0'MachineIdentifier' - not a feature
1'ProductName' - create a key (number) for each different one
2'EngineVersion' -break into x features
3'AppVersion' - break into x features
4 'AvSigVersion' - break into x features
5 'IsBeta' - binary 0 or 1
6 'RtpStateBitfield' 
7 'IsSxsPassiveMode'
8 'DefaultBrowsersIdentifier' 
9 'AVProductStatesIdentifier'
10 'AVProductsInstalled' 
 'AVProductsEnabled' 
 'HasTpm' 
 'CountryIdentifier'
 'CityIdentifier' 
 'OrganizationIdentifier' 
 'GeoNameIdentifier'
 'LocaleEnglishNameIdentifier' 
 'Platform' 
 'Processor' 
 'OsVer' 
 'OsBuild'
 'OsSuite' 
 'OsPlatformSubRelease' 
 'OsBuildLab' 
 'SkuEdition' 
 'IsProtected'
 'AutoSampleOptIn' 
 'PuaMode' 
 'SMode' 
 'IeVerIdentifier' 
 'SmartScreen'
 'Firewall' 
 'UacLuaenable' 
 'Census_MDC2FormFactor' 
 'Census_DeviceFamily'
 'Census_OEMNameIdentifier' 
 'Census_OEMModelIdentifier'
 'Census_ProcessorCoreCount' 
 'Census_ProcessorManufacturerIdentifier'
 'Census_ProcessorModelIdentifier' 
 'Census_ProcessorClass'
 'Census_PrimaryDiskTotalCapacity' 
 'Census_PrimaryDiskTypeName'
 'Census_SystemVolumeTotalCapacity' 
 'Census_HasOpticalDiskDrive'
 'Census_TotalPhysicalRAM' 
 'Census_ChassisTypeName'
 'Census_InternalPrimaryDiagonalDisplaySizeInInches'
 'Census_InternalPrimaryDisplayResolutionHorizontal'
 'Census_InternalPrimaryDisplayResolutionVertical'
 'Census_PowerPlatformRoleName' 
 'Census_InternalBatteryType'
 'Census_InternalBatteryNumberOfCharges' 
 'Census_OSVersion'
 'Census_OSArchitecture' 
 'Census_OSBranch' 
 'Census_OSBuildNumber'
 'Census_OSBuildRevision' 
 'Census_OSEdition' 
 'Census_OSSkuName'
 'Census_OSInstallTypeName' 
 'Census_OSInstallLanguageIdentifier'
 'Census_OSUILocaleIdentifier' 
 'Census_OSWUAutoUpdateOptionsName'
 'Census_IsPortableOperatingSystem' 
 'Census_GenuineStateName'
 'Census_ActivationChannel' 
 'Census_IsFlightingInternal'- binary feature
 'Census_IsFlightsDisabled' - binary feature
 'Census_FlightRing' 
 'Census_ThresholdOptIn'
 'Census_FirmwareManufacturerIdentifier'
 'Census_FirmwareVersionIdentifier' 
 'Census_IsSecureBootEnabled' - binary feature
 'Census_IsWIMBootEnabled'  - binary feature
 'Census_IsVirtualDevice' - binary feature
 'Census_IsTouchEnabled' -binary feature
 'Census_IsPenCapable' - binary feature
 'Census_IsAlwaysOnAlwaysConnectedCapable' - binary feature
 'Wdft_IsGamer' - binary feature
 'Wdft_RegionIdentifier' - fine as a feature

 ['0000010489e3af074adeac69c53e555e' 'win8defender' '1.1.15400.5'
 '4.18.1810.5' '1.281.501.0' '0' '7' '0' '' '53447' '1' '1' '1' '43'
 '58552' '18' '53' '42' 'windows10' 'x64' '10.0.0.0' '15063' '768' 'rs2'
 '15063.0.amd64fre.rs2_release.170317-1834' 'Home' '1' '0' '' '' '108' ''
 '1' '1' 'Notebook' 'Windows.Desktop' '2689' '30661' '4' '5' '3063' ''
 '488386' 'SSD' '123179' '0' '8192' 'Notebook' '15.5' '1920' '1080'
 'Mobile' '' '8' '10.0.15063.1387' 'amd64' 'rs2_release' '15063' '1387'
 'Core' 'CORE' 'Reset' '37' '158' 'AutoInstallAndRebootAtMaintenanceTime'
 '0' 'IS_GENUINE' 'OEM:DM' '' '0' 'Retail' '' '807' '8554' '1' '' '0' '0'
 '0' '0' '0' '7']


'''

def split_engine_version(engine_version):
    features = engine_version.split('.')
    if(len(features) > 4):
        raise Exception('Error the version number had more than 4 segments.')
    while len(features) < 4:
        features.append(0)
    return features

def split_app_version(app_version):
    features = app_version.split('.')
    if(len(features) > 4):
        raise Exception('Error the version number had more than 4 segments.')
    while len(features) < 4:
        features.append(0)
    return features

def split_avsig_version(avsig_version):
    features = avsig_version.split('.')
    if(len(features) > 4):
        raise Exception('Error the version number had more than 4 segments.')
    while len(features) < 4:
        features.append(0)
    return features

def split_census_os_version(census_os_version):
    features = census_os_version.split('.')
    if(len(features) > 4):
        raise Exception('Error the version number had more than 4 segments.')
    while len(features) < 4:
        features.append(0)
    return features

def split_os_version(os_version):
    features = os_version.split('.')
    if(len(features) > 4):
        raise Exception('Error the version number had more than 4 segments.')
    while len(features) < 4:
        features.append(0)
    return features

'''

'''

def get_ActivationChannel_key(data):
    mappings = {'Census_ActivationChannel':0, 'OEM:DM':1, 'Retail':2, 'OEM:NONSLP':3, 'Volume:GVLK':4, 'Volume:MAK':5,'Retail:TB:Eval':6, }
    return mappings[data]

def get_Censur_PrimaryDiskTypeName_key(data):
    mappings = {'Census_PrimaryDiskTypeName':0, 'SSD':1, 'HDD':2, 'UNKNOWN':3, 'Unspecified':4, '':5, }
    return mappings[data]

def get_Census_ChassisTypeName_key(data):
    mappings = {'Census_ChassisTypeName':0, 'Desktop':1, 'Notebook':2, 'MiniTower':3, 'Portable':4, 'Detachable':5, 'Laptop':6, 'AllinOne':7, 'LowProfileDesktop':8, 'SpaceSaving':9, 'Other':10, 'Unknown':11, 'HandHeld':12, 'UNKNOWN':13, 'Convertible':14, 'Tower':15, 'MainServerChassis':16, 'LunchBox':17, 'SubNotebook':18, 'MiniPC':19, 'RackMountChassis':20, 'Tablet':21, '30':22, 'StickPC':23, 'BusExpansionChassis':24, '':25, '36':26, '82':27, }
    return mappings[data]

def get_Census_DeviceFamily_key(data):
    mappings = {'Census_DeviceFamily':0, 'Windows.Desktop':1, 'Windows.Server':2, 'Windows':3, }
    return mappings[data]

def get_Census_MDC2FormFactor_key(data):
    mappings = {'Census_MDC2FormFactor':0, 'Notebook':1, 'Desktop':2, 'PCOther':3, 'AllInOne':4, 'SmallTablet':5, 'Convertible':6, 'Detachable':7, 'MediumServer':8, 'LargeTablet':9, 'SmallServer':10, 'LargeServer':11, 'ServerOther':12, }
    return mappings[data]

def get_Census_PowerPlatformRoleName_key(data):
    mappings = {'Census_PowerPlatformRoleName':0, 'Mobile':1, 'Desktop':2, 'UNKNOWN':3, 'Workstation':4, 'Slate':5, 'SOHOServer':6, 'AppliancePC':7, 'EnterpriseServer':8, 'PerformanceServer':9, }
    return mappings[data]

def get_FlightRing_key(data):
    mappings = {'Census_FlightRing':0, 'Retail':1, 'WIF':2, 'NOT_SET':3, 'Unknown':4, 'WIS':5, 'RP':6, 'Disabled':7, }
    return mappings[data]

def get_GenuineStateName_key(data):
    mappings = {'Census_GenuineStateName':0, 'IS_GENUINE':1, 'UNKNOWN':2, 'INVALID_LICENSE':3, 'OFFLINE':4, }
    return mappings[data]

def get_OSArchitecture_key(data):
    mappings = {'Census_OSArchitecture':0, 'amd64':1, 'x86':2, 'arm64':3, }
    return mappings[data]

def get_OSBranch_key(data):
    mappings = {'Census_OSBranch':0, 'rs4_release':1, 'rs1_release':2, 'rs3_release_svc_escrow':3, 'th2_release':4, 'rs3_release':5, 'th1_st1':6, 'rs2_release':7, 'rs3_release_svc_escrow_im':8, 'th1':9, 'th2_release_sec':10, 'rs5_release':11, 'rs_prerelease_flt':12, 'rs_prerelease':13, 'rs5_release_sigma':14, 'rs5_release_edge':15, }
    return mappings[data]

def get_OsbuildLab_key(data):
    #NOTE: not implemented yet
    return 0

def get_OSEdition_key(data):
    mappings = {'Census_OSEdition':0, 'Core':1, 'CoreSingleLanguage':2, 'Professional':3, 'CoreCountrySpecific':4, 'ProfessionalEducation':5, 'Education':6, 'Enterprise':7, 'ServerStandard':8, 'ProfessionalN':9, 'EnterpriseS':10, 'EducationN':11, 'CoreN':12, 'Cloud':13, 'ServerStandardEval':14, 'ServerDatacenterEval':15, 'ProfessionalWorkstation':16, 'ServerSolution':17, 'EnterpriseSN':18, 'ProfessionalEducationN':19, 'EnterpriseN':20, 'EnterpriseG':21, 'ProfessionalWorkstationN':22, 'ServerRdsh':23, }
    return mappings[data]

def get_OSInstallTypeName(data):
    mappings = {'Census_OSInstallTypeName':0, 'Reset':1, 'UUPUpgrade':2, 'Other':3, 'Upgrade':4, 'Update':5, 'Refresh':6, 'IBSClean':7, 'CleanPCRefresh':8, 'Clean':9, }
    return mappings[data]

def get_OsPlatformSubRelease_key(data):
    mappings = {'OsPlatformSubRelease':0, 'rs2':1, 'rs3':2, 'rs1':3, 'rs4':4, 'prers5':5, 'th2':6, 'th1':7, 'windows8.1':8, 'windows7':9, }
    return mappings[data]

def get_OSSkuName_key(data):
    mappings = {'Census_OSSkuName':0, 'CORE':1, 'CORE_SINGLELANGUAGE':2, 'PROFESSIONAL':3, 'CORE_COUNTRYSPECIFIC':4, 'EDUCATION':5, 'ENTERPRISE':6, 'STANDARD_SERVER':7, 'PROFESSIONAL_N':8, 'ENTERPRISE_S':9, 'EDUCATION_N':10, 'CORE_N':11, 'CLOUD':12, 'STANDARD_EVALUATION_SERVER':13, 'DATACENTER_EVALUATION_SERVER':14, 'PRO_WORKSTATION':15, 'SB_SOLUTION_SERVER':16, 'ENTERPRISE_S_N':17, 'ENTERPRISE_N':18, 'ENTERPRISEG':19, 'PRO_FOR_EDUCATION':20, 'PRO_WORKSTATION_N':21, 'SERVERRDSH':22, }
    return mappings[data]

def get_OSWUAutoUpdateOptionsName_key(data):
    mappings = {'Census_OSWUAutoUpdateOptionsName':0, 'AutoInstallAndRebootAtMaintenanceTime':1, 'UNKNOWN':2, 'Notify':3, 'FullAuto':4, 'Off':5, 'DownloadNotify':6, }
    return mappings[data]

def get_platform_key(data):
    mappings = {'Platform':0, 'windows10':1, 'windows8':2, 'windows2016':3, 'windows7':4, }
    return mappings[data]

def get_processor_key(data):
    mappings = {'Processor':0, 'x64':1, 'x86':2, 'arm64':3, }
    return mappings[data]

def get_product_name_key(data):
    mappings = {'ProductName':0,
    'mse':1, 
    'mseprerelease':2, 
    'scep':3, 
    'windowsintune':4, 
    'win8defender':5,
    'fep':6}

    return mappings[data]

def get_SkuEdition_key(data):
    mappings = {'SkuEdition':0, 'Home':1, 'Pro':2, 'Education':3, 'Invalid':4, 'Enterprise LTSB':5, 'Enterprise':6, 'Cloud':7, 'Server':8, }
    return mappings[data]

#NOTE: Not implemented
def get_SmartScreen_key(data):
    return 0

def get_Internal_BatteryType_key(data):
    mappings = {'Census_InternalBatteryType':0, '':1, 'lion':2, 'li-i':3, 'lip':4, 'liio':5, 'vbox':6, 'li p':7, 'real':8, 'unkn':9, 'pbac':10, 'li':11, 'bq20':12, 'nimh':13, 'lio':14, 'lgi0':15, 'lhp0':16, 'ithi':17, 'batt':18, 'lipp':19, 'lipo':20, }
    return mappings[data]

def get_Census_ProcessorClass_key(data):
    mappings = {'Census_ProcessorClass':0, '':1, 'mid':2, 'low':3, 'high':4, }
    return mappings[data]

def get_PuaMode_key(data):
    mappings = {'PuaMode':0, '':1, 'on':2, }
    return mappings[data]

def clean_data(all_data_objects):

    all_data_feature_vecs = []
    all_labels = []

    for data_object in all_data_objects:

        num_features = 96

        features = np.zeros((num_features,), dtype=float)

        #ignore the MachineIdentifier column
    
        #first feature is a number representing the product name
        features[0] = get_product_name_key(data_object.ProductName)
        
        #split the engine version into 4 features
        engine_version_features = split_engine_version(data_object.EngineVersion)

        features[1] = engine_version_features[0]
        features[2] = engine_version_features[1]
        features[3] = engine_version_features[2]
        features[4] = engine_version_features[3]

        #split the app version into 4 features
        app_version_features = split_app_version(data_object.AppVersion)

        features[5] = app_version_features[0]
        features[6] = app_version_features[1]
        features[7] = app_version_features[2]
        features[8] = app_version_features[3]

        #split the av sig version into 4 features
        avsig_version_features = split_avsig_version(data_object.AvSigVersion)

        features[9] = avsig_version_features[0]
        features[10] = avsig_version_features[1]
        features[11] = avsig_version_features[2]
        features[12] = avsig_version_features[3]

        #Handle features in which they do not have to be altered
        features[13] = data_object.IsBeta
        features[14] = data_object.RtpStateBitfield
        features[15] = data_object.IsSxsPassiveMode
        features[16] = data_object.DefaultBrowsersIdentifier
        features[17] = data_object.AVProductStatesIdentifier
        features[18] = data_object.AVProductsInstalled
        features[19] = data_object.AVProductsEnabled
        features[20] = data_object.HasTpm
        features[21] = data_object.CountryIdentifier
        features[22] = data_object.CityIdentifier
        features[23] = data_object.OrganizationIdentifier
        features[24] = data_object.GeoNameIdentifier
        features[25] = data_object.LocaleEnglishNameIdentifier

        #get the plateform key based on the platform
        features[26] = get_platform_key(data_object.Platform)

        #get the processor key based on the processor
        features[27] = get_processor_key(data_object.Processor)

        #Split the OsVer into 4 features
        os_version_features = split_os_version(data_object.OsVer)

        features[28] = os_version_features[0]
        features[29] = os_version_features[1]
        features[30] = os_version_features[2]
        features[31] = os_version_features[3]


        features[32] = data_object.OsBuild
        features[33] = data_object.OsSuite

        #get the OsPlatformSubRelease key
        features[34] = get_OsPlatformSubRelease_key(data_object.OsPlatformSubRelease)

        #get OsBuildLab key
        features[35] = get_OsbuildLab_key(data_object.OsBuildLab)

        #get SkuEdition_key
        features[36] = get_SkuEdition_key(data_object.SkuEdition)

        features[37] = data_object.IsProtected
        features[38] = data_object.AutoSampleOptIn

        features[39] = get_PuaMode_key(data_object.PuaMode)

        features[40] = data_object.SMode
        features[41] = data_object.IeVerIdentifier

        #get smartscreen key
        features[42] = get_SmartScreen_key(data_object.SmartScreen)
        features[43] = data_object.Firewall
        features[44] = data_object.UacLuaenable


        features[45] = get_Census_MDC2FormFactor_key(data_object.Census_MDC2FormFactor)

        features[46] = get_Census_DeviceFamily_key(data_object.Census_DeviceFamily)

        features[47] = data_object.Census_OEMNameIdentifier
        features[48] = data_object.Census_OEMModelIdentifier
        features[49] = data_object.Census_ProcessorCoreCount
        features[50] = data_object.Census_ProcessorManufacturerIdentifier
        features[51] = data_object.Census_ProcessorModelIdentifier
        features[52] = get_Census_ProcessorClass_key(data_object.Census_ProcessorClass)
        features[53] = data_object.Census_PrimaryDiskTotalCapacity

        features[54] = get_Censur_PrimaryDiskTypeName_key(data_object.Census_PrimaryDiskTypeName)
        
        features[55] = data_object.Census_SystemVolumeTotalCapacity
        features[56] = data_object.Census_HasOpticalDiskDrive
        features[57] = data_object.Census_TotalPhysicalRAM

        features[58] = get_Census_ChassisTypeName_key(data_object.Census_ChassisTypeName)
        
        features[59] = data_object.Census_InternalPrimaryDiagonalDisplaySizeInInches
        features[60] = data_object.Census_InternalPrimaryDisplayResolutionHorizontal
        features[61] = data_object.Census_InternalPrimaryDisplayResolutionVertical

        features[62] = get_Census_PowerPlatformRoleName_key(data_object.Census_PowerPlatformRoleName)
        
        features[63] = get_Internal_BatteryType_key(data_object.Census_InternalBatteryType)

        features[64] = data_object.Census_InternalBatteryNumberOfCharges

        ######HERE#####
        #Split the Census_OsVersion into 4 features
        census_os_version_features = split_census_os_version(data_object.Census_OSVersion)
        features[65] = census_os_version_features[0]
        features[93] = census_os_version_features[1]
        features[94] = census_os_version_features[2]
        features[95] = census_os_version_features[3]
        
        features[66] = get_OSArchitecture_key(data_object.Census_OSArchitecture)
        
        features[67] = get_OSBranch_key(data_object.Census_OSBranch)

        features[68] = data_object.Census_OSBuildNumber
        features[69] = data_object.Census_OSBuildRevision

        features[70] = get_OSEdition_key(data_object.Census_OSEdition)
        features[71] = get_OSSkuName_key(data_object.Census_OSSkuName)
        features[72] = get_OSInstallTypeName(data_object.Census_OSInstallTypeName)

        features[73] = data_object.Census_OSInstallLanguageIdentifier
        features[74] = data_object.Census_OSUILocaleIdentifier

        features[75] = get_OSWUAutoUpdateOptionsName_key(data_object.Census_OSWUAutoUpdateOptionsName)


        features[76] = data_object.Census_IsPortableOperatingSystem

        features[77] = get_GenuineStateName_key(data_object.Census_GenuineStateName)

        features[78] = get_ActivationChannel_key(data_object.Census_ActivationChannel)

        features[79] = data_object.Census_IsFlightingInternal
        features[80] = data_object.Census_IsFlightsDisabled

        features[81] = get_FlightRing_key(data_object.Census_FlightRing)

        features[82] = data_object.Census_ThresholdOptIn
        features[83] = data_object.Census_FirmwareManufacturerIdentifier
        features[84] = data_object.Census_FirmwareVersionIdentifier
        features[85] = data_object.Census_IsSecureBootEnabled
        features[86] = data_object.Census_IsWIMBootEnabled
        features[87] = data_object.Census_IsVirtualDevice
        features[88] = data_object.Census_IsTouchEnabled
        features[89] = data_object.Census_IsPenCapable
        features[90] = data_object.Census_IsAlwaysOnAlwaysConnectedCapable
        features[91] = data_object.Wdft_IsGamer
        features[92] = data_object.Wdft_RegionIdentifier
        
        #final feature is the label, this will be split off later
        label = data_object.HasDetections

        #NOTE: total of 96 features

        all_data_feature_vecs.append(features)
        all_labels.append(label)

    return all_data_feature_vecs, all_labels