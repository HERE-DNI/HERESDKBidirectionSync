---
title: "DrawOrderType (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestdrawordertype"
hidden: false
---

Package [com.here.sdk.mapview](sdk-for-android-explore-api-reference-latestpackage-summary)

# Enum Class DrawOrderType

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[java.lang.Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)\<[DrawOrderType](sdk-for-android-explore-api-reference-latestdrawordertype "enum class in com.here.sdk.mapview")\>
com.here.sdk.mapview.DrawOrderType
All Implemented Interfaces:
[Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html), [Comparable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html)`<`[`DrawOrderType`](sdk-for-android-explore-api-reference-latestdrawordertype "enum class in com.here.sdk.mapview")`>`, [Constable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/constant/Constable.html)

------------------------------------------------------------------------
public enum DrawOrderType extends [Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)\<[DrawOrderType](sdk-for-android-explore-api-reference-latestdrawordertype "enum class in com.here.sdk.mapview")\>
Specifies the type of map item draw order. Map item rendering behavior is chosen based on the draw order type.

Regardless of a draw order type map items with a higher draw order are drawn on top of map items with a lower draw order.

When having map items in a scene with the same draw order, but with different draw order types [`MAP_SCENE_ADDITION_ORDER_DEPENDENT`](#MAP_SCENE_ADDITION_ORDER_DEPENDENT) and [`MAP_SCENE_ADDITION_ORDER_INDEPENDENT`](#MAP_SCENE_ADDITION_ORDER_INDEPENDENT), [`MAP_SCENE_ADDITION_ORDER_DEPENDENT`](#MAP_SCENE_ADDITION_ORDER_DEPENDENT) items will be rendered on top of [`MAP_SCENE_ADDITION_ORDER_INDEPENDENT`](#MAP_SCENE_ADDITION_ORDER_INDEPENDENT) ones.

## Nested Class Summary

## Nested classes/interfaces inherited from class java.lang.[Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)

  [Enum.EnumDesc](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html)`<`[E](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html)` extends `[Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)`<`[E](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html)`>>`

## Enum Constant Summary

Enum Constants

Enum Constant

  Description

  [MAP_SCENE_ADDITION_ORDER_DEPENDENT](#MAP_SCENE_ADDITION_ORDER_DEPENDENT)

Draw order depends on the order of map item addition to a map scene.

[MAP_SCENE_ADDITION_ORDER_INDEPENDENT](#MAP_SCENE_ADDITION_ORDER_INDEPENDENT)

Draw order does not depend on the order of map item addition to a map scene.

## Method Summary

  All Methods
  Static Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  `static `[`DrawOrderType`](sdk-for-android-explore-api-reference-latestdrawordertype "enum class in com.here.sdk.mapview")

  [valueOf](#valueOf(java.lang.String))`(`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` name)`

Returns the enum constant of this class with the specified name.

`static `[`DrawOrderType`](sdk-for-android-explore-api-reference-latestdrawordertype "enum class in com.here.sdk.mapview")`[]`

  [values](#values())`()`

Returns an array containing the constants of this enum class, in the order they are declared.

### Methods inherited from class java.lang.[Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#clone()), [compareTo](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#compareTo(E)), [describeConstable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#describeConstable()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#finalize()), [getDeclaringClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#getDeclaringClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#hashCode()), [name](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#name()), [ordinal](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#ordinal()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#toString()), [valueOf](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#valueOf(java.lang.Class,java.lang.String))

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Enum Constant Details

### MAP_SCENE_ADDITION_ORDER_DEPENDENT

public static final [DrawOrderType](sdk-for-android-explore-api-reference-latestdrawordertype "enum class in com.here.sdk.mapview") MAP_SCENE_ADDITION_ORDER_DEPENDENT

    Draw order depends on the order of map item addition to a map scene.

    Multiple map items of the same type with the same draw order are drawn in the order of addition to a map scene. With this behavior map items are rendered one by one.

### MAP_SCENE_ADDITION_ORDER_INDEPENDENT

public static final [DrawOrderType](sdk-for-android-explore-api-reference-latestdrawordertype "enum class in com.here.sdk.mapview") MAP_SCENE_ADDITION_ORDER_INDEPENDENT

    Draw order does not depend on the order of map item addition to a map scene.

    Multiple map items of the same type with the same draw order are drawn in an arbitrary order and map items with similar attributes (e.g. color) are grouped and drawn together all at once for performance reasons. This way map items added/re-added to a map scene lastly may appear below already existing map items with the same draw order.

## Method Details

### values

public static [DrawOrderType](sdk-for-android-explore-api-reference-latestdrawordertype "enum class in com.here.sdk.mapview")\[\] values()

    Returns an array containing the constants of this enum class, in the order they are declared.
Returns:
    an array containing the constants of this enum class, in the order they are declared

### valueOf

public static [DrawOrderType](sdk-for-android-explore-api-reference-latestdrawordertype "enum class in com.here.sdk.mapview") valueOf([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)

    Returns the enum constant of this class with the specified name. The string must match *exactly* an identifier used to declare an enum constant in this class. (Extraneous whitespace characters are not permitted.)
Parameters:
    `name` - the name of the enum constant to be returned.

    Returns:
    the enum constant with the specified name

    Throws:
    [IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html) - if this enum class has no constant with the specified name

    [NullPointerException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/NullPointerException.html) - if the argument is null
