---
title: "RoadTexts (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestroadtexts"
hidden: false
---

Package [com.here.sdk.routing](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class RoadTexts

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.routing.RoadTexts
------------------------------------------------------------------------
public final class RoadTexts extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Textual attributes of road.

## Field Summary

Fields

Modifier and Type

  Field

  Description

  [`LocalizedTexts`](sdk-for-android-explore-api-reference-latestlocalizedtexts "class in com.here.sdk.core")

  [names](#names)

Road names in available languages.

[`LocalizedRoadNumbers`](sdk-for-android-explore-api-reference-latestlocalizedroadnumbers "class in com.here.sdk.routing")

  [numbersWithDirection](#numbersWithDirection)

Road numbers with cardinal direction in available languages.

## Constructor Summary

Constructors

Constructor

  Description

  [RoadTexts](#%3Cinit%3E())`()`

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

### names

@NonNull public [LocalizedTexts](sdk-for-android-explore-api-reference-latestlocalizedtexts "class in com.here.sdk.core") names

    Road names in available languages. Empty for unnamed roads.

### numbersWithDirection

@NonNull public [LocalizedRoadNumbers](sdk-for-android-explore-api-reference-latestlocalizedroadnumbers "class in com.here.sdk.routing") numbersWithDirection

    Road numbers with cardinal direction in available languages. Empty if the road has no numbers assigned.

## Constructor Details

  - ()" class="section detail">

### RoadTexts

public RoadTexts()

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
