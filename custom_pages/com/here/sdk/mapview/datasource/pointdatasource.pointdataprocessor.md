---
title: "PointDataSource.PointDataProcessor (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestpointdatasource-pointdataprocessor"
hidden: false
---

Package [com.here.sdk.mapview.datasource](sdk-for-android-explore-api-reference-latestpackage-summary)

# Interface PointDataSource.PointDataProcessor

Enclosing class:
[PointDataSource](sdk-for-android-explore-api-reference-latestpointdatasource "class in com.here.sdk.mapview.datasource")

<!-- -->

Functional Interface:
This is a functional interface and can therefore be used as the assignment target for a lambda expression or method reference.

------------------------------------------------------------------------
[@FunctionalInterface](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/FunctionalInterface.html) public static interface PointDataSource.PointDataProcessor
Called for each point, allowing inspection, removal or update of coordinates and attributes.

## Method Summary

  All Methods
  Instance Methods
  Abstract Methods

  Modifier and Type

  Method

  Description

  `boolean`

  [process](#process(com.here.sdk.mapview.datasource.PointDataAccessor))`(`[`PointDataAccessor`](sdk-for-android-explore-api-reference-latestpointdataaccessor "class in com.here.sdk.mapview.datasource")` pointAccessor)`

Called for each point, allowing inspection, removal or update of coordinates and attributes.

## Method Details

### process

boolean process(@NonNull [PointDataAccessor](sdk-for-android-explore-api-reference-latestpointdataaccessor "class in com.here.sdk.mapview.datasource") pointAccessor)

    Called for each point, allowing inspection, removal or update of coordinates and attributes.
Parameters:
    `pointAccessor` -

    the point data accessor.

    Returns:
    value indicating the result of the processing.
