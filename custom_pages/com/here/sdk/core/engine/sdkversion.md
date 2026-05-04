---
title: "SDKVersion (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestsdkversion"
hidden: false
---

Package [com.here.sdk.core.engine](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class SDKVersion

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.core.engine.SDKVersion
------------------------------------------------------------------------
public final class SDKVersion extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
The `SDKVersion` represents version information for an SDK product. It encapsulates various attributes related to the version, including product variant, version details and backend configuration. Please note, `sdk.core.engine.SDKBuildInformation` can be used to get `SDKVersion`.

## Field Summary

Fields

Modifier and Type

  Field

  Description

  [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [backendConfig](#backendConfig)

Backend config

[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [productVariant](#productVariant)

Product variant.

`int`

  [versionBuild](#versionBuild)

Build number.

`int`

  [versionGeneration](#versionGeneration)

Generation number.

`int`

  [versionMajor](#versionMajor)

Major version number.

`int`

  [versionMinor](#versionMinor)

Minor version number.

[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [versionName](#versionName)

Version information as string.

`int`

  [versionPatch](#versionPatch)

Patch number.

[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [versionTag](#versionTag)

Version tag.

## Constructor Summary

Constructors

Constructor

  Description

  [SDKVersion](#%3Cinit%3E(java.lang.String,java.lang.String,int,int,int,int,int,java.lang.String,java.lang.String))`(`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` productVariant, `[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` versionName, int versionGeneration, int versionMajor, int versionMinor, int versionPatch, int versionBuild, `[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` versionTag, `[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` backendConfig)`

Creates a new SDK version instance from the provided parameter values.

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

### productVariant

@NonNull public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) productVariant

    Product variant.

### versionName

@NonNull public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) versionName

    Version information as string.

### versionGeneration

public int versionGeneration

    Generation number.

### versionMajor

public int versionMajor

    Major version number.

### versionMinor

public int versionMinor

    Minor version number.

### versionPatch

public int versionPatch

    Patch number.

### versionBuild

public int versionBuild

    Build number.

### versionTag

@NonNull public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) versionTag

    Version tag.

### backendConfig

@NonNull public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) backendConfig

    Backend config

## Constructor Details

  - (java.lang.String,java.lang.String,int,int,int,int,int,java.lang.String,java.lang.String)" class="section detail">

### SDKVersion

public SDKVersion(@NonNull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) productVariant, @NonNull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) versionName, int versionGeneration, int versionMajor, int versionMinor, int versionPatch, int versionBuild, @NonNull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) versionTag, @NonNull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) backendConfig)

    Creates a new SDK version instance from the provided parameter values.
Parameters:
    `productVariant` -

    Product variant.

    `versionName` -

    Version information as string.

    `versionGeneration` -

    Generation number.

    `versionMajor` -

    Major version number.

    `versionMinor` -

    Minor version number.

    `versionPatch` -

    Patch number.

    `versionBuild` -

    Build number.

    `versionTag` -

    Version tag.

    `backendConfig` -

    Backend config

## Method Details

### equals

public boolean equals([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) obj)
Overrides:
    [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

### hashCode

public int hashCode()
Overrides:
    [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
