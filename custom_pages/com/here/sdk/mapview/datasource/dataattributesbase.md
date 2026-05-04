---
title: "DataAttributesBase (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestdataattributesbase"
hidden: false
---

Package [com.here.sdk.mapview.datasource](sdk-for-android-explore-api-reference-latestpackage-summary)

# Interface DataAttributesBase

All Known Implementing Classes:
[`DataAttributes`](sdk-for-android-explore-api-reference-latestdataattributes "class in com.here.sdk.mapview.datasource"), [`DataAttributesAccessor`](sdk-for-android-explore-api-reference-latestdataattributesaccessor "class in com.here.sdk.mapview.datasource")

------------------------------------------------------------------------
public interface DataAttributesBase
Interface for a collection of data attributes.

Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

## Method Summary

  All Methods
  Instance Methods
  Abstract Methods

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

## Method Details

### getAttributeNames

@NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)\> getAttributeNames()

    Returns a list of attribute names.
Returns:
    The list of attribute names.

### getValueType

@Nullable [DataAttributeValue.ValueType](sdk-for-android-explore-api-reference-latestdataattributevalue-valuetype "enum class in com.here.sdk.mapview.datasource") getValueType(@NonNull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)

    Returns the value type of an attribute or `null` if it is not contained.
Parameters:
    `name` -

    Attribute name.

    Returns:
    Attribute value type or `null` if it is not contained.

### getAsString

@Nullable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getAsString(@NonNull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)

    Gets the value of an attribute as a string or `null` if it is not contained.
Parameters:
    `name` -

    Attribute name.

    Returns:
    Attribute value.

### getString

@Nullable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getString(@NonNull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)

    Gets the value of a string attribute or `null` if it is not contained or the type doesn't match.
Parameters:
    `name` -

    Attribute name.

    Returns:
    Attribute value.

### getInt64

@Nullable [Long](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Long.html) getInt64(@NonNull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)

    Gets the value of a 64-bits integer attribute or `null` if it is not contained or the type doesn't match.
Parameters:
    `name` -

    Attribute name.

    Returns:
    Attribute value.

### getFloat

@Nullable [Float](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Float.html) getFloat(@NonNull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)

    Gets the value of a single precision floating decimal attribute or `null` if it is not contained or the type doesn't match.
Parameters:
    `name` -

    Attribute name.

    Returns:
    Attribute value.

### getDouble

@Nullable [Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html) getDouble(@NonNull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)

    Gets the value of a double precision floating decimal attribute or `null` if it is not contained or the type doesn't match.
Parameters:
    `name` -

    Attribute name.

    Returns:
    Attribute value.

### getBoolean

@Nullable [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html) getBoolean(@NonNull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)

    Gets the value of a boolean attribute or `null` if it is not contained or the type doesn't match.
Parameters:
    `name` -

    Attribute name.

    Returns:
    Attribute value.

### getValue

@Nullable [DataAttributeValue](sdk-for-android-explore-api-reference-latestdataattributevalue "class in com.here.sdk.mapview.datasource") getValue(@NonNull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)

    Gets the DataAttributeValue or `null` if it is not contained.
Parameters:
    `name` -

    Attribute name.

    Returns:
    Attribute value.
