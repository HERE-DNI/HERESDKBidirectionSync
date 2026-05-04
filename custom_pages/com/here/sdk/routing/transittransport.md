---
title: "TransitTransport (API Reference)"
slug: "sdk-for-android-explore-api-reference-latesttransittransport"
hidden: false
---

Package [com.here.sdk.routing](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class TransitTransport

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.routing.TransitTransport
------------------------------------------------------------------------
public final class TransitTransport extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Holds all the transit transport information.

## Field Summary

Fields

Modifier and Type

  Field

  Description

  [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [category](#category)

Human readable transport category (such as Bus, Gondola, Tram, Train, ...)

[`Color`](sdk-for-android-explore-api-reference-latestcolor "class in com.here.sdk.core")

  [color](#color)

Color of the transport polyline and background for the transport name.

[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [headsign](#headsign)

Transit line headsign.

[`TransitMode`](sdk-for-android-explore-api-reference-latesttransitmode "enum class in com.here.sdk.routing")

  [mode](#mode)

Transit mode of transport in the route.

[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [name](#name)

Transit line name.

[`Color`](sdk-for-android-explore-api-reference-latestcolor "class in com.here.sdk.core")

  [textColor](#textColor)

Color of the transport name.

## Constructor Summary

Constructors

Constructor

  Description

  [TransitTransport](#%3Cinit%3E(com.here.sdk.routing.TransitMode,java.lang.String,java.lang.String,java.lang.String,com.here.sdk.core.Color,com.here.sdk.core.Color))`(`[`TransitMode`](sdk-for-android-explore-api-reference-latesttransitmode "enum class in com.here.sdk.routing")` mode, `[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` name, `[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` headsign, `[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` category, `[`Color`](sdk-for-android-explore-api-reference-latestcolor "class in com.here.sdk.core")` color, `[`Color`](sdk-for-android-explore-api-reference-latestcolor "class in com.here.sdk.core")` textColor)`

Creates a new instance.

## Method Summary

  All Methods
  Instance Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  `boolean`

  [equals](#equals(java.lang.Object))`(`[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)` obj)`

  `int`

  [hashCode](#hashCode())`()`

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Field Details

### mode

@NonNull public [TransitMode](sdk-for-android-explore-api-reference-latesttransitmode "enum class in com.here.sdk.routing") mode

    Transit mode of transport in the route.

### name

@Nullable public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name

    Transit line name.

### headsign

@Nullable public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) headsign

    Transit line headsign.

### category

@Nullable public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) category

    Human readable transport category (such as Bus, Gondola, Tram, Train, ...)

### color

@Nullable public [Color](sdk-for-android-explore-api-reference-latestcolor "class in com.here.sdk.core") color

    Color of the transport polyline and background for the transport name.

### textColor

@Nullable public [Color](sdk-for-android-explore-api-reference-latestcolor "class in com.here.sdk.core") textColor

    Color of the transport name.

## Constructor Details

  - (com.here.sdk.routing.TransitMode,java.lang.String,java.lang.String,java.lang.String,com.here.sdk.core.Color,com.here.sdk.core.Color)" class="section detail">

### TransitTransport

public TransitTransport(@NonNull [TransitMode](sdk-for-android-explore-api-reference-latesttransitmode "enum class in com.here.sdk.routing") mode, @Nullable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name, @Nullable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) headsign, @Nullable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) category, @Nullable [Color](sdk-for-android-explore-api-reference-latestcolor "class in com.here.sdk.core") color, @Nullable [Color](sdk-for-android-explore-api-reference-latestcolor "class in com.here.sdk.core") textColor)

    Creates a new instance.
Parameters:
    `mode` -

    Transit mode of transport in the route.

    `name` -

    Transit line name.

    `headsign` -

    Transit line headsign.

    `category` -

    Human readable transport category (such as Bus, Gondola, Tram, Train, ...)

    `color` -

    Color of the transport polyline and background for the transport name.

    `textColor` -

    Color of the transport name.

## Method Details

### equals

public boolean equals([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) obj)
Overrides:
    [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

### hashCode

public int hashCode()
Overrides:
    [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
