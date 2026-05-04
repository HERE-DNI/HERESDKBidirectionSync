---
title: "SectionNotice (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestsectionnotice"
hidden: false
---

Package [com.here.sdk.routing](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class SectionNotice

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.routing.SectionNotice
------------------------------------------------------------------------
public final class SectionNotice extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Explains an issue encountered in a [`Section`](sdk-for-android-explore-api-reference-latestsection "class in com.here.sdk.routing").

## Field Summary

Fields

Modifier and Type

  Field

  Description

  [`SectionNoticeCode`](sdk-for-android-explore-api-reference-latestsectionnoticecode "enum class in com.here.sdk.routing")

  [code](#code)

The notice code.

[`NoticeSeverity`](sdk-for-android-explore-api-reference-latestnoticeseverity "enum class in com.here.sdk.routing")

  [severity](#severity)

The notice severity.

[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`ViolatedRestriction`](sdk-for-android-explore-api-reference-latestviolatedrestriction "class in com.here.sdk.routing")`>`

  [violatedRestrictions](#violatedRestrictions)

The following property `violated_restrictions` contains the notice detail information.

## Constructor Summary

Constructors

Constructor

  Description

  [SectionNotice](#%3Cinit%3E(com.here.sdk.routing.SectionNoticeCode,com.here.sdk.routing.NoticeSeverity))`(`[`SectionNoticeCode`](sdk-for-android-explore-api-reference-latestsectionnoticecode "enum class in com.here.sdk.routing")` code, `[`NoticeSeverity`](sdk-for-android-explore-api-reference-latestnoticeseverity "enum class in com.here.sdk.routing")` severity)`

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

### code

@NonNull public [SectionNoticeCode](sdk-for-android-explore-api-reference-latestsectionnoticecode "enum class in com.here.sdk.routing") code

    The notice code.

### severity

@NonNull public [NoticeSeverity](sdk-for-android-explore-api-reference-latestnoticeseverity "enum class in com.here.sdk.routing") severity

    The notice severity.

### violatedRestrictions

@NonNull public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[ViolatedRestriction](sdk-for-android-explore-api-reference-latestviolatedrestriction "class in com.here.sdk.routing")\> violatedRestrictions

    The following property `violated_restrictions` contains the notice detail information. Only three types of restrictions can have notice details: time dependent restriction, vehicle restriction and transport mode restriction. There is no one-to-one match of the `SectionNotice.code` and these three restriction types. For example, if `SectionNotice.code` is [`SectionNoticeCode.VIOLATED_VEHICLE_RESTRICTION`](sdk-for-android-explore-api-reference-latestsectionnoticecode#VIOLATED_VEHICLE_RESTRICTION), then it can be either vehicle restriction or transport mode restriction. If `SectionNotice.code` is [`SectionNoticeCode.SEASONAL_CLOSURE`](sdk-for-android-explore-api-reference-latestsectionnoticecode#SEASONAL_CLOSURE), then it is time dependent restriction. If the section notice is none of the above-mentioned three types, then this will be an empty list.

## Constructor Details

  - (com.here.sdk.routing.SectionNoticeCode,com.here.sdk.routing.NoticeSeverity)" class="section detail">

### SectionNotice

public SectionNotice(@NonNull [SectionNoticeCode](sdk-for-android-explore-api-reference-latestsectionnoticecode "enum class in com.here.sdk.routing") code, @NonNull [NoticeSeverity](sdk-for-android-explore-api-reference-latestnoticeseverity "enum class in com.here.sdk.routing") severity)

    Creates a new instance.
Parameters:
    `code` -

    The notice code.

    `severity` -

    The notice severity.

## Method Details

### equals

public boolean equals([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) obj)
Overrides:
    [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

### hashCode

public int hashCode()
Overrides:
    [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
