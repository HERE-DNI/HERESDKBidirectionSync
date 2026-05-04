---
title: "WebImage (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestwebimage"
hidden: false
---

Package [com.here.sdk.search](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class WebImage

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.search.WebImage
------------------------------------------------------------------------
public final class WebImage extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Contains image information and direct link to it.

## Field Summary

Fields

Modifier and Type

  Field

  Description

  [`WebSource`](sdk-for-android-explore-api-reference-latestwebsource "class in com.here.sdk.search")

  [source](#source)

Detailed information about image source.

## Constructor Summary

Constructors

Constructor

  Description

  [WebImage](#%3Cinit%3E(com.here.sdk.search.WebSource))`(`[`WebSource`](sdk-for-android-explore-api-reference-latestwebsource "class in com.here.sdk.search")` source)`

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

### source

@NonNull public [WebSource](sdk-for-android-explore-api-reference-latestwebsource "class in com.here.sdk.search") source

    Detailed information about image source.

## Constructor Details

  - (com.here.sdk.search.WebSource)" class="section detail">

### WebImage

public WebImage(@NonNull [WebSource](sdk-for-android-explore-api-reference-latestwebsource "class in com.here.sdk.search") source)

    Creates a new instance. Sets [`source`](#source) to the given source.
Parameters:
    `source` -

    Detailed information about image source.

## Method Details

### equals

public boolean equals([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) obj)
Overrides:
    [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

### hashCode

public int hashCode()
Overrides:
    [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
