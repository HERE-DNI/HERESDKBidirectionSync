---
title: "CatalogVersionHint (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestcatalogversionhint"
hidden: false
---

Package [com.here.sdk.core.engine](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class CatalogVersionHint

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.here.NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
com.here.sdk.core.engine.CatalogVersionHint
------------------------------------------------------------------------
public final class CatalogVersionHint extends [NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
This is a class for capturing user's intent for the desired catalog version to use in [`DesiredCatalog`](sdk-for-android-explore-api-reference-latestdesiredcatalog "class in com.here.sdk.core.engine") class.

You can request a specific or latest version of a catalog by calling the static functions [`specific(long)`](#specific(long)) and [`latest(boolean)`](#latest(boolean)) respectively. The HERE platform will make the best effort to provide an appropriate version for the catalog based on this version hint. Please take note that for the API [`specific(long)`](#specific(long)) to function properly, it is essential that the mutable and persistent storage should be cleaned.

## Method Summary

  All Methods
  Static Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  `static `[`CatalogVersionHint`](sdk-for-android-explore-api-reference-latestcatalogversionhint "class in com.here.sdk.core.engine")

  [latest](#latest(boolean))`(boolean ignoreCachedData)`

This static method can be called when you are interested in getting the most latest version of a catalog when initializing the HERE SDK with `SDKOptions` where you can specify the catalog(s) you want to use.

`static `[`CatalogVersionHint`](sdk-for-android-explore-api-reference-latestcatalogversionhint "class in com.here.sdk.core.engine")

  [specific](#specific(long))`(long version)`

This static method is used when you are interested in a specific version of a catalog, that you want to specify manually.

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Method Details

### specific

@NonNull public static [CatalogVersionHint](sdk-for-android-explore-api-reference-latestcatalogversionhint "class in com.here.sdk.core.engine") specific(long version)

    This static method is used when you are interested in a specific version of a catalog, that you want to specify manually. To ensure proper functioning of this API, it is essential to clean the mutable and persistent storage.
Parameters:
    `version` -

    An integer value indicating the version of catalog desired. If the desired version does not exist, the HERE platform will make the best effort to provide an appropriate version or result in error logs about invalid version.

    Returns:
    Instance of [`CatalogVersionHint`](sdk-for-android-explore-api-reference-latestcatalogversionhint "class in com.here.sdk.core.engine") with specified version.

### latest

@NonNull public static [CatalogVersionHint](sdk-for-android-explore-api-reference-latestcatalogversionhint "class in com.here.sdk.core.engine") latest(boolean ignoreCachedData)

    This static method can be called when you are interested in getting the most latest version of a catalog when initializing the HERE SDK with `SDKOptions` where you can specify the catalog(s) you want to use. In effect, this will auto-update the cached map data on each start, if possible. Use this only when you have no installed `Regions`. Since this affects only the map data cache, calling this at initialization time has no or only a very limited effect on the start-up time.

    In order to auto-update cached OCM-based map data, such as for the HERE SDK (Navigate), use the default HRN value: "hrn:here:data::olp-here:ocm" in your `DesiredCatalog`. Note that the HERE SDK (Explore) cannot be used with such settings and the initialization of the HERE SDK may fail - since it is based on a different map format.
Parameters:
    `ignoreCachedData` -

    A flag to specify handling of any cached data present on a device when trying to update the map version. If set to true, the HERE SDK will auto-update to the latest catalog version when no installed `Regions` are present. If present, this call will have no effect - use `updateCatalog()` via `MapUpdater` instead to update all map data to the latest version. Note that cached data present on a device - for example, data in the map cache or data cached by `PrefetchAroundLocationWithRadius` or `PrefetchAroundRouteOnIntervals` - will be become obsolete if a newer map version is available. Such data will be evicted using a LRU strategy over time. If set to false, the HERE SDK will auto-update to use the latest version, only when there is no cached map data at all (for example, at first install or after clearing the cache) *and* no installed map data. Otherwise, this call will have no effect.

    Returns:
    Instance of [`CatalogVersionHint`](sdk-for-android-explore-api-reference-latestcatalogversionhint "class in com.here.sdk.core.engine").
