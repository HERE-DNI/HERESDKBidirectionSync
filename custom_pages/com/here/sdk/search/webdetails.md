---
title: "WebDetails (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestwebdetails"
hidden: false
---

Package [com.here.sdk.search](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class WebDetails

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.search.WebDetails
------------------------------------------------------------------------
public final class WebDetails extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Contains information about images, editorials, rating and a urls to them.

## Field Summary

Fields

Modifier and Type

  Field

  Description

  [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`WebEditorial`](sdk-for-android-explore-api-reference-latestwebeditorial "class in com.here.sdk.search")`>`

  [editorials](#editorials)

The list of editorials associated with the place.

[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`WebImage`](sdk-for-android-explore-api-reference-latestwebimage "class in com.here.sdk.search")`>`

  [images](#images)

The list of images associated with the place.

[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`WebRating`](sdk-for-android-explore-api-reference-latestwebrating "class in com.here.sdk.search")`>`

  [ratings](#ratings)

The list of ratings associated with the place.

## Constructor Summary

Constructors

Constructor

  Description

  [WebDetails](#%3Cinit%3E())`()`

Creates a new instance.

## Method Summary

  All Methods
  Instance Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  `boolean`

  [equals](#equals(java.lang.Object))`(`[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)` obj)`

  `int`

  [hashCode](#hashCode())`()`

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Field Details

### images

@NonNull public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[WebImage](sdk-for-android-explore-api-reference-latestwebimage "class in com.here.sdk.search")\> images

    The list of images associated with the place. The images are provided by external suppliers and are only available to users with valid contracts with said suppliers. If the user has no such contracts, the list is empty.

### editorials

@NonNull public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[WebEditorial](sdk-for-android-explore-api-reference-latestwebeditorial "class in com.here.sdk.search")\> editorials

    The list of editorials associated with the place. The editorials are provided by external suppliers and are only available to users with valid contracts with said suppliers. If the user has no such contracts, the list is empty.

### ratings

@NonNull public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[WebRating](sdk-for-android-explore-api-reference-latestwebrating "class in com.here.sdk.search")\> ratings

    The list of ratings associated with the place. The ratings are provided by external suppliers and are only available to users with valid contracts with said suppliers. If the user has no such contracts, the list is empty.

## Constructor Details

  - ()" class="section detail">

### WebDetails

public WebDetails()

    Creates a new instance.

## Method Details

### equals

public boolean equals([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) obj)
Overrides:
    [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

### hashCode

public int hashCode()
Overrides:
    [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
