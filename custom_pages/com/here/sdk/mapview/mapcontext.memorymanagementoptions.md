---
title: "MapContext.MemoryManagementOptions (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestmapcontext-memorymanagementoptions"
hidden: false
---

Package [com.here.sdk.mapview](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class MapContext.MemoryManagementOptions

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.mapview.MapContext.MemoryManagementOptions
Enclosing class:
[MapContext](sdk-for-android-explore-api-reference-latestmapcontext "class in com.here.sdk.mapview")

------------------------------------------------------------------------
public static final class MapContext.MemoryManagementOptions extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Memory management options.

Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

## Field Summary

Fields

Modifier and Type

  Field

  Description

  [`MapContext.MemoryManagementStrategy`](sdk-for-android-explore-api-reference-latestmapcontext-memorymanagementstrategy "enum class in com.here.sdk.mapview")

  [memoryManagementStrategy](#memoryManagementStrategy)

The default setting MemoryManagementStrategy.DYNAMIC is suitable for common cases.

[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html)

  [tileCacheMemoryLimitInKiB](#tileCacheMemoryLimitInKiB)

Tile cache memory limit in kibibytes.

[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html)

  [videoMemoryLimitInKiB](#videoMemoryLimitInKiB)

Target video memory limit in kibibytes.

## Constructor Summary

Constructors

Constructor

  Description

  [MemoryManagementOptions](#%3Cinit%3E())`()`

Creates a new instance.

## Method Summary

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Field Details

### memoryManagementStrategy

@NonNull public [MapContext.MemoryManagementStrategy](sdk-for-android-explore-api-reference-latestmapcontext-memorymanagementstrategy "enum class in com.here.sdk.mapview") memoryManagementStrategy

    The default setting MemoryManagementStrategy.DYNAMIC is suitable for common cases. The map data cache can adjust dynamically to fit visible data. When the visible data needs extra memory, it would increase. When it's not needed, it will reduce to a limit which is calculated internally or by using [`tileCacheMemoryLimitInKiB`](#tileCacheMemoryLimitInKiB) option. The MemoryManagementStrategy.FIXED would be only useful when there is very strict memory consumption requirement for the application. It potentially can have flickering visual artifacts when the map data to be visualized is very large and exceeds the cache limit.

### tileCacheMemoryLimitInKiB

@Nullable public [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) tileCacheMemoryLimitInKiB

    Tile cache memory limit in kibibytes. Non positive or `null` values are ignored. Default value is `null`. Low tile cache limit will lead to eviction of tiles only if MemoryManagementStrategy is set to FIXED.

### videoMemoryLimitInKiB

@Nullable public [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) videoMemoryLimitInKiB

    Target video memory limit in kibibytes. Non positive or `null` values are ignored. Default value is `null`.

## Constructor Details

  - ()" class="section detail">

### MemoryManagementOptions

public MemoryManagementOptions()

    Creates a new instance.
