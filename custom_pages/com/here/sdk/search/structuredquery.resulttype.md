---
title: "StructuredQuery.ResultType (API Reference)"
slug: "sdk-for-android-explore-api-reference-lateststructuredquery-resulttype"
hidden: false
---

Package [com.here.sdk.search](sdk-for-android-explore-api-reference-latestpackage-summary)

# Enum Class StructuredQuery.ResultType

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[java.lang.Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)\<[StructuredQuery.ResultType](sdk-for-android-explore-api-reference-lateststructuredquery-resulttype "enum class in com.here.sdk.search")\>
com.here.sdk.search.StructuredQuery.ResultType
All Implemented Interfaces:
[Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html), [Comparable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html)`<`[`StructuredQuery.ResultType`](sdk-for-android-explore-api-reference-lateststructuredquery-resulttype "enum class in com.here.sdk.search")`>`, [Constable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/constant/Constable.html)

<!-- -->

Enclosing class:
[StructuredQuery](sdk-for-android-explore-api-reference-lateststructuredquery "class in com.here.sdk.search")

------------------------------------------------------------------------
public static enum StructuredQuery.ResultType extends [Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)\<[StructuredQuery.ResultType](sdk-for-android-explore-api-reference-lateststructuredquery-resulttype "enum class in com.here.sdk.search")\>
Specifies expected result type.

## Nested Class Summary

## Nested classes/interfaces inherited from class java.lang.[Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)

  [Enum.EnumDesc](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html)`<`[E](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html)` extends `[Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)`<`[E](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html)`>>`

## Enum Constant Summary

Enum Constants

Enum Constant

  Description

  [CITY](#CITY)

Expected result type is city.

[COUNTRY](#COUNTRY)

Expected result type is country.

[DISTRICT](#DISTRICT)

Expected result type is district.

[POSTAL_CODE](#POSTAL_CODE)

Expected result type is postal code.

[STREET](#STREET)

Expected result type is street.

## Method Summary

  All Methods
  Static Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  `static `[`StructuredQuery.ResultType`](sdk-for-android-explore-api-reference-lateststructuredquery-resulttype "enum class in com.here.sdk.search")

  [valueOf](#valueOf(java.lang.String))`(`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` name)`

Returns the enum constant of this class with the specified name.

`static `[`StructuredQuery.ResultType`](sdk-for-android-explore-api-reference-lateststructuredquery-resulttype "enum class in com.here.sdk.search")`[]`

  [values](#values())`()`

Returns an array containing the constants of this enum class, in the order they are declared.

### Methods inherited from class java.lang.[Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#clone()), [compareTo](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#compareTo(E)), [describeConstable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#describeConstable()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#finalize()), [getDeclaringClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#getDeclaringClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#hashCode()), [name](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#name()), [ordinal](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#ordinal()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#toString()), [valueOf](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#valueOf(java.lang.Class,java.lang.String))

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Enum Constant Details

### COUNTRY

public static final [StructuredQuery.ResultType](sdk-for-android-explore-api-reference-lateststructuredquery-resulttype "enum class in com.here.sdk.search") COUNTRY

    Expected result type is country.

### CITY

public static final [StructuredQuery.ResultType](sdk-for-android-explore-api-reference-lateststructuredquery-resulttype "enum class in com.here.sdk.search") CITY

    Expected result type is city.

### POSTAL_CODE

public static final [StructuredQuery.ResultType](sdk-for-android-explore-api-reference-lateststructuredquery-resulttype "enum class in com.here.sdk.search") POSTAL_CODE

    Expected result type is postal code.

### DISTRICT

public static final [StructuredQuery.ResultType](sdk-for-android-explore-api-reference-lateststructuredquery-resulttype "enum class in com.here.sdk.search") DISTRICT

    Expected result type is district.

### STREET

public static final [StructuredQuery.ResultType](sdk-for-android-explore-api-reference-lateststructuredquery-resulttype "enum class in com.here.sdk.search") STREET

    Expected result type is street.

## Method Details

### values

public static [StructuredQuery.ResultType](sdk-for-android-explore-api-reference-lateststructuredquery-resulttype "enum class in com.here.sdk.search")\[\] values()

    Returns an array containing the constants of this enum class, in the order they are declared.
Returns:
    an array containing the constants of this enum class, in the order they are declared

### valueOf

public static [StructuredQuery.ResultType](sdk-for-android-explore-api-reference-lateststructuredquery-resulttype "enum class in com.here.sdk.search") valueOf([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)

    Returns the enum constant of this class with the specified name. The string must match *exactly* an identifier used to declare an enum constant in this class. (Extraneous whitespace characters are not permitted.)
Parameters:
    `name` - the name of the enum constant to be returned.

    Returns:
    the enum constant with the specified name

    Throws:
    [IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html) - if this enum class has no constant with the specified name

    [NullPointerException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/NullPointerException.html) - if the argument is null
