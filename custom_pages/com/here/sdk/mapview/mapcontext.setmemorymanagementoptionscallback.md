---
title: "MapContext.SetMemoryManagementOptionsCallback (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestmapcontext-setmemorymanagementoptionscallback"
hidden: false
---

Package [com.here.sdk.mapview](sdk-for-android-explore-api-reference-latestpackage-summary)

# Interface MapContext.SetMemoryManagementOptionsCallback

Enclosing class:
[MapContext](sdk-for-android-explore-api-reference-latestmapcontext "class in com.here.sdk.mapview")

<!-- -->

Functional Interface:
This is a functional interface and can therefore be used as the assignment target for a lambda expression or method reference.

------------------------------------------------------------------------
[@FunctionalInterface](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/FunctionalInterface.html) public static interface MapContext.SetMemoryManagementOptionsCallback
Callback to handle the memory management result.

Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

## Method Summary

  All Methods
  Instance Methods
  Abstract Methods

  Modifier and Type

  Method

  Description

  `void`

  [onSetMemoryManagementOptions](#onSetMemoryManagementOptions(com.here.sdk.mapview.MapContext.MemoryManagementResult))`(`[`MapContext.MemoryManagementResult`](sdk-for-android-explore-api-reference-latestmapcontext-memorymanagementresult "class in com.here.sdk.mapview")` result)`

Callback to handle the memory management result.

## Method Details

### onSetMemoryManagementOptions

void onSetMemoryManagementOptions(@NonNull [MapContext.MemoryManagementResult](sdk-for-android-explore-api-reference-latestmapcontext-memorymanagementresult "class in com.here.sdk.mapview") result)

    Callback to handle the memory management result.

    Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.
Parameters:
    `result` -

    The memory management result.
