**This repository is archived and no longer managed.**

Please vist the [ArcGIS Explorer help documentation](https://doc.arcgis.com/en/explorer/windows/help/deploy.htm#ESRI_SECTION1_C30D73392D964D51A8B606128A8A6E8F) for more information on linking to Explorer

> # Explorer custom URL scheme
> 
> This is a multi-language repository that contains documentation and sample code for creating custom URL schemes in [Explorer for ArcGIS](http://doc.arcgis.com/en/Explorer/).
> 
> ## Supported versions
> 
> * **iOS:** Explorer for ArcGIS 18.1.0 or later
> * **Android:** Explorer for ArcGIS 18.1.0 or later [with limited support](#known-issues)
> 
> ## What's included
> 
> * [Documentation](#documentation) on the URL scheme structure
> * [Sample code](#sample) for Python
> 
> ## Get started
> 
> Read the following documentation and clone down the appropriate language into your development environment.
> <a name="documentation"></a>
> 
> ## Documentation
> 
> #### What is the Explorer for ArcGIS URL scheme?
> 
> A URL scheme allows you to launch a native app from another app, website, or email. You can set options in the URL that will be passed to the app you want to open, causing it to perform specific functions, such as opening a map to a specific location and scale. This capability is available on Explorer for ArcGIS for iOS and Android.
> 
> #### Explorer URL scheme overview
> 
> All Explorer URL schemes start with the application scheme of `arcgis-explorer://` and can contain additional query parameters in the following format:
> 
> `
> arcgis-explorer://?parameter=value&parameter=value
> `
> 
> The following diagram is meant to be used as a quick reference to show how the parameters can be used together. The rest of this topic describes each parameter in greater detail.
> 
> 
> ![image](https://user-images.githubusercontent.com/10168933/35809536-febe251e-0a56-11e8-8c93-86d8745fa3c4.png)
> 
> 
> * [`itemID`](#itemid)
> * [`center`, `scale`](#center-scale)
>   * [`wkid`, `rotation`, `markup`](#wkid-rotation-markup)
> * [`bookmark`](#bookmark)
> * [`search`](#search)
> 
> 
> #### Using URL scheme to customize map viewing experience
> ##### `itemID`
> 
> This is one of the simplest parameters that can be used. Explorer searches for the item (in ArcGIS Online or Portal) and attempts to open the map using the map’s default center and scale. If the user is not signed in, Explorer will continue without signing in and search ArcGIS for the item.
> 
> `itemID`: Sets Item ID for the map. The item referenced can be of type Web Map or Mobile Map Package that is shared with the current user. Mobile Map Packages will be automatically downloaded if not already on-device. If the item referenced is shared publically in ArcGIS Online, the user tapping on the URL scheme does not need to be signed in to Explorer in order to access the map.
> 
> The following examples show how you can open a specific map from a URL.
> 
> ```
> // open a public Web Map
> arcgis-explorer://?itemID=0c900ae2a1084d27b608233921ef1a84
> 
> // open a public Mobile Map Package
> arcgis-explorer://?itemID=6ca5f9cfea0c47b2969ee9750693301f
> 
> ```
> 
> NOTE: All other parameters require that a item id be specified.
> 
> In addition to opening a map to the default center and scale, there are a couple ways to set the map extent in order to provide a custom map viewing experience. You can specify the `center` and `scale` (optionally providing `wkid`, `rotation`, and/or `markup` parameters) or specify a `bookmark` from the map . Alternatively, you can `search` within the map to let Explorer determine how the initial extent should be set while also displaying the matching results. 
> 
> ##### `center`, `scale`
> 
> `center` and `scale` are used in conjuction to recenter a map. The `center` parameter can include either a set of latitude and longitude coordinates (decimal degrees), a query formatted address, or a feature search result. When specifying a `center`, the `scale` must also be provided.
> 
> - `center`: Centers the map to a certain location. Provide center in the following formats:
>   - Comma-seperated latitude/longitude (y/x) pair in WGS84 (WKID:4326)
>   - Address (plus-encode spaces) to be reverse geocoded by organization geocoder (Mobile Map Package's with locators will not utilize geocoder)
>   - Feature search result (plus-encode spaces). Explorer will automatically center on top result.
> - `scale`: Sets the scale in map units that the map should be rendered.
> 
> 
> The following examples show how you can use `center` and `scale` to adjust the map view point from a URL.
> 
> ```
> // center on a coordinate pair
> arcgis-explorer://?itemID=0c900ae2a1084d27b608233921ef1a84&center=41.780618,-88.179449&scale=3000
> 
> // center on a reverse geocoded address
> arcgis-explorer://?itemID=0c900ae2a1084d27b608233921ef1a84&center=899+Aurora+Ave,+Naperville,+Illinois&scale=1000
> 
> // center on a feature from map. In this case, Hydrant #43141
> arcgis-explorer://?itemID=0c900ae2a1084d27b608233921ef1a84&center=43141&scale=500
> ```
> 
> ##### `wkid`, `rotation`, `markup`
> 
> In addition to providing a `center` and `scale`, you can optionally specify any combination of the `wkid`, `rotation`, or `markup` parameters. Note, when using any of these parameters, an `itemID` and `center`/`scale` are required.
> - `wkid`: Specify coordinates in a different spatial reference. Defaults to WKID: 4326 (WGS84) if parameter is not used.
> - `rotation`: Rotate the given map 0-360 degrees. Sets the rotation in degrees that the map should be rendered. Acceptable values range from 0 - 360.
> - `markup`: Enable markup mode when opening a map.
> 
> The following examples show how the `wkid`, `rotation`, and `markup` parameters can be used together from a URL.
> 
> ```
> // rotate the map 180 degrees
> arcgis-explorer://?itemID=0c900ae2a1084d27b608233921ef1a84&center=41.780618,-88.179449&scale=1000&rotation=180
> 
> // center on coordinates in NAD83 / UTM zone 19N (WKID: 26919) spatial reference
> arcgis-explorer://?itemID=0c900ae2a1084d27b608233921ef1a84&center=4807094.8078305572,-1096767.7053304175&scale=1000&wkid=26919
> 
> // rotate the map 180 degrees and enable markup mode
> arcgis-explorer://?itemID=0c900ae2a1084d27b608233921ef1a84&center=41.780618,-88.179449&scale=1000&rotation=180&markup=true
> ```
> 
> ##### `bookmark`
> 
> Instead of providing a center and scale, the `bookmark` parameter can be used to open the map to a specific viewpoint by specifying a bookmark from the map. When providing a bookmark, you must also provide an `itemID` for the map. You cannot provide any additional parameters.
> - `bookmark`: Adjusts map viewpoint to the specified bookmark from the map. Bookmark name should be plus-encoded for spaces.
> 
> The following example shows how to open a map to a specific bookmark within the map from a URL.
> ```
> // open map to a bookmark named "Centennial Park"
> arcgis-explorer://?itemID=0c900ae2a1084d27b608233921ef1a84&bookmark=Centennial+Park
> ```
> 
> 
> ##### `search`
> 
> The `search` parameter allows you to quickly launch a map and execute a search, returning places and feature results without having to manually type your query using the search tool.
> - `search`: Executes a search, returning places and/or features. Query string should be plus-encoded for spaces.
> 
> The following examples show how you can use the search parameter in a URL.
> ```
> // search for an address from the geocoder
> arcgis-explorer://?itemID=15c3a41bc01e4f8b9922736f3c194c29&search=899+Aurora+Ave,+Naperville,+Illinois
> 
> // search for a POI from the geocoder
> arcgis-explorer://?itemID=15c3a41bc01e4f8b9922736f3c194c29&search=Gas+Station
> 
> // search for a feature from map. In this case, Hydrant #43141
> arcgis-explorer://?itemID=0c900ae2a1084d27b608233921ef1a84&search=43141
> ```
> 
> #### Known Issues
> 
> * Support on the Android version of Explorer for ArcGIS is limited to `itemID`, `center`/`scale`, and `rotation` parameters. Center parameter cannot reference feature from layer configured for search.
> 
> #### Errors
> If an error is encountered when processing a URL scheme, the user will receive an alert.
> <a name="sample"></a>
> 
> ## Sample code
> 
> * [Python](https://github.com/Esri/explorer-integration/tree/master/src/Python)
> 
> ## Resources and related repositories
> 
> * [Explorer for ArcGIS documentation](http://doc.arcgis.com/en/explorer/)
> 
> Not Esri's doc but still pretty dang useful :-)
> 
> * [Apple's guide to custom URL schemes](https://developer.apple.com/library/ios/featuredarticles/iPhoneURLScheme_Reference/Introduction/Introduction.html#//apple_ref/doc/uid/TP40007899)
> * [Google's guide to intents and intent filters](https://developer.android.com/guide/components/intents-filters.html)
> 
> ## Issues
> 
> Find a bug or want to request a new feature? Please let us know by [submitting an issue](https://github.com/Esri/explorer-integration/issues/new). Thank you!
> 
> ## Contribute
> 
> Anyone and everyone is welcome to contribute. See our [guidelines for contributing](https://github.com/esri/contributing).
> 
> ## Licensing
> Copyright 2016 Esri
> 
> Licensed under the Apache License, Version 2.0 (the "License");
> you may not use this file except in compliance with the License.
> You may obtain a copy of the License at
> 
>    http://www.apache.org/licenses/LICENSE-2.0
> 
> Unless required by applicable law or agreed to in writing, software
> distributed under the License is distributed on an "AS IS" BASIS,
> WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
> See the License for the specific language governing permissions and
> limitations under the License.
> 
> [](Esri Tags: iOS, Android, Explorer, URL Scheme)
> [](Esri Language: Java, Swift, Javascript)
> 
