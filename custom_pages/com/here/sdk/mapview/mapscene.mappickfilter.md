---
title: "MapScene.MapPickFilter (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestmapscene-mappickfilter"
hidden: false
---

Package [com.here.sdk.mapview](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class MapScene.MapPickFilter

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.here.NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
com.here.sdk.mapview.MapScene.MapPickFilter
Enclosing class:
[MapScene](sdk-for-android-explore-api-reference-latestmapscene "class in com.here.sdk.mapview")

------------------------------------------------------------------------
public static final class MapScene.MapPickFilter extends [NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
Filter for the map content to be picked.

## Nested Class Summary

Nested Classes

Modifier and Type

  Class

  Description

  `static enum `

  [MapScene.MapPickFilter.ContentType](sdk-for-android-explore-api-reference-latestmapscene-mappickfilter-contenttype)

Type of the map content to be picked.

## Constructor Summary

Constructors

Constructor

  Description

  [MapPickFilter](#%3Cinit%3E(java.util.List))`(`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`MapScene.MapPickFilter.ContentType`](sdk-for-android-explore-api-reference-latestmapscene-mappickfilter-contenttype "enum class in com.here.sdk.mapview")`> filter)`

Creates a new instance of [`MapScene.MapPickFilter`](sdk-for-android-explore-api-reference-latestmapscene-mappickfilter "class in com.here.sdk.mapview").

## Method Summary

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Constructor Details

  - (java.util.List)" class="section detail">

### MapPickFilter

public MapPickFilter(@NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[MapScene.MapPickFilter.ContentType](sdk-for-android-explore-api-reference-latestmapscene-mappickfilter-contenttype "enum class in com.here.sdk.mapview")\> filter)

    Creates a new instance of [`MapScene.MapPickFilter`](sdk-for-android-explore-api-reference-latestmapscene-mappickfilter "class in com.here.sdk.mapview").
Parameters:
    `filter` -

    List of pickable map content. For an empty list all of the content will be picked.
