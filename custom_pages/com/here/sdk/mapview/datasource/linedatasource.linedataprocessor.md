---
title: "LineDataSource.LineDataProcessor (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestlinedatasource-linedataprocessor"
hidden: false
---

Package [com.here.sdk.mapview.datasource](sdk-for-android-explore-api-reference-latestpackage-summary)

# Interface LineDataSource.LineDataProcessor

Enclosing class:
[LineDataSource](sdk-for-android-explore-api-reference-latestlinedatasource "class in com.here.sdk.mapview.datasource")

<!-- -->

Functional Interface:
This is a functional interface and can therefore be used as the assignment target for a lambda expression or method reference.

------------------------------------------------------------------------
[@FunctionalInterface](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/FunctionalInterface.html) public static interface LineDataSource.LineDataProcessor
Called for each line, allowing inspection, removal or update of coordinates and attributes.

## Method Summary

  All Methods
  Instance Methods
  Abstract Methods

  Modifier and Type

  Method

  Description

  `boolean`

  [process](#process(com.here.sdk.mapview.datasource.LineDataAccessor))`(`[`LineDataAccessor`](sdk-for-android-explore-api-reference-latestlinedataaccessor "class in com.here.sdk.mapview.datasource")` lineAccessor)`

Called for each line, allowing inspection, removal or update of coordinates and attributes.

## Method Details

### process

boolean process(@NonNull [LineDataAccessor](sdk-for-android-explore-api-reference-latestlinedataaccessor "class in com.here.sdk.mapview.datasource") lineAccessor)

    Called for each line, allowing inspection, removal or update of coordinates and attributes.
Parameters:
    `lineAccessor` -

    the line data accessor.

    Returns:
    value indicating the result of the processing.
