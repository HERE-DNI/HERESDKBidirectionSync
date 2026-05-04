---
title: "DesiredCatalog (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestdesiredcatalog"
hidden: false
---

Package [com.here.sdk.core.engine](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class DesiredCatalog

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.core.engine.DesiredCatalog
------------------------------------------------------------------------
public final class DesiredCatalog extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
This class provides an interface to the user, to identify a catalog on the HERE platform, whose data he wants to access. The user can specify the HERE Resource Name (HRN) for the catalog along with a hint for the desired version. If the desired version is not available, the HERE platform will determine the best version to use for a specific catalog or result in error logs. For information on how to specify the catalog version, see [`CatalogVersionHint`](sdk-for-android-explore-api-reference-latestcatalogversionhint "class in com.here.sdk.core.engine"). For information about catalogs and related concepts see [`CatalogIdentifier`](sdk-for-android-explore-api-reference-latestcatalogidentifier "class in com.here.sdk.core.engine").

## Field Summary

Fields

Modifier and Type

  Field

  Description

  [`CatalogIdentifier`](sdk-for-android-explore-api-reference-latestcatalogidentifier "class in com.here.sdk.core.engine")

  [id](#id)

The identifier for the catalog to be accessed on the HERE platform.

## Constructor Summary

Constructors

Constructor

  Description

  [DesiredCatalog](#%3Cinit%3E(java.lang.String,com.here.sdk.core.engine.CatalogVersionHint))`(`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` hrn, `[`CatalogVersionHint`](sdk-for-android-explore-api-reference-latestcatalogversionhint "class in com.here.sdk.core.engine")` version)`

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

### id

@NonNull public [CatalogIdentifier](sdk-for-android-explore-api-reference-latestcatalogidentifier "class in com.here.sdk.core.engine") id

    The identifier for the catalog to be accessed on the HERE platform. See [`CatalogIdentifier`](sdk-for-android-explore-api-reference-latestcatalogidentifier "class in com.here.sdk.core.engine").

## Constructor Details

  - (java.lang.String,com.here.sdk.core.engine.CatalogVersionHint)" class="section detail">

### DesiredCatalog

public DesiredCatalog(@NonNull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) hrn, @NonNull [CatalogVersionHint](sdk-for-android-explore-api-reference-latestcatalogversionhint "class in com.here.sdk.core.engine") version)

    Creates a new instance.
Parameters:
    `hrn` -

    A HERE Resource Name (HRN) for this catalog. This is a unique string returned by the HERE platform when you add a new catalog to your project. For more information, see [`CatalogIdentifier.hrn`](sdk-for-android-explore-api-reference-latestcatalogidentifier#hrn)

    `version` -

    The version to use for this Catalog's data. You should use either [`CatalogVersionHint.specific(long)`](sdk-for-android-explore-api-reference-latestcatalogversionhint#specific(long)) to specify a specific version of the catalog or [`CatalogVersionHint.latest(boolean)`](sdk-for-android-explore-api-reference-latestcatalogversionhint#latest(boolean)) to access the latest version of the catalog available on the HERE platform. Based on the value in this field, the HERE platform will determine the best version to use for this catalog or result in error logs if the desired version is not available.

## Method Details

### equals

public boolean equals([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) obj)
Overrides:
    [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

### hashCode

public int hashCode()
Overrides:
    [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
