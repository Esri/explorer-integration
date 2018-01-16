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

#### Basic URL scheme structure

All Explorer URL schemes start with the identifier `arcgis-explorer` and can contain additional parameters that follow the form:

`
arcgis-explorer://?parameter=value&parameter=value
`

The rest of this topic describes how to use the various parameters Explorer currently supports.
* [`itemID`](#itemid)
* `center`
* `wkid`
* `scale`
* `rotation`
* `search`
* `bookmark`
* `markup` 


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
arcgis-explorer://?itemID=e3767862254a4719982faaa0eef5e63d
```

**NOTE:** All other parameters require that a item id be specified.

#### Change intial extent for the map

There are a couple ways to set the map extent to provide a custom map viewing experience. One way is to specify the `center`/`scale` and optionally providing `wkid` and/or `rotation`. Alternatively, you can specify a `bookmark` from the map. In 

##### `center`, `scale`

Use this to recenter the map once loaded to a different coordinate than the user’s current location. The `center` parameter includes either a set of latitude and longitude coordinates (decimal degrees), or a query formatted address. When specifying a `center`, a `scale` must also be provided.

`center`: Sets where the center of the map display should be.

`scale`: Sets the scale in map units that the map should be rendered.


The following example URL displays a Public Web Map centered on a coordinate pair:

```
arcgis-explorer://?itemID=2adf08a4a1a84834a773805a6e86f69e&center=43.656789,-70.278083&scale=90000
```

The following example URL displays a Public Web Map centered on an address:

```
arcgis-explorer://?itemID=2adf08a4a1a84834a773805a6e86f69e&center=271+Park+Ave,+Portland+ME&scale=90000
```

The following example URL displays a Public Web Map centered on a place of interest:

```
arcgis-explorer://?itemID=2adf08a4a1a84834a773805a6e86f69e&center=Hadlock+Field,+Portland+ME&scale=15000
```

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
