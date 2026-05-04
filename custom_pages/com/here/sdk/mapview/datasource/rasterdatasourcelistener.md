---
title: "RasterDataSourceListener (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestrasterdatasourcelistener"
hidden: false
---

Package [com.here.sdk.mapview.datasource](sdk-for-android-explore-api-reference-latestpackage-summary)

# Interface RasterDataSourceListener

------------------------------------------------------------------------
public interface RasterDataSourceListener
Listener for RasterDataSource events.

## Method Summary

  All Methods
  Instance Methods
  Abstract Methods

  Modifier and Type

  Method

  Description

  `void`

  [onRasterDataSourceError](#onRasterDataSourceError(com.here.sdk.mapview.datasource.RasterDataSourceError))`(`[`RasterDataSourceError`](sdk-for-android-explore-api-reference-latestrasterdatasourceerror "enum class in com.here.sdk.mapview.datasource")` dataSourceError)`

The method to call on the listener when a data source error occurs.

`void`

  [onRasterDataSourceReady](#onRasterDataSourceReady())`()`

The method to call on the listener when data source is ready to use.

## Method Details

### onRasterDataSourceReady

void onRasterDataSourceReady()

    The method to call on the listener when data source is ready to use.

### onRasterDataSourceError

void onRasterDataSourceError(@NonNull [RasterDataSourceError](sdk-for-android-explore-api-reference-latestrasterdatasourceerror "enum class in com.here.sdk.mapview.datasource") dataSourceError)

    The method to call on the listener when a data source error occurs.
Parameters:
    `dataSourceError` -

    a data source error.
