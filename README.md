# Explorer custom URL scheme

This is a multi-language repository that contains documentation and sample code for creating custom URL schemes in [Explorer for ArcGIS](http://doc.arcgis.com/en/Explorer/).

## Supported versions

* Explorer for ArcGIS 2.0.0 or later

## What's included

* [Documentation](#documentation) on the URL scheme structure
* [Sample code](#sample) for iOS (Swift), Android (Java), and Python

## Get started

Read the following documentation and clone down the appropriate language into your development environment.
<a name="documentation"></a>

## Documentation

####What is the Explorer for ArcGIS URL scheme?

A URL scheme allows you to launch a native app from another app, website, or email. You can set options in the URL that will be passed to the app you want to open, causing it to perform specific functions, such as searching for opening a map to a specific centered location and scale. This capability is available on the iOS and Android platforms.

####Basic URL scheme structure

All Explorer URL schemes start with the identifier `arcgis-explorer` and can contain additional parameters that follow the form:

`
arcgis-explorer://?parameter=value&parameter=value
`

The rest of this topic describes the various parameters Explorer currently supports.

####Open a specific Web Map or Mobile Map Package

This is one of the simplest schemes that can be used. It requests the Item ID and attempts to open the map using the map’s default center and scale.

`id`: Sets Item ID for the map.

The following example URL defines an Item ID:

```
arcgis-explorer://?id=2adf08a4a1a84834a773805a6e86f69e
```

**NOTE:** All other paramaters require that a item id be specified.

####Specify a custom center

Use this to recenter the map once loaded to a different coordinate than the user’s current location:

`center`: Sets where the center of the map display should be.

The `center` parameter includes either a set of latitude and longitude coordinates (decimal degrees), or a query formatted address.

The following example URL displays a Public Web Map centered on a coordinate pair:

```
arcgis-explorer://?id=2adf08a4a1a84834a773805a6e86f69e&center=43.656789,-70.278083
```

The following example URL displays a Public Web Map centered on an address:

```
arcgis-explorer://?id=2adf08a4a1a84834a773805a6e86f69e&center=271+Park+Ave,+Portland+ME
```

The following example URL displays a Public Web Map centered on a place of interest:

```
arcgis-explorer://?id=2adf08a4a1a84834a773805a6e86f69e&center=Hadlock+Field,+Portland+ME
```

####Specify a custom scale

Explorer can also open the map to a custom scale. 

`scale`: Sets the scale in map units that the map should be rendered. 

The following example URL displays a Public Web Map at a custom scale:

```
arcgis-explorer://?id=2adf08a4a1a84834a773805a6e86f69e&scale=12000
```

####Specify a custom rotation

Explorer can also open the map to a custom rotation. 

`rotation`: Sets the rotation in degrees that the map should be rendered. Acceptable values range from 0 - 360.

The following example URL displays a Public Web Map at a custom rotation:

```
arcgis-explorer://?id=2adf08a4a1a84834a773805a6e86f69e&rotation=90
```


####Errors
If an error is encountered when processing a URL scheme, the user will receive an alert.
<a name="sample"></a>

## Sample code

* [Swift (iOS)](https://github.com/Esri/explorer-integration/tree/master/src/Swift)
* [Java (Android)](https://github.com/Esri/explorer-integration/tree/master/src/Android)
* [Python](https://github.com/Esri/explorer-integration/tree/master/src/Python)

## Resources and related repositories

* [Explorer for ArcGIS documentation](http://doc.arcgis.com/en/explorer/)
* [Collector for ArcGIS integration repository](http://developers.arcgis.com)

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
