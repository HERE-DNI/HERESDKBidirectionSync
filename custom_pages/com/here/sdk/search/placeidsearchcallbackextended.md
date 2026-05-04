---
title: "PlaceIdSearchCallbackExtended (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestplaceidsearchcallbackextended"
hidden: false
---

Package [com.here.sdk.search](sdk-for-android-explore-api-reference-latestpackage-summary)

# Interface PlaceIdSearchCallbackExtended

Functional Interface:
This is a functional interface and can therefore be used as the assignment target for a lambda expression or method reference.

------------------------------------------------------------------------
[@FunctionalInterface](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/FunctionalInterface.html) public interface PlaceIdSearchCallbackExtended
The method will be called on the main thread when a search by id call has been completed.

## Method Summary

  All Methods
  Instance Methods
  Abstract Methods

  Modifier and Type

  Method

  Description

  `void`

  [onPlaceIdSearchExtendedCompleted](#onPlaceIdSearchExtendedCompleted(com.here.sdk.search.SearchError,com.here.sdk.search.Place,com.here.sdk.search.ResponseDetails))`(`[`SearchError`](sdk-for-android-explore-api-reference-latestsearcherror "enum class in com.here.sdk.search")` searchError, `[`Place`](sdk-for-android-explore-api-reference-latestplace "class in com.here.sdk.search")` place, `[`ResponseDetails`](sdk-for-android-explore-api-reference-latestresponsedetails "class in com.here.sdk.search")` responseDetails)`

The method will be called on the main thread when a search by id call has been completed.

## Method Details

### onPlaceIdSearchExtendedCompleted

void onPlaceIdSearchExtendedCompleted(@Nullable [SearchError](sdk-for-android-explore-api-reference-latestsearcherror "enum class in com.here.sdk.search") searchError, @Nullable [Place](sdk-for-android-explore-api-reference-latestplace "class in com.here.sdk.search") place, @Nullable [ResponseDetails](sdk-for-android-explore-api-reference-latestresponsedetails "class in com.here.sdk.search") responseDetails)

    The method will be called on the main thread when a search by id call has been completed.
Parameters:
    `searchError` -

    The search error.

    `place` -

    The place.

    `responseDetails` -

    The response details.
