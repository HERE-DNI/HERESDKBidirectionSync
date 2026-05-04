---
title: "TileSource.DataVersion (API Reference)"
slug: "sdk-for-android-explore-api-reference-latesttilesource-dataversion"
hidden: false
---

Package [com.here.sdk.mapview.datasource](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class TileSource.DataVersion

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.mapview.datasource.TileSource.DataVersion
Enclosing interface:
[TileSource](sdk-for-android-explore-api-reference-latesttilesource "interface in com.here.sdk.mapview.datasource")

------------------------------------------------------------------------
public static final class TileSource.DataVersion extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Tile data version.

## Field Summary

Fields

Modifier and Type

  Field

  Description

  `int`

  [majorVersion](#majorVersion)

Major version number.

`int`

  [minorVersion](#minorVersion)

Minor version number.

## Constructor Summary

Constructors

Constructor

  Description

  [DataVersion](#%3Cinit%3E(int,int))`(int majorVersion, int minorVersion)`

Creates a new instance.

## Method Summary

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Field Details

### majorVersion

public int majorVersion

    Major version number. Describes changes in underlying data that would require a complete reload (e.g. geometry changes).

### minorVersion

public int minorVersion

    Minor version number. Describes changes in underlying data that would not require a complete reload (e.g. attributes changes).

## Constructor Details

  - (int,int)" class="section detail">

### DataVersion

public DataVersion(int majorVersion, int minorVersion)

    Creates a new instance.
Parameters:
    `majorVersion` -

    Major version number. Describes changes in underlying data that would require a complete reload (e.g. geometry changes).

    `minorVersion` -

    Minor version number. Describes changes in underlying data that would not require a complete reload (e.g. attributes changes).
