---
title: "Attribution (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestattribution"
hidden: false
---

Package [com.here.sdk.routing](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class Attribution

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.routing.Attribution
------------------------------------------------------------------------
public final class Attribution extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Holds all the data on a URL address to an external resource.

## Field Summary

Fields

Modifier and Type

  Field

  Description

  [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [href](#href)

An URL address that links to a particular resource.

[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [hrefText](#hrefText)

The interactive (or clickable) portion of the text.

[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [text](#text)

Text describing the url address (e.g.

[`AttributionType`](sdk-for-android-explore-api-reference-latestattributiontype "enum class in com.here.sdk.routing")

  [type](#type)

Attribution link type.

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

### href

@Nullable public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) href

    An URL address that links to a particular resource.

### text

@NonNull public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) text

    Text describing the url address (e.g. The example website).

### hrefText

@Nullable public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) hrefText

    The interactive (or clickable) portion of the text. If not present (default), the entire content of the text attribute will be considered.

### type

@NonNull public [AttributionType](sdk-for-android-explore-api-reference-latestattributiontype "enum class in com.here.sdk.routing") type

    Attribution link type.

## Method Details

### equals

public boolean equals([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) obj)
Overrides:
    [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

### hashCode

public int hashCode()
Overrides:
    [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
