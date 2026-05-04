---
title: "HazardousMaterial (API Reference)"
slug: "sdk-for-android-explore-api-reference-latesthazardousmaterial"
hidden: false
---

Package [com.here.sdk.transport](sdk-for-android-explore-api-reference-latestpackage-summary)

# Enum Class HazardousMaterial

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[java.lang.Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)\<[HazardousMaterial](sdk-for-android-explore-api-reference-latesthazardousmaterial "enum class in com.here.sdk.transport")\>
com.here.sdk.transport.HazardousMaterial
All Implemented Interfaces:
[Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html), [Comparable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html)`<`[`HazardousMaterial`](sdk-for-android-explore-api-reference-latesthazardousmaterial "enum class in com.here.sdk.transport")`>`, [Constable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/constant/Constable.html)

------------------------------------------------------------------------
public enum HazardousMaterial extends [Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)\<[HazardousMaterial](sdk-for-android-explore-api-reference-latesthazardousmaterial "enum class in com.here.sdk.transport")\>
Identifiers for different types of hazardous materials which can be shipped by the truck.

## Nested Class Summary

## Nested classes/interfaces inherited from class java.lang.[Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)

  [Enum.EnumDesc](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html)`<`[E](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html)` extends `[Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)`<`[E](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html)`>>`

## Enum Constant Summary

Enum Constants

Enum Constant

  Description

  [COMBUSTIBLE](#COMBUSTIBLE)

Combustible material.

[CORROSIVE](#CORROSIVE)

Corrosive material.

[EXPLOSIVE](#EXPLOSIVE)

Explosive material.

[FLAMMABLE](#FLAMMABLE)

Flammable material.

[GAS](#GAS)

Gas.

[HARMFUL_TO_WATER](#HARMFUL_TO_WATER)

Materials that are harmful to water.

[ORGANIC](#ORGANIC)

Organic material.

[OTHER](#OTHER)

Any other hazardous material.

[POISON](#POISON)

Poisonous material.

[POISONOUS_INHALATION](#POISONOUS_INHALATION)

Materials that are poisonous upon inhalation.

[RADIOACTIVE](#RADIOACTIVE)

Radioactive material.

## Method Summary

  All Methods
  Static Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  `static `[`HazardousMaterial`](sdk-for-android-explore-api-reference-latesthazardousmaterial "enum class in com.here.sdk.transport")

  [valueOf](#valueOf(java.lang.String))`(`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` name)`

Returns the enum constant of this class with the specified name.

`static `[`HazardousMaterial`](sdk-for-android-explore-api-reference-latesthazardousmaterial "enum class in com.here.sdk.transport")`[]`

  [values](#values())`()`

Returns an array containing the constants of this enum class, in the order they are declared.

### Methods inherited from class java.lang.[Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#clone()), [compareTo](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#compareTo(E)), [describeConstable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#describeConstable()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#finalize()), [getDeclaringClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#getDeclaringClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#hashCode()), [name](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#name()), [ordinal](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#ordinal()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#toString()), [valueOf](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#valueOf(java.lang.Class,java.lang.String))

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Enum Constant Details

### EXPLOSIVE

public static final [HazardousMaterial](sdk-for-android-explore-api-reference-latesthazardousmaterial "enum class in com.here.sdk.transport") EXPLOSIVE

    Explosive material.

### GAS

public static final [HazardousMaterial](sdk-for-android-explore-api-reference-latesthazardousmaterial "enum class in com.here.sdk.transport") GAS

    Gas.

### FLAMMABLE

public static final [HazardousMaterial](sdk-for-android-explore-api-reference-latesthazardousmaterial "enum class in com.here.sdk.transport") FLAMMABLE

    Flammable material.

### COMBUSTIBLE

public static final [HazardousMaterial](sdk-for-android-explore-api-reference-latesthazardousmaterial "enum class in com.here.sdk.transport") COMBUSTIBLE

    Combustible material.

### ORGANIC

public static final [HazardousMaterial](sdk-for-android-explore-api-reference-latesthazardousmaterial "enum class in com.here.sdk.transport") ORGANIC

    Organic material.

### POISON

public static final [HazardousMaterial](sdk-for-android-explore-api-reference-latesthazardousmaterial "enum class in com.here.sdk.transport") POISON

    Poisonous material.

### RADIOACTIVE

public static final [HazardousMaterial](sdk-for-android-explore-api-reference-latesthazardousmaterial "enum class in com.here.sdk.transport") RADIOACTIVE

    Radioactive material.

### CORROSIVE

public static final [HazardousMaterial](sdk-for-android-explore-api-reference-latesthazardousmaterial "enum class in com.here.sdk.transport") CORROSIVE

    Corrosive material.

### POISONOUS_INHALATION

public static final [HazardousMaterial](sdk-for-android-explore-api-reference-latesthazardousmaterial "enum class in com.here.sdk.transport") POISONOUS_INHALATION

    Materials that are poisonous upon inhalation.

### HARMFUL_TO_WATER

public static final [HazardousMaterial](sdk-for-android-explore-api-reference-latesthazardousmaterial "enum class in com.here.sdk.transport") HARMFUL_TO_WATER

    Materials that are harmful to water.

### OTHER

public static final [HazardousMaterial](sdk-for-android-explore-api-reference-latesthazardousmaterial "enum class in com.here.sdk.transport") OTHER

    Any other hazardous material.

## Method Details

### values

public static [HazardousMaterial](sdk-for-android-explore-api-reference-latesthazardousmaterial "enum class in com.here.sdk.transport")\[\] values()

    Returns an array containing the constants of this enum class, in the order they are declared.
Returns:
    an array containing the constants of this enum class, in the order they are declared

### valueOf

public static [HazardousMaterial](sdk-for-android-explore-api-reference-latesthazardousmaterial "enum class in com.here.sdk.transport") valueOf([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)

    Returns the enum constant of this class with the specified name. The string must match *exactly* an identifier used to declare an enum constant in this class. (Extraneous whitespace characters are not permitted.)
Parameters:
    `name` - the name of the enum constant to be returned.

    Returns:
    the enum constant with the specified name

    Throws:
    [IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html) - if this enum class has no constant with the specified name

    [NullPointerException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/NullPointerException.html) - if the argument is null
