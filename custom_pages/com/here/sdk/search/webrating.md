---
title: "WebRating (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestwebrating"
hidden: false
---

Package [com.here.sdk.search](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class WebRating

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.search.WebRating
------------------------------------------------------------------------
public final class WebRating extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Contains information about rating and a url to review.

## Field Summary

Fields

Modifier and Type

  Field

  Description

  `double`

  [average](#average)

Avarage value of all ratings.

`int`

  [count](#count)

Total number of ratings.

[`WebSource`](sdk-for-android-explore-api-reference-latestwebsource "class in com.here.sdk.search")

  [source](#source)

Detailed information about rating.

## Constructor Summary

Constructors

Constructor

  Description

  [WebRating](#%3Cinit%3E())`()`

Creates a new instance.

[WebRating](#%3Cinit%3E(int,double,com.here.sdk.search.WebSource))`(int count, double average, `[`WebSource`](sdk-for-android-explore-api-reference-latestwebsource "class in com.here.sdk.search")` source)`

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

### count

public int count

    Total number of ratings.

### average

public double average

    Avarage value of all ratings.

### source

@NonNull public [WebSource](sdk-for-android-explore-api-reference-latestwebsource "class in com.here.sdk.search") source

    Detailed information about rating.

## Constructor Details

  - (int,double,com.here.sdk.search.WebSource)" class="section detail">

### WebRating

public WebRating(int count, double average, @NonNull [WebSource](sdk-for-android-explore-api-reference-latestwebsource "class in com.here.sdk.search") source)

    Creates a new instance.
Parameters:
    `count` -

    Total number of ratings.

    `average` -

    Avarage value of all ratings.

    `source` -

    Detailed information about rating.
- ()" class="section detail">

### WebRating

public WebRating()

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
