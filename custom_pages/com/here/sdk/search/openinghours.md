---
title: "OpeningHours (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestopeninghours"
hidden: false
---

Package [com.here.sdk.search](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class OpeningHours

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.search.OpeningHours
------------------------------------------------------------------------
public final class OpeningHours extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Represents opening hours information.

## Field Summary

Fields

Modifier and Type

  Field

  Description

  [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`PlaceCategory`](sdk-for-android-explore-api-reference-latestplacecategory "class in com.here.sdk.search")`>`

  [categories](#categories)

The list of categories related to opening hours information.

`boolean`

  [isOpen](#isOpen)

Boolean flag informing if the place is open or closed at the time when the search request was initiated.

[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`ScheduleDetails`](sdk-for-android-explore-api-reference-latestscheduledetails "class in com.here.sdk.search")`>`

  [scheduleDetailsList](#scheduleDetailsList)

The list of schedule details.

[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`>`

  [text](#text)

The list of opening hours presented as localized text.

## Constructor Summary

Constructors

Constructor

  Description

  [OpeningHours](#%3Cinit%3E(java.util.List,boolean,java.util.List,java.util.List))`(`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`> text, boolean isOpen, `[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`ScheduleDetails`](sdk-for-android-explore-api-reference-latestscheduledetails "class in com.here.sdk.search")`> scheduleDetailsList, `[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`PlaceCategory`](sdk-for-android-explore-api-reference-latestplacecategory "class in com.here.sdk.search")`> categories)`

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

### text

@NonNull public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)\> text

    The list of opening hours presented as localized text.

### isOpen

public boolean isOpen

    Boolean flag informing if the place is open or closed at the time when the search request was initiated. For offline search, this is calculated using device's time, so it may give incorrect value if device and place are located in different time zones.

### scheduleDetailsList

@NonNull public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[ScheduleDetails](sdk-for-android-explore-api-reference-latestscheduledetails "class in com.here.sdk.search")\> scheduleDetailsList

    The list of schedule details.

### categories

@NonNull public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[PlaceCategory](sdk-for-android-explore-api-reference-latestplacecategory "class in com.here.sdk.search")\> categories

    The list of categories related to opening hours information. This data is not available in offline search.

## Constructor Details

  - (java.util.List,boolean,java.util.List,java.util.List)" class="section detail">

### OpeningHours

public OpeningHours(@NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)\> text, boolean isOpen, @NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[ScheduleDetails](sdk-for-android-explore-api-reference-latestscheduledetails "class in com.here.sdk.search")\> scheduleDetailsList, @NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[PlaceCategory](sdk-for-android-explore-api-reference-latestplacecategory "class in com.here.sdk.search")\> categories)

    Creates a new instance.
Parameters:
    `text` -

    The list of opening hours presented as localized text.

    `isOpen` -

    Boolean flag informing if the place is open or closed at the time when the search request was initiated. For offline search, this is calculated using device's time, so it may give incorrect value if device and place are located in different time zones.

    `scheduleDetailsList` -

    The list of schedule details.

    `categories` -

    The list of categories related to opening hours information. This data is not available in offline search.

## Method Details

### equals

public boolean equals([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) obj)
Overrides:
    [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

### hashCode

public int hashCode()
Overrides:
    [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
