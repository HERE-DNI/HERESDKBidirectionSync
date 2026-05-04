---
title: "LocationTime (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestlocationtime"
hidden: false
---

Package [com.here.sdk.core](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class LocationTime

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.core.LocationTime
------------------------------------------------------------------------
public final class LocationTime extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
This struct presents all the time data tied to a location, like an arrival or departure time. The time data is originally specified in RFC 3339, section 5.6 format. For example, "2022-03-23T16:07:31+01:00" in Cracow, Poland, i.e. a Central European Time (CET) location. Note that this struct doesn't give any data on the tied location. The location should be derived from the context.

## Field Summary

Fields

Modifier and Type

  Field

  Description

  `final `[Date](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html)

  [localTime](#localTime)

The time as observed in the tied location.

`final `[`Duration`](sdk-for-android-explore-api-reference-latestduration "class in com.here.time")

  [utcOffset](#utcOffset)

The UTC offset is the difference between the local time and the Coordinated Universal Time (UTC) in seconds.

`final `[Date](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html)

  [utcTime](#utcTime)

The time as Coordinated Universal Time (UTC).

## Constructor Summary

Constructors

Constructor

  Description

  [LocationTime](#%3Cinit%3E(java.util.Date,java.util.Date,com.here.time.Duration))`(`[Date](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html)` localTime, `[Date](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html)` utcTime, `[`Duration`](sdk-for-android-explore-api-reference-latestduration "class in com.here.time")` utcOffset)`

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

### localTime

@NonNull public final [Date](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html) localTime

    The time as observed in the tied location. For example, if a route is requested in Cracow, Poland, the local time is "2022-03-23T16:07:31" in CET, i.e. one hour ahead of the UTC time.

### utcTime

@NonNull public final [Date](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html) utcTime

    The time as Coordinated Universal Time (UTC). For example, if a route is requested in Poland, the UTC time is "2022-03-23T15:07:31", i.e. one hour behind the local time.

### utcOffset

@NonNull public final [Duration](sdk-for-android-explore-api-reference-latestduration "class in com.here.time") utcOffset

    The UTC offset is the difference between the local time and the Coordinated Universal Time (UTC) in seconds. For example, if the local time is UTC+01:00, it is +3600 and if the local time is UTC-05:00, it is -18000.

## Constructor Details

  - (java.util.Date,java.util.Date,com.here.time.Duration)" class="section detail">

### LocationTime

public LocationTime(@NonNull [Date](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html) localTime, @NonNull [Date](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html) utcTime, @NonNull [Duration](sdk-for-android-explore-api-reference-latestduration "class in com.here.time") utcOffset)

    Creates a new instance.
Parameters:
    `localTime` -

    The time as observed in the tied location. For example, if a route is requested in Cracow, Poland, the local time is "2022-03-23T16:07:31" in CET, i.e. one hour ahead of the UTC time.

    `utcTime` -

    The time as Coordinated Universal Time (UTC). For example, if a route is requested in Poland, the UTC time is "2022-03-23T15:07:31", i.e. one hour behind the local time.

    `utcOffset` -

    The UTC offset is the difference between the local time and the Coordinated Universal Time (UTC) in seconds. For example, if the local time is UTC+01:00, it is +3600 and if the local time is UTC-05:00, it is -18000.

## Method Details

### equals

public boolean equals([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) obj)
Overrides:
    [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

### hashCode

public int hashCode()
Overrides:
    [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
