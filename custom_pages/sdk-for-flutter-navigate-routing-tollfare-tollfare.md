---
title: "TollFare constructor - TollFare - routing library - Dart API"
slug: "sdk-for-flutter-navigate-routing-tollfare-tollfare"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="routing/TollFare-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">TollFare</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">TollFare</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-param-currency" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">currency</span>, </span>
2.  <span id="sdk-for-flutter-navigate-param-price" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">price</span>, </span>
3.  <span id="sdk-for-flutter-navigate-param-paymentMethods" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-routing-paymentmethod">PaymentMethod</a></span>\></span></span> <span class="parameter-name">paymentMethods</span>, \<a href="sdk-for-flutter-navigate-core-timerule-class"></span>
4.  <span id="sdk-for-flutter-navigate-param-timeRule" class="parameter"><span class="type-annotation">[TimeRule</a>?</span> <span class="parameter-name">timeRule</span> = <span class="default-value">null</span>, </span>
5.  <span id="sdk-for-flutter-navigate-param-transponders" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter">String</span>\></span></span> <span class="parameter-name">transponders</span> = <span class="default-value">const \[\]</span>, </span>
6.  <span id="sdk-for-flutter-navigate-param-pass" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-tollfarepass-class">TollFarePass</a>?</span> <span class="parameter-name">pass</span> = <span class="default-value">null</span>, </span>

\])

</div>

<div class="section desc markdown">

Creates a new instance.

- `currency` The currency in which the toll is to be paid in ISO 4217 format, e.g. "USD".
- `price` The amount of the toll be paid.
- `paymentMethods` The list of accepted payment methods like cash and credit card.
- `timeRule` The time domain when this fare is valid. If this field is missing, it means the fare is always valid. For a detailed description of the Time Domain specification and usage in routing services, please refer to the documentation available in the <a href="https://www.here.com/docs/bundle/routing-api-developer-guide-v8/page/topics/time-domain.html">Time Domain</a>
- `transponders` The list of available transponders.
- `pass` Specifies whether this <a href="sdk-for-flutter-navigate-routing-tollfare-class">TollFare</a> is a multi-travel pass, and its characteristics.

</div>

## Implementation

``` dart
TollFare(String currency, double price, List<PaymentMethod> paymentMethods, [TimeRule? timeRule = null, List<String> transponders = const [], TollFarePass? pass = null])
  : currency = currency, price = price, paymentMethods = paymentMethods, timeRule = timeRule, transponders = transponders, pass = pass ?? null;
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

