---
title: "EVMobilityServiceProviderPreferences (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestevmobilityserviceproviderpreferences"
hidden: false
---

Package [com.here.sdk.routing](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class EVMobilityServiceProviderPreferences

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.routing.EVMobilityServiceProviderPreferences
------------------------------------------------------------------------
public final class EVMobilityServiceProviderPreferences extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Defines preference level per known E-Mobility Service Provider. The E-Mobility Service Provider ID partner id as received from https://www.here.com/docs/bundle/ev-charge-points-api-developer-guide/page/topics/resource-roamings.html An alternative way to get `partnerId` is the `eMobilityServiceProviders.partnerId` as part of `HERE SDK Search`. Maximum number of E-Mobility Service Providers is limited to 10 across all preference. Defaults to using all available providers with no prioritization.

## Field Summary

Fields

Modifier and Type

  Field

  Description

  [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`>`

  [high](#high)

Specifies the E-Mobility Service Provider partnerId that are preferred the most.

[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`>`

  [low](#low)

Specifies the E-Mobility Service Provider partnerId that are preferred the least.

[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`>`

  [medium](#medium)

Specifies the E-Mobility Service Provider partnerId that can be used when no better provider could be found or reached.

## Constructor Summary

Constructors

Constructor

  Description

  [EVMobilityServiceProviderPreferences](#%3Cinit%3E())`()`

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

### high

@NonNull public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)\> high

    Specifies the E-Mobility Service Provider partnerId that are preferred the most.

### medium

@NonNull public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)\> medium

    Specifies the E-Mobility Service Provider partnerId that can be used when no better provider could be found or reached.

### low

@NonNull public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)\> low

    Specifies the E-Mobility Service Provider partnerId that are preferred the least.

## Constructor Details

  - ()" class="section detail">

### EVMobilityServiceProviderPreferences

public EVMobilityServiceProviderPreferences()

    Creates a new instance.

## Method Details

### equals

public boolean equals([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) obj)
Overrides:
    [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

### hashCode

public int hashCode()
Overrides:
    [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
