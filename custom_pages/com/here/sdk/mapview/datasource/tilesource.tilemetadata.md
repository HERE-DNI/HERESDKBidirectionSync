---
title: "TileSource.TileMetadata (API Reference)"
slug: "sdk-for-android-explore-api-reference-latesttilesource-tilemetadata"
hidden: false
---

Package [com.here.sdk.mapview.datasource](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class TileSource.TileMetadata

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.mapview.datasource.TileSource.TileMetadata
Enclosing interface:
[TileSource](sdk-for-android-explore-api-reference-latesttilesource "interface in com.here.sdk.mapview.datasource")

------------------------------------------------------------------------
public static final class TileSource.TileMetadata extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Tile metadata.

## Field Summary

Fields

Modifier and Type

  Field

  Description

  [Date](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html)

  [dataExpiryTimestamp](#dataExpiryTimestamp)

Tile data expiry timestamp, relative to Epoch.

[`TileSource.DataVersion`](sdk-for-android-explore-api-reference-latesttilesource-dataversion "class in com.here.sdk.mapview.datasource")

  [dataVersion](#dataVersion)

Tile data version.

## Constructor Summary

Constructors

Constructor

  Description

  [TileMetadata](#%3Cinit%3E(com.here.sdk.mapview.datasource.TileSource.DataVersion,java.util.Date))`(`[`TileSource.DataVersion`](sdk-for-android-explore-api-reference-latesttilesource-dataversion "class in com.here.sdk.mapview.datasource")` dataVersion, `[Date](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html)` dataExpiryTimestamp)`

Creates a new instance.

## Method Summary

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Field Details

### dataVersion

@NonNull public [TileSource.DataVersion](sdk-for-android-explore-api-reference-latesttilesource-dataversion "class in com.here.sdk.mapview.datasource") dataVersion

    Tile data version.

### dataExpiryTimestamp

@NonNull public [Date](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html) dataExpiryTimestamp

    Tile data expiry timestamp, relative to Epoch. Sub-second time-points are not supported.

## Constructor Details

  - (com.here.sdk.mapview.datasource.TileSource.DataVersion,java.util.Date)" class="section detail">

### TileMetadata

public TileMetadata(@NonNull [TileSource.DataVersion](sdk-for-android-explore-api-reference-latesttilesource-dataversion "class in com.here.sdk.mapview.datasource") dataVersion, @NonNull [Date](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html) dataExpiryTimestamp)

    Creates a new instance.
Parameters:
    `dataVersion` -

    Tile data version.

    `dataExpiryTimestamp` -

    Tile data expiry timestamp, relative to Epoch. Sub-second time-points are not supported.
