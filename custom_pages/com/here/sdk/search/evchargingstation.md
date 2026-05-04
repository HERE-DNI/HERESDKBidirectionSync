---
title: "EVChargingStation (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestevchargingstation"
hidden: false
---

Package [com.here.sdk.search](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class EVChargingStation

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.search.EVChargingStation
------------------------------------------------------------------------
public final class EVChargingStation extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Group of connectors for electric vehicles (EVs), defined by a common charging connector type and maximum power level.

Use [`PlaceCategory.BUSINESS_AND_SERVICES_EV_CHARGING_STATION`](sdk-for-android-explore-api-reference-latestplacecategory#BUSINESS_AND_SERVICES_EV_CHARGING_STATION) to find stations. In the `Details` of a `Place` result you can find the list of found pools containing stations, if any.

For offline EV rich attributes, enable [`LayerConfiguration.Feature.EV`](sdk-for-android-explore-api-reference-latestlayerconfiguration-feature#EV) in [`SDKOptions.layerConfiguration`](sdk-for-android-explore-api-reference-latestsdkoptions#layerConfiguration).

## Field Summary

Fields

Modifier and Type

  Field

  Description

  [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html)

  [availableConnectorCount](#availableConnectorCount)

Number of available physical connectors at the charging station.

[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [chargingMode](#chargingMode)

Charging mode of the charging station.

[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html)

  [connectorCount](#connectorCount)

Number of physical connectors at the charging station.

[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [connectorTypeId](#connectorTypeId)

ID of the connector type.

[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [connectorTypeName](#connectorTypeName)

Name of the connector type.

[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [currentRangeInAmperes](#currentRangeInAmperes)

Current range provided by the charging station, in amperes.

[Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html)

  [hasFixedCable](#hasFixedCable)

Indicates that the cable is fixed or not fixed for a specific Connector Type on the charge station.

[Date](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html)

  [lastUpdated](#lastUpdated)

Last update of the `available_connector_count` and `occupied_connector_count` fields.

[Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html)

  [maxPowerInKilowatts](#maxPowerInKilowatts)

Maximum charge power of connectors in kW.

[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html)

  [occupiedConnectorCount](#occupiedConnectorCount)

Number of occupied physical connectors at the charging station.

[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html)

  [outOfServiceConnectorCount](#outOfServiceConnectorCount)

Number of physical connectors that are out of service at the charging station.

[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html)

  [phaseCount](#phaseCount)

Number of phases used by the charging station.

[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [physicalReference](#physicalReference)

Printed on the outside of the EVSE for visual identification.

[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [powerFeedTypeId](#powerFeedTypeId)

ID of the power feed type, as defined by the https://en.wikipedia.org/wiki/SAE_J1772#Charging standard.

[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [powerFeedTypeName](#powerFeedTypeName)

Name of the power feed type, as defined by the https://en.wikipedia.org/wiki/SAE_J1772#Charging standard.

[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html)

  [reservedConnectorCount](#reservedConnectorCount)

Number of physical connectors that are reserved at the charging station.

[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [supplierName](#supplierName)

The EV charging station operator.

[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [voltageRangeInVolts](#voltageRangeInVolts)

Voltage range of the charge provided by the charging station, in volts.

## Constructor Summary

Constructors

Constructor

  Description

  [EVChargingStation](#%3Cinit%3E())`()`

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

### supplierName

@Nullable public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) supplierName

    The EV charging station operator. This field is always `null` for offline search using the `OfflineSearchEngine`. For online search using the `SearchEngine`, it can be null if data is unavailable.

### connectorTypeName

@Nullable public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) connectorTypeName

    Name of the connector type. For more information on the current connector types, see https://www.here.com/docs/bundle/ev-charge-points-api-developer-guide/page/topics/resource-type-connector.html May include customer-facing names. In such cases, a 'customer names' label is present. This field can be `null` if data is unavailable.

### connectorTypeId

@Nullable public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) connectorTypeId

    ID of the connector type. For more information on the current connector types, see https://www.here.com/docs/bundle/ev-charge-points-api-developer-guide/page/topics/resource-type-connector.html This field is always `null` for offline search using the `OfflineSearchEngine`. For online searches using the `SearchEngine`, it may be `null` if the data is unavailable.

### powerFeedTypeName

@Nullable public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) powerFeedTypeName

    Name of the power feed type, as defined by the https://en.wikipedia.org/wiki/SAE_J1772#Charging standard. Provides the customer information on the charge level of the specific Connector Type. Also, can describe level that is used in North America and Australia. In that case label 'North America (Australia)' is present. This field can be `null` if data is unavailable.

### powerFeedTypeId

@Nullable public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) powerFeedTypeId

    ID of the power feed type, as defined by the https://en.wikipedia.org/wiki/SAE_J1772#Charging standard. No data in case of offline search. This field is always `null` for offline search using the `OfflineSearchEngine`. For online searches using the `SearchEngine`, it may be `null` if the data is unavailable.

### maxPowerInKilowatts

@Nullable public [Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html) maxPowerInKilowatts

    Maximum charge power of connectors in kW. This field can be `null` if data is unavailable.

### connectorCount

@Nullable public [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) connectorCount

    Number of physical connectors at the charging station. This field can be `null` if data is unavailable.

### availableConnectorCount

@Nullable public [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) availableConnectorCount

    Number of available physical connectors at the charging station. This field is always `null` for offline search using the `OfflineSearchEngine`. For online searches using the `SearchEngine`, it may be `null` if the data is unavailable.

### occupiedConnectorCount

@Nullable public [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) occupiedConnectorCount

    Number of occupied physical connectors at the charging station. This field is always `null` for offline search using the `OfflineSearchEngine`. For online searches using the `SearchEngine`, it may be `null` if the data is unavailable.

### outOfServiceConnectorCount

@Nullable public [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) outOfServiceConnectorCount

    Number of physical connectors that are out of service at the charging station. This field is always `null` for offline search using the `OfflineSearchEngine`. For online searches using the `SearchEngine`, it may be `null` if the data is unavailable.

### reservedConnectorCount

@Nullable public [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) reservedConnectorCount

    Number of physical connectors that are reserved at the charging station. This field is always `null` for offline search using the `OfflineSearchEngine`. For online searches using the `SearchEngine`, it may be `null` if the data is unavailable.

### lastUpdated

@Nullable public [Date](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html) lastUpdated

    Last update of the `available_connector_count` and `occupied_connector_count` fields. This field is always `null` for offline search using the `OfflineSearchEngine`. For online searches using the `SearchEngine`, it may be `null` if the data is unavailable.

### chargingMode

@Nullable public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) chargingMode

    Charging mode of the charging station. For more information, see https://en.wikipedia.org/w/index.php?title=Charging_station&oldid=1013010605#IEC-61851-1_Charging_Modes standard. This field can be `null` if data is unavailable.

### voltageRangeInVolts

@Nullable public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) voltageRangeInVolts

    Voltage range of the charge provided by the charging station, in volts. Values are alphanumeric represented by the voltage range followed by 'V' and by the current type 'AC' or 'DC', for example: '100-120V AC'. This field can be `null` if data is unavailable.

### currentRangeInAmperes

@Nullable public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) currentRangeInAmperes

    Current range provided by the charging station, in amperes. Values are alphanumeric represented by the Ampere value followed by an 'A', for example '12A-80A'. This field can be `null` if data is unavailable.

### phaseCount

@Nullable public [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) phaseCount

    Number of phases used by the charging station. This field can be `null` if data is unavailable.

### hasFixedCable

@Nullable public [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html) hasFixedCable

    Indicates that the cable is fixed or not fixed for a specific Connector Type on the charge station. This field can be `null` if data is unavailable.

### physicalReference

@Nullable public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) physicalReference

    Printed on the outside of the EVSE for visual identification. Available only in offline search. This field can be `null` if data is unavailable.

## Constructor Details

  - ()" class="section detail">

### EVChargingStation

public EVChargingStation()

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
