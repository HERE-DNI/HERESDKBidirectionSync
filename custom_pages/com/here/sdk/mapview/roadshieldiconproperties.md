---
title: "RoadShieldIconProperties (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestroadshieldiconproperties"
hidden: false
---

Package [com.here.sdk.mapview](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class RoadShieldIconProperties

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.mapview.RoadShieldIconProperties
------------------------------------------------------------------------
public final class RoadShieldIconProperties extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Contains the information required to create a road shield image.

## Field Summary

Fields

Modifier and Type

  Field

  Description

  [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [countryCode](#countryCode)

The country code in ISO-3166-1 alpha-3 format, which will determine the type of road shield.

[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [routeNumberName](#routeNumberName)

A string that is used to additionally determine the road shield's visual representation.

[`RouteType`](sdk-for-android-explore-api-reference-latestroutetype "enum class in com.here.sdk.core")

  [routeType](#routeType)

The type of route indicating the significance of the road in a range from 0 to 6.

[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [shieldText](#shieldText)

The text of the road-shield.

[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [stateCode](#stateCode)

The state code for the road.

## Constructor Summary

Constructors

Constructor

  Description

  [RoadShieldIconProperties](#%3Cinit%3E(com.here.sdk.core.RouteType,java.lang.String,java.lang.String,java.lang.String,java.lang.String))`(`[`RouteType`](sdk-for-android-explore-api-reference-latestroutetype "enum class in com.here.sdk.core")` routeType, `[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` countryCode, `[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` stateCode, `[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` routeNumberName, `[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` shieldText)`

Creates a new instance.

## Method Summary

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Field Details

### routeType

@NonNull public [RouteType](sdk-for-android-explore-api-reference-latestroutetype "enum class in com.here.sdk.core") routeType

    The type of route indicating the significance of the road in a range from 0 to 6. A value of 1 stands for the most major route and 6 the most minor, with 0 being of unknown type.

### countryCode

@NonNull public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) countryCode

    The country code in ISO-3166-1 alpha-3 format, which will determine the type of road shield.

### stateCode

@NonNull public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) stateCode

    The state code for the road. It's a 2-letter code in ISO 3166-2 format. For example the ones listed for US on this page https://en.wikipedia.org/wiki/ISO_3166-2:US. The code "AL" is for Alabama. Another example is the code for autonomous communities listed on https://en.wikipedia.org/wiki/ISO_3166-2:ES. Can be empty if not required for the particular country.

### routeNumberName

@NonNull public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) routeNumberName

    A string that is used to additionally determine the road shield's visual representation. In a routing context, the text can be taken from a `LocalizedRoadNumber`, which is available for each `Span` of a `Route` object. Typically, the string contains the number of a road, such as "E100". Internally, the text is parsed with a RegEx pattern and the results will be used along with other properties such as `routeType`, `countryCode` and `stateCode` to identify the visual representation of a road shield icon.

    Note that the actual text which will be displayed on the road shield icon is set with [`shieldText`](#shieldText). In order to determine the visuals of the icon, `countryCode`, `routeType` and eventually the `stateCode` is in most cases sufficient to determine the type of road shield. In this case an empty string should be passed.

    **Note:** Texts that contain a `CardinalDirection` are currently not supported and may lead to unexpected results. See `LocalizedRoadNumber` for more details, it provides texts with and without a cardinal direction.

### shieldText

@NonNull public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) shieldText

    The text of the road-shield. This is the text which is displayed on the road-shield in reality. It will be in the output road-shield icon.

## Constructor Details

  - (com.here.sdk.core.RouteType,java.lang.String,java.lang.String,java.lang.String,java.lang.String)" class="section detail">

### RoadShieldIconProperties

public RoadShieldIconProperties(@NonNull [RouteType](sdk-for-android-explore-api-reference-latestroutetype "enum class in com.here.sdk.core") routeType, @NonNull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) countryCode, @NonNull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) stateCode, @NonNull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) routeNumberName, @NonNull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) shieldText)

    Creates a new instance.
Parameters:
    `routeType` -

    The type of route indicating the significance of the road in a range from 0 to 6. A value of 1 stands for the most major route and 6 the most minor, with 0 being of unknown type.

    `countryCode` -

    The country code in ISO-3166-1 alpha-3 format, which will determine the type of road shield.

    `stateCode` -

    The state code for the road. It's a 2-letter code in ISO 3166-2 format. For example the ones listed for US on this page https://en.wikipedia.org/wiki/ISO_3166-2:US. The code "AL" is for Alabama. Another example is the code for autonomous communities listed on https://en.wikipedia.org/wiki/ISO_3166-2:ES. Can be empty if not required for the particular country.

    `routeNumberName` -

    A string that is used to additionally determine the road shield's visual representation. In a routing context, the text can be taken from a `LocalizedRoadNumber`, which is available for each `Span` of a `Route` object. Typically, the string contains the number of a road, such as "E100". Internally, the text is parsed with a RegEx pattern and the results will be used along with other properties such as `routeType`, `countryCode` and `stateCode` to identify the visual representation of a road shield icon.

    Note that the actual text which will be displayed on the road shield icon is set with [`shieldText`](#shieldText). In order to determine the visuals of the icon, `countryCode`, `routeType` and eventually the `stateCode` is in most cases sufficient to determine the type of road shield. In this case an empty string should be passed.

    **Note:** Texts that contain a `CardinalDirection` are currently not supported and may lead to unexpected results. See `LocalizedRoadNumber` for more details, it provides texts with and without a cardinal direction.

    `shieldText` -

    The text of the road-shield. This is the text which is displayed on the road-shield in reality. It will be in the output road-shield icon.
