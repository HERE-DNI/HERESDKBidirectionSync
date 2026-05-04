---
title: "Duration (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestduration"
hidden: false
---

Package [com.here.time](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class Duration

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.time.Duration
All Implemented Interfaces:
[Comparable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html)`<`[`Duration`](sdk-for-android-explore-api-reference-latestduration "class in com.here.time")`>`

------------------------------------------------------------------------
public final class Duration extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) implements [Comparable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html)\<[Duration](sdk-for-android-explore-api-reference-latestduration "class in com.here.time")\>
Represents duration in time (both positive and negative).

The duration is represented as number of seconds (see [`getSeconds()`](#getSeconds())) and number of nanonseconds in a second (see [`getNano()`](#getNano())).

Duration can be created from various units of time by calling on of `of*` methods. The `to*` family of methods convert duration to a value expressed in desired unit of time.

## Method Summary

  All Methods
  Static Methods
  Instance Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  `int`

  [compareTo](#compareTo(com.here.time.Duration))`(`[`Duration`](sdk-for-android-explore-api-reference-latestduration "class in com.here.time")` duration)`

  `boolean`

  [equals](#equals(java.lang.Object))`(`[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)` o)`

  `int`

  [getNano](#getNano())`()`

  `long`

  [getSeconds](#getSeconds())`()`

  `int`

  [hashCode](#hashCode())`()`

  `static `[`Duration`](sdk-for-android-explore-api-reference-latestduration "class in com.here.time")

  [ofDays](#ofDays(long))`(long days)`

Creates a duration representing specified number of days.

`static `[`Duration`](sdk-for-android-explore-api-reference-latestduration "class in com.here.time")

  [ofHours](#ofHours(long))`(long hours)`

Creates a duration representing specified number of hours.

`static `[`Duration`](sdk-for-android-explore-api-reference-latestduration "class in com.here.time")

  [ofMillis](#ofMillis(long))`(long milliseconds)`

Creates a duration representing specified number of milliseconds.

`static `[`Duration`](sdk-for-android-explore-api-reference-latestduration "class in com.here.time")

  [ofMinutes](#ofMinutes(long))`(long minutes)`

Creates a duration representing specified number of hours.

`static `[`Duration`](sdk-for-android-explore-api-reference-latestduration "class in com.here.time")

  [ofNanos](#ofNanos(long))`(long nanoseconds)`

Creates a duration representing specified number of nanoseconds.

`static `[`Duration`](sdk-for-android-explore-api-reference-latestduration "class in com.here.time")

  [ofSeconds](#ofSeconds(long))`(long seconds)`

Creates a duration representing specified number of seconds.

`static `[`Duration`](sdk-for-android-explore-api-reference-latestduration "class in com.here.time")

  [ofSeconds](#ofSeconds(long,long))`(long seconds, long nanoAdjustment)`

Creates a duration representing specified number of seconds and an adjustment in nanoseconds.

`long`

  [toDays](#toDays())`()`

Converts this duration to days.

`long`

  [toDaysPart](#toDaysPart())`()`

Same as [`toDays()`](#toDays()).

`long`

  [toHours](#toHours())`()`

Converts this duration to hours.

`int`

  [toHoursPart](#toHoursPart())`()`

Gets the hours part of this duration.

`long`

  [toMillis](#toMillis())`()`

Converts this duration to milliseconds.

`int`

  [toMillisPart](#toMillisPart())`()`

Gets the milliseconds part of this duration.

`long`

  [toMinutes](#toMinutes())`()`

Converts this duration to minutes.

`int`

  [toMinutesPart](#toMinutesPart())`()`

Gets the minutes part of this duration.

`long`

  [toNanos](#toNanos())`()`

Converts this duration to nanoseconds.

`int`

  [toNanosPart](#toNanosPart())`()`

Gets the nanoseconds part of this duration.

`long`

  [toSeconds](#toSeconds())`()`

Converts this duration to seconds.

`int`

  [toSecondsPart](#toSecondsPart())`()`

Gets the seconds part of this duration.

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Method Details

### getNano

public int getNano()
Returns:
    The nanoseconds component of this duration.

### getSeconds

public long getSeconds()
Returns:
    The seconds component of this duration.

### ofDays

public static [Duration](sdk-for-android-explore-api-reference-latestduration "class in com.here.time") ofDays(long days) throws [ArithmeticException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/ArithmeticException.html)

    Creates a duration representing specified number of days. A Day is assumed to always be 24 hours.
Parameters:
    `days` - The number of days.

    Returns:
    The Duration representing the specified number of days.

    Throws:
    [ArithmeticException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/ArithmeticException.html) - if the input is outside the range possible to represent by a Duration

### ofHours

public static [Duration](sdk-for-android-explore-api-reference-latestduration "class in com.here.time") ofHours(long hours) throws [ArithmeticException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/ArithmeticException.html)

    Creates a duration representing specified number of hours. An hour is assumed to always be 60 minutes.
Parameters:
    `hours` - The number of hours.

    Returns:
    The Duration representing the specified number of hours.

    Throws:
    [ArithmeticException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/ArithmeticException.html) - if the input is outside the range possible to represent by a Duration

### ofMinutes

public static [Duration](sdk-for-android-explore-api-reference-latestduration "class in com.here.time") ofMinutes(long minutes) throws [ArithmeticException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/ArithmeticException.html)

    Creates a duration representing specified number of hours. A minute is assumed to always be 60 seconds.
Parameters:
    `minutes` - The number of minutes.

    Returns:
    The Duration representing the specified number of minutes.

    Throws:
    [ArithmeticException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/ArithmeticException.html) - if the input is outside the range possible to represent by a Duration

### ofSeconds

public static [Duration](sdk-for-android-explore-api-reference-latestduration "class in com.here.time") ofSeconds(long seconds)

    Creates a duration representing specified number of seconds.
Parameters:
    `seconds` - The number of seconds.

    Returns:
    The Duration representing the specified number of seconds.

### ofSeconds

public static [Duration](sdk-for-android-explore-api-reference-latestduration "class in com.here.time") ofSeconds(long seconds, long nanoAdjustment)

    Creates a duration representing specified number of seconds and an adjustment in nanoseconds.
Parameters:
    `seconds` - The number of seconds.

    `nanoAdjustment` - The nanosecond adjustment to the number of seconds.

    Returns:
    The Duration representing the specified number of seconds, adjusted.

### ofMillis

public static [Duration](sdk-for-android-explore-api-reference-latestduration "class in com.here.time") ofMillis(long milliseconds)

    Creates a duration representing specified number of milliseconds.
Parameters:
    `milliseconds` - The number of milliseconds.

    Returns:
    The Duration representing the specified number of milliseconds.

### ofNanos

public static [Duration](sdk-for-android-explore-api-reference-latestduration "class in com.here.time") ofNanos(long nanoseconds)

    Creates a duration representing specified number of nanoseconds.
Parameters:
    `nanoseconds` - The number of nanoseconds.

    Returns:
    The Duration representing the specified number of nanoseconds.

### toNanos

public long toNanos() throws [ArithmeticException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/ArithmeticException.html)

    Converts this duration to nanoseconds.
Returns:
    Total number of nanoseconds in this duration.

    Throws:
    [ArithmeticException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/ArithmeticException.html) - if the resulting value cannot be represented by `long` type.

### toNanosPart

public int toNanosPart()

    Gets the nanoseconds part of this duration. Equals to [`getNano()`](#getNano()).
Returns:
    The nanoseconds part of this duration, value from 0 to 999999999.

### toMillis

public long toMillis() throws [ArithmeticException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/ArithmeticException.html)

    Converts this duration to milliseconds. Any data past milliseconds precision is simply discarded. There is no mathematical rounding, so a duration of 999999 nanoseconds will still be converted to 0 milliseconds.
Returns:
    Total number of milliseconds in this duration.

    Throws:
    [ArithmeticException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/ArithmeticException.html) - if the resulting value cannot be represented by `long` type.

### toMillisPart

public int toMillisPart()

    Gets the milliseconds part of this duration.
Returns:
    The milliseconds part of this duration.

### toSeconds

public long toSeconds()

    Converts this duration to seconds. Any data past seconds precision is simply discarded. There is no mathematical rounding, so a duration of 999 milliseconds will still be converted to 0 seconds.
Returns:
    Total number of seconds in this duration.

### toSecondsPart

public int toSecondsPart()

    Gets the seconds part of this duration.
Returns:
    The seconds part of this duration, value from 0 to 59.

### toMinutes

public long toMinutes()

    Converts this duration to minutes. Any data past minute precision is simply discarded. There is no mathematical rounding, so a duration of 59 seconds and 999 milliseconds will still be converted to 0 minutes.
Returns:
    Total number of minutes in this duration.

### toMinutesPart

public int toMinutesPart()

    Gets the minutes part of this duration.
Returns:
    The minutes part of this duration, value from 0 to 59.

### toHours

public long toHours()

    Converts this duration to hours. Any data past hour precision is simply discarded. There is no mathematical rounding, so a duration of 59 minutes and 59 seconds will still be converted to 0 hours.
Returns:
    The number of full hours in this duration.

### toHoursPart

public int toHoursPart()

    Gets the hours part of this duration.
Returns:
    The hours part of this duration, value from 0 to 23.

### toDays

public long toDays()

    Converts this duration to days. Any data past day precision is simply discarded. There is no mathematical rounding, so a duration of 23 hours 59 minutes and 59 seconds will still be converted to 0 days. Day is always assumed to be 24 hours.
Returns:
    The number of full days in this duration.

### toDaysPart

public long toDaysPart()

    Same as [`toDays()`](#toDays()).
Returns:
    The number of full days in this duration.

### compareTo

public int compareTo([Duration](sdk-for-android-explore-api-reference-latestduration "class in com.here.time") duration)
Specified by:
    [compareTo](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html#compareTo(T)) in interface [Comparable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html)`<`[`Duration`](sdk-for-android-explore-api-reference-latestduration "class in com.here.time")`>`

### equals

public boolean equals([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) o)
Overrides:
    [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

### hashCode

public int hashCode()
Overrides:
    [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
