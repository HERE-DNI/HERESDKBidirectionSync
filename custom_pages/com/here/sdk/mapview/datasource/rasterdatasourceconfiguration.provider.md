---
title: "RasterDataSourceConfiguration.Provider (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestrasterdatasourceconfiguration-provider"
hidden: false
---

Package [com.here.sdk.mapview.datasource](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class RasterDataSourceConfiguration.Provider

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.mapview.datasource.RasterDataSourceConfiguration.Provider
Enclosing class:
[RasterDataSourceConfiguration](sdk-for-android-explore-api-reference-latestrasterdatasourceconfiguration "class in com.here.sdk.mapview.datasource")

------------------------------------------------------------------------
public static final class RasterDataSourceConfiguration.Provider extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Configuration of a data provider.

## Field Summary

Fields

Modifier and Type

  Field

  Description

  `boolean`

  [hasAlphaChannel](#hasAlphaChannel)

A flag indicating whether the image content contains an alpha channel for transparency.

[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)`<`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html), [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`>`

  [headers](#headers)

The optional name-value pairs specifying HTTP headers that are passed with each tile request.

[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html)`>`

  [storageLevels](#storageLevels)

The storage levels available for this data source.

[`TilingScheme`](sdk-for-android-explore-api-reference-latesttilingscheme "enum class in com.here.sdk.mapview.datasource")

  [tilingScheme](#tilingScheme)

The tiling scheme used by this source.

[`TileUrlProviderCallback`](sdk-for-android-explore-api-reference-latesttileurlprovidercallback "interface in com.here.sdk.mapview.datasource")

  [urlProvider](#urlProvider)

Provides a function that generates URLs based on tile coordinates and storage level.

## Constructor Summary

Constructors

Constructor

  Description

  [Provider](#%3Cinit%3E(com.here.sdk.mapview.datasource.TileUrlProviderCallback,com.here.sdk.mapview.datasource.TilingScheme,java.util.List))`(`[`TileUrlProviderCallback`](sdk-for-android-explore-api-reference-latesttileurlprovidercallback "interface in com.here.sdk.mapview.datasource")` urlProvider, `[`TilingScheme`](sdk-for-android-explore-api-reference-latesttilingscheme "enum class in com.here.sdk.mapview.datasource")` tilingScheme, `[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html)`> storageLevels)`

Creates a new instance.

[Provider](#%3Cinit%3E(com.here.sdk.mapview.datasource.TileUrlProviderCallback,com.here.sdk.mapview.datasource.TilingScheme,java.util.List,boolean,java.util.Map))`(`[`TileUrlProviderCallback`](sdk-for-android-explore-api-reference-latesttileurlprovidercallback "interface in com.here.sdk.mapview.datasource")` urlProvider, `[`TilingScheme`](sdk-for-android-explore-api-reference-latesttilingscheme "enum class in com.here.sdk.mapview.datasource")` tilingScheme, `[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html)`> storageLevels, boolean hasAlphaChannel, `[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)`<`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html), [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`> headers)`

Creates a new instance.

## Method Summary

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Field Details

### urlProvider

@NonNull public [TileUrlProviderCallback](sdk-for-android-explore-api-reference-latesttileurlprovidercallback "interface in com.here.sdk.mapview.datasource") urlProvider

    Provides a function that generates URLs based on tile coordinates and storage level.

### tilingScheme

@NonNull public [TilingScheme](sdk-for-android-explore-api-reference-latesttilingscheme "enum class in com.here.sdk.mapview.datasource") tilingScheme

    The tiling scheme used by this source.

### storageLevels

@NonNull public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html)\> storageLevels

    The storage levels available for this data source. Supported range \[0, 31\]. At least one level must be available for this provider to be used as a source of data. At storage level zero, the whole world is represented by one tile. At storage level 1 the world is split in 2x2 tiles (or in 2x1 tiles, depending on the tiling scheme). The tiling process continues in this fashion until sufficient granularity has been achieved. In the XYZ addresing scheme for tiles, z value of the tile key coresponds to the storage level. Depending on the available storage levels and the given camera zoom level, the appropriate z value of the tile key will be determined.

### hasAlphaChannel

public boolean hasAlphaChannel

    A flag indicating whether the image content contains an alpha channel for transparency. Default value is `false`.

### headers

@Nullable public [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)\<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html),[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)\> headers

    The optional name-value pairs specifying HTTP headers that are passed with each tile request.

## Constructor Details

  - (com.here.sdk.mapview.datasource.TileUrlProviderCallback,com.here.sdk.mapview.datasource.TilingScheme,java.util.List,boolean,java.util.Map)" class="section detail">

### Provider

public Provider(@NonNull [TileUrlProviderCallback](sdk-for-android-explore-api-reference-latesttileurlprovidercallback "interface in com.here.sdk.mapview.datasource") urlProvider, @NonNull [TilingScheme](sdk-for-android-explore-api-reference-latesttilingscheme "enum class in com.here.sdk.mapview.datasource") tilingScheme, @NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html)\> storageLevels, boolean hasAlphaChannel, @Nullable [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)\<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html),[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)\> headers)

    Creates a new instance.
Parameters:
    `urlProvider` -

    Provides a function that generates URLs based on tile coordinates and storage level.

    `tilingScheme` -

    The tiling scheme used by this source.

    `storageLevels` -

    The storage levels available for this data source. Supported range \[0, 31\]. At least one level must be available for this provider to be used as a source of data. At storage level zero, the whole world is represented by one tile. At storage level 1 the world is split in 2x2 tiles (or in 2x1 tiles, depending on the tiling scheme). The tiling process continues in this fashion until sufficient granularity has been achieved. In the XYZ addresing scheme for tiles, z value of the tile key coresponds to the storage level. Depending on the available storage levels and the given camera zoom level, the appropriate z value of the tile key will be determined.

    `hasAlphaChannel` -

    A flag indicating whether the image content contains an alpha channel for transparency. Default value is `false`.

    `headers` -

    The optional name-value pairs specifying HTTP headers that are passed with each tile request.
- (com.here.sdk.mapview.datasource.TileUrlProviderCallback,com.here.sdk.mapview.datasource.TilingScheme,java.util.List)" class="section detail">

### Provider

public Provider(@NonNull [TileUrlProviderCallback](sdk-for-android-explore-api-reference-latesttileurlprovidercallback "interface in com.here.sdk.mapview.datasource") urlProvider, @NonNull [TilingScheme](sdk-for-android-explore-api-reference-latesttilingscheme "enum class in com.here.sdk.mapview.datasource") tilingScheme, @NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html)\> storageLevels)

    Creates a new instance.
Parameters:
    `urlProvider` -

    Provides a function that generates URLs based on tile coordinates and storage level.

    `tilingScheme` -

    The tiling scheme used by this source.

    `storageLevels` -

    The storage levels available for this data source. Supported range \[0, 31\]. At least one level must be available for this provider to be used as a source of data. At storage level zero, the whole world is represented by one tile. At storage level 1 the world is split in 2x2 tiles (or in 2x1 tiles, depending on the tiling scheme). The tiling process continues in this fashion until sufficient granularity has been achieved. In the XYZ addresing scheme for tiles, z value of the tile key coresponds to the storage level. Depending on the available storage levels and the given camera zoom level, the appropriate z value of the tile key will be determined.
