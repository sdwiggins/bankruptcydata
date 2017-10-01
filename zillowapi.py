"""TODO: Figure out how pyzillow reads the xml files
documentation: https://github.com/hanneshapke/pyzillow
"""

from pyzillow.pyzillow import ZillowWrapper, GetDeepSearchResults

address = '28631 Lapine Avenue'
zipcode = '91390'

zillow_data = ZillowWrapper("X1-ZWz18zxh578kjv_2avji")
deep_search_response = zillow_data.get_deep_search_results(address, zipcode)
result = GetDeepSearchResults(deep_search_response)

print(result.zestimate_amount) # zillow id, needed for the GetUpdatedPropertyDetails
