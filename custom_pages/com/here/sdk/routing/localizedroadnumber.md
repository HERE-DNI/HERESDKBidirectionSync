---
title: "LocalizedRoadNumber (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestlocalizedroadnumber"
hidden: false
---

Package [com.here.sdk.routing](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class LocalizedRoadNumber

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.routing.LocalizedRoadNumber
------------------------------------------------------------------------
public final class LocalizedRoadNumber extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Used to represent road number localized to specific language with optional direction and route type information.

## Field Summary

Fields

Modifier and Type

  Field

  Description

  [`CardinalDirection`](sdk-for-android-explore-api-reference-latestcardinaldirection "enum class in com.here.sdk.core")

  [direction](#direction)

Road direction.

[`LocalizedText`](sdk-for-android-explore-api-reference-latestlocalizedtext "class in com.here.sdk.core")

  [localizedNumber](#localizedNumber)

Road number with locale information.

[`RouteType`](sdk-for-android-explore-api-reference-latestroutetype "enum class in com.here.sdk.core")

  [routeType](#routeType)

The route type of the LocalizedRoadNumber.

## Constructor Summary

Constructors

Constructor

  Description

  [LocalizedRoadNumber](#%3Cinit%3E(com.here.sdk.core.LocalizedText,com.here.sdk.core.RouteType))`(`[`LocalizedText`](sdk-for-android-explore-api-reference-latestlocalizedtext "class in com.here.sdk.core")` localizedNumber, `[`RouteType`](sdk-for-android-explore-api-reference-latestroutetype "enum class in com.here.sdk.core")` routeType)`

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

  [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [getTextWithDirection](#getTextWithDirection())`()`

Returns the whole road number information including its cardinal direction.

`int`

  [hashCode](#hashCode())`()`

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Field Details

### localizedNumber

@NonNull public [LocalizedText](sdk-for-android-explore-api-reference-latestlocalizedtext "class in com.here.sdk.core") localizedNumber

    Road number with locale information.

### direction

@Nullable public [CardinalDirection](sdk-for-android-explore-api-reference-latestcardinaldirection "enum class in com.here.sdk.core") direction

    Road direction. This property indicates the official directional identifier assigned to highways. Can be `null` when direction is not assigned to highways. The direction indicates the same information as on the signpost shield: For example, if is "101 West", the directions contains WEST. Note that the official direction is not necessarily the travel direction. For example, US-101 through the city of Sunnyvale is physically located East to West. However, the official direction on sign is North/South.

### routeType

@NonNull public [RouteType](sdk-for-android-explore-api-reference-latestroutetype "enum class in com.here.sdk.core") routeType

    The route type of the LocalizedRoadNumber.

## Constructor Details

  - (com.here.sdk.core.LocalizedText,com.here.sdk.core.RouteType)" class="section detail">

### LocalizedRoadNumber

public LocalizedRoadNumber(@NonNull [LocalizedText](sdk-for-android-explore-api-reference-latestlocalizedtext "class in com.here.sdk.core") localizedNumber, @NonNull [RouteType](sdk-for-android-explore-api-reference-latestroutetype "enum class in com.here.sdk.core") routeType)

    Creates a new instance.
Parameters:
    `localizedNumber` -

    Road number with locale information.

    `routeType` -

    The route type of the LocalizedRoadNumber.

## Method Details

### equals

public boolean equals([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) obj)
Overrides:
    [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

### hashCode

public int hashCode()
Overrides:
    [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

### getTextWithDirection

@NonNull public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getTextWithDirection()

    Returns the whole road number information including its cardinal direction. In case direction is empty, the original localized text will be returned.
Returns:
    The whole road number information including its cardinal direction.
