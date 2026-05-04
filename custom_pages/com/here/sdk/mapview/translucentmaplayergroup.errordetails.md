---
title: "TranslucentMapLayerGroup.ErrorDetails (API Reference)"
slug: "sdk-for-android-explore-api-reference-latesttranslucentmaplayergroup-errordetails"
hidden: false
---

Package [com.here.sdk.mapview](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class TranslucentMapLayerGroup.ErrorDetails

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.mapview.TranslucentMapLayerGroup.ErrorDetails
Enclosing class:
[TranslucentMapLayerGroup](sdk-for-android-explore-api-reference-latesttranslucentmaplayergroup "class in com.here.sdk.mapview")

------------------------------------------------------------------------
public static final class TranslucentMapLayerGroup.ErrorDetails extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Describes the reason for failing to create the group.

## Field Summary

Fields

Modifier and Type

  Field

  Description

  [`TranslucentMapLayerGroup.ErrorCode`](sdk-for-android-explore-api-reference-latesttranslucentmaplayergroup-errorcode "enum class in com.here.sdk.mapview")

  [errorCode](#errorCode)

The error code.

[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [errorDescription](#errorDescription)

A description of the error, if available.

## Constructor Summary

Constructors

Constructor

  Description

  [ErrorDetails](#%3Cinit%3E(com.here.sdk.mapview.TranslucentMapLayerGroup.ErrorCode,java.lang.String))`(`[`TranslucentMapLayerGroup.ErrorCode`](sdk-for-android-explore-api-reference-latesttranslucentmaplayergroup-errorcode "enum class in com.here.sdk.mapview")` errorCode, `[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` errorDescription)`

Creates a new instance.

## Method Summary

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Field Details

### errorCode

@NonNull public [TranslucentMapLayerGroup.ErrorCode](sdk-for-android-explore-api-reference-latesttranslucentmaplayergroup-errorcode "enum class in com.here.sdk.mapview") errorCode

    The error code.

### errorDescription

@Nullable public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) errorDescription

    A description of the error, if available.

## Constructor Details

  - (com.here.sdk.mapview.TranslucentMapLayerGroup.ErrorCode,java.lang.String)" class="section detail">

### ErrorDetails

public ErrorDetails(@NonNull [TranslucentMapLayerGroup.ErrorCode](sdk-for-android-explore-api-reference-latesttranslucentmaplayergroup-errorcode "enum class in com.here.sdk.mapview") errorCode, @Nullable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) errorDescription)

    Creates a new instance.
Parameters:
    `errorCode` -

    The error code.

    `errorDescription` -

    A description of the error, if available.
