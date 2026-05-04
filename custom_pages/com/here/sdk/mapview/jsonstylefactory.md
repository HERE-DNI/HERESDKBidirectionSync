---
title: "JsonStyleFactory (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestjsonstylefactory"
hidden: false
---

Package [com.here.sdk.mapview](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class JsonStyleFactory

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.here.NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
com.here.sdk.mapview.JsonStyleFactory
------------------------------------------------------------------------
public final class JsonStyleFactory extends [NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
A factory of [`Style`](sdk-for-android-explore-api-reference-lateststyle "class in com.here.sdk.mapview") objects from styles defined in JSON format. For more details see Custom Layer Style Reference in the documentation.

Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

## Nested Class Summary

Nested Classes

Modifier and Type

  Class

  Description

  `static enum `

  [JsonStyleFactory.InstantiationErrorCode](sdk-for-android-explore-api-reference-latestjsonstylefactory-instantiationerrorcode)

Describes reasons for failing to create a [`Style`](sdk-for-android-explore-api-reference-lateststyle "class in com.here.sdk.mapview") from a JSON source.

`static final class `

  [JsonStyleFactory.InstantiationErrorDetails](sdk-for-android-explore-api-reference-latestjsonstylefactory-instantiationerrordetails)

Describes the reason for failing to create a [`Style`](sdk-for-android-explore-api-reference-lateststyle "class in com.here.sdk.mapview") from a JSON source.

`static final class `

  [JsonStyleFactory.InstantiationException](sdk-for-android-explore-api-reference-latestjsonstylefactory-instantiationexception)

Thrown when failing to create a [`Style`](sdk-for-android-explore-api-reference-lateststyle "class in com.here.sdk.mapview") from a JSON source.

## Method Summary

  All Methods
  Static Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  `static `[`Style`](sdk-for-android-explore-api-reference-lateststyle "class in com.here.sdk.mapview")

  [createFromString](#createFromString(java.lang.String))`(`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` styleString)`

Creates an instance of Style from a JSON string.

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Method Details

### createFromString

@NonNull public static [Style](sdk-for-android-explore-api-reference-lateststyle "class in com.here.sdk.mapview") createFromString(@NonNull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) styleString) throws [JsonStyleFactory.InstantiationException](sdk-for-android-explore-api-reference-latestjsonstylefactory-instantiationexception "class in com.here.sdk.mapview")

    Creates an instance of Style from a JSON string.
Parameters:
    `styleString` -

    JSON style string.

    Returns:
    Style instance.

    Throws:
    [`JsonStyleFactory.InstantiationException`](sdk-for-android-explore-api-reference-latestjsonstylefactory-instantiationexception "class in com.here.sdk.mapview") -

    Indicates failure to create [`Style`](sdk-for-android-explore-api-reference-lateststyle "class in com.here.sdk.mapview") from JSON string.
