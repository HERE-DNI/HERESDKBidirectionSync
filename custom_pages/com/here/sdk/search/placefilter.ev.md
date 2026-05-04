---
title: "PlaceFilter.Ev (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestplacefilter-ev"
hidden: false
---

Package [com.here.sdk.search](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class PlaceFilter.Ev

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.search.PlaceFilter.Ev
Enclosing class:
[PlaceFilter](sdk-for-android-explore-api-reference-latestplacefilter "class in com.here.sdk.search")

------------------------------------------------------------------------
public static final class PlaceFilter.Ev extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Constraints that are applicable on the places of category EV station.

## Field Summary

Fields

Modifier and Type

  Field

  Description

  [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`>`

  [connectorTypeIDs](#connectorTypeIDs)

Filter to retrieve EV charging stations with at least one of the connector type IDs.

[`CurrentType`](sdk-for-android-explore-api-reference-latestcurrenttype "enum class in com.here.sdk.core")

  [currentType](#currentType)

Filter to retrieve EV charging stations with the given current type provided at one of the station EVSE.

[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`>`

  [eMobilityServiceProviderPartnerIDs](#eMobilityServiceProviderPartnerIDs)

Filter to retrieve EV charging stations with at least one matching e-Mobility Service Provider Partner ID.

[Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html)

  [minPowerInKilowatts](#minPowerInKilowatts)

Filter to retrieve EV charging stations with the given minimum charging power in KW delivered by at least one of the station EVSE.

[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`>`

  [supplierNames](#supplierNames)

Sets a constraint on the charge point operator name of the EV station.

## Constructor Summary

Constructors

Constructor

  Description

  [Ev](#%3Cinit%3E())`()`

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

### supplierNames

@NonNull public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)\> supplierNames

    Sets a constraint on the charge point operator name of the EV station.

    Not supported in `OfflineSearchEngine` (only available for the Navigate license).

### connectorTypeIDs

@NonNull public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)\> connectorTypeIDs

    Filter to retrieve EV charging stations with at least one of the connector type IDs. For more information on the current connector types, see https://www.here.com/docs/bundle/ev-charge-points-api-developer-guide/page/topics/resource-type-connector.html

    Not supported in `OfflineSearchEngine` (only available for the Navigate license).

### minPowerInKilowatts

@Nullable public [Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html) minPowerInKilowatts

    Filter to retrieve EV charging stations with the given minimum charging power in KW delivered by at least one of the station EVSE. Not supported for `suggestByText` in `OfflineSearchEngine` (only available for the Navigate license).

### eMobilityServiceProviderPartnerIDs

@NonNull public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)\> eMobilityServiceProviderPartnerIDs

    Filter to retrieve EV charging stations with at least one matching e-Mobility Service Provider Partner ID.

    Not supported in `OfflineSearchEngine` (only available for the Navigate license).

### currentType

@Nullable public [CurrentType](sdk-for-android-explore-api-reference-latestcurrenttype "enum class in com.here.sdk.core") currentType

    Filter to retrieve EV charging stations with the given current type provided at one of the station EVSE. Accepted is either AC or DC. Not supported for `suggestByText` in `OfflineSearchEngine` (only available for the Navigate license).

## Constructor Details

  - ()" class="section detail">

### Ev

public Ev()

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
