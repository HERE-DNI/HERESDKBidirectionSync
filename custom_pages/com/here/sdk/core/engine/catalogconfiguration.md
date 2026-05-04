---
title: "CatalogConfiguration (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestcatalogconfiguration"
hidden: false
---

Package [com.here.sdk.core.engine](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class CatalogConfiguration

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.core.engine.CatalogConfiguration
------------------------------------------------------------------------
public final class CatalogConfiguration extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Using this class you can configure in the [`SDKOptions`](sdk-for-android-explore-api-reference-latestsdkoptions "class in com.here.sdk.core.engine"), how the [`SDKNativeEngine`](sdk-for-android-explore-api-reference-latestsdknativeengine "class in com.here.sdk.core.engine") should access, use and store the data for the desired catalog.

Using this class, you can access default catalogs on the HERE platform and also custom catalogs such as for self-hosted or BYOD (bring your own data) use cases.

For information on how the user can identify a catalog on the HERE platform, see [`DesiredCatalog`](sdk-for-android-explore-api-reference-latestdesiredcatalog "class in com.here.sdk.core.engine") For further information about catalogs and related concepts see [`CatalogIdentifier`](sdk-for-android-explore-api-reference-latestcatalogidentifier "class in com.here.sdk.core.engine").

**Note:** This API is only applicable for the Navigate license.

## Field Summary

Fields

Modifier and Type

  Field

  Description

  `boolean`

  [allowDownload](#allowDownload)

A flag to indicate if the data for this catalog is allowed to be stored in persistent storage for use with offline maps.

[`Duration`](sdk-for-android-explore-api-reference-latestduration "class in com.here.time")

  [cacheExpirationPeriod](#cacheExpirationPeriod)

Expiration time in seconds for how long the catalog data is retained in the map cache before it is removed.

[`DesiredCatalog`](sdk-for-android-explore-api-reference-latestdesiredcatalog "class in com.here.sdk.core.engine")

  [catalog](#catalog)

The identifier for the desired catalog to be accessed on the HERE platform.

[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [patchHrn](#patchHrn)

Some catalogs may have additional modifications to their data contained in an entirely separate catalog, called the patch catalog.

## Constructor Summary

Constructors

Constructor

  Description

  [CatalogConfiguration](#%3Cinit%3E(com.here.sdk.core.engine.DesiredCatalog))`(`[`DesiredCatalog`](sdk-for-android-explore-api-reference-latestdesiredcatalog "class in com.here.sdk.core.engine")` catalog)`

Creates a new instance.

## Method Summary

  All Methods
  Static Methods
  Instance Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  `boolean`

  [equals](#equals(java.lang.Object))`(`[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)` obj)`

  `static `[`CatalogConfiguration`](sdk-for-android-explore-api-reference-latestcatalogconfiguration "class in com.here.sdk.core.engine")

  [getDefault](#getDefault(com.here.sdk.core.engine.CatalogType))`(`[`CatalogType`](sdk-for-android-explore-api-reference-latestcatalogtype "enum class in com.here.sdk.core.engine")` catalogType)`

Gets the default catalog configuration for the specified catalog type.

`int`

  [hashCode](#hashCode())`()`

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Field Details

### catalog

@NonNull public [DesiredCatalog](sdk-for-android-explore-api-reference-latestdesiredcatalog "class in com.here.sdk.core.engine") catalog

    The identifier for the desired catalog to be accessed on the HERE platform. See [`DesiredCatalog`](sdk-for-android-explore-api-reference-latestdesiredcatalog "class in com.here.sdk.core.engine").

### patchHrn

@Nullable public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) patchHrn

    Some catalogs may have additional modifications to their data contained in an entirely separate catalog, called the patch catalog. This field indicates the HERE Resource Name (HRN) for the patch catalog. When this field is present, the catalog's data as referenced by [`catalog`](#catalog) is merged with data from the patch catalog. If this field is `null`, then incremental updates are disabled.

### cacheExpirationPeriod

@Nullable public [Duration](sdk-for-android-explore-api-reference-latestduration "class in com.here.time") cacheExpirationPeriod

    Expiration time in seconds for how long the catalog data is retained in the map cache before it is removed. Cache path is specified by [`SDKOptions.cachePath`](sdk-for-android-explore-api-reference-latestsdkoptions#cachePath). If not set, the cache will be deleted on a Least Recently Used (LRU) basis.

### allowDownload

public boolean allowDownload

    A flag to indicate if the data for this catalog is allowed to be stored in persistent storage for use with offline maps. The storage path is specified in [`SDKOptions.persistentMapStoragePath`](sdk-for-android-explore-api-reference-latestsdkoptions#persistentMapStoragePath). If set to false, the data is not stored in persistent storage and is only retained in the cache for a limited time (see [`cacheExpirationPeriod`](#cacheExpirationPeriod)). Defaults to `true`.

## Constructor Details

  - (com.here.sdk.core.engine.DesiredCatalog)" class="section detail">

### CatalogConfiguration

public CatalogConfiguration(@NonNull [DesiredCatalog](sdk-for-android-explore-api-reference-latestdesiredcatalog "class in com.here.sdk.core.engine") catalog)

    Creates a new instance.
Parameters:
    `catalog` -

    The identifier for the desired catalog to be accessed on the HERE platform. See [`DesiredCatalog`](sdk-for-android-explore-api-reference-latestdesiredcatalog "class in com.here.sdk.core.engine").

## Method Details

### equals

public boolean equals([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) obj)
Overrides:
    [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

### hashCode

public int hashCode()
Overrides:
    [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

### getDefault

@NonNull public static [CatalogConfiguration](sdk-for-android-explore-api-reference-latestcatalogconfiguration "class in com.here.sdk.core.engine") getDefault(@NonNull [CatalogType](sdk-for-android-explore-api-reference-latestcatalogtype "enum class in com.here.sdk.core.engine") catalogType)

    Gets the default catalog configuration for the specified catalog type. It uses the catalog version that was the latest at the time when the HERE SDK was built.
Parameters:
    `catalogType` -

    Catalog type

    Returns:
    Instance of [`CatalogConfiguration`](sdk-for-android-explore-api-reference-latestcatalogconfiguration "class in com.here.sdk.core.engine").
