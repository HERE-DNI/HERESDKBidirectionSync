---
title: "EVSEPaymentSupport enum - ev library - Dart API"
slug: "sdk-for-flutter-explore-ev-evsepaymentsupport"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="ev/ev-library-sidebar.html" data-below-sidebar="ev/EVSEPaymentSupport-enum-sidebar.html">

<div>

# <span class="kind-enum">EVSEPaymentSupport</span> enum

</div>

<div class="section desc markdown">

Represents the payment support functionality on EVSE for ad-hoc customers (without pre-registration).

**Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

</div>

## Values

<span class="name">chipCard</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-ev-evsepaymentsupport">EVSEPaymentSupport</a></span>  
EVSE has a payment terminal that supports chip cards.

<span class="name">contactlessCard</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-ev-evsepaymentsupport">EVSEPaymentSupport</a></span>  
EVSE has a payment terminal that supports contactless cards.

<span class="name">creditCard</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-ev-evsepaymentsupport">EVSEPaymentSupport</a></span>  
EVSE has a payment terminal that makes it possible to pay for charging using a credit card.

<span class="name">debitCard</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-ev-evsepaymentsupport">EVSEPaymentSupport</a></span>  
EVSE has a payment terminal that makes it possible to pay for charging using a debit card.

<span class="name">pedTerminal</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-ev-evsepaymentsupport">EVSEPaymentSupport</a></span>  
EVSE has a payment terminal with a pin-code entry device.

<span class="name">rfidReader</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-ev-evsepaymentsupport">EVSEPaymentSupport</a></span>  
Charging at this EVSE can be authorized with an RFID token.

<span class="name">authByCarPlugAndCharge</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-ev-evsepaymentsupport">EVSEPaymentSupport</a></span>  
ISO 15118 Plug&Charge enables drivers to plug in and charge up instantly using automatic EV-to-charging station authentication technology.

<span class="name">authByCarAutocharge</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-ev-evsepaymentsupport">EVSEPaymentSupport</a></span>  
Autocharge enables drivers to plug in and charge up instantly using automatic EV-to-charging station authentication technology.

<span class="name">onlineApplePay</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-ev-evsepaymentsupport">EVSEPaymentSupport</a></span>  
Authenticate & pay with Apple Pay.

<span class="name">onlinePaypal</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-ev-evsepaymentsupport">EVSEPaymentSupport</a></span>  
Authenticate & pay with PayPal.

<span class="name">onlineCreditCard</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-ev-evsepaymentsupport">EVSEPaymentSupport</a></span>  
Authenticate & pay with credit card online.

<span class="name">onlineGooglePay</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-ev-evsepaymentsupport">EVSEPaymentSupport</a></span>  
Authenticate & pay with Google Pay.

<span class="name">onlineBankPayment</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-ev-evsepaymentsupport">EVSEPaymentSupport</a></span>  
Authenticate & pay with online bank payment.

<span class="name">terminalQrCode</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-ev-evsepaymentsupport">EVSEPaymentSupport</a></span>  
Initiate authentication & payment with QR code on the terminal.

<span class="name">terminalSms</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-ev-evsepaymentsupport">EVSEPaymentSupport</a></span>  
Authenticate & pay with SMS on the terminal.

<span class="name">operatorApp</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-ev-evsepaymentsupport">EVSEPaymentSupport</a></span>  
Authenticate & pay with charge point operator application on mobile phone.

<span class="name">mobilePayment</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-ev-evsepaymentsupport">EVSEPaymentSupport</a></span>  
Used with <a href="sdk-for-flutter-explore-ev-evsepaymentsupport">EVSEPaymentSupport.operatorApp</a>, <a href="sdk-for-flutter-explore-ev-evsepaymentsupport">EVSEPaymentSupport.onlineApplePay</a>, <a href="sdk-for-flutter-explore-ev-evsepaymentsupport">EVSEPaymentSupport.onlinePaypal</a>, <a href="sdk-for-flutter-explore-ev-evsepaymentsupport">EVSEPaymentSupport.onlineCreditCard</a>, <a href="sdk-for-flutter-explore-ev-evsepaymentsupport">EVSEPaymentSupport.onlineGooglePay</a>, <a href="sdk-for-flutter-explore-ev-evsepaymentsupport">EVSEPaymentSupport.onlineBankPayment</a>, <a href="sdk-for-flutter-explore-ev-evsepaymentsupport">EVSEPaymentSupport.terminalSms</a>, <a href="sdk-for-flutter-explore-ev-evsepaymentsupport">EVSEPaymentSupport.terminalQrCode</a>, and <a href="sdk-for-flutter-explore-ev-evsepaymentsupport">EVSEPaymentSupport.contactlessCard</a>. Whenever one or more of those payment types is specified, <a href="sdk-for-flutter-explore-ev-evsepaymentsupport">EVSEPaymentSupport.mobilePayment</a> is also specified.

## Properties

<span class="name"><a href="sdk-for-flutter-explore-ev-evsepaymentsupport-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-ev-evsepaymentsupport-index">index</a></span> <span class="signature">→ int</span>  
A numeric identifier for the enumerated value.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-ev-evsepaymentsupport-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-explore-ev-evsepaymentsupport-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-ev-evsepaymentsupport-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-explore-ev-evsepaymentsupport-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

## Constants

<span class="name"><a href="sdk-for-flutter-explore-ev-evsepaymentsupport-values-constant">values</a></span> <span class="signature">→ const List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-explore-ev-evsepaymentsupport">EVSEPaymentSupport</a></span>\></span></span>  
A constant List of the values in this enum, in order of their declaration.

</div>

<!-- /.main-content --> <!-- /.sidebar-offcanvas --> <span class="no-break"> here_sdk 4.26.0 </span>

