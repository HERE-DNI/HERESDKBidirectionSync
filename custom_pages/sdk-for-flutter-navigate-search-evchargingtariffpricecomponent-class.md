---
title: "EVChargingTariffPriceComponent class - search library - Dart API"
slug: "sdk-for-flutter-navigate-search-evchargingtariffpricecomponent-class"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="search/search-library-sidebar.html" data-below-sidebar="search/EVChargingTariffPriceComponent-class-sidebar.html">

<div>

# <span class="kind-class">EVChargingTariffPriceComponent</span> class

</div>

<div class="section desc markdown">

Represents the price component of an EV charging tariff.

**Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-search-evchargingtariffpricecomponent-evchargingtariffpricecomponent">EVChargingTariffPriceComponent</a></span><span class="signature">()</span>  

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-search-evchargingtariffpricecomponent-dimension">dimension</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-search-evchargingtariffdimension">EVChargingTariffDimension</a></span>  
The dimension or type of the price component.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-evchargingtariffpricecomponent-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-evchargingtariffpricecomponent-price">price</a></span> <span class="signature">↔ double</span>  
The price per unit, excluding VAT. The units are defined by the <a href="sdk-for-flutter-navigate-search-evchargingtariffpricecomponent-dimension">EVChargingTariffPriceComponent.dimension</a>

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-evchargingtariffpricecomponent-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-evchargingtariffpricecomponent-step">step</a></span> <span class="signature">↔ double?</span>  
Dimension quantity used as a unit of billing. Present for all other dimensions except <a href="sdk-for-flutter-navigate-search-evchargingtariffdimension">EVChargingTariffDimension.flat</a>. The customer is charged price for each full or partial step of the dimension consumed. For <a href="sdk-for-flutter-navigate-search-evchargingtariffdimension">EVChargingTariffDimension.energy</a>, the step size unit is 1 Wh, for <a href="sdk-for-flutter-navigate-search-evchargingtariffdimension">EVChargingTariffDimension.time</a> and <a href="sdk-for-flutter-navigate-search-evchargingtariffdimension">EVChargingTariffDimension.parkingTime</a> it is 1 second. For example, if step is 300 for time, then time is billed in 5 minute steps, rounded upwards. Similarly, if step is 100 for energy, then energy is billed in 100 Wh = 0.1 kWh steps.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-evchargingtariffpricecomponent-vat">vat</a></span> <span class="signature">↔ double?</span>  
The VAT percentage of the price component. If not present, no VAT is applicable.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-search-evchargingtariffpricecomponent-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-evchargingtariffpricecomponent-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-search-evchargingtariffpricecomponent-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

