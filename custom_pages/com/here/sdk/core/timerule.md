---
title: "TimeRule (API Reference)"
slug: "sdk-for-android-explore-api-reference-latesttimerule"
hidden: false
---

Package [com.here.sdk.core](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class TimeRule

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.here.NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
com.here.sdk.core.TimeRule
------------------------------------------------------------------------
public final class TimeRule extends [NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
Used to indicate a time period of one or more intervals in [GDF](https://www.here.com/docs/bundle/routing-api-developer-guide-v8/page/concepts/time-domain.html) specification. For example: -\*(M3f21h2){M9}(M11f12h2){-M9}+(h15){h2}(h20){h2}, which represents: March 2nd Sunday 02h:00m for 9 months ONLY DURING November 1st Sunday 02h:00m from 9 months ago BUT NOT from 15:00 to 17:00 OR 20:00 to 22:00

The operator \* represents reccuring occurrence, `+` represents a logical OR operation and `-` represents exclusion meaning, BUT NOT operations.

This example string represents a time period that meets the following criteria:

- `M3f21h2`: M3 denotes third month of the year, i.e. March, f2 stands for the second Sunday of the month (as "f" might indicate "first", "second", "third", etc.), 1 stands for the day of the week (1...7, Day of week, Sunday = day 1), and h2 represents the hour of the day (02:00) in 24 hour format.
- `{M9}`: This denotes "for 9 months", with "M9" standing for nine months. The brackets {} indicate a duration.
- `M11f12h2`: M11 denotes 11th month of the year, i.e. November, f1 stands for the first Monday of the month, 2 stands for the day of the week (1...7, Day of week, Monday = day 2), and h2 represents the hour of the day (02:00) in 24 hour format.
- {-M9}: This denotes "9 months ago from the current stated time", with "-M9" standing for nine months in the past.
- `(h15){h2}(h20){h2}`: 15:00 to 17:00 OR 20:00 to 22:00 The brackets {} denotes duration, and the negative sign - represents a past duration.

Note: The time period is a logical AND (&&) combination of two components or points in time and it only applies if a point in time is in both components.

For more advanced examples of `TimeRule` see [here](https://www.here.com/docs/bundle/routing-api-developer-guide-v8/page/topics/time-domain.html#time-domain-advanced-examples).

## Constructor Summary

Constructors

Constructor

  Description

  [TimeRule](#%3Cinit%3E(java.lang.String,int,java.lang.String))`(`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` timeRule, int timeZoneOffsetSeconds, `[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` dstSpec)`

Creates a new instance of this class.

## Method Summary

  All Methods
  Instance Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  `boolean`

  [appliesTo](#appliesTo(java.util.Date))`(`[Date](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html)` dateTime)`

  `boolean`

  [equals](#equals(java.lang.Object))`(`[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)` rhs)`

  [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [getDstSpec](#getDstSpec())`()`

Gets the value of day saving time specification, as a string in ISO 14825 format, for the location where the time rule applies.

[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [getTimeRuleString](#getTimeRuleString())`()`

Gets the value of time rule as a string in ISO 14825 format.

`int`

  [getTimeZoneOffsetSeconds](#getTimeZoneOffsetSeconds())`()`

Gets the value of time zone offset in seconds for the location where the time rule applies.

`int`

  [hashCode](#hashCode())`()`

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Constructor Details

  - (java.lang.String,int,java.lang.String)" class="section detail">

### TimeRule

public TimeRule(@NonNull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) timeRule, int timeZoneOffsetSeconds, @NonNull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) dstSpec)

    Creates a new instance of this class.
Parameters:
    `timeRule` -

    The time rule as a string in ISO 14825 format.

    `timeZoneOffsetSeconds` -

    The time zone offset in seconds for the location where the time rule applies.

    `dstSpec` -

    Day saving time specification, as a string in ISO 14825 format, for the location where the time rule applies.

## Method Details

### equals

public boolean equals([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) rhs)
Overrides:
    [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

### hashCode

public int hashCode()
Overrides:
    [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

### appliesTo

public boolean appliesTo(@NonNull [Date](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html) dateTime)
Parameters:
    `dateTime` -

    date and time that should be used for rule verification.

    Returns:
    `true` if the time domain rules applies to the given date and time., `false` - otherwise.

### getTimeRuleString

@NonNull public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getTimeRuleString()

    Gets the value of time rule as a string in ISO 14825 format.
Returns:
    The time rule as a string in ISO 14825 format.

### getTimeZoneOffsetSeconds

public int getTimeZoneOffsetSeconds()

    Gets the value of time zone offset in seconds for the location where the time rule applies.
Returns:
    The time zone offset in seconds for the location where the time rule applies.

### getDstSpec

@NonNull public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getDstSpec()

    Gets the value of day saving time specification, as a string in ISO 14825 format, for the location where the time rule applies.
Returns:
    Day saving time specification, as a string in ISO 14825 format, for the location where the time rule applies.
