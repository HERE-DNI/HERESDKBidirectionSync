---
title: "MapContext (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestmapcontext"
hidden: false
---

Package [com.here.sdk.mapview](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class MapContext

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.here.NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
com.here.sdk.mapview.MapContext
------------------------------------------------------------------------
public final class MapContext extends [NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
MapContext is the rendering engine and the context in which virtual geographic maps get rendered.

It runs the render loop or offers the means for the user to run a custom one.

Data sources, assets and virtual maps can be attached to the context. A virtual map can only render data from sources attached to the same context.

The graphics backend to be used by the engine can be choosen by the user or a platform suitable one can be automatically selected internally. Only one graphics backend can be active and once selected it cannot be changed.

## Nested Class Summary

Nested Classes

Modifier and Type

  Class

  Description

  `static enum `

  [MapContext.FreeResourceSeverity](sdk-for-android-explore-api-reference-latestmapcontext-freeresourceseverity)

The severity of a free resource request.

`static final class `

  [MapContext.MemoryManagementOptions](sdk-for-android-explore-api-reference-latestmapcontext-memorymanagementoptions)

Memory management options.

`static final class `

  [MapContext.MemoryManagementResult](sdk-for-android-explore-api-reference-latestmapcontext-memorymanagementresult)

Memory management result.

`static enum `

  [MapContext.MemoryManagementResultCode](sdk-for-android-explore-api-reference-latestmapcontext-memorymanagementresultcode)

The memory management result code.

`static enum `

  [MapContext.MemoryManagementStrategy](sdk-for-android-explore-api-reference-latestmapcontext-memorymanagementstrategy)

The memory management strategy.

`static enum `

  [MapContext.ResourceType](sdk-for-android-explore-api-reference-latestmapcontext-resourcetype)

Types of system resources used by [`MapContext`](sdk-for-android-explore-api-reference-latestmapcontext "class in com.here.sdk.mapview") or any of the entities attached to it, like [`HereMap`](sdk-for-android-explore-api-reference-latestheremap "class in com.here.sdk.mapview").

`static interface `

  [MapContext.SetMemoryManagementOptionsCallback](sdk-for-android-explore-api-reference-latestmapcontext-setmemorymanagementoptionscallback)

Callback to handle the memory management result.

## Method Summary

  All Methods
  Instance Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  `void`

  [freeResource](#freeResource(com.here.sdk.mapview.MapContext.ResourceType,com.here.sdk.mapview.MapContext.FreeResourceSeverity))`(`[`MapContext.ResourceType`](sdk-for-android-explore-api-reference-latestmapcontext-resourcetype "enum class in com.here.sdk.mapview")` type, `[`MapContext.FreeResourceSeverity`](sdk-for-android-explore-api-reference-latestmapcontext-freeresourceseverity "enum class in com.here.sdk.mapview")` severity)`

Frees a system resource held by the [`MapContext`](sdk-for-android-explore-api-reference-latestmapcontext "class in com.here.sdk.mapview") and all entities attached to it, like [`HereMap`](sdk-for-android-explore-api-reference-latestheremap "class in com.here.sdk.mapview").

[`MapContext.MemoryManagementOptions`](sdk-for-android-explore-api-reference-latestmapcontext-memorymanagementoptions "class in com.here.sdk.mapview")

  [getMemoryManagementOptions](#getMemoryManagementOptions())`()`

  `void`

  [setMemoryManagementOptions](#setMemoryManagementOptions(com.here.sdk.mapview.MapContext.MemoryManagementOptions,com.here.sdk.mapview.MapContext.SetMemoryManagementOptionsCallback))`(`[`MapContext.MemoryManagementOptions`](sdk-for-android-explore-api-reference-latestmapcontext-memorymanagementoptions "class in com.here.sdk.mapview")` memoryManagementOptions, `[`MapContext.SetMemoryManagementOptionsCallback`](sdk-for-android-explore-api-reference-latestmapcontext-setmemorymanagementoptionscallback "interface in com.here.sdk.mapview")` callback)`

Sets memory management options for controlling tile cache and video memory usage.

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Method Details

### freeResource

public void freeResource(@NonNull [MapContext.ResourceType](sdk-for-android-explore-api-reference-latestmapcontext-resourcetype "enum class in com.here.sdk.mapview") type, @NonNull [MapContext.FreeResourceSeverity](sdk-for-android-explore-api-reference-latestmapcontext-freeresourceseverity "enum class in com.here.sdk.mapview") severity)

    Frees a system resource held by the [`MapContext`](sdk-for-android-explore-api-reference-latestmapcontext "class in com.here.sdk.mapview") and all entities attached to it, like [`HereMap`](sdk-for-android-explore-api-reference-latestheremap "class in com.here.sdk.mapview"). This function is intended for use when a system resource availability becomes low. For example, some memory can be freed when the application transitions to the background state.
Parameters:
    `type` -

    Type of resource to be freed.

    `severity` -

    Severity of the request.

### getMemoryManagementOptions

@NonNull public [MapContext.MemoryManagementOptions](sdk-for-android-explore-api-reference-latestmapcontext-memorymanagementoptions "class in com.here.sdk.mapview") getMemoryManagementOptions()
Returns:
    Gets the current memory management options. Returns the actual applied memory limits. If the underlying system limits exceed int32_t max value (2,147,483,647 KiB or ~2 TiB), the returned value is clamped to int32_t max.

    Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

### setMemoryManagementOptions

public void setMemoryManagementOptions(@NonNull [MapContext.MemoryManagementOptions](sdk-for-android-explore-api-reference-latestmapcontext-memorymanagementoptions "class in com.here.sdk.mapview") memoryManagementOptions, @Nullable [MapContext.SetMemoryManagementOptionsCallback](sdk-for-android-explore-api-reference-latestmapcontext-setmemorymanagementoptionscallback "interface in com.here.sdk.mapview") callback)

    Sets memory management options for controlling tile cache and video memory usage. In [`MapContext.MemoryManagementOptions`](sdk-for-android-explore-api-reference-latestmapcontext-memorymanagementoptions "class in com.here.sdk.mapview") optional parameters with `null` or non positive values will be ignored, preserving their existing settings.

    Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.
Parameters:
    `memoryManagementOptions` -

    The memory management options to set.

    `callback` -

    Optional callback used upon completion to pass the return value to the caller.

    The callback is called on the main thread.
