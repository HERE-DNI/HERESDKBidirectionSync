---
title: "TileUrlProviderFactory (API Reference)"
slug: "sdk-for-android-explore-api-reference-latesttileurlproviderfactory"
hidden: false
---

Package [com.here.sdk.mapview.datasource](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class TileUrlProviderFactory

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.here.NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
com.here.sdk.mapview.datasource.TileUrlProviderFactory
------------------------------------------------------------------------
public final class TileUrlProviderFactory extends [NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
Factory for generating a [`TileUrlProviderCallback`](sdk-for-android-explore-api-reference-latesttileurlprovidercallback "interface in com.here.sdk.mapview.datasource") utilized in creating a tile URL.

## Method Summary

  All Methods
  Static Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  `static `[`TileUrlProviderCallback`](sdk-for-android-explore-api-reference-latesttileurlprovidercallback "interface in com.here.sdk.mapview.datasource")

  [fromXyzUrlTemplate](#fromXyzUrlTemplate(java.lang.String))`(`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` urlTemplate)`

Creates [`TileUrlProviderCallback`](sdk-for-android-explore-api-reference-latesttileurlprovidercallback "interface in com.here.sdk.mapview.datasource") for the given URL template.

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Method Details

### fromXyzUrlTemplate

@Nullable public static [TileUrlProviderCallback](sdk-for-android-explore-api-reference-latesttileurlprovidercallback "interface in com.here.sdk.mapview.datasource") fromXyzUrlTemplate(@NonNull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) urlTemplate)

    Creates [`TileUrlProviderCallback`](sdk-for-android-explore-api-reference-latesttileurlprovidercallback "interface in com.here.sdk.mapview.datasource") for the given URL template. A url template should look like this 'https://TestRasterTileService.com/{z}/{x}/{y}/' here the z parameter is the storage level, x and y define the location of the tile. The valid range for X and Y is from 0 to 2^level − 1.
Parameters:
    `urlTemplate` -

    The url template

    Returns:
    `null` if the provided template is not valid xyz url type.
