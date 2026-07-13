---
title: "FarePrice class - routing library - Dart API"
slug: "sdk-for-flutter-navigate-routing-fareprice-class"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="routing/routing-library-sidebar.html" data-below-sidebar="routing/FarePrice-class-sidebar.html">

<div>

# <span class="kind-class">FarePrice</span> class

</div>

<div class="section desc markdown">

Price of a fare.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-routing-fareprice-fareprice">FarePrice</a></span><span class="signature">()</span>  

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-routing-fareprice-currency">currency</a></span> <span class="signature">↔ String</span>  
Local currency of the price compliant to ISO 4217. For example, "GBP" for the British pound sterling. Defaults to "EUR" string.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-fareprice-estimated">estimated</a></span> <span class="signature">↔ bool</span>  
`True` when the fare price is estimated based on best guess and the actual price may differ. Defaults to `false`.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-fareprice-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-fareprice-maximum">maximum</a></span> <span class="signature">↔ double</span>  
Maximum price when the price is of <a href="sdk-for-flutter-navigate-routing-farepricetype">FarePriceType.range</a> type. Otherwise, it is equal to <a href="sdk-for-flutter-navigate-routing-fareprice-minimum">FarePrice.minimum</a>. Defaults to 0.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-fareprice-minimum">minimum</a></span> <span class="signature">↔ double</span>  
Minimum price when the price is of <a href="sdk-for-flutter-navigate-routing-farepricetype">FarePriceType.range</a> type. Otherwise, it is equal to <a href="sdk-for-flutter-navigate-routing-fareprice-maximum">FarePrice.maximum</a>. Defaults to 0.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-fareprice-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-fareprice-type">type</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-routing-farepricetype">FarePriceType</a></span>  
Type of price represented by this object. Defaults to <a href="sdk-for-flutter-navigate-routing-farepricetype">FarePriceType.value</a>.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-fareprice-validityperiod">validityPeriod</a></span> <span class="signature">↔ Duration?</span>  
When set, the price is paid for a specific duration.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-routing-fareprice-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-fareprice-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-routing-fareprice-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

