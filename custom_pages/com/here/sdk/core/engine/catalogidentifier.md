---
title: "CatalogIdentifier (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestcatalogidentifier"
hidden: false
---

Package [com.here.sdk.core.engine](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class CatalogIdentifier

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.core.engine.CatalogIdentifier
------------------------------------------------------------------------
public final class CatalogIdentifier extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
This class is used to identify any catalog in the HERE platform.

A catalog is a storage-representation to store map data on the HERE platform. The data inside a catalog is divided into layers, where each layer consists of datasets with similar functional attributes in the physical world. For example, there can be a layer for road-topology, a layer for road-attributes (such as speed limits) and a layer for places and business addresses. All these layers, in different geographic regions, can be grouped together into a catalog to create a representation of the world we live in, called HERE map. It can be also used to render a `MapView`. Each geographic region is cut into geospatial tiles for efficient search, map display, routing, map matching, and driver warnings. Each tile partitions the map data (in one or more layers, depending on the product) in the geolocation of that specific tile. The data inside a catalog is logically managed and access controlled as a single set. If you have any data that you want to bring to the HERE platform, you need a catalog to contain it. For additional information about catalogs, and related concepts of data representation on the HERE platform, refer to [the Data API](https://www.here.com/docs/bundle/data-api-developer-guide/page/rest/catalogs.html) and [Introduction to Mapping Concepts](https://www.here.com/docs/bundle/introduction-to-mapping-concepts-user-guide/page/topics/maps-layers-tiles.html)

## Field Summary

Fields

Modifier and Type

  Field

  Description

  [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [hrn](#hrn)

A HERE Resource Name (HRN) for this catalog.

[Long](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Long.html)

  [version](#version)

A version number for a catalog.

## Constructor Summary

Constructors

Constructor

  Description

  [CatalogIdentifier](#%3Cinit%3E())`()`

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

### hrn

@NonNull public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) hrn

    A HERE Resource Name (HRN) for this catalog. This is a unique string returned by the HERE platform when you add a new catalog to your project. For information about catalog creation process refer to [the Data API](https://www.here.com/docs/bundle/data-api-developer-guide/page/rest/creating-a-catalog.html) By default, this field points to a default catalog on HERE platform, which contains data for the whole world excluding the region of Japan. Use [`CatalogConfiguration.getDefault(com.here.sdk.core.engine.CatalogType)`](sdk-for-android-explore-api-reference-latestcatalogconfiguration#getDefault(com.here.sdk.core.engine.CatalogType)) to get the default HRN value for use with the HERE platform.

### version

@Nullable public [Long](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Long.html) version

    A version number for a catalog. When accessing a catalog, this version must be specified. Set `null` to automatically get the latest version for a catalog. The field defaults to `null`. Since the data inside a catalog can be updated, each published modification needs to correlate to a specific version number. Note: when `CatalogIdentifier` created with [`DesiredCatalog`](sdk-for-android-explore-api-reference-latestdesiredcatalog "class in com.here.sdk.core.engine") then:

    - numerical `-1` corresponds to [`CatalogVersionHint.latest(boolean)`](sdk-for-android-explore-api-reference-latestcatalogversionhint#latest(boolean)) with `ignoreCachedData` set to `true`;
    - `null` corresponds to [`CatalogVersionHint.latest(boolean)`](sdk-for-android-explore-api-reference-latestcatalogversionhint#latest(boolean)) with `ignoreCachedData` set to `false`;
    - other numerical values correspond to `version` passed to [`CatalogVersionHint.specific(long)`](sdk-for-android-explore-api-reference-latestcatalogversionhint#specific(long)).

## Constructor Details

  - ()" class="section detail">

### CatalogIdentifier

public CatalogIdentifier()

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
