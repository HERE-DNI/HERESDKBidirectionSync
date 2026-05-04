---
title: "PlaceIdSearchCallback (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestplaceidsearchcallback"
hidden: false
---

Package [com.here.sdk.search](sdk-for-android-explore-api-reference-latestpackage-summary)

# Interface PlaceIdSearchCallback

Functional Interface:
This is a functional interface and can therefore be used as the assignment target for a lambda expression or method reference.

------------------------------------------------------------------------
[@FunctionalInterface](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/FunctionalInterface.html) public interface PlaceIdSearchCallback
The method will be called on the main thread when a search by id call has been completed.

## Method Summary

  All Methods
  Instance Methods
  Abstract Methods

  Modifier and Type

  Method

  Description

  `void`

  [onPlaceIdSearchCompleted](#onPlaceIdSearchCompleted(com.here.sdk.search.SearchError,com.here.sdk.search.Place))`(`[`SearchError`](sdk-for-android-explore-api-reference-latestsearcherror "enum class in com.here.sdk.search")` searchError, `[`Place`](sdk-for-android-explore-api-reference-latestplace "class in com.here.sdk.search")` place)`

The method will be called on the main thread when a search by id call has been completed.

## Method Details

### onPlaceIdSearchCompleted

void onPlaceIdSearchCompleted(@Nullable [SearchError](sdk-for-android-explore-api-reference-latestsearcherror "enum class in com.here.sdk.search") searchError, @Nullable [Place](sdk-for-android-explore-api-reference-latestplace "class in com.here.sdk.search") place)

    The method will be called on the main thread when a search by id call has been completed.
Parameters:
    `searchError` -

    The search error.

    `place` -

    The place.
