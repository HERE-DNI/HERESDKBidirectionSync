---
title: "PostAction (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestpostaction"
hidden: false
---

Package [com.here.sdk.routing](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class PostAction

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.routing.PostAction
------------------------------------------------------------------------
public final class PostAction extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
An action that must be done after arrival, i.e. completing a section in the route.

## Field Summary

Fields

Modifier and Type

  Field

  Description

  [`PostActionType`](sdk-for-android-explore-api-reference-latestpostactiontype "enum class in com.here.sdk.routing")

  [action](#action)

Type of this action.

[`ChargingActionDetails`](sdk-for-android-explore-api-reference-latestchargingactiondetails "class in com.here.sdk.routing")

  [chargingDetails](#chargingDetails)

The additional information that is available if the action is of type charging.

[`Duration`](sdk-for-android-explore-api-reference-latestduration "class in com.here.time")

  [duration](#duration)

Estimated duration of this action.

## Constructor Summary

Constructors

Constructor

  Description

  [PostAction](#%3Cinit%3E())`()`

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

### action

@NonNull public [PostActionType](sdk-for-android-explore-api-reference-latestpostactiontype "enum class in com.here.sdk.routing") action

    Type of this action. Defaults to [`PostActionType.CHARGING_SETUP`](sdk-for-android-explore-api-reference-latestpostactiontype#CHARGING_SETUP).

### duration

@NonNull public [Duration](sdk-for-android-explore-api-reference-latestduration "class in com.here.time") duration

    Estimated duration of this action. Defaults to 0 seconds.

### chargingDetails

@Nullable public [ChargingActionDetails](sdk-for-android-explore-api-reference-latestchargingactiondetails "class in com.here.sdk.routing") chargingDetails

    The additional information that is available if the action is of type charging.

## Constructor Details

  - ()" class="section detail">

### PostAction

public PostAction()

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
