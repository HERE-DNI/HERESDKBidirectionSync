---
title: "StructuredQuery.AddressElements (API Reference)"
slug: "sdk-for-android-explore-api-reference-lateststructuredquery-addresselements"
hidden: false
---

Package [com.here.sdk.search](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class StructuredQuery.AddressElements

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.search.StructuredQuery.AddressElements
Enclosing class:
[StructuredQuery](sdk-for-android-explore-api-reference-lateststructuredquery "class in com.here.sdk.search")

------------------------------------------------------------------------
public static final class StructuredQuery.AddressElements extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Defines query address elements which will be used to build address hierarchy during searches. It is advised to provide at least one intermediate address element when a large address element is provided for small admin area searches. For example if a user is building a query for a street and providing only country as an address element, consider providing city along with it.

## Field Summary

Fields

Modifier and Type

  Field

  Description

  [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [city](#city)

An optional field of city name, which will be used to get the results only from the given city.

[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [country](#country)

An optional field of country name or code, which will be used to get the results only from the given country.

[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [district](#district)

An optional field of district, which will be used to get the results only from the given district.

[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [postalCode](#postalCode)

An optional field of postal code, which will be used to get the results only within the given postal code.

## Constructor Summary

Constructors

Constructor

  Description

  [AddressElements](#%3Cinit%3E())`()`

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

### country

@Nullable public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) country

    An optional field of country name or code, which will be used to get the results only from the given country.

### city

@Nullable public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) city

    An optional field of city name, which will be used to get the results only from the given city.

### postalCode

@Nullable public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) postalCode

    An optional field of postal code, which will be used to get the results only within the given postal code.

### district

@Nullable public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) district

    An optional field of district, which will be used to get the results only from the given district.

## Constructor Details

  - ()" class="section detail">

### AddressElements

public AddressElements()

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
