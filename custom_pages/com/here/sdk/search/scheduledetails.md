---
title: "ScheduleDetails (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestscheduledetails"
hidden: false
---

Package [com.here.sdk.search](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class ScheduleDetails

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.search.ScheduleDetails
------------------------------------------------------------------------
public final class ScheduleDetails extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Encapsulates schedule details complying with the iCalendar specification: https://tools.ietf.org/html/rfc5545.

## Field Summary

Fields

Modifier and Type

  Field

  Description

  [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [duration](#duration)

Specifies a positive duration of time for the iCalendar component, for example "PT24H00M" (lasts 24h).

[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [recurrence](#recurrence)

The recurrence information for a iCalendar component, for example "FREQ:DAILY;BYDAY:MO,TU,WE,TH,FR,SA".

[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [start](#start)

Specifies when the iCalendar component begins, for example "T000000" (starts at midnight).

## Constructor Summary

Constructors

Constructor

  Description

  [ScheduleDetails](#%3Cinit%3E(java.lang.String,java.lang.String,java.lang.String))`(`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` start, `[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` duration, `[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` recurrence)`

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

### start

@NonNull public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) start

    Specifies when the iCalendar component begins, for example "T000000" (starts at midnight).

### duration

@NonNull public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) duration

    Specifies a positive duration of time for the iCalendar component, for example "PT24H00M" (lasts 24h).

### recurrence

@NonNull public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) recurrence

    The recurrence information for a iCalendar component, for example "FREQ:DAILY;BYDAY:MO,TU,WE,TH,FR,SA".

## Constructor Details

  - (java.lang.String,java.lang.String,java.lang.String)" class="section detail">

### ScheduleDetails

public ScheduleDetails(@NonNull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) start, @NonNull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) duration, @NonNull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) recurrence)

    Creates a new instance.
Parameters:
    `start` -

    Specifies when the iCalendar component begins, for example "T000000" (starts at midnight).

    `duration` -

    Specifies a positive duration of time for the iCalendar component, for example "PT24H00M" (lasts 24h).

    `recurrence` -

    The recurrence information for a iCalendar component, for example "FREQ:DAILY;BYDAY:MO,TU,WE,TH,FR,SA".

## Method Details

### equals

public boolean equals([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) obj)
Overrides:
    [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

### hashCode

public int hashCode()
Overrides:
    [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
