---
title: "Toll (API Reference)"
slug: "sdk-for-android-explore-api-reference-latesttoll"
hidden: false
---

Package [com.here.sdk.routing](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class Toll

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.routing.Toll
------------------------------------------------------------------------
public final class Toll extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
This struct presents all the data for a toll.

**Note**: If you're using the `OfflineRoutingEngine`, be aware that this feature is currently in **beta**. As a result, there may be some bugs or unexpected behaviors. Additionally, this feature and related APIs may be updated in future releases without going through the deprecation process. Note that the `OfflineRoutingEngine` is only available for the Navigate license. If you're using the `RoutingEngine`, this feature is considered to be stable.

## Field Summary

Fields

Modifier and Type

  Field

  Description

  [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [countryCode](#countryCode)

The country in which the toll is to be paid in ISO-3166-1 alpha-3 format, e.g.

[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`TollFare`](sdk-for-android-explore-api-reference-latesttollfare "class in com.here.sdk.routing")`>`

  [fares](#fares)

The list of toll fares possible for the toll which may depend on time of day, payment method, vehicle characteristics, etc.

[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`>`

  [tollSystems](#tollSystems)

Names of the multiple toll systems which are associated with the toll, e.g.

## Constructor Summary

Constructors

Constructor

  Description

  [Toll](#%3Cinit%3E())`()`

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

### countryCode

@NonNull public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) countryCode

    The country in which the toll is to be paid in ISO-3166-1 alpha-3 format, e.g. "USA".

### tollSystems

@NonNull public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)\> tollSystems

    Names of the multiple toll systems which are associated with the toll, e.g. \["ATLANDES“, "ASF", "COFIROUTE"\]. When the toll information covers several toll roads and the toll system of the each road is different, all toll system names are listed here and the last element will be one of the exit toll booth.

### fares

@NonNull public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[TollFare](sdk-for-android-explore-api-reference-latesttollfare "class in com.here.sdk.routing")\> fares

    The list of toll fares possible for the toll which may depend on time of day, payment method, vehicle characteristics, etc. If there are multiple toll fares that the router cannot disambiguate, then the list will contain more than one toll fare. Note that this list contains at least one element, i.e. it is never empty.

## Constructor Details

  - ()" class="section detail">

### Toll

public Toll()

## Method Details

### equals

public boolean equals([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) obj)
Overrides:
    [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

### hashCode

public int hashCode()
Overrides:
    [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
