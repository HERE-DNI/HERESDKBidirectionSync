---
title: "SearchOptions (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestsearchoptions"
hidden: false
---

Package [com.here.sdk.search](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class SearchOptions

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.search.SearchOptions
------------------------------------------------------------------------
public final class SearchOptions extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Encapsulates options that control the behavior of search and suggest operations.

## Field Summary

Fields

Modifier and Type

  Field

  Description

  `boolean`

  [distributedResults](#distributedResults)

Indicates if search along the route should produce well-distributed results.

`boolean`

  [highDensityEncodingEnabled](#highDensityEncodingEnabled)

Allows enabling high density encoding of relevant parameters.

[`LanguageCode`](sdk-for-android-explore-api-reference-latestlanguagecode "enum class in com.here.sdk.core")

  [languageCode](#languageCode)

The preferred language of the result.

[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html)

  [maxItems](#maxItems)

The maximum number of items in the response.

## Constructor Summary

Constructors

Constructor

  Description

  [SearchOptions](#%3Cinit%3E())`()`

Creates an Options object.

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

### languageCode

@Nullable public [LanguageCode](sdk-for-android-explore-api-reference-latestlanguagecode "enum class in com.here.sdk.core") languageCode

    The preferred language of the result. When unset or unsupported language is chosen, results will be returned in their local language.

### maxItems

@Nullable public [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) maxItems

    The maximum number of items in the response. It should be in the range \[1, 100\]. When not set, results will be limited to 20. For location search (reverse geocode) by default results limited to 1.

### highDensityEncodingEnabled

public boolean highDensityEncodingEnabled

    Allows enabling high density encoding of relevant parameters. For now, it only affects input parameters of type `GeoCorridor`. Only supported for search in `SearchEngine`, otherwise it is ignored. **Note:** This is a closed-alpha release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process. Only participants of the closed-alpha group can get access from HERE to use this feature, otherwise, a [`SearchError.FORBIDDEN`](sdk-for-android-explore-api-reference-latestsearcherror#FORBIDDEN) will be propagated in callbacks.

### distributedResults

public boolean distributedResults

    Indicates if search along the route should produce well-distributed results. It is only supported for:

    - `searchByCategory` API with [`CategoryQuery.Area.corridorArea`](sdk-for-android-explore-api-reference-latestcategoryquery-area#corridorArea) set
    - `searchByText` API with [`TextQuery.Area.corridorArea`](sdk-for-android-explore-api-reference-latesttextquery-area#corridorArea) set Otherwise, this value is ignored.

## Constructor Details

  - ()" class="section detail">

### SearchOptions

public SearchOptions()

    Creates an Options object. If no parameters are passed, uses default values (see fields description).

## Method Details

### equals

public boolean equals([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) obj)
Overrides:
    [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

### hashCode

public int hashCode()
Overrides:
    [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
