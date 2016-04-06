from django.shortcuts import render,HttpResponse
import json

import core

def AssetWithNoAssetId(request):
    if request.method == 'POST':
        ass_handler = core.Asset(request)
        res = ass_handler.get_asset_id_by_sn()
        return  HttpResponse(json.dumps(res))


