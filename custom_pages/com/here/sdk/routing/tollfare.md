---
title: "TollFare (API Reference)"
slug: "sdk-for-android-explore-api-reference-latesttollfare"
hidden: false
---

Package [com.here.sdk.routing](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class TollFare

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.routing.TollFare
------------------------------------------------------------------------
public final class TollFare extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
This struct presents all the fare data for a toll.

**Note**: If you're using the `OfflineRoutingEngine`, be aware that this feature is currently in **beta**. As a result, there may be some bugs or unexpected behaviors. Additionally, this feature and related APIs may be updated in future releases without going through the deprecation process. Note that the `OfflineRoutingEngine` is only available for the Navigate license. If you're using the `RoutingEngine`, this feature is considered to be stable.

## Field Summary

Fields

Modifier and Type

  Field

  Description

  [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [currency](#currency)

The currency in which the toll is to be paid in ISO 4217 format, e.g.

[`TollFarePass`](sdk-for-android-explore-api-reference-latesttollfarepass "class in com.here.sdk.routing")

  [pass](#pass)

Specifies whether this [`TollFare`](sdk-for-android-explore-api-reference-latesttollfare "class in com.here.sdk.routing") is a multi-travel pass, and its characteristics.

[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`PaymentMethod`](sdk-for-android-explore-api-reference-latestpaymentmethod "enum class in com.here.sdk.routing")`>`

  [paymentMethods](#paymentMethods)

The list of accepted payment methods like cash and credit card.

`double`

  [price](#price)

The amount of the toll be paid.

[`TimeRule`](sdk-for-android-explore-api-reference-latesttimerule "class in com.here.sdk.core")

  [timeRule](#timeRule)

The time domain when this fare is valid.

[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`>`

  [transponders](#transponders)

The list of available transponders.

## Constructor Summary

Constructors

Constructor

  Description

  [TollFare](#%3Cinit%3E(java.lang.String,double,java.util.List))`(`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` currency, double price, `[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`PaymentMethod`](sdk-for-android-explore-api-reference-latestpaymentmethod "enum class in com.here.sdk.routing")`> paymentMethods)`

Creates a new instance.

[TollFare](#%3Cinit%3E(java.lang.String,double,java.util.List,com.here.sdk.core.TimeRule))`(`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` currency, double price, `[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`PaymentMethod`](sdk-for-android-explore-api-reference-latestpaymentmethod "enum class in com.here.sdk.routing")`> paymentMethods, `[`TimeRule`](sdk-for-android-explore-api-reference-latesttimerule "class in com.here.sdk.core")` timeRule)`

Creates a new instance.

[TollFare](#%3Cinit%3E(java.lang.String,double,java.util.List,com.here.sdk.core.TimeRule,java.util.List))`(`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` currency, double price, `[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`PaymentMethod`](sdk-for-android-explore-api-reference-latestpaymentmethod "enum class in com.here.sdk.routing")`> paymentMethods, `[`TimeRule`](sdk-for-android-explore-api-reference-latesttimerule "class in com.here.sdk.core")` timeRule, `[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`> transponders)`

Creates a new instance.

[TollFare](#%3Cinit%3E(java.lang.String,double,java.util.List,com.here.sdk.core.TimeRule,java.util.List,com.here.sdk.routing.TollFarePass))`(`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` currency, double price, `[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`PaymentMethod`](sdk-for-android-explore-api-reference-latestpaymentmethod "enum class in com.here.sdk.routing")`> paymentMethods, `[`TimeRule`](sdk-for-android-explore-api-reference-latesttimerule "class in com.here.sdk.core")` timeRule, `[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`> transponders, `[`TollFarePass`](sdk-for-android-explore-api-reference-latesttollfarepass "class in com.here.sdk.routing")` pass)`

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

### currency

@NonNull public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) currency

    The currency in which the toll is to be paid in ISO 4217 format, e.g. "USD".

### price

public double price

    The amount of the toll be paid.

### paymentMethods

@NonNull public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[PaymentMethod](sdk-for-android-explore-api-reference-latestpaymentmethod "enum class in com.here.sdk.routing")\> paymentMethods

    The list of accepted payment methods like cash and credit card.

### timeRule

@Nullable public [TimeRule](sdk-for-android-explore-api-reference-latesttimerule "class in com.here.sdk.core") timeRule

    The time domain when this fare is valid. If this field is missing, it means the fare is always valid. For a detailed description of the Time Domain specification and usage in routing services, please refer to the documentation available in the [Time Domain](https://www.here.com/docs/bundle/routing-api-developer-guide-v8/page/topics/time-domain.html)

### transponders

@NonNull public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)\> transponders

    The list of available transponders.

### pass

@Nullable public [TollFarePass](sdk-for-android-explore-api-reference-latesttollfarepass "class in com.here.sdk.routing") pass

    Specifies whether this [`TollFare`](sdk-for-android-explore-api-reference-latesttollfare "class in com.here.sdk.routing") is a multi-travel pass, and its characteristics.

## Constructor Details

  - (java.lang.String,double,java.util.List)" class="section detail">

### TollFare

public TollFare(@NonNull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) currency, double price, @NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[PaymentMethod](sdk-for-android-explore-api-reference-latestpaymentmethod "enum class in com.here.sdk.routing")\> paymentMethods)

    Creates a new instance.
Parameters:
    `currency` -

    The currency in which the toll is to be paid in ISO 4217 format, e.g. "USD".

    `price` -

    The amount of the toll be paid.

    `paymentMethods` -

    The list of accepted payment methods like cash and credit card.
- (java.lang.String,double,java.util.List,com.here.sdk.core.TimeRule)" class="section detail">

### TollFare

public TollFare(@NonNull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) currency, double price, @NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[PaymentMethod](sdk-for-android-explore-api-reference-latestpaymentmethod "enum class in com.here.sdk.routing")\> paymentMethods, @Nullable [TimeRule](sdk-for-android-explore-api-reference-latesttimerule "class in com.here.sdk.core") timeRule)

    Creates a new instance.
Parameters:
    `currency` -

    The currency in which the toll is to be paid in ISO 4217 format, e.g. "USD".

    `price` -

    The amount of the toll be paid.

    `paymentMethods` -

    The list of accepted payment methods like cash and credit card.

    `timeRule` -

    The time domain when this fare is valid. If this field is missing, it means the fare is always valid. For a detailed description of the Time Domain specification and usage in routing services, please refer to the documentation available in the [Time Domain](https://www.here.com/docs/bundle/routing-api-developer-guide-v8/page/topics/time-domain.html)
- (java.lang.String,double,java.util.List,com.here.sdk.core.TimeRule,java.util.List)" class="section detail">

### TollFare

public TollFare(@NonNull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) currency, double price, @NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[PaymentMethod](sdk-for-android-explore-api-reference-latestpaymentmethod "enum class in com.here.sdk.routing")\> paymentMethods, @Nullable [TimeRule](sdk-for-android-explore-api-reference-latesttimerule "class in com.here.sdk.core") timeRule, @NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)\> transponders)

    Creates a new instance.
Parameters:
    `currency` -

    The currency in which the toll is to be paid in ISO 4217 format, e.g. "USD".

    `price` -

    The amount of the toll be paid.

    `paymentMethods` -

    The list of accepted payment methods like cash and credit card.

    `timeRule` -

    The time domain when this fare is valid. If this field is missing, it means the fare is always valid. For a detailed description of the Time Domain specification and usage in routing services, please refer to the documentation available in the [Time Domain](https://www.here.com/docs/bundle/routing-api-developer-guide-v8/page/topics/time-domain.html)

    `transponders` -

    The list of available transponders.
- (java.lang.String,double,java.util.List,com.here.sdk.core.TimeRule,java.util.List,com.here.sdk.routing.TollFarePass)" class="section detail">

### TollFare

public TollFare(@NonNull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) currency, double price, @NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[PaymentMethod](sdk-for-android-explore-api-reference-latestpaymentmethod "enum class in com.here.sdk.routing")\> paymentMethods, @Nullable [TimeRule](sdk-for-android-explore-api-reference-latesttimerule "class in com.here.sdk.core") timeRule, @NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)\> transponders, @Nullable [TollFarePass](sdk-for-android-explore-api-reference-latesttollfarepass "class in com.here.sdk.routing") pass)

    Creates a new instance.
Parameters:
    `currency` -

    The currency in which the toll is to be paid in ISO 4217 format, e.g. "USD".

    `price` -

    The amount of the toll be paid.

    `paymentMethods` -

    The list of accepted payment methods like cash and credit card.

    `timeRule` -

    The time domain when this fare is valid. If this field is missing, it means the fare is always valid. For a detailed description of the Time Domain specification and usage in routing services, please refer to the documentation available in the [Time Domain](https://www.here.com/docs/bundle/routing-api-developer-guide-v8/page/topics/time-domain.html)

    `transponders` -

    The list of available transponders.

    `pass` -

    Specifies whether this [`TollFare`](sdk-for-android-explore-api-reference-latesttollfare "class in com.here.sdk.routing") is a multi-travel pass, and its characteristics.

## Method Details

### equals

public boolean equals([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) obj)
Overrides:
    [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

### hashCode

public int hashCode()
Overrides:
    [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
