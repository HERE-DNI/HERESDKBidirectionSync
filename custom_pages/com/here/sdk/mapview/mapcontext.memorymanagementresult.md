---
title: "MapContext.MemoryManagementResult (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestmapcontext-memorymanagementresult"
hidden: false
---

Package [com.here.sdk.mapview](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class MapContext.MemoryManagementResult

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.mapview.MapContext.MemoryManagementResult
Enclosing class:
[MapContext](sdk-for-android-explore-api-reference-latestmapcontext "class in com.here.sdk.mapview")

------------------------------------------------------------------------
public static final class MapContext.MemoryManagementResult extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Memory management result.

Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

## Field Summary

Fields

Modifier and Type

  Field

  Description

  [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html)

  [diffBetweenVideoMemoryLimitAndRequirementInKiB](#diffBetweenVideoMemoryLimitAndRequirementInKiB)

The difference in kibibytes between the limit and the video-memory requirement for only the currently visible data.

[`MapContext.MemoryManagementResultCode`](sdk-for-android-explore-api-reference-latestmapcontext-memorymanagementresultcode "enum class in com.here.sdk.mapview")

  [resultCode](#resultCode)

The result code of the memory management request.

## Constructor Summary

Constructors

Constructor

  Description

  [MemoryManagementResult](#%3Cinit%3E(com.here.sdk.mapview.MapContext.MemoryManagementResultCode))`(`[`MapContext.MemoryManagementResultCode`](sdk-for-android-explore-api-reference-latestmapcontext-memorymanagementresultcode "enum class in com.here.sdk.mapview")` resultCode)`

Creates a new instance.

## Method Summary

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Field Details

### diffBetweenVideoMemoryLimitAndRequirementInKiB

@Nullable public [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) diffBetweenVideoMemoryLimitAndRequirementInKiB

    The difference in kibibytes between the limit and the video-memory requirement for only the currently visible data. If positive, the returned value is the surplus value over the currently required bare minimum. Even when positive, if the limit set is low, the application could later breach the limit and delete even visible data. A non positive value means the limit cannot fit the existing visible data and there could be data disappearing or flickering. If for some reason the callback is ignored or correct memory limit cannot be calculated, `null` value is returned.

### resultCode

@NonNull public [MapContext.MemoryManagementResultCode](sdk-for-android-explore-api-reference-latestmapcontext-memorymanagementresultcode "enum class in com.here.sdk.mapview") resultCode

    The result code of the memory management request.

## Constructor Details

  - (com.here.sdk.mapview.MapContext.MemoryManagementResultCode)" class="section detail">

### MemoryManagementResult

public MemoryManagementResult(@NonNull [MapContext.MemoryManagementResultCode](sdk-for-android-explore-api-reference-latestmapcontext-memorymanagementresultcode "enum class in com.here.sdk.mapview") resultCode)

    Creates a new instance.
Parameters:
    `resultCode` -

    The result code of the memory management request.
