---
title: "MapContext.MemoryManagementResultCode (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestmapcontext-memorymanagementresultcode"
hidden: false
---

Package [com.here.sdk.mapview](sdk-for-android-explore-api-reference-latestpackage-summary)

# Enum Class MapContext.MemoryManagementResultCode

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[java.lang.Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)\<[MapContext.MemoryManagementResultCode](sdk-for-android-explore-api-reference-latestmapcontext-memorymanagementresultcode "enum class in com.here.sdk.mapview")\>
com.here.sdk.mapview.MapContext.MemoryManagementResultCode
All Implemented Interfaces:
[Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html), [Comparable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html)`<`[`MapContext.MemoryManagementResultCode`](sdk-for-android-explore-api-reference-latestmapcontext-memorymanagementresultcode "enum class in com.here.sdk.mapview")`>`, [Constable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/constant/Constable.html)

<!-- -->

Enclosing class:
[MapContext](sdk-for-android-explore-api-reference-latestmapcontext "class in com.here.sdk.mapview")

------------------------------------------------------------------------
public static enum MapContext.MemoryManagementResultCode extends [Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)\<[MapContext.MemoryManagementResultCode](sdk-for-android-explore-api-reference-latestmapcontext-memorymanagementresultcode "enum class in com.here.sdk.mapview")\>
The memory management result code.

Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

## Nested Class Summary

## Nested classes/interfaces inherited from class java.lang.[Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)

  [Enum.EnumDesc](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html)`<`[E](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html)` extends `[Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)`<`[E](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html)`>>`

## Enum Constant Summary

Enum Constants

Enum Constant

  Description

  [APPLIED](#APPLIED)

The memory management options were successfully applied.

[FAILED](#FAILED)

The memory management options could not be applied due to other errors.

[FAILED_BOTH_MEMORY_LIMITS_EXCEEDED](#FAILED_BOTH_MEMORY_LIMITS_EXCEEDED)

Both video memory and CPU tile cache limits were exceeded and limits were not applied.

[TILE_CACHE_CPU_MEMORY_LIMIT_EXCEEDED](#TILE_CACHE_CPU_MEMORY_LIMIT_EXCEEDED)

The requested memory limit exceeds the maximum allowed limit for CPU tile cache.

[VIDEO_MEMORY_LIMIT_EXCEEDED](#VIDEO_MEMORY_LIMIT_EXCEEDED)

The requested memory limit exceeds the maximum allowed limit for video memory.

## Method Summary

  All Methods
  Static Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  `static `[`MapContext.MemoryManagementResultCode`](sdk-for-android-explore-api-reference-latestmapcontext-memorymanagementresultcode "enum class in com.here.sdk.mapview")

  [valueOf](#valueOf(java.lang.String))`(`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` name)`

Returns the enum constant of this class with the specified name.

`static `[`MapContext.MemoryManagementResultCode`](sdk-for-android-explore-api-reference-latestmapcontext-memorymanagementresultcode "enum class in com.here.sdk.mapview")`[]`

  [values](#values())`()`

Returns an array containing the constants of this enum class, in the order they are declared.

### Methods inherited from class java.lang.[Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#clone()), [compareTo](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#compareTo(E)), [describeConstable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#describeConstable()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#finalize()), [getDeclaringClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#getDeclaringClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#hashCode()), [name](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#name()), [ordinal](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#ordinal()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#toString()), [valueOf](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#valueOf(java.lang.Class,java.lang.String))

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Enum Constant Details

### APPLIED

public static final [MapContext.MemoryManagementResultCode](sdk-for-android-explore-api-reference-latestmapcontext-memorymanagementresultcode "enum class in com.here.sdk.mapview") APPLIED

    The memory management options were successfully applied.

### TILE_CACHE_CPU_MEMORY_LIMIT_EXCEEDED

public static final [MapContext.MemoryManagementResultCode](sdk-for-android-explore-api-reference-latestmapcontext-memorymanagementresultcode "enum class in com.here.sdk.mapview") TILE_CACHE_CPU_MEMORY_LIMIT_EXCEEDED

    The requested memory limit exceeds the maximum allowed limit for CPU tile cache. Previous value of CPU tile cache limit is preserved. Video memory limit applied correctly.

### VIDEO_MEMORY_LIMIT_EXCEEDED

public static final [MapContext.MemoryManagementResultCode](sdk-for-android-explore-api-reference-latestmapcontext-memorymanagementresultcode "enum class in com.here.sdk.mapview") VIDEO_MEMORY_LIMIT_EXCEEDED

    The requested memory limit exceeds the maximum allowed limit for video memory. Previous value of video memory limit is preserved. CPU tile cache limit applied correctly.

### FAILED_BOTH_MEMORY_LIMITS_EXCEEDED

public static final [MapContext.MemoryManagementResultCode](sdk-for-android-explore-api-reference-latestmapcontext-memorymanagementresultcode "enum class in com.here.sdk.mapview") FAILED_BOTH_MEMORY_LIMITS_EXCEEDED

    Both video memory and CPU tile cache limits were exceeded and limits were not applied. Previous values of video memory and CPU tile cache limits are preserved.

### FAILED

public static final [MapContext.MemoryManagementResultCode](sdk-for-android-explore-api-reference-latestmapcontext-memorymanagementresultcode "enum class in com.here.sdk.mapview") FAILED

    The memory management options could not be applied due to other errors.

## Method Details

### values

public static [MapContext.MemoryManagementResultCode](sdk-for-android-explore-api-reference-latestmapcontext-memorymanagementresultcode "enum class in com.here.sdk.mapview")\[\] values()

    Returns an array containing the constants of this enum class, in the order they are declared.
Returns:
    an array containing the constants of this enum class, in the order they are declared

### valueOf

public static [MapContext.MemoryManagementResultCode](sdk-for-android-explore-api-reference-latestmapcontext-memorymanagementresultcode "enum class in com.here.sdk.mapview") valueOf([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)

    Returns the enum constant of this class with the specified name. The string must match *exactly* an identifier used to declare an enum constant in this class. (Extraneous whitespace characters are not permitted.)
Parameters:
    `name` - the name of the enum constant to be returned.

    Returns:
    the enum constant with the specified name

    Throws:
    [IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html) - if this enum class has no constant with the specified name

    [NullPointerException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/NullPointerException.html) - if the argument is null
