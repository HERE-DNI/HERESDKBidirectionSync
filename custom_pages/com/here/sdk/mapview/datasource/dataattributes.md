---
title: "DataAttributes (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestdataattributes"
hidden: false
---

Package [com.here.sdk.mapview.datasource](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class DataAttributes

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.here.NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
com.here.sdk.mapview.datasource.DataAttributes
All Implemented Interfaces:
[`DataAttributesBase`](sdk-for-android-explore-api-reference-latestdataattributesbase "interface in com.here.sdk.mapview.datasource")

------------------------------------------------------------------------
public final class DataAttributes extends [NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here") implements [DataAttributesBase](sdk-for-android-explore-api-reference-latestdataattributesbase "interface in com.here.sdk.mapview.datasource")
Data attributes collection.

Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

## Method Summary

  All Methods
  Instance Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [getAsString](#getAsString(java.lang.String))`(`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` name)`

Gets the value of an attribute as a string or `null` if it is not contained.

[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`>`

  [getAttributeNames](#getAttributeNames())`()`

Returns a list of attribute names.

[Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html)

  [getBoolean](#getBoolean(java.lang.String))`(`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` name)`

Gets the value of a boolean attribute or `null` if it is not contained or the type doesn't match.

[Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html)

  [getDouble](#getDouble(java.lang.String))`(`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` name)`

Gets the value of a double precision floating decimal attribute or `null` if it is not contained or the type doesn't match.

[Float](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Float.html)

  [getFloat](#getFloat(java.lang.String))`(`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` name)`

Gets the value of a single precision floating decimal attribute or `null` if it is not contained or the type doesn't match.

[Long](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Long.html)

  [getInt64](#getInt64(java.lang.String))`(`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` name)`

Gets the value of a 64-bits integer attribute or `null` if it is not contained or the type doesn't match.

[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [getString](#getString(java.lang.String))`(`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` name)`

Gets the value of a string attribute or `null` if it is not contained or the type doesn't match.

[`DataAttributeValue`](sdk-for-android-explore-api-reference-latestdataattributevalue "class in com.here.sdk.mapview.datasource")

  [getValue](#getValue(java.lang.String))`(`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` name)`

Gets the DataAttributeValue or `null` if it is not contained.

[`DataAttributeValue.ValueType`](sdk-for-android-explore-api-reference-latestdataattributevalue-valuetype "enum class in com.here.sdk.mapview.datasource")

  [getValueType](#getValueType(java.lang.String))`(`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` name)`

Returns the value type of an attribute or `null` if it is not contained.

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Method Details

### getAttributeNames

@NonNull public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)\> getAttributeNames()

    Returns a list of attribute names.
Specified by:
    [`getAttributeNames`](sdk-for-android-explore-api-reference-latestdataattributesbase#getAttributeNames()) in interface [`DataAttributesBase`](sdk-for-android-explore-api-reference-latestdataattributesbase "interface in com.here.sdk.mapview.datasource")

    Returns:
    The list of attribute names.

### getValueType

@Nullable public [DataAttributeValue.ValueType](sdk-for-android-explore-api-reference-latestdataattributevalue-valuetype "enum class in com.here.sdk.mapview.datasource") getValueType(@NonNull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)

    Returns the value type of an attribute or `null` if it is not contained.
Specified by:
    [`getValueType`](sdk-for-android-explore-api-reference-latestdataattributesbase#getValueType(java.lang.String)) in interface [`DataAttributesBase`](sdk-for-android-explore-api-reference-latestdataattributesbase "interface in com.here.sdk.mapview.datasource")

    Parameters:
    `name` -

    Attribute name.

    Returns:
    Attribute value type or `null` if it is not contained.

### getAsString

@Nullable public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getAsString(@NonNull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)

    Gets the value of an attribute as a string or `null` if it is not contained.
Specified by:
    [`getAsString`](sdk-for-android-explore-api-reference-latestdataattributesbase#getAsString(java.lang.String)) in interface [`DataAttributesBase`](sdk-for-android-explore-api-reference-latestdataattributesbase "interface in com.here.sdk.mapview.datasource")

    Parameters:
    `name` -

    Attribute name.

    Returns:
    Attribute value.

### getString

@Nullable public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getString(@NonNull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)

    Gets the value of a string attribute or `null` if it is not contained or the type doesn't match.
Specified by:
    [`getString`](sdk-for-android-explore-api-reference-latestdataattributesbase#getString(java.lang.String)) in interface [`DataAttributesBase`](sdk-for-android-explore-api-reference-latestdataattributesbase "interface in com.here.sdk.mapview.datasource")

    Parameters:
    `name` -

    Attribute name.

    Returns:
    Attribute value.

### getInt64

@Nullable public [Long](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Long.html) getInt64(@NonNull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)

    Gets the value of a 64-bits integer attribute or `null` if it is not contained or the type doesn't match.
Specified by:
    [`getInt64`](sdk-for-android-explore-api-reference-latestdataattributesbase#getInt64(java.lang.String)) in interface [`DataAttributesBase`](sdk-for-android-explore-api-reference-latestdataattributesbase "interface in com.here.sdk.mapview.datasource")

    Parameters:
    `name` -

    Attribute name.

    Returns:
    Attribute value.

### getFloat

@Nullable public [Float](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Float.html) getFloat(@NonNull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)

    Gets the value of a single precision floating decimal attribute or `null` if it is not contained or the type doesn't match.
Specified by:
    [`getFloat`](sdk-for-android-explore-api-reference-latestdataattributesbase#getFloat(java.lang.String)) in interface [`DataAttributesBase`](sdk-for-android-explore-api-reference-latestdataattributesbase "interface in com.here.sdk.mapview.datasource")

    Parameters:
    `name` -

    Attribute name.

    Returns:
    Attribute value.

### getDouble

@Nullable public [Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html) getDouble(@NonNull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)

    Gets the value of a double precision floating decimal attribute or `null` if it is not contained or the type doesn't match.
Specified by:
    [`getDouble`](sdk-for-android-explore-api-reference-latestdataattributesbase#getDouble(java.lang.String)) in interface [`DataAttributesBase`](sdk-for-android-explore-api-reference-latestdataattributesbase "interface in com.here.sdk.mapview.datasource")

    Parameters:
    `name` -

    Attribute name.

    Returns:
    Attribute value.

### getBoolean

@Nullable public [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html) getBoolean(@NonNull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)

    Gets the value of a boolean attribute or `null` if it is not contained or the type doesn't match.
Specified by:
    [`getBoolean`](sdk-for-android-explore-api-reference-latestdataattributesbase#getBoolean(java.lang.String)) in interface [`DataAttributesBase`](sdk-for-android-explore-api-reference-latestdataattributesbase "interface in com.here.sdk.mapview.datasource")

    Parameters:
    `name` -

    Attribute name.

    Returns:
    Attribute value.

### getValue

@Nullable public [DataAttributeValue](sdk-for-android-explore-api-reference-latestdataattributevalue "class in com.here.sdk.mapview.datasource") getValue(@NonNull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)

    Gets the DataAttributeValue or `null` if it is not contained.
Specified by:
    [`getValue`](sdk-for-android-explore-api-reference-latestdataattributesbase#getValue(java.lang.String)) in interface [`DataAttributesBase`](sdk-for-android-explore-api-reference-latestdataattributesbase "interface in com.here.sdk.mapview.datasource")

    Parameters:
    `name` -

    Attribute name.

    Returns:
    Attribute value.
