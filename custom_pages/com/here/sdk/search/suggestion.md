---
title: "Suggestion (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestsuggestion"
hidden: false
---

Package [com.here.sdk.search](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class Suggestion

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.here.NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
com.here.sdk.search.Suggestion
------------------------------------------------------------------------
public final class Suggestion extends [NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
Suggestion is meant to provide relevant suggestions to partial queries, like "restaur", "starbu", "eiffel". Represents a relevant response to user queries. Suggestions (please check [`SuggestionType`](sdk-for-android-explore-api-reference-latestsuggestiontype "enum class in com.here.sdk.search")) are either: Place: [`SuggestionType.PLACE`](sdk-for-android-explore-api-reference-latestsuggestiontype#PLACE) Query: [`SuggestionType.CHAIN`](sdk-for-android-explore-api-reference-latestsuggestiontype#CHAIN) or [`SuggestionType.CATEGORY`](sdk-for-android-explore-api-reference-latestsuggestiontype#CATEGORY)

With "Place" you get data for a concrete place in the world. With "Query" something to follow-up, a way to perform more focused search.

## Method Summary

  All Methods
  Instance Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)`<`[`HighlightType`](sdk-for-android-explore-api-reference-latesthighlighttype "enum class in com.here.sdk.search"), [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`IndexRange`](android-sdk-apirange "class in com.here.sdk.search")`>>`

  [getHighlights](#getHighlights())`()`

The text slices matching the input query.

[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [getHref](#getHref())`()`

Gets the direct link for Discover query.

[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [getId](#getId())`()`

Gets the suggested item id.

[`Place`](sdk-for-android-explore-api-reference-latestplace "class in com.here.sdk.search")

  [getPlace](#getPlace())`()`

Gets the suggested place item.

[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [getTitle](#getTitle())`()`

Gets the localized title for the suggestion.

[`SuggestionType`](sdk-for-android-explore-api-reference-latestsuggestiontype "enum class in com.here.sdk.search")

  [getType](#getType())`()`

Gets the type of suggestion.

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Method Details

### getHighlights

@NonNull public [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)\<[HighlightType](sdk-for-android-explore-api-reference-latesthighlighttype "enum class in com.here.sdk.search"),[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[IndexRange](android-sdk-apirange "class in com.here.sdk.search")\>\> getHighlights()

    The text slices matching the input query.
Returns:
    Associated container where [`HighlightType`](sdk-for-android-explore-api-reference-latesthighlighttype "enum class in com.here.sdk.search") is a key and list of [`IndexRange`](android-sdk-apirange "class in com.here.sdk.search") value.

### getTitle

@NonNull public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getTitle()

    Gets the localized title for the suggestion.
Returns:
    The localized title for the suggestion.

### getType

@NonNull public [SuggestionType](sdk-for-android-explore-api-reference-latestsuggestiontype "enum class in com.here.sdk.search") getType()

    Gets the type of suggestion.
Returns:
    Type of the suggestion.

### getPlace

@Nullable public [Place](sdk-for-android-explore-api-reference-latestplace "class in com.here.sdk.search") getPlace()

    Gets the suggested place item.

    Available only for [`SuggestionType.PLACE`](sdk-for-android-explore-api-reference-latestsuggestiontype#PLACE).
Returns:
    The suggested place.

### getId

@Nullable public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getId()

    Gets the suggested item id.

    For online search, suggestion of type [`SuggestionType.PLACE`](sdk-for-android-explore-api-reference-latestsuggestiontype#PLACE) will have Suggestion.id same as Place.id. For offline search, only suggestion of type [`SuggestionType.CHAIN`](sdk-for-android-explore-api-reference-latestsuggestiontype#CHAIN), will have this property filled with identifier number of an associated chain. For example, the chain ID "8778" corresponds to the chain name "ABC Shop". For other types, [`SuggestionType.PLACE`](sdk-for-android-explore-api-reference-latestsuggestiontype#PLACE) and [`SuggestionType.CATEGORY`](sdk-for-android-explore-api-reference-latestsuggestiontype#CATEGORY) this property will be null.
Returns:
    The unique id of suggested item. It can be used to query further information.

### getHref

@Nullable public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getHref()

    Gets the direct link for Discover query.

    Available only for [`SuggestionType.CHAIN`](sdk-for-android-explore-api-reference-latestsuggestiontype#CHAIN) and [`SuggestionType.CATEGORY`](sdk-for-android-explore-api-reference-latestsuggestiontype#CATEGORY). This is not supported in offline search.
Returns:
    Direct URL for precise query.
