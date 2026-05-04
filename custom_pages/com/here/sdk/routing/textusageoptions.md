---
title: "TextUsageOptions (API Reference)"
slug: "sdk-for-android-explore-api-reference-latesttextusageoptions"
hidden: false
---

Package [com.here.sdk.routing](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class TextUsageOptions

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.routing.TextUsageOptions
------------------------------------------------------------------------
public final class TextUsageOptions extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Specify whether the text should be used when generating notification.

## Field Summary

Fields

Modifier and Type

  Field

  Description

  [`LocalizedTextPreference`](sdk-for-android-explore-api-reference-latestlocalizedtextpreference "enum class in com.here.sdk.routing")

  [roadNumber](#roadNumber)

An option whether road number should be used when generating notification.

[`LocalizedTextPreference`](sdk-for-android-explore-api-reference-latestlocalizedtextpreference "enum class in com.here.sdk.routing")

  [signpostDirection](#signpostDirection)

An option whether signpost direction should be used when generating notification.

[`LocalizedTextPreference`](sdk-for-android-explore-api-reference-latestlocalizedtextpreference "enum class in com.here.sdk.routing")

  [streetName](#streetName)

An option whether street name should be used when generating notification.

## Constructor Summary

Constructors

Constructor

  Description

  [TextUsageOptions](#%3Cinit%3E())`()`

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

### streetName

@NonNull public [LocalizedTextPreference](sdk-for-android-explore-api-reference-latestlocalizedtextpreference "enum class in com.here.sdk.routing") streetName

    An option whether street name should be used when generating notification. Defaults to [`LocalizedTextPreference.USE_ALWAYS`](sdk-for-android-explore-api-reference-latestlocalizedtextpreference#USE_ALWAYS).

### roadNumber

@NonNull public [LocalizedTextPreference](sdk-for-android-explore-api-reference-latestlocalizedtextpreference "enum class in com.here.sdk.routing") roadNumber

    An option whether road number should be used when generating notification. Defaults to [`LocalizedTextPreference.USE_ALWAYS`](sdk-for-android-explore-api-reference-latestlocalizedtextpreference#USE_ALWAYS).

### signpostDirection

@NonNull public [LocalizedTextPreference](sdk-for-android-explore-api-reference-latestlocalizedtextpreference "enum class in com.here.sdk.routing") signpostDirection

    An option whether signpost direction should be used when generating notification. Defaults to [`LocalizedTextPreference.USE_ALWAYS`](sdk-for-android-explore-api-reference-latestlocalizedtextpreference#USE_ALWAYS).

## Constructor Details

  - ()" class="section detail">

### TextUsageOptions

public TextUsageOptions()

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
