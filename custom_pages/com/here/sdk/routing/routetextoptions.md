---
title: "RouteTextOptions (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestroutetextoptions"
hidden: false
---

Package [com.here.sdk.routing](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class RouteTextOptions

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.routing.RouteTextOptions
------------------------------------------------------------------------
public final class RouteTextOptions extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Specify how textual output should be provided.

## Field Summary

Fields

Modifier and Type

  Field

  Description

  [`LanguageCode`](sdk-for-android-explore-api-reference-latestlanguagecode "enum class in com.here.sdk.core")

  [language](#language)

The language for all textual information.

[`TextUsageOptions`](sdk-for-android-explore-api-reference-latesttextusageoptions "class in com.here.sdk.routing")

  [textUsageOptions](#textUsageOptions)

An option whether street name, road number and sign post direction should be used when generating notification.

[`UnitSystem`](sdk-for-android-explore-api-reference-latestunitsystem "enum class in com.here.sdk.core")

  [unitSystem](#unitSystem)

Defines the measurement system used in instruction text.

## Constructor Summary

Constructors

Constructor

  Description

  [RouteTextOptions](#%3Cinit%3E())`()`

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

### language

@NonNull public [LanguageCode](sdk-for-android-explore-api-reference-latestlanguagecode "enum class in com.here.sdk.core") language

    The language for all textual information. When the specified language is not supported, the default language is used, which is English (United States).

### unitSystem

@NonNull public [UnitSystem](sdk-for-android-explore-api-reference-latestunitsystem "enum class in com.here.sdk.core") unitSystem

    Defines the measurement system used in instruction text. When imperial is selected, units used are based on the language specified in the request. Defaults to metric.

### textUsageOptions

@NonNull public [TextUsageOptions](sdk-for-android-explore-api-reference-latesttextusageoptions "class in com.here.sdk.routing") textUsageOptions

    An option whether street name, road number and sign post direction should be used when generating notification. Defaults to each attribute as [`LocalizedTextPreference.USE_ALWAYS`](sdk-for-android-explore-api-reference-latestlocalizedtextpreference#USE_ALWAYS).

## Constructor Details

  - ()" class="section detail">

### RouteTextOptions

public RouteTextOptions()

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
