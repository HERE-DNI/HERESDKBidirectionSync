---
title: "MapMarkerCluster.CounterStyle (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestmapmarkercluster-counterstyle"
hidden: false
---

Package [com.here.sdk.mapview](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class MapMarkerCluster.CounterStyle

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.mapview.MapMarkerCluster.CounterStyle
Enclosing class:
[MapMarkerCluster](sdk-for-android-explore-api-reference-latestmapmarkercluster "class in com.here.sdk.mapview")

------------------------------------------------------------------------
public static final class MapMarkerCluster.CounterStyle extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Styling options for a marker cluster which is represented by the marker count as a text.

## Field Summary

Fields

Modifier and Type

  Field

  Description

  [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [aboveMaxText](#aboveMaxText)

String to display if there are more markers clustered than [`maxCountNumber`](#maxCountNumber).

`double`

  [fontSize](#fontSize)

Font size of counter.

`int`

  [maxCountNumber](#maxCountNumber)

Maximal number of markers represented as exact number.

[`Anchor2D`](sdk-for-android-explore-api-reference-latestanchor2d "class in com.here.sdk.core")

  [textAnchor](#textAnchor)

Anchor of counter in regards to marker cluster image.

[`Color`](sdk-for-android-explore-api-reference-latestcolor "class in com.here.sdk.core")

  [textColor](#textColor)

Font color of counter.

## Constructor Summary

Constructors

Constructor

  Description

  [CounterStyle](#%3Cinit%3E())`()`

Creates a new instance.

## Method Summary

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Field Details

### textColor

@NonNull public [Color](sdk-for-android-explore-api-reference-latestcolor "class in com.here.sdk.core") textColor

    Font color of counter. Default value is white.

### fontSize

public double fontSize

    Font size of counter. Default value is 20.

### textAnchor

@NonNull public [Anchor2D](sdk-for-android-explore-api-reference-latestanchor2d "class in com.here.sdk.core") textAnchor

    Anchor of counter in regards to marker cluster image. Default is at the center.

### maxCountNumber

public int maxCountNumber

    Maximal number of markers represented as exact number. Values smaller than 2 will be clamped to 2. Default value is 99. When this value is changed, it is recommended to adapt [`aboveMaxText`](#aboveMaxText) accordingly.

### aboveMaxText

@NonNull public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) aboveMaxText

    String to display if there are more markers clustered than [`maxCountNumber`](#maxCountNumber). Default value is "+99".

## Constructor Details

  - ()" class="section detail">

### CounterStyle

public CounterStyle()

    Creates a new instance.
