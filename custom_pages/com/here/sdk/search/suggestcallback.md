---
title: "SuggestCallback (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestsuggestcallback"
hidden: false
---

Package [com.here.sdk.search](sdk-for-android-explore-api-reference-latestpackage-summary)

# Interface SuggestCallback

Functional Interface:
This is a functional interface and can therefore be used as the assignment target for a lambda expression or method reference.

------------------------------------------------------------------------
[@FunctionalInterface](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/FunctionalInterface.html) public interface SuggestCallback
The method will be called on the main thread when a suggest call has been completed. The first argument indicates an error in case of a failure. The second argument contains the results. Both arguments cannot be `null` at the same time - or not `null` at the same time.

## Method Summary

  All Methods
  Instance Methods
  Abstract Methods

  Modifier and Type

  Method

  Description

  `void`

  [onSuggestCompleted](#onSuggestCompleted(com.here.sdk.search.SearchError,java.util.List))`(`[`SearchError`](sdk-for-android-explore-api-reference-latestsearcherror "enum class in com.here.sdk.search")` searchError, `[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`Suggestion`](sdk-for-android-explore-api-reference-latestsuggestion "class in com.here.sdk.search")`> suggestions)`

The method will be called on the main thread when a suggest call has been completed.

## Method Details

### onSuggestCompleted

void onSuggestCompleted(@Nullable [SearchError](sdk-for-android-explore-api-reference-latestsearcherror "enum class in com.here.sdk.search") searchError, @Nullable [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[Suggestion](sdk-for-android-explore-api-reference-latestsuggestion "class in com.here.sdk.search")\> suggestions)

    The method will be called on the main thread when a suggest call has been completed. The first argument indicates an error in case of a failure. The second argument contains the results. Both arguments cannot be `null` at the same time - or not `null` at the same time.
Parameters:
    `searchError` -

    An error enum indicating what went wrong. It is `null` for an operation that succeeds.

    `suggestions` -

    The list of suggestion results. It is `null` in case of an error.
