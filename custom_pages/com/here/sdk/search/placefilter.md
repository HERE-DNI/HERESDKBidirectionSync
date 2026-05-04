---
title: "PlaceFilter (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestplacefilter"
hidden: false
---

Package [com.here.sdk.search](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class PlaceFilter

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.search.PlaceFilter
------------------------------------------------------------------------
public final class PlaceFilter extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
The filter options to specify a place. Consists of fuel, truck and EV options.

## Nested Class Summary

Nested Classes

Modifier and Type

  Class

  Description

  `static final class `

  [PlaceFilter.Ev](sdk-for-android-explore-api-reference-latestplacefilter-ev)

Constraints that are applicable on the places of category EV station.

## Field Summary

Fields

Modifier and Type

  Field

  Description

  [`PlaceFilter.Ev`](sdk-for-android-explore-api-reference-latestplacefilter-ev "class in com.here.sdk.search")

  [ev](#ev)

Constraints that are applicable on the places of category EV station.

[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`FuelType`](sdk-for-android-explore-api-reference-latestfueltype "enum class in com.here.sdk.transport")`>`

  [fuelTypes](#fuelTypes)

The list of [`FuelType`](sdk-for-android-explore-api-reference-latestfueltype "enum class in com.here.sdk.transport") elements that should be used to find only the [`FuelStation`](sdk-for-android-explore-api-reference-latestfuelstation "class in com.here.sdk.search") search results that support all of them.

[`TruckClass`](sdk-for-android-explore-api-reference-latesttruckclass "enum class in com.here.sdk.transport")

  [truckClass](#truckClass)

Should be used to find only the [`FuelStation`](sdk-for-android-explore-api-reference-latestfuelstation "class in com.here.sdk.search") search results with minimum supported [`TruckClass`](sdk-for-android-explore-api-reference-latesttruckclass "enum class in com.here.sdk.transport").

[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`TruckFuelType`](sdk-for-android-explore-api-reference-latesttruckfueltype "enum class in com.here.sdk.transport")`>`

  [truckFuelTypes](#truckFuelTypes)

The list of [`TruckFuelType`](sdk-for-android-explore-api-reference-latesttruckfueltype "enum class in com.here.sdk.transport") elements that should be used to find only the [`FuelStation`](sdk-for-android-explore-api-reference-latestfuelstation "class in com.here.sdk.search") search results that support all of them.

## Constructor Summary

Constructors

Constructor

  Description

  [PlaceFilter](#%3Cinit%3E())`()`

Creates a new instance.

## Method Summary

  All Methods
  Instance Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  `boolean`

  [equals](#equals(java.lang.Object))`(`[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)` obj)`

  `int`

  [hashCode](#hashCode())`()`

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Field Details

### fuelTypes

@NonNull public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[FuelType](sdk-for-android-explore-api-reference-latestfueltype "enum class in com.here.sdk.transport")\> fuelTypes

    The list of [`FuelType`](sdk-for-android-explore-api-reference-latestfueltype "enum class in com.here.sdk.transport") elements that should be used to find only the [`FuelStation`](sdk-for-android-explore-api-reference-latestfuelstation "class in com.here.sdk.search") search results that support all of them. This filter is available to use with the `SearchEngine` and `OfflineSearchEngine` (only available for the Navigate license), however `OfflineSearchEngine` supports it only for `searchByText` and `searchByCategory` with allowed fuel types `DIESEL`, `LPG`, `BIO_DIESEL`, `CNG`, `DIESEL_WITH_ADDITIVES`, `E10`, `E85`, `ETHANOL`, `ETHANOL_WITH_ADDITIVES`, `GASOLINE`, `HYDROGEN`, `LNG`, `MIDGRADE`, `PREMIUM` and `REGULAR`.

    **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

### truckFuelTypes

@NonNull public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[TruckFuelType](sdk-for-android-explore-api-reference-latesttruckfueltype "enum class in com.here.sdk.transport")\> truckFuelTypes

    The list of [`TruckFuelType`](sdk-for-android-explore-api-reference-latesttruckfueltype "enum class in com.here.sdk.transport") elements that should be used to find only the [`FuelStation`](sdk-for-android-explore-api-reference-latestfuelstation "class in com.here.sdk.search") search results that support all of them. Not supported for `suggestByText` in `OfflineSearchEngine` (only available for the Navigate license).

    **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

### truckClass

@Nullable public [TruckClass](sdk-for-android-explore-api-reference-latesttruckclass "enum class in com.here.sdk.transport") truckClass

    Should be used to find only the [`FuelStation`](sdk-for-android-explore-api-reference-latestfuelstation "class in com.here.sdk.search") search results with minimum supported [`TruckClass`](sdk-for-android-explore-api-reference-latesttruckclass "enum class in com.here.sdk.transport"). This filter is only available to use with the `SearchEngine`. The `OfflineSearchEngine` (only available for the Navigate license) does not apply this filter. [`TruckClass.LIGHT_CLASS`](sdk-for-android-explore-api-reference-latesttruckclass#LIGHT_CLASS) is not accepted in the filter. Otherwise will result in [`SearchError.INVALID_TRUCK_CLASS`](sdk-for-android-explore-api-reference-latestsearcherror#INVALID_TRUCK_CLASS).

    **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

### ev

@NonNull public [PlaceFilter.Ev](sdk-for-android-explore-api-reference-latestplacefilter-ev "class in com.here.sdk.search") ev

    Constraints that are applicable on the places of category EV station.

## Constructor Details

  - ()" class="section detail">

### PlaceFilter

public PlaceFilter()

    Creates a new instance.

## Method Details

### equals

public boolean equals([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) obj)
Overrides:
    [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

### hashCode

public int hashCode()
Overrides:
    [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
