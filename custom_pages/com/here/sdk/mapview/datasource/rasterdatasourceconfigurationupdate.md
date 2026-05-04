---
title: "RasterDataSourceConfigurationUpdate (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestrasterdatasourceconfigurationupdate"
hidden: false
---

Package [com.here.sdk.mapview.datasource](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class RasterDataSourceConfigurationUpdate

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.mapview.datasource.RasterDataSourceConfigurationUpdate
------------------------------------------------------------------------
public final class RasterDataSourceConfigurationUpdate extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Configuration update for a RasterDataSource.

## Field Summary

Fields

Modifier and Type

  Field

  Description

  [Long](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Long.html)

  [cacheDiskSize](#cacheDiskSize)

Optional update of the cache disk size, in bytes.

[Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html)

  [ignoreExpiredData](#ignoreExpiredData)

Optional update of the flag indicating whether expired data should be ignored until refreshed.

[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)`<`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html), [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`>`

  [providerHeaders](#providerHeaders)

Optional update of the provider headers.

## Constructor Summary

Constructors

Constructor

  Description

  [RasterDataSourceConfigurationUpdate](#%3Cinit%3E(java.util.Map,java.lang.Boolean,java.lang.Long))`(`[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)`<`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html), [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`> providerHeaders, `[Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html)` ignoreExpiredData, `[Long](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Long.html)` cacheDiskSize)`

Creates a new instance.

## Method Summary

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Field Details

### providerHeaders

@Nullable public [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)\<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html),[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)\> providerHeaders

    Optional update of the provider headers. The new list replaces the current one. When not set, no change is made to the current list.

### ignoreExpiredData

@Nullable public [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html) ignoreExpiredData

    Optional update of the flag indicating whether expired data should be ignored until refreshed. When not set, no change is made to the current flag state.

### cacheDiskSize

@Nullable public [Long](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Long.html) cacheDiskSize

    Optional update of the cache disk size, in bytes. When not set, no change is made to the current value.

## Constructor Details

  - (java.util.Map,java.lang.Boolean,java.lang.Long)" class="section detail">

### RasterDataSourceConfigurationUpdate

public RasterDataSourceConfigurationUpdate(@Nullable [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)\<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html),[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)\> providerHeaders, @Nullable [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html) ignoreExpiredData, @Nullable [Long](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Long.html) cacheDiskSize)

    Creates a new instance.
Parameters:
    `providerHeaders` -

    Optional update of the provider headers. The new list replaces the current one. When not set, no change is made to the current list.

    `ignoreExpiredData` -

    Optional update of the flag indicating whether expired data should be ignored until refreshed. When not set, no change is made to the current flag state.

    `cacheDiskSize` -

    Optional update of the cache disk size, in bytes. When not set, no change is made to the current value.
