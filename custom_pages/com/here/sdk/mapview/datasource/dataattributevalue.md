---
title: "DataAttributeValue (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestdataattributevalue"
hidden: false
---

Package [com.here.sdk.mapview.datasource](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class DataAttributeValue

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.here.NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
com.here.sdk.mapview.datasource.DataAttributeValue
------------------------------------------------------------------------
public final class DataAttributeValue extends [NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
Encapsulates a data attribute value. Supports basic types and arrays of basic types.

Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

## Nested Class Summary

Nested Classes

Modifier and Type

  Class

  Description

  `static enum `

  [DataAttributeValue.ValueType](sdk-for-android-explore-api-reference-latestdataattributevalue-valuetype)

Supported types of the data attribute values.

## Constructor Summary

Constructors

Constructor

  Description

  [DataAttributeValue](#%3Cinit%3E(boolean))`(boolean value)`

Creates a boolean data attribute value.

[DataAttributeValue](#%3Cinit%3E(double))`(double value)`

Creates a double precision floating decimal data attribute value.

[DataAttributeValue](#%3Cinit%3E(float))`(float value)`

Creates a single precision floating decimal data attribute value.

[DataAttributeValue](#%3Cinit%3E(long))`(long value)`

Creates a 64-bit integer data attribute value.

[DataAttributeValue](#%3Cinit%3E(java.lang.String))`(`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` value)`

Creates a string data attribute value.

[DataAttributeValue](#%3Cinit%3E(java.util.List))`(`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`DataAttributeValue`](sdk-for-android-explore-api-reference-latestdataattributevalue "class in com.here.sdk.mapview.datasource")`> value)`

Creates an aggregated data attribute value.

## Method Summary

  All Methods
  Instance Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`DataAttributeValue`](sdk-for-android-explore-api-reference-latestdataattributevalue "class in com.here.sdk.mapview.datasource")`>`

  [getArray](#getArray())`()`

Gets the array value or `null` if the type doesn't match.

[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [getAsString](#getAsString())`()`

Returns a string representation of the contained value.

[Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html)

  [getBoolean](#getBoolean())`()`

Gets the boolean value or `null` if the type doesn't match.

[Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html)

  [getDouble](#getDouble())`()`

Gets the double precision floating decimal value or `null` if the type doesn't match.

[Float](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Float.html)

  [getFloat](#getFloat())`()`

Gets the single precision floating decimal value or `null` if the type doesn't match.

[Long](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Long.html)

  [getInt64](#getInt64())`()`

Gets 64-bits integer value or `null` if the type doesn't match.

[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [getString](#getString())`()`

Gets the string value or `null` if the type doesn't match.

[`DataAttributeValue.ValueType`](sdk-for-android-explore-api-reference-latestdataattributevalue-valuetype "enum class in com.here.sdk.mapview.datasource")

  [getType](#getType())`()`

Returns the type of the value.

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Constructor Details

  - (java.lang.String)" class="section detail">

### DataAttributeValue

public DataAttributeValue(@NonNull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) value)

    Creates a string data attribute value.
Parameters:
    `value` -

    Attribute value.
- (long)" class="section detail">

### DataAttributeValue

public DataAttributeValue(long value)

    Creates a 64-bit integer data attribute value.
Parameters:
    `value` -

    Attribute value.
- (float)" class="section detail">

### DataAttributeValue

public DataAttributeValue(float value)

    Creates a single precision floating decimal data attribute value.
Parameters:
    `value` -

    Attribute value.
- (double)" class="section detail">

### DataAttributeValue

public DataAttributeValue(double value)

    Creates a double precision floating decimal data attribute value.
Parameters:
    `value` -

    Attribute value.
- (boolean)" class="section detail">

### DataAttributeValue

public DataAttributeValue(boolean value)

    Creates a boolean data attribute value.
Parameters:
    `value` -

    Attribute value.
- (java.util.List)" class="section detail">

### DataAttributeValue

public DataAttributeValue(@NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[DataAttributeValue](sdk-for-android-explore-api-reference-latestdataattributevalue "class in com.here.sdk.mapview.datasource")\> value)

    Creates an aggregated data attribute value.
Parameters:
    `value` -

    Attribute value.

## Method Details

### getType

@NonNull public [DataAttributeValue.ValueType](sdk-for-android-explore-api-reference-latestdataattributevalue-valuetype "enum class in com.here.sdk.mapview.datasource") getType()

    Returns the type of the value.
Returns:
    The type of the value.

### getString

@Nullable public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getString()

    Gets the string value or `null` if the type doesn't match.
Returns:
    Attribute value.

### getInt64

@Nullable public [Long](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Long.html) getInt64()

    Gets 64-bits integer value or `null` if the type doesn't match.
Returns:
    Attribute value.

### getFloat

@Nullable public [Float](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Float.html) getFloat()

    Gets the single precision floating decimal value or `null` if the type doesn't match.
Returns:
    Attribute value.

### getDouble

@Nullable public [Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html) getDouble()

    Gets the double precision floating decimal value or `null` if the type doesn't match.
Returns:
    Attribute value.

### getBoolean

@Nullable public [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html) getBoolean()

    Gets the boolean value or `null` if the type doesn't match.
Returns:
    Attribute value.

### getArray

@Nullable public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[DataAttributeValue](sdk-for-android-explore-api-reference-latestdataattributevalue "class in com.here.sdk.mapview.datasource")\> getArray()

    Gets the array value or `null` if the type doesn't match.
Returns:
    Attribute value.

### getAsString

@NonNull public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getAsString()

    Returns a string representation of the contained value.
Returns:
    Attribute value.
