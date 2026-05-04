---
title: "SearchCallback (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestsearchcallback"
hidden: false
---

Package [com.here.sdk.search](sdk-for-android-explore-api-reference-latestpackage-summary)

# Interface SearchCallback

Functional Interface:
This is a functional interface and can therefore be used as the assignment target for a lambda expression or method reference.

------------------------------------------------------------------------
[@FunctionalInterface](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/FunctionalInterface.html) public interface SearchCallback
The method will be called on the main thread when a search call has been completed. The first argument indicates an error in case of a failure. The second argument contains the results. Both arguments cannot be `null` at the same time - or not `null` at the same time.

## Method Summary

  All Methods
  Instance Methods
  Abstract Methods

  Modifier and Type

  Method

  Description

  `void`

  [onSearchCompleted](#onSearchCompleted(com.here.sdk.search.SearchError,java.util.List))`(`[`SearchError`](sdk-for-android-explore-api-reference-latestsearcherror "enum class in com.here.sdk.search")` searchError, `[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`Place`](sdk-for-android-explore-api-reference-latestplace "class in com.here.sdk.search")`> places)`

The method will be called on the main thread when a search call has been completed.

## Method Details

### onSearchCompleted

void onSearchCompleted(@Nullable [SearchError](sdk-for-android-explore-api-reference-latestsearcherror "enum class in com.here.sdk.search") searchError, @Nullable [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[Place](sdk-for-android-explore-api-reference-latestplace "class in com.here.sdk.search")\> places)

    The method will be called on the main thread when a search call has been completed. The first argument indicates an error in case of a failure. The second argument contains the results. Both arguments cannot be `null` at the same time - or not `null` at the same time.
Parameters:
    `searchError` -

    An error enum indicating what went wrong. It is `null` for an operation that succeeds.

    `places` -

    The list of search results. It is `null` in case of an error.
