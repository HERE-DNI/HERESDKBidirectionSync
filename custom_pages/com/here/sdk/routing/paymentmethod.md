---
title: "PaymentMethod (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestpaymentmethod"
hidden: false
---

Package [com.here.sdk.routing](sdk-for-android-explore-api-reference-latestpackage-summary)

# Enum Class PaymentMethod

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[java.lang.Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)\<[PaymentMethod](sdk-for-android-explore-api-reference-latestpaymentmethod "enum class in com.here.sdk.routing")\>
com.here.sdk.routing.PaymentMethod
All Implemented Interfaces:
[Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html), [Comparable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html)`<`[`PaymentMethod`](sdk-for-android-explore-api-reference-latestpaymentmethod "enum class in com.here.sdk.routing")`>`, [Constable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/constant/Constable.html)

------------------------------------------------------------------------
public enum PaymentMethod extends [Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)\<[PaymentMethod](sdk-for-android-explore-api-reference-latestpaymentmethod "enum class in com.here.sdk.routing")\>
Available payment methods.

## Nested Class Summary

## Nested classes/interfaces inherited from class java.lang.[Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)

  [Enum.EnumDesc](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html)`<`[E](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html)` extends `[Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)`<`[E](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html)`>>`

## Enum Constant Summary

Enum Constants

Enum Constant

  Description

  [BANK_CARD](#BANK_CARD)

Payment with a bank card.

[CASH](#CASH)

Payment with cash money.

[CASH_EXACT](#CASH_EXACT)

Payment with exact cash money, i.e.

[CREDIT_CARD](#CREDIT_CARD)

Payment with a credit card.

[PASS_SUBSCRIPTION](#PASS_SUBSCRIPTION)

Payment with a pass subscription.

[TRANSPONDER](#TRANSPONDER)

Payment with a transponder.

[TRAVEL_CARD](#TRAVEL_CARD)

Payment with a travel card.

[UNKNOWN](#UNKNOWN)

Payment with an unknown method.

[VIDEO_TOLL](#VIDEO_TOLL)

Payment with a video toll, i.e.

## Method Summary

  All Methods
  Static Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  `static `[`PaymentMethod`](sdk-for-android-explore-api-reference-latestpaymentmethod "enum class in com.here.sdk.routing")

  [valueOf](#valueOf(java.lang.String))`(`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` name)`

Returns the enum constant of this class with the specified name.

`static `[`PaymentMethod`](sdk-for-android-explore-api-reference-latestpaymentmethod "enum class in com.here.sdk.routing")`[]`

  [values](#values())`()`

Returns an array containing the constants of this enum class, in the order they are declared.

### Methods inherited from class java.lang.[Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#clone()), [compareTo](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#compareTo(E)), [describeConstable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#describeConstable()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#finalize()), [getDeclaringClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#getDeclaringClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#hashCode()), [name](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#name()), [ordinal](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#ordinal()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#toString()), [valueOf](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#valueOf(java.lang.Class,java.lang.String))

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Enum Constant Details

### UNKNOWN

public static final [PaymentMethod](sdk-for-android-explore-api-reference-latestpaymentmethod "enum class in com.here.sdk.routing") UNKNOWN

    Payment with an unknown method.

### CASH

public static final [PaymentMethod](sdk-for-android-explore-api-reference-latestpaymentmethod "enum class in com.here.sdk.routing") CASH

    Payment with cash money.

### BANK_CARD

public static final [PaymentMethod](sdk-for-android-explore-api-reference-latestpaymentmethod "enum class in com.here.sdk.routing") BANK_CARD

    Payment with a bank card.

### CREDIT_CARD

public static final [PaymentMethod](sdk-for-android-explore-api-reference-latestpaymentmethod "enum class in com.here.sdk.routing") CREDIT_CARD

    Payment with a credit card.

### PASS_SUBSCRIPTION

public static final [PaymentMethod](sdk-for-android-explore-api-reference-latestpaymentmethod "enum class in com.here.sdk.routing") PASS_SUBSCRIPTION

    Payment with a pass subscription.

### TRANSPONDER

public static final [PaymentMethod](sdk-for-android-explore-api-reference-latestpaymentmethod "enum class in com.here.sdk.routing") TRANSPONDER

    Payment with a transponder.

### VIDEO_TOLL

public static final [PaymentMethod](sdk-for-android-explore-api-reference-latestpaymentmethod "enum class in com.here.sdk.routing") VIDEO_TOLL

    Payment with a video toll, i.e. toll by license plate.

### CASH_EXACT

public static final [PaymentMethod](sdk-for-android-explore-api-reference-latestpaymentmethod "enum class in com.here.sdk.routing") CASH_EXACT

    Payment with exact cash money, i.e. toll booth accepts exact change only.

### TRAVEL_CARD

public static final [PaymentMethod](sdk-for-android-explore-api-reference-latestpaymentmethod "enum class in com.here.sdk.routing") TRAVEL_CARD

    Payment with a travel card.

## Method Details

### values

public static [PaymentMethod](sdk-for-android-explore-api-reference-latestpaymentmethod "enum class in com.here.sdk.routing")\[\] values()

    Returns an array containing the constants of this enum class, in the order they are declared.
Returns:
    an array containing the constants of this enum class, in the order they are declared

### valueOf

public static [PaymentMethod](sdk-for-android-explore-api-reference-latestpaymentmethod "enum class in com.here.sdk.routing") valueOf([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)

    Returns the enum constant of this class with the specified name. The string must match *exactly* an identifier used to declare an enum constant in this class. (Extraneous whitespace characters are not permitted.)
Parameters:
    `name` - the name of the enum constant to be returned.

    Returns:
    the enum constant with the specified name

    Throws:
    [IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html) - if this enum class has no constant with the specified name

    [NullPointerException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/NullPointerException.html) - if the argument is null
