---
title: "EVChargingPool (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestevchargingpool"
hidden: false
---

Package [com.here.sdk.search](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class EVChargingPool

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.search.EVChargingPool
------------------------------------------------------------------------
public final class EVChargingPool extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
A charging pool for electric vehicles is an area equipped with one or more charging stations.

Use [`PlaceCategory.BUSINESS_AND_SERVICES_EV_CHARGING_STATION`](sdk-for-android-explore-api-reference-latestplacecategory#BUSINESS_AND_SERVICES_EV_CHARGING_STATION) to find stations. In the `Details` of a `Place` result you can find the list of found pools containing stations, if any.

For offline EV rich attributes, also enable [`LayerConfiguration.Feature.EV`](sdk-for-android-explore-api-reference-latestlayerconfiguration-feature#EV) in [`SDKOptions.layerConfiguration`](sdk-for-android-explore-api-reference-latestsdkoptions#layerConfiguration).

## Field Summary

Fields

Modifier and Type

  Field

  Description

  [`EVAccessType`](sdk-for-android-explore-api-reference-latestevaccesstype "enum class in com.here.sdk.search")

  [access](#access)

The accessibility level of the charging pool, or `null` if unknown.

[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`EVAccessRestrictionReason`](sdk-for-android-explore-api-reference-latestevaccessrestrictionreason "enum class in com.here.sdk.search")`>`

  [accessRestrictionReasons](#accessRestrictionReasons)

Contains the list of reasons for restriction.

[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`EVChargingStation`](sdk-for-android-explore-api-reference-latestevchargingstation "class in com.here.sdk.search")`>`

  [chargingStations](#chargingStations)

List of charging stations.

[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [cpoId](#cpoId)

CPO (Charge Point Operator) id for charging pool.

[`EVChargingPoolDetails`](sdk-for-android-explore-api-reference-latestevchargingpooldetails "class in com.here.sdk.search")

  [details](#details)

EV charging station attributes details.

[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`EMobilityServiceProvider`](sdk-for-android-explore-api-reference-latestemobilityserviceprovider "class in com.here.sdk.search")`>`

  [eMobilityServiceProviders](#eMobilityServiceProviders)

List of e-Mobility Service Providers.

[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`Evse`](sdk-for-android-explore-api-reference-latestevse "class in com.here.sdk.search")`>`

  [evseInfo](#evseInfo)

Charge Point Operator (CPO) ID uses the Electric Vehicle Supply Equipment ID (EVSE ID) for an exact identification of the charging infrastructure and charging point.

[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [id](#id)

HERE ID of the charging pool.

## Constructor Summary

Constructors

Constructor

  Description

  [EVChargingPool](#%3Cinit%3E(java.util.List,java.util.List,java.util.List))`(`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`EVChargingStation`](sdk-for-android-explore-api-reference-latestevchargingstation "class in com.here.sdk.search")`> chargingStations, `[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`EMobilityServiceProvider`](sdk-for-android-explore-api-reference-latestemobilityserviceprovider "class in com.here.sdk.search")`> eMobilityServiceProviders, `[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`EVAccessRestrictionReason`](sdk-for-android-explore-api-reference-latestevaccessrestrictionreason "enum class in com.here.sdk.search")`> accessRestrictionReasons)`

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

### chargingStations

@NonNull public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[EVChargingStation](sdk-for-android-explore-api-reference-latestevchargingstation "class in com.here.sdk.search")\> chargingStations

    List of charging stations.

### eMobilityServiceProviders

@NonNull public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[EMobilityServiceProvider](sdk-for-android-explore-api-reference-latestemobilityserviceprovider "class in com.here.sdk.search")\> eMobilityServiceProviders

    List of e-Mobility Service Providers. Only online search fills this field.

### access

@Nullable public [EVAccessType](sdk-for-android-explore-api-reference-latestevaccesstype "enum class in com.here.sdk.search") access

    The accessibility level of the charging pool, or `null` if unknown.

### accessRestrictionReasons

@NonNull public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[EVAccessRestrictionReason](sdk-for-android-explore-api-reference-latestevaccessrestrictionreason "enum class in com.here.sdk.search")\> accessRestrictionReasons

    Contains the list of reasons for restriction. Populated only for offline search and when access is [`EVAccessType.RESTRICTED_ACCESS`](sdk-for-android-explore-api-reference-latestevaccesstype#RESTRICTED_ACCESS).

### details

@Nullable public [EVChargingPoolDetails](sdk-for-android-explore-api-reference-latestevchargingpooldetails "class in com.here.sdk.search") details

    EV charging station attributes details. It is available only for a place that has charging station for electric vehicles. Only offline search fills this field.

    **Note:** Not available as part of [`Suggestion`](sdk-for-android-explore-api-reference-latestsuggestion "class in com.here.sdk.search") results.

### id

@Nullable public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id

    HERE ID of the charging pool. Only online search fills this field.

### cpoId

@Nullable public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) cpoId

    CPO (Charge Point Operator) id for charging pool. Only online search fills this field.

### evseInfo

@NonNull public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[Evse](sdk-for-android-explore-api-reference-latestevse "class in com.here.sdk.search")\> evseInfo

    Charge Point Operator (CPO) ID uses the Electric Vehicle Supply Equipment ID (EVSE ID) for an exact identification of the charging infrastructure and charging point. Only online search fills this field.

## Constructor Details

  - (java.util.List,java.util.List,java.util.List)" class="section detail">

### EVChargingPool

public EVChargingPool(@NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[EVChargingStation](sdk-for-android-explore-api-reference-latestevchargingstation "class in com.here.sdk.search")\> chargingStations, @NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[EMobilityServiceProvider](sdk-for-android-explore-api-reference-latestemobilityserviceprovider "class in com.here.sdk.search")\> eMobilityServiceProviders, @NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[EVAccessRestrictionReason](sdk-for-android-explore-api-reference-latestevaccessrestrictionreason "enum class in com.here.sdk.search")\> accessRestrictionReasons)

    Creates a new instance.
Parameters:
    `chargingStations` -

    List of charging stations.

    `eMobilityServiceProviders` -

    List of e-Mobility Service Providers. Only online search fills this field.

    `accessRestrictionReasons` -

    Contains the list of reasons for restriction. Populated only for offline search and when access is [`EVAccessType.RESTRICTED_ACCESS`](sdk-for-android-explore-api-reference-latestevaccesstype#RESTRICTED_ACCESS).

## Method Details

### equals

public boolean equals([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) obj)
Overrides:
    [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

### hashCode

public int hashCode()
Overrides:
    [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
