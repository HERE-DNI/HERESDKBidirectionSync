---
title: "EVSEPaymentSupport (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-ev-evsepaymentsupport"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-explore-com-here-sdk-ev-package-summary">com.here.sdk.ev</a>

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object java.lang.Enum \< EVSEPaymentSupport \> com.here.sdk.ev.EVSEPaymentSupport → java.lang.Enum \< EVSEPaymentSupport \> com.here.sdk.ev.EVSEPaymentSupport → com.here.sdk.ev.EVSEPaymentSupport

</div>

<div id="sdk-for-android-explore-class-description" class="section class-description">

All Implemented Interfaces:  
<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html" class="external-link" title="class or interface in java.io"><code>Serializable</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html" class="external-link" title="class or interface in java.lang"><code>Comparable</code></a>`<`<a href="sdk-for-android-explore-com-here-sdk-ev-evsepaymentsupport" title="enum class in com.here.sdk.ev">`EVSEPaymentSupport`</a>`>`, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/constant/Constable.html" class="external-link" title="class or interface in java.lang.constant"><code>Constable</code></a>

<div class="type-signature">

<span class="modifiers">public enum </span><span class="element-name type-name-label">EVSEPaymentSupport</span> <span class="extends-implements">extends <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html" class="external-link" title="class or interface in java.lang">Enum</a>\<<a href="sdk-for-android-explore-com-here-sdk-ev-evsepaymentsupport" title="enum class in com.here.sdk.ev">EVSEPaymentSupport</a>\></span>

</div>

<div class="block">

Represents the payment support functionality on EVSE for ad-hoc customers (without pre-registration). Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

</div>

</div>

- <div id="sdk-for-android-explore-nested-class-summary" class="section nested-class-summary">

  <div class="inherited-list">

  ## Nested classes/interfaces inherited from class java.lang.<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html" class="external-link" title="class or interface in java.lang">Enum</a>

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html" class="external-link" title="class or interface in java.lang"><code>Enum.EnumDesc</code></a>`<`<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html" class="external-link" title="class or interface in java.lang"><code>E</code></a>` extends `<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html" class="external-link" title="class or interface in java.lang"><code>Enum</code></a>`<`<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html" class="external-link" title="class or interface in java.lang"><code>E</code></a>`>>`

  </div>

  </div>

- <div id="sdk-for-android-explore-enum-constant-summary" class="section constants-summary">

  ## Enum Constant Summary

  <div class="caption">

  Enum Constants

  </div>

  <div class="summary-table two-column-summary">

  <div class="table-header col-first">

  Enum Constant

  </div>

  <div class="table-header col-last">

  Description

  </div>

  <div class="col-first even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-ev-evsepaymentsupport#AUTH_BY_CAR_AUTOCHARGE" class="member-name-link"><code>AUTH_BY_CAR_AUTOCHARGE</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Autocharge enables drivers to plug in and charge up instantly using automatic EV-to-charging station authentication technology.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-ev-evsepaymentsupport#AUTH_BY_CAR_PLUG_AND_CHARGE" class="member-name-link"><code>AUTH_BY_CAR_PLUG_AND_CHARGE</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  ISO 15118 Plug&Charge enables drivers to plug in and charge up instantly using automatic EV-to-charging station authentication technology.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-ev-evsepaymentsupport#CHIP_CARD" class="member-name-link"><code>CHIP_CARD</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  EVSE has a payment terminal that supports chip cards.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-ev-evsepaymentsupport#CONTACTLESS_CARD" class="member-name-link"><code>CONTACTLESS_CARD</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  EVSE has a payment terminal that supports contactless cards.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-ev-evsepaymentsupport#CREDIT_CARD" class="member-name-link"><code>CREDIT_CARD</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  EVSE has a payment terminal that makes it possible to pay for charging using a credit card.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-ev-evsepaymentsupport#DEBIT_CARD" class="member-name-link"><code>DEBIT_CARD</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  EVSE has a payment terminal that makes it possible to pay for charging using a debit card.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-ev-evsepaymentsupport#MOBILE_PAYMENT" class="member-name-link"><code>MOBILE_PAYMENT</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Used with OPERATOR_APP , ONLINE_APPLE_PAY , ONLINE_PAYPAL , ONLINE_CREDIT_CARD , ONLINE_GOOGLE_PAY , ONLINE_BANK_PAYMENT , TERMINAL_SMS , TERMINAL_QR_CODE , and CONTACTLESS_CARD .

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-ev-evsepaymentsupport#ONLINE_APPLE_PAY" class="member-name-link"><code>ONLINE_APPLE_PAY</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Authenticate & pay with Apple Pay.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-ev-evsepaymentsupport#ONLINE_BANK_PAYMENT" class="member-name-link"><code>ONLINE_BANK_PAYMENT</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Authenticate & pay with online bank payment.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-ev-evsepaymentsupport#ONLINE_CREDIT_CARD" class="member-name-link"><code>ONLINE_CREDIT_CARD</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Authenticate & pay with credit card online.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-ev-evsepaymentsupport#ONLINE_GOOGLE_PAY" class="member-name-link"><code>ONLINE_GOOGLE_PAY</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Authenticate & pay with Google Pay.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-ev-evsepaymentsupport#ONLINE_PAYPAL" class="member-name-link"><code>ONLINE_PAYPAL</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Authenticate & pay with PayPal.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-ev-evsepaymentsupport#OPERATOR_APP" class="member-name-link"><code>OPERATOR_APP</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Authenticate & pay with charge point operator application on mobile phone.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-ev-evsepaymentsupport#PED_TERMINAL" class="member-name-link"><code>PED_TERMINAL</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  EVSE has a payment terminal with a pin-code entry device.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-ev-evsepaymentsupport#RFID_READER" class="member-name-link"><code>RFID_READER</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Charging at this EVSE can be authorized with an RFID token.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-ev-evsepaymentsupport#TERMINAL_QR_CODE" class="member-name-link"><code>TERMINAL_QR_CODE</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Initiate authentication & payment with QR code on the terminal.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-ev-evsepaymentsupport#TERMINAL_SMS" class="member-name-link"><code>TERMINAL_SMS</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Authenticate & pay with SMS on the terminal.

  </div>

  </div>

  </div>

  </div>

- <div id="sdk-for-android-explore-method-summary" class="section method-summary">

  <div id="sdk-for-android-explore-method-summary-table">

  <div class="summary-table three-column-summary">

  <div class="table-header col-first">

  Modifier and Type

  </div>

  <div class="table-header col-second">

  Method

  </div>

  <div class="table-header col-last">

  Description

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  `static `<a href="sdk-for-android-explore-com-here-sdk-ev-evsepaymentsupport" title="enum class in com.here.sdk.ev">`EVSEPaymentSupport`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

      valueOf ( String name)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  <div class="block">

  Returns the enum constant of this class with the specified name.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  `static `<a href="sdk-for-android-explore-com-here-sdk-ev-evsepaymentsupport" title="enum class in com.here.sdk.ev">`EVSEPaymentSupport`</a>`[]`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

      values ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  <div class="block">

  Returns an array containing the constants of this enum class, in the order they are declared.

  </div>

  </div>

  </div>

  </div>

  <div class="inherited-list">

  ### Methods inherited from class java.lang.<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html" class="external-link" title="class or interface in java.lang">Enum</a>

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#clone()" class="external-link" title="class or interface in java.lang"><code>clone</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#compareTo(E)" class="external-link" title="class or interface in java.lang"><code>compareTo</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#describeConstable()" class="external-link" title="class or interface in java.lang"><code>describeConstable</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#equals(java.lang.Object)" class="external-link" title="class or interface in java.lang"><code>equals</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#finalize()" class="external-link" title="class or interface in java.lang"><code>finalize</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#getDeclaringClass()" class="external-link" title="class or interface in java.lang"><code>getDeclaringClass</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#hashCode()" class="external-link" title="class or interface in java.lang"><code>hashCode</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#name()" class="external-link" title="class or interface in java.lang"><code>name</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#ordinal()" class="external-link" title="class or interface in java.lang"><code>ordinal</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#toString()" class="external-link" title="class or interface in java.lang"><code>toString</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#valueOf(java.lang.Class,java.lang.String)" class="external-link" title="class or interface in java.lang"><code>valueOf</code></a>

  </div>

  <div class="inherited-list">

  ### Methods inherited from class java.lang.<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a>

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" class="external-link" title="class or interface in java.lang"><code>getClass</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" class="external-link" title="class or interface in java.lang"><code>notify</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" class="external-link" title="class or interface in java.lang"><code>notifyAll</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>

  </div>

  </div>

<!-- -->

- <div id="sdk-for-android-explore-enum-constant-detail" class="section constant-details">

  ## Enum Constant Details

  - <div id="sdk-for-android-explore-CHIP_CARD" class="section detail">

    ### CHIP_CARD

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-explore-com-here-sdk-ev-evsepaymentsupport" title="enum class in com.here.sdk.ev">EVSEPaymentSupport</a></span> <span class="element-name">CHIP_CARD</span>

    </div>

    <div class="block">

    EVSE has a payment terminal that supports chip cards.

    </div>

    </div>

  - <div id="sdk-for-android-explore-CONTACTLESS_CARD" class="section detail">

    ### CONTACTLESS_CARD

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-explore-com-here-sdk-ev-evsepaymentsupport" title="enum class in com.here.sdk.ev">EVSEPaymentSupport</a></span> <span class="element-name">CONTACTLESS_CARD</span>

    </div>

    <div class="block">

    EVSE has a payment terminal that supports contactless cards.

    </div>

    </div>

  - <div id="sdk-for-android-explore-CREDIT_CARD" class="section detail">

    ### CREDIT_CARD

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-explore-com-here-sdk-ev-evsepaymentsupport" title="enum class in com.here.sdk.ev">EVSEPaymentSupport</a></span> <span class="element-name">CREDIT_CARD</span>

    </div>

    <div class="block">

    EVSE has a payment terminal that makes it possible to pay for charging using a credit card.

    </div>

    </div>

  - <div id="sdk-for-android-explore-DEBIT_CARD" class="section detail">

    ### DEBIT_CARD

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-explore-com-here-sdk-ev-evsepaymentsupport" title="enum class in com.here.sdk.ev">EVSEPaymentSupport</a></span> <span class="element-name">DEBIT_CARD</span>

    </div>

    <div class="block">

    EVSE has a payment terminal that makes it possible to pay for charging using a debit card.

    </div>

    </div>

  - <div id="sdk-for-android-explore-PED_TERMINAL" class="section detail">

    ### PED_TERMINAL

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-explore-com-here-sdk-ev-evsepaymentsupport" title="enum class in com.here.sdk.ev">EVSEPaymentSupport</a></span> <span class="element-name">PED_TERMINAL</span>

    </div>

    <div class="block">

    EVSE has a payment terminal with a pin-code entry device.

    </div>

    </div>

  - <div id="sdk-for-android-explore-RFID_READER" class="section detail">

    ### RFID_READER

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-explore-com-here-sdk-ev-evsepaymentsupport" title="enum class in com.here.sdk.ev">EVSEPaymentSupport</a></span> <span class="element-name">RFID_READER</span>

    </div>

    <div class="block">

    Charging at this EVSE can be authorized with an RFID token.

    </div>

    </div>

  - <div id="sdk-for-android-explore-AUTH_BY_CAR_PLUG_AND_CHARGE" class="section detail">

    ### AUTH_BY_CAR_PLUG_AND_CHARGE

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-explore-com-here-sdk-ev-evsepaymentsupport" title="enum class in com.here.sdk.ev">EVSEPaymentSupport</a></span> <span class="element-name">AUTH_BY_CAR_PLUG_AND_CHARGE</span>

    </div>

    <div class="block">

    ISO 15118 Plug&Charge enables drivers to plug in and charge up instantly using automatic EV-to-charging station authentication technology.

    </div>

    </div>

  - <div id="sdk-for-android-explore-AUTH_BY_CAR_AUTOCHARGE" class="section detail">

    ### AUTH_BY_CAR_AUTOCHARGE

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-explore-com-here-sdk-ev-evsepaymentsupport" title="enum class in com.here.sdk.ev">EVSEPaymentSupport</a></span> <span class="element-name">AUTH_BY_CAR_AUTOCHARGE</span>

    </div>

    <div class="block">

    Autocharge enables drivers to plug in and charge up instantly using automatic EV-to-charging station authentication technology.

    </div>

    </div>

  - <div id="sdk-for-android-explore-ONLINE_APPLE_PAY" class="section detail">

    ### ONLINE_APPLE_PAY

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-explore-com-here-sdk-ev-evsepaymentsupport" title="enum class in com.here.sdk.ev">EVSEPaymentSupport</a></span> <span class="element-name">ONLINE_APPLE_PAY</span>

    </div>

    <div class="block">

    Authenticate & pay with Apple Pay.

    </div>

    </div>

  - <div id="sdk-for-android-explore-ONLINE_PAYPAL" class="section detail">

    ### ONLINE_PAYPAL

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-explore-com-here-sdk-ev-evsepaymentsupport" title="enum class in com.here.sdk.ev">EVSEPaymentSupport</a></span> <span class="element-name">ONLINE_PAYPAL</span>

    </div>

    <div class="block">

    Authenticate & pay with PayPal.

    </div>

    </div>

  - <div id="sdk-for-android-explore-ONLINE_CREDIT_CARD" class="section detail">

    ### ONLINE_CREDIT_CARD

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-explore-com-here-sdk-ev-evsepaymentsupport" title="enum class in com.here.sdk.ev">EVSEPaymentSupport</a></span> <span class="element-name">ONLINE_CREDIT_CARD</span>

    </div>

    <div class="block">

    Authenticate & pay with credit card online.

    </div>

    </div>

  - <div id="sdk-for-android-explore-ONLINE_GOOGLE_PAY" class="section detail">

    ### ONLINE_GOOGLE_PAY

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-explore-com-here-sdk-ev-evsepaymentsupport" title="enum class in com.here.sdk.ev">EVSEPaymentSupport</a></span> <span class="element-name">ONLINE_GOOGLE_PAY</span>

    </div>

    <div class="block">

    Authenticate & pay with Google Pay.

    </div>

    </div>

  - <div id="sdk-for-android-explore-ONLINE_BANK_PAYMENT" class="section detail">

    ### ONLINE_BANK_PAYMENT

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-explore-com-here-sdk-ev-evsepaymentsupport" title="enum class in com.here.sdk.ev">EVSEPaymentSupport</a></span> <span class="element-name">ONLINE_BANK_PAYMENT</span>

    </div>

    <div class="block">

    Authenticate & pay with online bank payment.

    </div>

    </div>

  - <div id="sdk-for-android-explore-TERMINAL_QR_CODE" class="section detail">

    ### TERMINAL_QR_CODE

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-explore-com-here-sdk-ev-evsepaymentsupport" title="enum class in com.here.sdk.ev">EVSEPaymentSupport</a></span> <span class="element-name">TERMINAL_QR_CODE</span>

    </div>

    <div class="block">

    Initiate authentication & payment with QR code on the terminal.

    </div>

    </div>

  - <div id="sdk-for-android-explore-TERMINAL_SMS" class="section detail">

    ### TERMINAL_SMS

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-explore-com-here-sdk-ev-evsepaymentsupport" title="enum class in com.here.sdk.ev">EVSEPaymentSupport</a></span> <span class="element-name">TERMINAL_SMS</span>

    </div>

    <div class="block">

    Authenticate & pay with SMS on the terminal.

    </div>

    </div>

  - <div id="sdk-for-android-explore-OPERATOR_APP" class="section detail">

    ### OPERATOR_APP

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-explore-com-here-sdk-ev-evsepaymentsupport" title="enum class in com.here.sdk.ev">EVSEPaymentSupport</a></span> <span class="element-name">OPERATOR_APP</span>

    </div>

    <div class="block">

    Authenticate & pay with charge point operator application on mobile phone.

    </div>

    </div>

  - <div id="sdk-for-android-explore-MOBILE_PAYMENT" class="section detail">

    ### MOBILE_PAYMENT

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-explore-com-here-sdk-ev-evsepaymentsupport" title="enum class in com.here.sdk.ev">EVSEPaymentSupport</a></span> <span class="element-name">MOBILE_PAYMENT</span>

    </div>

    <div class="block">

    Used with OPERATOR_APP , ONLINE_APPLE_PAY , ONLINE_PAYPAL , ONLINE_CREDIT_CARD , ONLINE_GOOGLE_PAY , ONLINE_BANK_PAYMENT , TERMINAL_SMS , TERMINAL_QR_CODE , and CONTACTLESS_CARD . Whenever one or more of those payment types is specified, MOBILE_PAYMENT is also specified.

    </div>

    </div>

  </div>

- <div id="sdk-for-android-explore-method-detail" class="section method-details">

  - <div id="sdk-for-android-explore-values" class="section detail">

    ### values

    <div class="member-signature">

    <span class="modifiers">public static</span> <span class="return-type"><a href="sdk-for-android-explore-com-here-sdk-ev-evsepaymentsupport" title="enum class in com.here.sdk.ev">EVSEPaymentSupport</a>\[\]</span> <span class="element-name">values</span>()

    </div>

    <div class="block">

    Returns an array containing the constants of this enum class, in the order they are declared.

    </div>

    Returns:  
    an array containing the constants of this enum class, in the order they are declared

    </div>

  - <div id="sdk-for-android-explore-valueOf-java-lang-String" class="section detail">

    ### valueOf

    <div class="member-signature">

    <span class="modifiers">public static</span> <span class="return-type"><a href="sdk-for-android-explore-com-here-sdk-ev-evsepaymentsupport" title="enum class in com.here.sdk.ev">EVSEPaymentSupport</a></span> <span class="element-name">valueOf</span><wbr></wbr><span class="parameters">(<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a> name)</span>

    </div>

    <div class="block">

    Returns the enum constant of this class with the specified name. The string must match exactly an identifier used to declare an enum constant in this class. (Extraneous whitespace characters are not permitted.)

    </div>

    Parameters:  
    `name` - the name of the enum constant to be returned.

    Returns:  
    the enum constant with the specified name

    Throws:  
    <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html" class="external-link" title="class or interface in java.lang"><code>IllegalArgumentException</code></a> - if this enum class has no constant with the specified name

    <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/NullPointerException.html" class="external-link" title="class or interface in java.lang"><code>NullPointerException</code></a> - if the argument is null

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

