---
title: "PolygonDataSource.PolygonDataProcessor (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestpolygondatasource-polygondataprocessor"
hidden: false
---

Package [com.here.sdk.mapview.datasource](sdk-for-android-explore-api-reference-latestpackage-summary)

# Interface PolygonDataSource.PolygonDataProcessor

Enclosing class:
[PolygonDataSource](sdk-for-android-explore-api-reference-latestpolygondatasource "class in com.here.sdk.mapview.datasource")

<!-- -->

Functional Interface:
This is a functional interface and can therefore be used as the assignment target for a lambda expression or method reference.

------------------------------------------------------------------------
[@FunctionalInterface](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/FunctionalInterface.html) public static interface PolygonDataSource.PolygonDataProcessor
Called for each polygon, allowing inspection, removal or update of coordinates and attributes.

## Method Summary

  All Methods
  Instance Methods
  Abstract Methods

  Modifier and Type

  Method

  Description

  `boolean`

  [process](#process(com.here.sdk.mapview.datasource.PolygonDataAccessor))`(`[`PolygonDataAccessor`](sdk-for-android-explore-api-reference-latestpolygondataaccessor "class in com.here.sdk.mapview.datasource")` polygonAccessor)`

Called for each polygon, allowing inspection, removal or update of coordinates and attributes.

## Method Details

### process

boolean process(@NonNull [PolygonDataAccessor](sdk-for-android-explore-api-reference-latestpolygondataaccessor "class in com.here.sdk.mapview.datasource") polygonAccessor)

    Called for each polygon, allowing inspection, removal or update of coordinates and attributes.
Parameters:
    `polygonAccessor` -

    the polygon data accessor.

    Returns:
    value indicating the result of the processing.
