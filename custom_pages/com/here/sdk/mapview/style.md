---
title: "Style (API Reference)"
slug: "sdk-for-android-explore-api-reference-lateststyle"
hidden: false
---

Package [com.here.sdk.mapview](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class Style

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.here.NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
com.here.sdk.mapview.Style
------------------------------------------------------------------------
public final class Style extends [NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
A style that defines the visual appearance of map rendered features. A [`Style`](sdk-for-android-explore-api-reference-lateststyle "class in com.here.sdk.mapview") can be created using a [`JsonStyleFactory`](sdk-for-android-explore-api-reference-latestjsonstylefactory "class in com.here.sdk.mapview").

Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

## Method Summary

  All Methods
  Instance Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  `void`

  [update](#update(com.here.sdk.mapview.Style))`(`[`Style`](sdk-for-android-explore-api-reference-lateststyle "class in com.here.sdk.mapview")` style)`

Updates this style with content from another style.

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Method Details

### update

public void update(@NonNull [Style](sdk-for-android-explore-api-reference-lateststyle "class in com.here.sdk.mapview") style)

    Updates this style with content from another style. Only style definitions update is curently supported.
Parameters:
    `style` -

    Style used as source to update the current style.
