from django.conf.urls import include,url
import views

urlpatterns = [
    url(r'report/asset_with_no_asset_id/',views.AssetWithNoAssetId,name="AcquireAssetId"),
]