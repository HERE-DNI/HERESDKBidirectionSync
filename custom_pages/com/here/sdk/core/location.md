---
title: "Location (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestlocation"
hidden: false
---

Package [com.here.sdk.core](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class Location

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.core.Location
------------------------------------------------------------------------
public final class Location extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Describes a location in the world at a given time.

## Field Summary

Fields

Modifier and Type

  Field

  Description

  [Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html)

  [bearingAccuracyInDegrees](#bearingAccuracyInDegrees)

Estimated bearing accuracy for this location, in degrees.

[Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html)

  [bearingInDegrees](#bearingInDegrees)

Bearing (also known as course) is the device's horizontal direction of travel.

[`GeoCoordinates`](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core")

  [coordinates](#coordinates)

The geographic coordinates of the location.

[`Duration`](sdk-for-android-explore-api-reference-latestduration "class in com.here.time")

  [gnssTime](#gnssTime)

Optional gnss time at which the location was determined.

[Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html)

  [horizontalAccuracyInMeters](#horizontalAccuracyInMeters)

The estimated horizontal accuracy.

[`LocationTechnology`](sdk-for-android-explore-api-reference-latestlocationtechnology "enum class in com.here.sdk.core")

  [locationTechnology](#locationTechnology)

Optional technology or provider of this location.

[Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html)

  [pitchInDegrees](#pitchInDegrees)

Pitch of this location, in degrees.

[`LocationSource`](sdk-for-android-explore-api-reference-latestlocationsource "enum class in com.here.sdk.core")

  [source](#source)

Optional source of this location.

[Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html)

  [speedAccuracyInMetersPerSecond](#speedAccuracyInMetersPerSecond)

Estimated speed accuracy of this location, in meters per second.

[Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html)

  [speedInMetersPerSecond](#speedInMetersPerSecond)

Current speed of the device.

[Date](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html)

  [time](#time)

The time at which the location was determined.

[`Duration`](sdk-for-android-explore-api-reference-latestduration "class in com.here.time")

  [timestampSinceBoot](#timestampSinceBoot)

The time at which the location was determined, relative to device boot time.

[Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html)

  [verticalAccuracyInMeters](#verticalAccuracyInMeters)

Estimated vertical accuracy.

## Constructor Summary

Constructors

Constructor

  Description

  [Location](#%3Cinit%3E(com.here.sdk.core.GeoCoordinates))`(`[`GeoCoordinates`](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core")` coordinates)`

Creates a new Location instance from the provided GeoCoordinates value.

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

### coordinates

@NonNull public [GeoCoordinates](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core") coordinates

    The geographic coordinates of the location.

### bearingInDegrees

@Nullable public [Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html) bearingInDegrees

    Bearing (also known as course) is the device's horizontal direction of travel. Starts at 0 in the geographical north and rotates around the compass in a clockwise direction. This means for going north it is equal to 0, for northeast it is 45, for east it is 90 and so on. Note that this may be different from the orientation of the device. If it cannot be determined, the value is `null`. Otherwise, it is guaranteed to be in the range \[0, 360).

### speedInMetersPerSecond

@Nullable public [Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html) speedInMetersPerSecond

    Current speed of the device. If it cannot be determined, the value is `null`.

### time

@Nullable public [Date](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html) time

    The time at which the location was determined.

### horizontalAccuracyInMeters

@Nullable public [Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html) horizontalAccuracyInMeters

    The estimated horizontal accuracy. The actual location will lie within this radius of uncertainty.

### verticalAccuracyInMeters

@Nullable public [Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html) verticalAccuracyInMeters

    Estimated vertical accuracy. Given that the received Location contains the altitude, the real value of the altitude is estimated to lie within the following range: \[altitude - vertical accuracy, altitude + vertical accuracy\]. For example, when the altitude is equal to 50 and the vertical accuracy is 8, then the actual value is most likely in the range \[42, 58\].

### bearingAccuracyInDegrees

@Nullable public [Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html) bearingAccuracyInDegrees

    Estimated bearing accuracy for this location, in degrees. If it cannot be determined, the value is `null`.

### speedAccuracyInMetersPerSecond

@Nullable public [Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html) speedAccuracyInMetersPerSecond

    Estimated speed accuracy of this location, in meters per second. If it cannot be determined, the value is `null`.

### timestampSinceBoot

@Nullable public [Duration](sdk-for-android-explore-api-reference-latestduration "class in com.here.time") timestampSinceBoot

    The time at which the location was determined, relative to device boot time. This time is monotonic and not affected by leap time or other system time adjustments, so this is the recommended basis for general purpose interval timing between location updates. If it cannot be determined, the value is `null`.

### locationTechnology

@Nullable public [LocationTechnology](sdk-for-android-explore-api-reference-latestlocationtechnology "enum class in com.here.sdk.core") locationTechnology

    Optional technology or provider of this location. If it cannot be determined, the value is `null`.

### source

@Nullable public [LocationSource](sdk-for-android-explore-api-reference-latestlocationsource "enum class in com.here.sdk.core") source

    Optional source of this location. If it cannot be determined, the value is `null`.

### gnssTime

@Nullable public [Duration](sdk-for-android-explore-api-reference-latestduration "class in com.here.time") gnssTime

    Optional gnss time at which the location was determined. It is a time interval from the Unix time epoch in milliseconds. If it cannot be determined, the value is `null`.

### pitchInDegrees

@Nullable public [Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html) pitchInDegrees

    Pitch of this location, in degrees. If it cannot be determined, the value is `null`.

## Constructor Details

  - (com.here.sdk.core.GeoCoordinates)" class="section detail">

### Location

public Location(@NonNull [GeoCoordinates](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core") coordinates)

    Creates a new Location instance from the provided GeoCoordinates value. timestamp is initialized with `January 1, 1970, 00:00:00 GMT` value. The rest of the fields will be initialized to null.
Parameters:
    `coordinates` -

    The geographic coordinates of the location.

## Method Details

### equals

public boolean equals([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) obj)
Overrides:
    [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

### hashCode

public int hashCode()
Overrides:
    [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
