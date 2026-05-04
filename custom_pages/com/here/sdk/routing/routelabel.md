---
title: "RouteLabel (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestroutelabel"
hidden: false
---

Package [com.here.sdk.routing](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class RouteLabel

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.routing.RouteLabel
------------------------------------------------------------------------
public final class RouteLabel extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
The main street name or road number for a route. A route can contain more than one such street name or route number. To include route labels in the route response, enable it using [`RouteOptions.enableRouteLabels`](sdk-for-android-explore-api-reference-latestrouteoptions#enableRouteLabels).

## Field Summary

Fields

Modifier and Type

  Field

  Description

  [`LocalizedText`](sdk-for-android-explore-api-reference-latestlocalizedtext "class in com.here.sdk.core")

  [name](#name)

The street name or route number for the route label.

[`RouteLabelType`](sdk-for-android-explore-api-reference-latestroutelabeltype "enum class in com.here.sdk.routing")

  [type](#type)

The type of the route label, describing if the route label contains a street name or a route number.

## Constructor Summary

Constructors

Constructor

  Description

  [RouteLabel](#%3Cinit%3E(com.here.sdk.core.LocalizedText))`(`[`LocalizedText`](sdk-for-android-explore-api-reference-latestlocalizedtext "class in com.here.sdk.core")` name)`

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

### name

@NonNull public [LocalizedText](sdk-for-android-explore-api-reference-latestlocalizedtext "class in com.here.sdk.core") name

    The street name or route number for the route label.

### type

@NonNull public [RouteLabelType](sdk-for-android-explore-api-reference-latestroutelabeltype "enum class in com.here.sdk.routing") type

    The type of the route label, describing if the route label contains a street name or a route number.

## Constructor Details

  - (com.here.sdk.core.LocalizedText)" class="section detail">

### RouteLabel

public RouteLabel(@NonNull [LocalizedText](sdk-for-android-explore-api-reference-latestlocalizedtext "class in com.here.sdk.core") name)

    Creates a new instance.
Parameters:
    `name` -

    The street name or route number for the route label.

## Method Details

### equals

public boolean equals([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) obj)
Overrides:
    [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

### hashCode

public int hashCode()
Overrides:
    [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
