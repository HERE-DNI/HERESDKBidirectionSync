---
title: "Metadata (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestmetadata"
hidden: false
---

Package [com.here.sdk.core](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class Metadata

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.here.NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
com.here.sdk.core.Metadata
------------------------------------------------------------------------
public final class Metadata extends [NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
Holds metadata on behalf of a map item. An instance of this class can contain metadata items of varying types, such as String, Integer, Double, GeoCoordinates etc. and can also hold arbitrary metadata types by the use of the CustomMetadataValue interface.

## Constructor Summary

Constructors

Constructor

  Description

  [Metadata](#%3Cinit%3E())`()`

Creates an instance of this class.

## Method Summary

  All Methods
  Instance Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  [`CustomMetadataValue`](sdk-for-android-explore-api-reference-latestcustommetadatavalue "interface in com.here.sdk.core")

  [getCustomValue](#getCustomValue(java.lang.String))`(`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` key)`

Obtains an instance of the CustomMetadataValue class associated with a given key.

[Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html)

  [getDouble](#getDouble(java.lang.String))`(`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` key)`

Obtains a Double value associated with a given key.

[`GeoCoordinates`](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core")

  [getGeoCoordinates](#getGeoCoordinates(java.lang.String))`(`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` key)`

Obtains a GeoCoordinates value associated with a given key.

[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html)

  [getInteger](#getInteger(java.lang.String))`(`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` key)`

Obtains an Integer value associated with a given key.

[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [getString](#getString(java.lang.String))`(`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` key)`

Obtains a String value associated with a given key.

[`MetadataType`](sdk-for-android-explore-api-reference-latestmetadatatype "enum class in com.here.sdk.core")

  [getType](#getType(java.lang.String))`(`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` key)`

Determines the type of a metadata value.

`void`

  [removeValue](#removeValue(java.lang.String))`(`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` key)`

Removes a metadata key and its associated value.

`void`

  [setCustomValue](#setCustomValue(java.lang.String,com.here.sdk.core.CustomMetadataValue))`(`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` key, `[`CustomMetadataValue`](sdk-for-android-explore-api-reference-latestcustommetadatavalue "interface in com.here.sdk.core")` value)`

Creates a key:value pair, where the value is a type derived from CustomMetadataValue.

`void`

  [setDouble](#setDouble(java.lang.String,double))`(`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` key, double value)`

Creates a key:value pair, where the value is of type Double.

`void`

  [setGeoCoordinates](#setGeoCoordinates(java.lang.String,com.here.sdk.core.GeoCoordinates))`(`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` key, `[`GeoCoordinates`](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core")` value)`

Creates a key:value pair, where the value is of type GeoCoordinates.

`void`

  [setInteger](#setInteger(java.lang.String,int))`(`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` key, int value)`

Creates a key:value pair, where the value is of type Integer.

`void`

  [setString](#setString(java.lang.String,java.lang.String))`(`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` key, `[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` value)`

Creates a key:value pair, where the value is of type String.

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Constructor Details

  - ()" class="section detail">

### Metadata

public Metadata()

    Creates an instance of this class.

## Method Details

### getCustomValue

@Nullable public [CustomMetadataValue](sdk-for-android-explore-api-reference-latestcustommetadatavalue "interface in com.here.sdk.core") getCustomValue(@NonNull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) key)

    Obtains an instance of the CustomMetadataValue class associated with a given key.
Parameters:
    `key` -

    The name of the key for which to obtain the value.

    Returns:
    The value associated with the key.

### getDouble

@Nullable public [Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html) getDouble(@NonNull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) key)

    Obtains a Double value associated with a given key.
Parameters:
    `key` -

    The name of the key for which to obtain the value.

    Returns:
    The value associated with the key.

### getGeoCoordinates

@Nullable public [GeoCoordinates](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core") getGeoCoordinates(@NonNull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) key)

    Obtains a GeoCoordinates value associated with a given key.
Parameters:
    `key` -

    The name of the key for which to obtain the value.

    Returns:
    The value associated with the key.

### getInteger

@Nullable public [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) getInteger(@NonNull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) key)

    Obtains an Integer value associated with a given key.
Parameters:
    `key` -

    The name of the key for which to obtain the value.

    Returns:
    The value associated with the key.

### getString

@Nullable public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getString(@NonNull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) key)

    Obtains a String value associated with a given key.
Parameters:
    `key` -

    The name of the key for which to obtain the value.

    Returns:
    The value associated with the key.

### getType

@Nullable public [MetadataType](sdk-for-android-explore-api-reference-latestmetadatatype "enum class in com.here.sdk.core") getType(@NonNull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) key)

    Determines the type of a metadata value. If the type of a metadata value associated with a key is not known, this method will enable the type to be queried, in order to know which get method to call. i.e. getDouble(), getInteger() etc.
Parameters:
    `key` -

    The name of the key for which to obtain the type.

    Returns:
    An enumeration describing the type of the value associated with the key.

### removeValue

public void removeValue(@NonNull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) key)

    Removes a metadata key and its associated value.
Parameters:
    `key` -

    The name of the key to be removed.

### setCustomValue

public void setCustomValue(@NonNull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) key, @NonNull [CustomMetadataValue](sdk-for-android-explore-api-reference-latestcustommetadatavalue "interface in com.here.sdk.core") value)

    Creates a key:value pair, where the value is a type derived from CustomMetadataValue. If the given key already exists, its value will be replaced by the new one.
Parameters:
    `key` -

    The name of the key to be created or replaced.

    `value` -

    The value to be assigned to the key.

### setDouble

public void setDouble(@NonNull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) key, double value)

    Creates a key:value pair, where the value is of type Double. If the given key already exists, its value will be replaced by the new one.
Parameters:
    `key` -

    The name of the key to be created or replaced.

    `value` -

    The value to be assigned to the key.

### setGeoCoordinates

public void setGeoCoordinates(@NonNull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) key, @NonNull [GeoCoordinates](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core") value)

    Creates a key:value pair, where the value is of type GeoCoordinates. If the given key already exists, its value will be replaced by the new one.
Parameters:
    `key` -

    The name of the key to be created or replaced.

    `value` -

    The value to be assigned to the key.

### setInteger

public void setInteger(@NonNull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) key, int value)

    Creates a key:value pair, where the value is of type Integer. If the given key already exists, its value will be replaced by the new one.
Parameters:
    `key` -

    The name of the key to be created or replaced.

    `value` -

    The value to be assigned to the key.

### setString

public void setString(@NonNull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) key, @NonNull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) value)

    Creates a key:value pair, where the value is of type String. If the given key already exists, its value will be replaced by the new one.
Parameters:
    `key` -

    The name of the key to be created or replaced.

    `value` -

    The value to be assigned to the key.
