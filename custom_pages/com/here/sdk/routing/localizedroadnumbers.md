---
title: "LocalizedRoadNumbers (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestlocalizedroadnumbers"
hidden: false
---

Package [com.here.sdk.routing](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class LocalizedRoadNumbers

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.routing.LocalizedRoadNumbers
------------------------------------------------------------------------
public final class LocalizedRoadNumbers extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
The list of multiple names or titles for the same entity, possibly in different languages.

## Field Summary

Fields

Modifier and Type

  Field

  Description

  [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`LocalizedRoadNumber`](sdk-for-android-explore-api-reference-latestlocalizedroadnumber "class in com.here.sdk.routing")`>`

  [items](#items)

The list of road number information items.

## Constructor Summary

Constructors

Constructor

  Description

  [LocalizedRoadNumbers](#%3Cinit%3E())`()`

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

  [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [getDefaultValue](#getDefaultValue())`()`

Returns the default value.

[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [getPreferredValueForLocales](#getPreferredValueForLocales(java.util.List))`(`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[Locale](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Locale.html)`> locales)`

Returns best name or title to be presented to the user according to specified locales.

`int`

  [hashCode](#hashCode())`()`

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Field Details

### items

@NonNull public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[LocalizedRoadNumber](sdk-for-android-explore-api-reference-latestlocalizedroadnumber "class in com.here.sdk.routing")\> items

    The list of road number information items. Recommended to use helper methods instead of directly accessing the items.

## Constructor Details

  - ()" class="section detail">

### LocalizedRoadNumbers

public LocalizedRoadNumbers()

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

### getPreferredValueForLocales

@Nullable public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getPreferredValueForLocales(@NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[Locale](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Locale.html)\> locales)

    Returns best name or title to be presented to the user according to specified locales. The locales are expected to be ordered by priority. If no matching locale found - the default is returned. In case of empty list returns `null`.
Parameters:
    `locales` -

    Locales

    Returns:
    The best name or title to be presented to the user according to specified locales, default or `null` if list is empty.

### getDefaultValue

@Nullable public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getDefaultValue()

    Returns the default value.
Returns:
    The default value or null\` if list is empty.
