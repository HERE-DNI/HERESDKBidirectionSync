---
title: "SDKOptions.ActionOnCacheLock (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestsdkoptions-actiononcachelock"
hidden: false
---

Package [com.here.sdk.core.engine](sdk-for-android-explore-api-reference-latestpackage-summary)

# Enum Class SDKOptions.ActionOnCacheLock

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[java.lang.Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)\<[SDKOptions.ActionOnCacheLock](sdk-for-android-explore-api-reference-latestsdkoptions-actiononcachelock "enum class in com.here.sdk.core.engine")\>
com.here.sdk.core.engine.SDKOptions.ActionOnCacheLock
All Implemented Interfaces:
[Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html), [Comparable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html)`<`[`SDKOptions.ActionOnCacheLock`](sdk-for-android-explore-api-reference-latestsdkoptions-actiononcachelock "enum class in com.here.sdk.core.engine")`>`, [Constable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/constant/Constable.html)

<!-- -->

Enclosing class:
[SDKOptions](sdk-for-android-explore-api-reference-latestsdkoptions "class in com.here.sdk.core.engine")

------------------------------------------------------------------------
public static enum SDKOptions.ActionOnCacheLock extends [Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)\<[SDKOptions.ActionOnCacheLock](sdk-for-android-explore-api-reference-latestsdkoptions-actiononcachelock "enum class in com.here.sdk.core.engine")\>
Action on cache lock

## Nested Class Summary

## Nested classes/interfaces inherited from class java.lang.[Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)

  [Enum.EnumDesc](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html)`<`[E](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html)` extends `[Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)`<`[E](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html)`>>`

## Enum Constant Summary

Enum Constants

Enum Constant

  Description

  [KILL_LOCKING_APP](#KILL_LOCKING_APP)

The HERE SDK will make several attempts to kill the locking process for a maximum period of 500 milliseconds.

[NO_ACTION](#NO_ACTION)

No action is performed.

[WAIT_LOCKING_APP_FINISH](#WAIT_LOCKING_APP_FINISH)

Current process waits 500 milliseconds for the cache to be unlocked.

## Method Summary

  All Methods
  Static Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  `static `[`SDKOptions.ActionOnCacheLock`](sdk-for-android-explore-api-reference-latestsdkoptions-actiononcachelock "enum class in com.here.sdk.core.engine")

  [valueOf](#valueOf(java.lang.String))`(`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` name)`

Returns the enum constant of this class with the specified name.

`static `[`SDKOptions.ActionOnCacheLock`](sdk-for-android-explore-api-reference-latestsdkoptions-actiononcachelock "enum class in com.here.sdk.core.engine")`[]`

  [values](#values())`()`

Returns an array containing the constants of this enum class, in the order they are declared.

### Methods inherited from class java.lang.[Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#clone()), [compareTo](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#compareTo(E)), [describeConstable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#describeConstable()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#finalize()), [getDeclaringClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#getDeclaringClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#hashCode()), [name](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#name()), [ordinal](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#ordinal()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#toString()), [valueOf](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#valueOf(java.lang.Class,java.lang.String))

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Enum Constant Details

### NO_ACTION

public static final [SDKOptions.ActionOnCacheLock](sdk-for-android-explore-api-reference-latestsdkoptions-actiononcachelock "enum class in com.here.sdk.core.engine") NO_ACTION

    No action is performed.

### WAIT_LOCKING_APP_FINISH

public static final [SDKOptions.ActionOnCacheLock](sdk-for-android-explore-api-reference-latestsdkoptions-actiononcachelock "enum class in com.here.sdk.core.engine") WAIT_LOCKING_APP_FINISH

    Current process waits 500 milliseconds for the cache to be unlocked.

### KILL_LOCKING_APP

public static final [SDKOptions.ActionOnCacheLock](sdk-for-android-explore-api-reference-latestsdkoptions-actiononcachelock "enum class in com.here.sdk.core.engine") KILL_LOCKING_APP

    The HERE SDK will make several attempts to kill the locking process for a maximum period of 500 milliseconds.

## Method Details

### values

public static [SDKOptions.ActionOnCacheLock](sdk-for-android-explore-api-reference-latestsdkoptions-actiononcachelock "enum class in com.here.sdk.core.engine")\[\] values()

    Returns an array containing the constants of this enum class, in the order they are declared.
Returns:
    an array containing the constants of this enum class, in the order they are declared

### valueOf

public static [SDKOptions.ActionOnCacheLock](sdk-for-android-explore-api-reference-latestsdkoptions-actiononcachelock "enum class in com.here.sdk.core.engine") valueOf([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)

    Returns the enum constant of this class with the specified name. The string must match *exactly* an identifier used to declare an enum constant in this class. (Extraneous whitespace characters are not permitted.)
Parameters:
    `name` - the name of the enum constant to be returned.

    Returns:
    the enum constant with the specified name

    Throws:
    [IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html) - if this enum class has no constant with the specified name

    [NullPointerException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/NullPointerException.html) - if the argument is null
