---
title: "GestureType (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestgesturetype"
hidden: false
---

Package [com.here.sdk.gestures](sdk-for-android-explore-api-reference-latestpackage-summary)

# Enum Class GestureType

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[java.lang.Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)\<[GestureType](sdk-for-android-explore-api-reference-latestgesturetype "enum class in com.here.sdk.gestures")\>
com.here.sdk.gestures.GestureType
All Implemented Interfaces:
[Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html), [Comparable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html)`<`[`GestureType`](sdk-for-android-explore-api-reference-latestgesturetype "enum class in com.here.sdk.gestures")`>`, [Constable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/constant/Constable.html)

------------------------------------------------------------------------
public enum GestureType extends [Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)\<[GestureType](sdk-for-android-explore-api-reference-latestgesturetype "enum class in com.here.sdk.gestures")\>
Enum that represents the type of a gesture.

## Nested Class Summary

## Nested classes/interfaces inherited from class java.lang.[Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)

  [Enum.EnumDesc](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html)`<`[E](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html)` extends `[Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)`<`[E](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html)`>>`

## Enum Constant Summary

Enum Constants

Enum Constant

  Description

  [DOUBLE_TAP](#DOUBLE_TAP)

Double-tap performed with one finger.

[PAN](#PAN)

Panning gesture with a one or two fingers.

[PINCH_ROTATE](#PINCH_ROTATE)

Pinching and rotating gesture using two fingers.

[TWO_FINGER_PAN](#TWO_FINGER_PAN)

Vertical panning gesture with two fingers.

[TWO_FINGER_TAP](#TWO_FINGER_TAP)

Single-tap performed with two fingers.

## Method Summary

  All Methods
  Static Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  `static `[`GestureType`](sdk-for-android-explore-api-reference-latestgesturetype "enum class in com.here.sdk.gestures")

  [valueOf](#valueOf(java.lang.String))`(`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` name)`

Returns the enum constant of this class with the specified name.

`static `[`GestureType`](sdk-for-android-explore-api-reference-latestgesturetype "enum class in com.here.sdk.gestures")`[]`

  [values](#values())`()`

Returns an array containing the constants of this enum class, in the order they are declared.

### Methods inherited from class java.lang.[Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#clone()), [compareTo](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#compareTo(E)), [describeConstable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#describeConstable()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#finalize()), [getDeclaringClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#getDeclaringClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#hashCode()), [name](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#name()), [ordinal](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#ordinal()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#toString()), [valueOf](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#valueOf(java.lang.Class,java.lang.String))

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Enum Constant Details

### TWO_FINGER_TAP

public static final [GestureType](sdk-for-android-explore-api-reference-latestgesturetype "enum class in com.here.sdk.gestures") TWO_FINGER_TAP

    Single-tap performed with two fingers. When performed on a map view, this instantly zooms the map out by a factor of 0.5 and the map becomes twice as small.

### DOUBLE_TAP

public static final [GestureType](sdk-for-android-explore-api-reference-latestgesturetype "enum class in com.here.sdk.gestures") DOUBLE_TAP

    Double-tap performed with one finger. When performed on a map view, this instantly zooms the map in by a factor of 2 and the map becomes twice as big.

### PAN

public static final [GestureType](sdk-for-android-explore-api-reference-latestgesturetype "enum class in com.here.sdk.gestures") PAN

    Panning gesture with a one or two fingers. When performed on a map view, this continuously moves the map.

### TWO_FINGER_PAN

public static final [GestureType](sdk-for-android-explore-api-reference-latestgesturetype "enum class in com.here.sdk.gestures") TWO_FINGER_PAN

    Vertical panning gesture with two fingers. When performed on a map view, this continuously tilts the map.

### PINCH_ROTATE

public static final [GestureType](sdk-for-android-explore-api-reference-latestgesturetype "enum class in com.here.sdk.gestures") PINCH_ROTATE

    Pinching and rotating gesture using two fingers. When performed on a map view, this continuously scales, zooms or rotates the map.

## Method Details

### values

public static [GestureType](sdk-for-android-explore-api-reference-latestgesturetype "enum class in com.here.sdk.gestures")\[\] values()

    Returns an array containing the constants of this enum class, in the order they are declared.
Returns:
    an array containing the constants of this enum class, in the order they are declared

### valueOf

public static [GestureType](sdk-for-android-explore-api-reference-latestgesturetype "enum class in com.here.sdk.gestures") valueOf([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)

    Returns the enum constant of this class with the specified name. The string must match *exactly* an identifier used to declare an enum constant in this class. (Extraneous whitespace characters are not permitted.)
Parameters:
    `name` - the name of the enum constant to be returned.

    Returns:
    the enum constant with the specified name

    Throws:
    [IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html) - if this enum class has no constant with the specified name

    [NullPointerException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/NullPointerException.html) - if the argument is null
