---
title: "TileUrlProviderCallback (API Reference)"
slug: "sdk-for-android-explore-api-reference-latesttileurlprovidercallback"
hidden: false
---

Package [com.here.sdk.mapview.datasource](sdk-for-android-explore-api-reference-latestpackage-summary)

# Interface TileUrlProviderCallback

Functional Interface:
This is a functional interface and can therefore be used as the assignment target for a lambda expression or method reference.

------------------------------------------------------------------------
[@FunctionalInterface](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/FunctionalInterface.html) public interface TileUrlProviderCallback
Provides the URL as String for the given tile coordinates and storage level.

The first and second parameters correspond to the X and Y coordinates of the tile, respectively, and have values ranging from 0 to 2^level − 1. The third parameter indicates the level of the tile.

## Method Summary

  All Methods
  Instance Methods
  Abstract Methods

  Modifier and Type

  Method

  Description

  [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [onTileUrlRequest](#onTileUrlRequest(int,int,int))`(int x, int y, int level)`

Provides the URL as String for the given tile coordinates and storage level.

## Method Details

### onTileUrlRequest

@NonNull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) onTileUrlRequest(int x, int y, int level)

    Provides the URL as String for the given tile coordinates and storage level.

    The first and second parameters correspond to the X and Y coordinates of the tile, respectively, and have values ranging from 0 to 2^level − 1. The third parameter indicates the level of the tile.
Parameters:
    `x` -

    X coordinate of the tile. This ranges from 0 to 2^level − 1.

    `y` -

    Y coordinate of the tile. This ranges from 0 to 2^level − 1.

    `level` -

    Level of the tile.

    Returns:
    the URL.
