---
title: "RasterDataSourceConfiguration.Cache (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestrasterdatasourceconfiguration-cache"
hidden: false
---

Package [com.here.sdk.mapview.datasource](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class RasterDataSourceConfiguration.Cache

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.mapview.datasource.RasterDataSourceConfiguration.Cache
Enclosing class:
[RasterDataSourceConfiguration](sdk-for-android-explore-api-reference-latestrasterdatasourceconfiguration "class in com.here.sdk.mapview.datasource")

------------------------------------------------------------------------
public static final class RasterDataSourceConfiguration.Cache extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Configuration of a local data cache.

## Field Summary

Fields

Modifier and Type

  Field

  Description

  `long`

  [diskSize](#diskSize)

The maximum size to use on disk for the cache, in bytes.

[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [path](#path)

The path to the directory to use for the cache.

## Constructor Summary

Constructors

Constructor

  Description

  [Cache](#%3Cinit%3E(java.lang.String))`(`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` path)`

Constructs a Cache object from the provided path and a default cache size of 32 MiB.

[Cache](#%3Cinit%3E(java.lang.String,long))`(`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` path, long diskSize)`

Constructs a Cache object from the provided path and cache size.

## Method Summary

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Field Details

### path

@NonNull public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) path

    The path to the directory to use for the cache. By default, the map gets initialized with a data path which can be fetched from `SDKOptions.cachePath`. The cache will be relative to this path, unless an absolute path is provided. The cache can be stored in an internal/external storage as long as the app has read/write permissions. Empty string means the data path will be used for caching. If the provided path, either as absolute path or as relative path is invalid, then caching will be disabled. There is no contraint regarding the existence of the path. If the path does not exist but is valid, it will be created.

### diskSize

public long diskSize

    The maximum size to use on disk for the cache, in bytes. Default is 32 MiB. This cache is independent from the map cache as defined via `SDKOptions`. Its size is only limited by the total device storage capacity.

## Constructor Details

  - (java.lang.String)" class="section detail">

### Cache

public Cache(@NonNull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) path)

    Constructs a Cache object from the provided path and a default cache size of 32 MiB.
Parameters:
    `path` -

    The path to the directory to use for the cache. By default, the map gets initialized with a data path which can be fetched from `SDKOptions.cachePath`. The cache will be relative to this path, unless an absolute path is provided. The cache can be stored in an internal/external storage as long as the app has read/write permissions. Empty string means the data path will be used for caching. If the provided path, either as absolute path or as relative path is invalid, then caching will be disabled. There is no contraint regarding the existence of the path. If the path does not exist but is valid, it will be created.
- (java.lang.String,long)" class="section detail">

### Cache

public Cache(@NonNull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) path, long diskSize)

    Constructs a Cache object from the provided path and cache size.
Parameters:
    `path` -

    The path to the directory to use for the cache. By default, the map gets initialized with a data path which can be fetched from `SDKOptions.cachePath`. The cache will be relative to this path, unless an absolute path is provided. The cache can be stored in an internal/external storage as long as the app has read/write permissions. Empty string means the data path will be used for caching. If the provided path, either as absolute path or as relative path is invalid, then caching will be disabled. There is no contraint regarding the existence of the path. If the path does not exist but is valid, it will be created.

    `diskSize` -

    The maximum size to use on disk for the cache, in bytes. Default is 32 MiB. This cache is independent from the map cache as defined via `SDKOptions`. Its size is only limited by the total device storage capacity.
