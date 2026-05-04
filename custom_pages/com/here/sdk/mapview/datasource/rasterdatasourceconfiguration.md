---
title: "RasterDataSourceConfiguration (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestrasterdatasourceconfiguration"
hidden: false
---

Package [com.here.sdk.mapview.datasource](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class RasterDataSourceConfiguration

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.mapview.datasource.RasterDataSourceConfiguration
------------------------------------------------------------------------
public final class RasterDataSourceConfiguration extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Called on the main thread after `fromJsonFile()` method finishes loading the configuration.

## Nested Class Summary

Nested Classes

Modifier and Type

  Class

  Description

  `static final class `

  [RasterDataSourceConfiguration.Cache](sdk-for-android-explore-api-reference-latestrasterdatasourceconfiguration-cache)

Configuration of a local data cache.

`static final class `

  [RasterDataSourceConfiguration.Provider](sdk-for-android-explore-api-reference-latestrasterdatasourceconfiguration-provider)

Configuration of a data provider.

## Field Summary

Fields

Modifier and Type

  Field

  Description

  [`RasterDataSourceConfiguration.Cache`](sdk-for-android-explore-api-reference-latestrasterdatasourceconfiguration-cache "class in com.here.sdk.mapview.datasource")

  [cache](#cache)

Local cache configuration.

`boolean`

  [ignoreExpiredData](#ignoreExpiredData)

A flag indicating whether expired data should be ignored until refreshed.

[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [name](#name)

The unique name of the data source.

[`RasterDataSourceConfiguration.Provider`](sdk-for-android-explore-api-reference-latestrasterdatasourceconfiguration-provider "class in com.here.sdk.mapview.datasource")

  [provider](#provider)

Data provider configuration.

## Constructor Summary

Constructors

Constructor

  Description

  [RasterDataSourceConfiguration](#%3Cinit%3E(java.lang.String,com.here.sdk.mapview.datasource.RasterDataSourceConfiguration.Provider,com.here.sdk.mapview.datasource.RasterDataSourceConfiguration.Cache))`(`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` name, `[`RasterDataSourceConfiguration.Provider`](sdk-for-android-explore-api-reference-latestrasterdatasourceconfiguration-provider "class in com.here.sdk.mapview.datasource")` provider, `[`RasterDataSourceConfiguration.Cache`](sdk-for-android-explore-api-reference-latestrasterdatasourceconfiguration-cache "class in com.here.sdk.mapview.datasource")` cache)`

Creates a new instance.

[RasterDataSourceConfiguration](#%3Cinit%3E(java.lang.String,com.here.sdk.mapview.datasource.RasterDataSourceConfiguration.Provider,com.here.sdk.mapview.datasource.RasterDataSourceConfiguration.Cache,boolean))`(`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` name, `[`RasterDataSourceConfiguration.Provider`](sdk-for-android-explore-api-reference-latestrasterdatasourceconfiguration-provider "class in com.here.sdk.mapview.datasource")` provider, `[`RasterDataSourceConfiguration.Cache`](sdk-for-android-explore-api-reference-latestrasterdatasourceconfiguration-cache "class in com.here.sdk.mapview.datasource")` cache, boolean ignoreExpiredData)`

Creates a new instance.

## Method Summary

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Field Details

### name

@NonNull public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name

    The unique name of the data source.

### provider

@NonNull public [RasterDataSourceConfiguration.Provider](sdk-for-android-explore-api-reference-latestrasterdatasourceconfiguration-provider "class in com.here.sdk.mapview.datasource") provider

    Data provider configuration.

### cache

@NonNull public [RasterDataSourceConfiguration.Cache](sdk-for-android-explore-api-reference-latestrasterdatasourceconfiguration-cache "class in com.here.sdk.mapview.datasource") cache

    Local cache configuration.

### ignoreExpiredData

public boolean ignoreExpiredData

    A flag indicating whether expired data should be ignored until refreshed. Default value is `false`.

## Constructor Details

  - (java.lang.String,com.here.sdk.mapview.datasource.RasterDataSourceConfiguration.Provider,com.here.sdk.mapview.datasource.RasterDataSourceConfiguration.Cache)" class="section detail">

### RasterDataSourceConfiguration

public RasterDataSourceConfiguration(@NonNull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name, @NonNull [RasterDataSourceConfiguration.Provider](sdk-for-android-explore-api-reference-latestrasterdatasourceconfiguration-provider "class in com.here.sdk.mapview.datasource") provider, @NonNull [RasterDataSourceConfiguration.Cache](sdk-for-android-explore-api-reference-latestrasterdatasourceconfiguration-cache "class in com.here.sdk.mapview.datasource") cache)

    Creates a new instance.
Parameters:
    `name` -

    The unique name of the data source.

    `provider` -

    Data provider configuration.

    `cache` -

    Local cache configuration.
- (java.lang.String,com.here.sdk.mapview.datasource.RasterDataSourceConfiguration.Provider,com.here.sdk.mapview.datasource.RasterDataSourceConfiguration.Cache,boolean)" class="section detail">

### RasterDataSourceConfiguration

public RasterDataSourceConfiguration(@NonNull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name, @NonNull [RasterDataSourceConfiguration.Provider](sdk-for-android-explore-api-reference-latestrasterdatasourceconfiguration-provider "class in com.here.sdk.mapview.datasource") provider, @NonNull [RasterDataSourceConfiguration.Cache](sdk-for-android-explore-api-reference-latestrasterdatasourceconfiguration-cache "class in com.here.sdk.mapview.datasource") cache, boolean ignoreExpiredData)

    Creates a new instance.
Parameters:
    `name` -

    The unique name of the data source.

    `provider` -

    Data provider configuration.

    `cache` -

    Local cache configuration.

    `ignoreExpiredData` -

    A flag indicating whether expired data should be ignored until refreshed. Default value is `false`.
