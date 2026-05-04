---
title: "DataAttributesBuilder (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestdataattributesbuilder"
hidden: false
---

Package [com.here.sdk.mapview.datasource](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class DataAttributesBuilder

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.here.NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
com.here.sdk.mapview.datasource.DataAttributesBuilder
------------------------------------------------------------------------
public final class DataAttributesBuilder extends [NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
Data attributes collection builder.

Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

## Constructor Summary

Constructors

Constructor

  Description

  [DataAttributesBuilder](#%3Cinit%3E())`()`

Creates a data attributes builder instance.

## Method Summary

  All Methods
  Instance Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  [`DataAttributes`](sdk-for-android-explore-api-reference-latestdataattributes "class in com.here.sdk.mapview.datasource")

  [build](#build())`()`

Builds instance of DataAttributes.

[`DataAttributesBuilder`](sdk-for-android-explore-api-reference-latestdataattributesbuilder "class in com.here.sdk.mapview.datasource")

  [with](#with(java.lang.String,boolean))`(`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` name, boolean value)`

Configures the builder to add the given attribute.

[`DataAttributesBuilder`](sdk-for-android-explore-api-reference-latestdataattributesbuilder "class in com.here.sdk.mapview.datasource")

  [with](#with(java.lang.String,double))`(`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` name, double value)`

Configures the builder to add the given attribute.

[`DataAttributesBuilder`](sdk-for-android-explore-api-reference-latestdataattributesbuilder "class in com.here.sdk.mapview.datasource")

  [with](#with(java.lang.String,float))`(`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` name, float value)`

Configures the builder to add the given attribute.

[`DataAttributesBuilder`](sdk-for-android-explore-api-reference-latestdataattributesbuilder "class in com.here.sdk.mapview.datasource")

  [with](#with(java.lang.String,long))`(`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` name, long value)`

Configures the builder to add the given attribute.

[`DataAttributesBuilder`](sdk-for-android-explore-api-reference-latestdataattributesbuilder "class in com.here.sdk.mapview.datasource")

  [with](#with(java.lang.String,com.here.sdk.mapview.datasource.DataAttributeValue))`(`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` name, `[`DataAttributeValue`](sdk-for-android-explore-api-reference-latestdataattributevalue "class in com.here.sdk.mapview.datasource")` value)`

Configures the builder to add the given attribute.

[`DataAttributesBuilder`](sdk-for-android-explore-api-reference-latestdataattributesbuilder "class in com.here.sdk.mapview.datasource")

  [with](#with(java.lang.String,java.lang.String))`(`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` name, `[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` value)`

Configures the builder to add the given attribute.

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Constructor Details

  - ()" class="section detail">

### DataAttributesBuilder

public DataAttributesBuilder()

    Creates a data attributes builder instance.

## Method Details

### with

@NonNull public [DataAttributesBuilder](sdk-for-android-explore-api-reference-latestdataattributesbuilder "class in com.here.sdk.mapview.datasource") with(@NonNull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name, @NonNull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) value)

    Configures the builder to add the given attribute.
Parameters:
    `name` -

    Attribute name.

    `value` -

    Attribute value.

    Returns:
    This data attributes builder instance.

### with

@NonNull public [DataAttributesBuilder](sdk-for-android-explore-api-reference-latestdataattributesbuilder "class in com.here.sdk.mapview.datasource") with(@NonNull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name, long value)

    Configures the builder to add the given attribute.
Parameters:
    `name` -

    Attribute name.

    `value` -

    Attribute value.

    Returns:
    This data attributes builder instance.

### with

@NonNull public [DataAttributesBuilder](sdk-for-android-explore-api-reference-latestdataattributesbuilder "class in com.here.sdk.mapview.datasource") with(@NonNull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name, float value)

    Configures the builder to add the given attribute.
Parameters:
    `name` -

    Attribute name.

    `value` -

    Attribute value.

    Returns:
    This data attributes builder instance.

### with

@NonNull public [DataAttributesBuilder](sdk-for-android-explore-api-reference-latestdataattributesbuilder "class in com.here.sdk.mapview.datasource") with(@NonNull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name, double value)

    Configures the builder to add the given attribute.
Parameters:
    `name` -

    Attribute name.

    `value` -

    Attribute value.

    Returns:
    This data attributes builder instance.

### with

@NonNull public [DataAttributesBuilder](sdk-for-android-explore-api-reference-latestdataattributesbuilder "class in com.here.sdk.mapview.datasource") with(@NonNull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name, boolean value)

    Configures the builder to add the given attribute.
Parameters:
    `name` -

    Attribute name.

    `value` -

    Attribute value.

    Returns:
    This data attributes builder instance.

### with

@NonNull public [DataAttributesBuilder](sdk-for-android-explore-api-reference-latestdataattributesbuilder "class in com.here.sdk.mapview.datasource") with(@NonNull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name, @NonNull [DataAttributeValue](sdk-for-android-explore-api-reference-latestdataattributevalue "class in com.here.sdk.mapview.datasource") value)

    Configures the builder to add the given attribute.
Parameters:
    `name` -

    Attribute name.

    `value` -

    Attribute value.

    Returns:
    This data attributes builder instance.

### build

@NonNull public [DataAttributes](sdk-for-android-explore-api-reference-latestdataattributes "class in com.here.sdk.mapview.datasource") build()

    Builds instance of DataAttributes.
Returns:
    Instance of the data attributes created with the given attributes.
