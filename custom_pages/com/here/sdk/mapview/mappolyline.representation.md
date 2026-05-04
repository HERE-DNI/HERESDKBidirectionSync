---
title: "MapPolyline.Representation (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestmappolyline-representation"
hidden: false
---

Package [com.here.sdk.mapview](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class MapPolyline.Representation

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.here.NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
[com.here.sdk.mapview.MapItemRepresentation](sdk-for-android-explore-api-reference-latestmapitemrepresentation "class in com.here.sdk.mapview")
com.here.sdk.mapview.MapPolyline.Representation
Direct Known Subclasses:
[`MapPolyline.DashImageRepresentation`](sdk-for-android-explore-api-reference-latestmappolyline-dashimagerepresentation "class in com.here.sdk.mapview"), [`MapPolyline.DashRepresentation`](sdk-for-android-explore-api-reference-latestmappolyline-dashrepresentation "class in com.here.sdk.mapview"), [`MapPolyline.SolidRepresentation`](sdk-for-android-explore-api-reference-latestmappolyline-solidrepresentation "class in com.here.sdk.mapview")

<!-- -->

Enclosing class:
[MapPolyline](sdk-for-android-explore-api-reference-latestmappolyline "class in com.here.sdk.mapview")

------------------------------------------------------------------------
public static class MapPolyline.Representation extends [MapItemRepresentation](sdk-for-android-explore-api-reference-latestmapitemrepresentation "class in com.here.sdk.mapview")
Base class to represent the visual appearance of a [`MapPolyline`](sdk-for-android-explore-api-reference-latestmappolyline "class in com.here.sdk.mapview").

## Nested Class Summary

Nested Classes

Modifier and Type

  Class

  Description

  `static enum `

  [MapPolyline.Representation.InstantiationErrorCode](sdk-for-android-explore-api-reference-latestmappolyline-representation-instantiationerrorcode)

Describes a reason for failing to create a [`MapPolyline.Representation`](sdk-for-android-explore-api-reference-latestmappolyline-representation "class in com.here.sdk.mapview").

`static final class `

  [MapPolyline.Representation.InstantiationException](sdk-for-android-explore-api-reference-latestmappolyline-representation-instantiationexception)

Thrown when a problem occurs while trying to create [`MapPolyline.Representation`](sdk-for-android-explore-api-reference-latestmappolyline-representation "class in com.here.sdk.mapview").

## Method Summary

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))
