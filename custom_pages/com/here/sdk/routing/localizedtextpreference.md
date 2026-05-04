---
title: "LocalizedTextPreference (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestlocalizedtextpreference"
hidden: false
---

Package [com.here.sdk.routing](sdk-for-android-explore-api-reference-latestpackage-summary)

# Enum Class LocalizedTextPreference

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[java.lang.Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)\<[LocalizedTextPreference](sdk-for-android-explore-api-reference-latestlocalizedtextpreference "enum class in com.here.sdk.routing")\>
com.here.sdk.routing.LocalizedTextPreference
All Implemented Interfaces:
[Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html), [Comparable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html)`<`[`LocalizedTextPreference`](sdk-for-android-explore-api-reference-latestlocalizedtextpreference "enum class in com.here.sdk.routing")`>`, [Constable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/constant/Constable.html)

------------------------------------------------------------------------
public enum LocalizedTextPreference extends [Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)\<[LocalizedTextPreference](sdk-for-android-explore-api-reference-latestlocalizedtextpreference "enum class in com.here.sdk.routing")\>
Indicates the option of localized text usage.

## Nested Class Summary

## Nested classes/interfaces inherited from class java.lang.[Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)

  [Enum.EnumDesc](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html)`<`[E](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html)` extends `[Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)`<`[E](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html)`>>`

## Enum Constant Summary

Enum Constants

Enum Constant

  Description

  [USE_ALWAYS](#USE_ALWAYS)

Information is included in the notification, if available.

[USE_IF_LANGUAGE_IS_COMPATIBLE](#USE_IF_LANGUAGE_IS_COMPATIBLE)

Information is included in the notification, if available and its language code is compatible with the voice package language.

[USE_NEVER](#USE_NEVER)

Information is not included in the notification.

## Method Summary

  All Methods
  Static Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  `static `[`LocalizedTextPreference`](sdk-for-android-explore-api-reference-latestlocalizedtextpreference "enum class in com.here.sdk.routing")

  [valueOf](#valueOf(java.lang.String))`(`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` name)`

Returns the enum constant of this class with the specified name.

`static `[`LocalizedTextPreference`](sdk-for-android-explore-api-reference-latestlocalizedtextpreference "enum class in com.here.sdk.routing")`[]`

  [values](#values())`()`

Returns an array containing the constants of this enum class, in the order they are declared.

### Methods inherited from class java.lang.[Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#clone()), [compareTo](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#compareTo(E)), [describeConstable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#describeConstable()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#finalize()), [getDeclaringClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#getDeclaringClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#hashCode()), [name](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#name()), [ordinal](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#ordinal()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#toString()), [valueOf](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#valueOf(java.lang.Class,java.lang.String))

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Enum Constant Details

### USE_NEVER

public static final [LocalizedTextPreference](sdk-for-android-explore-api-reference-latestlocalizedtextpreference "enum class in com.here.sdk.routing") USE_NEVER

    Information is not included in the notification.

### USE_ALWAYS

public static final [LocalizedTextPreference](sdk-for-android-explore-api-reference-latestlocalizedtextpreference "enum class in com.here.sdk.routing") USE_ALWAYS

    Information is included in the notification, if available.

### USE_IF_LANGUAGE_IS_COMPATIBLE

public static final [LocalizedTextPreference](sdk-for-android-explore-api-reference-latestlocalizedtextpreference "enum class in com.here.sdk.routing") USE_IF_LANGUAGE_IS_COMPATIBLE

    Information is included in the notification, if available and its language code is compatible with the voice package language. For example, in case the voice package language is German and the localized text information is in Italian, the information is then excluded from the notification. More examples: \| Voice package language \| Information language \| Included \| \| en-GB \| en \| yes \| \| en-GB \| de \| no \| \| pt-BR \| pt \| yes \| \| pt-PT \| pt \| yes \|

## Method Details

### values

public static [LocalizedTextPreference](sdk-for-android-explore-api-reference-latestlocalizedtextpreference "enum class in com.here.sdk.routing")\[\] values()

    Returns an array containing the constants of this enum class, in the order they are declared.
Returns:
    an array containing the constants of this enum class, in the order they are declared

### valueOf

public static [LocalizedTextPreference](sdk-for-android-explore-api-reference-latestlocalizedtextpreference "enum class in com.here.sdk.routing") valueOf([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)

    Returns the enum constant of this class with the specified name. The string must match *exactly* an identifier used to declare an enum constant in this class. (Extraneous whitespace characters are not permitted.)
Parameters:
    `name` - the name of the enum constant to be returned.

    Returns:
    the enum constant with the specified name

    Throws:
    [IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html) - if this enum class has no constant with the specified name

    [NullPointerException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/NullPointerException.html) - if the argument is null
