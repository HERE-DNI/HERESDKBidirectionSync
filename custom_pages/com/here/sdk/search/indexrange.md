---
title: "IndexRange (API Reference)"
slug: "android-sdk-apirange"
hidden: false
---

Package [com.here.sdk.search](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class IndexRange

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.here.NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
com.here.sdk.search.IndexRange
------------------------------------------------------------------------
public final class IndexRange extends [NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
Holds information to which part of the text, input query was matched. The first character is denoted by a value of 0.

## Method Summary

  All Methods
  Instance Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  `int`

  [getEnd](#getEnd())`()`

Gets the position indicating the end of the highlighted part, exclusive.

`int`

  [getStart](#getStart())`()`

Gets the position of the first character that matches a query.

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Method Details

### getStart

public int getStart()

    Gets the position of the first character that matches a query.
Returns:
    Position of the first character that matches a query.

### getEnd

public int getEnd()

    Gets the position indicating the end of the highlighted part, exclusive.
Returns:
    Position indicating the end of the highlighted part, exclusive.
