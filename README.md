# Explorer custom URL scheme

This is a multi-language repository that contains documentation and sample code for creating custom URL schemes in [Explorer for ArcGIS](http://doc.arcgis.com/en/Explorer/).

## Supported versions

* **iOS:** Explorer for ArcGIS 18.1.0
* **Android:** Explorer for ArcGIS 17.1.0 Beta

## What's included

* [Documentation](#documentation) on the URL scheme structure
* [Sample code](#sample) for Python

## Get started

Read the following documentation and clone down the appropriate language into your development environment.
<a name="documentation"></a>

## Documentation

#### What is the Explorer for ArcGIS URL scheme?

A URL scheme allows you to launch a native app from another app, website, or email. You can set options in the URL that will be passed to the app you want to open, causing it to perform specific functions, such as opening a map to a specific location and scale. This capability is available on Explorer for ArcGIS for iOS and Android.

#### Explorer URL scheme overview

All Explorer URL schemes start with the identifier `arcgis-explorer` and can contain additional parameters that follow the form:

`
arcgis-explorer://?parameter=value&parameter=value
`

The following parameter tree is meant to be used as a quick reference to show how the parameters can be used together.

```
itemID
│  
└─── center & scale (used together)
│   +─── wkid
│   +─── markup
│   +─── rotation
│   
└─── search
│  
└─── bookmark 
```

The rest of this topic describes the various parameters Explorer currently supports.
* [`itemID`](#itemid)
* [`center`, `scale`](#center-scale)
  * [`wkid`, `rotation`, `markup`](wkid-rotation-markup)
* `search`
* `bookmark`


#### Open a specific Web Map or Mobile Map Package 
##### `itemID`

This is one of the simplest schemes that can be used. It requests the Item ID and attempts to open the map using the map’s default center and scale.

`itemID`: Sets Item ID for the map. The item referenced can be of type Web Map or Mobile Map Package that is shared with the current user. Mobile Map Packages will be automatically downloaded if not already on-device. It is important to note that if the item is publically shared in ArcGIS Online the user tapping on the URL scheme does not need to be signed into Explorer in order to access the map.

The following example URL defines an Item ID to a Public Web Map:

```
arcgis-explorer://?itemID=2adf08a4a1a84834a773805a6e86f69e
```

The following example URL defines an Item ID to a Public Mobile Map Package:

```
arcgis-explorer://?itemID=6ca5f9cfea0c47b2969ee9750693301f
```

**NOTE:** All other parameters require that a item id be specified.

#### Change initial extent for the map

There are a couple ways to set the map extent to provide a custom map viewing experience. You can specify the `center` & `scale` (optionally providing `wkid`, `rotation`, and/or `markup` parameters) or specify a `bookmark` from the map . Alternatively, you can `search` within the map to let Explorer determine how the initial extent should be set while also displaying the matching results. 

##### `center`, `scale`

Use this to recenter the map once loaded to a different coordinate than the user’s current location. The `center` parameter includes either a set of latitude and longitude coordinates (decimal degrees), or a query formatted address. When specifying a `center`, a `scale` must also be provided.

- `center`: Provide center in the following formats:
  - Comma-seperated latitude/longitude (y/x) pair in WGS84 (WKID:4326)
  - Address (plus-encode spaces) to be reverse geocoded by organization geocoder (Mobile Map Package's with locators will not look to geocoder)
  - Feature search result (plus-encode spaces)
- `scale`: Sets the scale in map units that the map should be rendered.


The following example URL's display a Public Web Map centered on a coordinate pair, address, and feature respectively:

```
arcgis-explorer://?itemID=2adf08a4a1a84834a773805a6e86f69e&center=43.656789,-70.278083&scale=90000
arcgis-explorer://?itemID=2adf08a4a1a84834a773805a6e86f69e&center=271+Park+Ave,+Portland+ME&scale=90000
arcgis-explorer://?itemID=2adf08a4a1a84834a773805a6e86f69e&center=Hadlock+Field,+Portland+ME&scale=15000
```

##### `wkid`, `rotation`, `markup`



#### Specify a custom rotation

Optionally, Explorer can also open the map to a custom rotation. When specifying a `rotation`, a `center` and `scale` must also be provided.

`rotation`: Sets the rotation in degrees that the map should be rendered. Acceptable values range from 0 - 360.

The following example URL displays a Public Web Map centered on a coordinate pair with a rotation applied to the map:

```
arcgis-explorer://?itemID=2adf08a4a1a84834a773805a6e86f69e&center=43.656789,-70.278083&scale=90000&rotation=180
```

#### Errors
If an error is encountered when processing a URL scheme, the user will receive an alert.
<a name="sample"></a>

## Sample code

* [Python](https://github.com/Esri/explorer-integration/tree/master/src/Python)

## Resources and related repositories

* [Explorer for ArcGIS documentation](http://doc.arcgis.com/en/explorer/)

Not Esri's doc but still pretty dang useful :-)

* [Apple's guide to custom URL schemes](https://developer.apple.com/library/ios/featuredarticles/iPhoneURLScheme_Reference/Introduction/Introduction.html#//apple_ref/doc/uid/TP40007899)
* [Google's guide to intents and intent filters](https://developer.android.com/guide/components/intents-filters.html)

## Issues

Find a bug or want to request a new feature? Please let us know by [submitting an issue](https://github.com/Esri/explorer-integration/issues/new). Thank you!

## Contribute

Anyone and everyone is welcome to contribute. See our [guidelines for contributing](https://github.com/esri/contributing).

## Licensing
Copyright 2016 Esri

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

[](Esri Tags: iOS, Android, Explorer, URL Scheme)
[](Esri Language: Java, Swift, Javascript)
