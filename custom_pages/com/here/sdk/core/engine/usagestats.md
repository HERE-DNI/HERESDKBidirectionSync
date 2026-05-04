---
title: "UsageStats (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestusagestats"
hidden: false
---

Package [com.here.sdk.core.engine](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class UsageStats

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.core.engine.UsageStats
------------------------------------------------------------------------
public final class UsageStats extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
A class that gathers statistics of the HERE SDK network usage for uploaded and downloaded data.

**Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

## Nested Class Summary

Nested Classes

Modifier and Type

  Class

  Description

  `static enum `

  [UsageStats.Feature](sdk-for-android-explore-api-reference-latestusagestats-feature)

Represents the feature enum associated with the gathered usage stats.

`static final class `

  [UsageStats.NetworkStats](sdk-for-android-explore-api-reference-latestusagestats-networkstats)

Provides network statistics in bytes per method.

## Field Summary

Fields

Modifier and Type

  Field

  Description

  [`UsageStats.Feature`](sdk-for-android-explore-api-reference-latestusagestats-feature "enum class in com.here.sdk.core.engine")

  [feature](#feature)

Represents the HERE SDK feature associated with the gathered usage statistics.

[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`UsageStats.NetworkStats`](sdk-for-android-explore-api-reference-latestusagestats-networkstats "class in com.here.sdk.core.engine")`>`

  [networkStats](#networkStats)

Provides network statistics.

## Constructor Summary

Constructors

Constructor

  Description

  [UsageStats](#%3Cinit%3E(java.util.List,com.here.sdk.core.engine.UsageStats.Feature))`(`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`UsageStats.NetworkStats`](sdk-for-android-explore-api-reference-latestusagestats-networkstats "class in com.here.sdk.core.engine")`> networkStats, `[`UsageStats.Feature`](sdk-for-android-explore-api-reference-latestusagestats-feature "enum class in com.here.sdk.core.engine")` feature)`

Creates a new instance.

## Method Summary

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Field Details

### networkStats

@NonNull public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[UsageStats.NetworkStats](sdk-for-android-explore-api-reference-latestusagestats-networkstats "class in com.here.sdk.core.engine")\> networkStats

    Provides network statistics.

### feature

@NonNull public [UsageStats.Feature](sdk-for-android-explore-api-reference-latestusagestats-feature "enum class in com.here.sdk.core.engine") feature

    Represents the HERE SDK feature associated with the gathered usage statistics.

## Constructor Details

  - (java.util.List,com.here.sdk.core.engine.UsageStats.Feature)" class="section detail">

### UsageStats

public UsageStats(@NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[UsageStats.NetworkStats](sdk-for-android-explore-api-reference-latestusagestats-networkstats "class in com.here.sdk.core.engine")\> networkStats, @NonNull [UsageStats.Feature](sdk-for-android-explore-api-reference-latestusagestats-feature "enum class in com.here.sdk.core.engine") feature)

    Creates a new instance.
Parameters:
    `networkStats` -

    Provides network statistics.

    `feature` -

    Represents the HERE SDK feature associated with the gathered usage statistics.
