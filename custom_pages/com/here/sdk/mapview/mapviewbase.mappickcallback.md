---
title: "MapViewBase.MapPickCallback (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestmapviewbase-mappickcallback"
hidden: false
---

Package [com.here.sdk.mapview](sdk-for-android-explore-api-reference-latestpackage-summary)

# Interface MapViewBase.MapPickCallback

Enclosing interface:
[MapViewBase](sdk-for-android-explore-api-reference-latestmapviewbase "interface in com.here.sdk.mapview")

<!-- -->

Functional Interface:
This is a functional interface and can therefore be used as the assignment target for a lambda expression or method reference.

------------------------------------------------------------------------
[@FunctionalInterface](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/FunctionalInterface.html) public static interface MapViewBase.MapPickCallback
Callback for a pick request. In case of an error the result is not set.

## Method Summary

  All Methods
  Instance Methods
  Abstract Methods

  Modifier and Type

  Method

  Description

  `void`

  [onPickMap](#onPickMap(com.here.sdk.mapview.MapPickResult))`(`[`MapPickResult`](sdk-for-android-explore-api-reference-latestmappickresult "class in com.here.sdk.mapview")` mapPickResult)`

Callback for a pick request.

## Method Details

### onPickMap

void onPickMap(@Nullable [MapPickResult](sdk-for-android-explore-api-reference-latestmappickresult "class in com.here.sdk.mapview") mapPickResult)

    Callback for a pick request. In case of an error the result is not set.
Parameters:
    `mapPickResult` -

    The operation result.
