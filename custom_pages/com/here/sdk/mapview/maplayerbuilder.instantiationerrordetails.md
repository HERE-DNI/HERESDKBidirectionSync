---
title: "MapLayerBuilder.InstantiationErrorDetails (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestmaplayerbuilder-instantiationerrordetails"
hidden: false
---

Package [com.here.sdk.mapview](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class MapLayerBuilder.InstantiationErrorDetails

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.mapview.MapLayerBuilder.InstantiationErrorDetails
Enclosing class:
[MapLayerBuilder](sdk-for-android-explore-api-reference-latestmaplayerbuilder "class in com.here.sdk.mapview")

------------------------------------------------------------------------
public static final class MapLayerBuilder.InstantiationErrorDetails extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Describes the reason for failing to build a [`MapLayer`](sdk-for-android-explore-api-reference-latestmaplayer "class in com.here.sdk.mapview").

## Field Summary

Fields

Modifier and Type

  Field

  Description

  [`MapLayerBuilder.InstantiationErrorCode`](sdk-for-android-explore-api-reference-latestmaplayerbuilder-instantiationerrorcode "enum class in com.here.sdk.mapview")

  [errorCode](#errorCode)

The error code.

[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [errorDescription](#errorDescription)

A description of the error, if available.

## Constructor Summary

Constructors

Constructor

  Description

  [InstantiationErrorDetails](#%3Cinit%3E(com.here.sdk.mapview.MapLayerBuilder.InstantiationErrorCode,java.lang.String))`(`[`MapLayerBuilder.InstantiationErrorCode`](sdk-for-android-explore-api-reference-latestmaplayerbuilder-instantiationerrorcode "enum class in com.here.sdk.mapview")` errorCode, `[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` errorDescription)`

Creates a new instance.

## Method Summary

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Field Details

### errorCode

@NonNull public [MapLayerBuilder.InstantiationErrorCode](sdk-for-android-explore-api-reference-latestmaplayerbuilder-instantiationerrorcode "enum class in com.here.sdk.mapview") errorCode

    The error code.

### errorDescription

@Nullable public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) errorDescription

    A description of the error, if available.

## Constructor Details

  - (com.here.sdk.mapview.MapLayerBuilder.InstantiationErrorCode,java.lang.String)" class="section detail">

### InstantiationErrorDetails

public InstantiationErrorDetails(@NonNull [MapLayerBuilder.InstantiationErrorCode](sdk-for-android-explore-api-reference-latestmaplayerbuilder-instantiationerrorcode "enum class in com.here.sdk.mapview") errorCode, @Nullable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) errorDescription)

    Creates a new instance.
Parameters:
    `errorCode` -

    The error code.

    `errorDescription` -

    A description of the error, if available.
