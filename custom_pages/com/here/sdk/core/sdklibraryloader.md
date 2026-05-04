---
title: "SDKLibraryLoader (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestsdklibraryloader"
hidden: false
---

Package [com.here.sdk.core](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class SDKLibraryLoader

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.core.SDKLibraryLoader
------------------------------------------------------------------------
public final class SDKLibraryLoader extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Loads HERE SDK native libraries. Usually it's instantiated automatically during the initialisation of SDK, but can be used in client code for optimisation of launch time.

## Constructor Summary

Constructors

Constructor

  Description

  [SDKLibraryLoader](#%3Cinit%3E(java.lang.String))`(`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` functionalityName)`

Reads and loads list of libraries related to given functionality.

## Method Summary

  All Methods
  Static Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  `static `[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`[]`

  [getLibrariesToLoad](#getLibrariesToLoad(java.lang.String))`(`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` functionalityName)`

Returns list of libraries to load

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Constructor Details

  - (java.lang.String)" class="section detail">

### SDKLibraryLoader

public SDKLibraryLoader(@NonNull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) functionalityName)

    Reads and loads list of libraries related to given functionality.
Parameters:
    `functionalityName` - Functionality name. Currently "SDK" must always be passed.

## Method Details

### getLibrariesToLoad

@NonNull public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)\[\] getLibrariesToLoad(@NonNull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) functionalityName)

    Returns list of libraries to load
Parameters:
    `functionalityName` - Functionality name. Currently "SDK" must always be passed.

    Returns:
    list of libraries.
