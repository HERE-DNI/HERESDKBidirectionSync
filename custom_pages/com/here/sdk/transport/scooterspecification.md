---
title: "ScooterSpecification (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestscooterspecification"
hidden: false
---

Package [com.here.sdk.transport](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class ScooterSpecification

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.transport.ScooterSpecification
------------------------------------------------------------------------
public final class ScooterSpecification extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Scooter specific settings.

## Field Summary

Fields

Modifier and Type

  Field

  Description

  `boolean`

  [allowScooterOnHighway](#allowScooterOnHighway)

Specifies whether scooter is allowed on highway or not.

## Constructor Summary

Constructors

Constructor

  Description

  [ScooterSpecification](#%3Cinit%3E())`()`

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

### allowScooterOnHighway

public boolean allowScooterOnHighway

    Specifies whether scooter is allowed on highway or not. `True` means scooter is allowed to use highways and `false` means otherwise. Defaults to `false`. Note that there is a similar parameter in `AvoidanceOptions`, to disallow highway usage, see `RoadFeatures.CONTROLLED_ACCESS_HIGHWAY`. As the avoidance options takes precedence, if this parameter is also used, then scooters are not allowed to use highways even if `allowHighway` is set to `true`. However, if no alternative route is possible, the calculated route may use highways. In such a case, a `SectionNotice` will be provided in the related `Section` to indicate that the highway usage restriction is violated on this route. A few examples:

    1 - If no avoidance option is set, and `allowHighway = false`, when no route is found without highway usage, a notice is received.

    2 - If no avoidance option is set, and `allowHighway = true`, when no route is found without highway usage, no notice is received.

    3 - If only `avoid[features] = controlledAccessHighway` is set, when no route is found without highway usage, a notice is received.

    4 - If both `avoid[features] = controlledAccessHighway` and `allowHighway = true` are set, when no route is found without highway usage, a notice is received.

## Constructor Details

  - ()" class="section detail">

### ScooterSpecification

public ScooterSpecification()

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
