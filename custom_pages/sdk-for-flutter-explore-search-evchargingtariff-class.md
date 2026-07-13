---
title: "EVChargingTariff class - search library - Dart API"
slug: "sdk-for-flutter-explore-search-evchargingtariff-class"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="search/search-library-sidebar.html" data-below-sidebar="search/EVChargingTariff-class-sidebar.html">

<div>

# <span class="kind-class">EVChargingTariff</span> class

</div>

<div class="section desc markdown">

Tariffs provide detailed pricing information for charging electric vehicles at a specific location.

Each tariff describes how costs are calculated based on various factors such as energy consumed, time spent charging, and session duration. Tariffs are typically associated with specific connectors or connector groups, and are only included in the response when relevant data is available and requested. **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-explore-search-evchargingtariff-evchargingtariff">EVChargingTariff</a></span><span class="signature">()</span>  

## Properties

<span class="name"><a href="sdk-for-flutter-explore-search-evchargingtariff-currency">currency</a></span> <span class="signature">↔ String</span>  
The currency in which the prices are given, represented by the ISO 4217 standard currency code (e.g., EUR, DKK).

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-evchargingtariff-elements">elements</a></span> <span class="signature">↔ List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-explore-search-evchargingtariffelement-class">EVChargingTariffElement</a></span>\></span></span>  
Elements composing the tariff. Each element can have multiple components. When multiple elements are present, the associated condition helps the client to select the element that matches the charging session. If no condition matches, the element without any condition applies.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-evchargingtariff-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-evchargingtariff-name">name</a></span> <span class="signature">↔ String?</span>  
Name of the tariff. The name is not mandatory for ad-hoc tariffs, but may exist.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-evchargingtariff-partner">partner</a></span> <span class="signature">↔ String</span>  
Name of the partner providing the tariff, either the charge point operator or eMSP.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-evchargingtariff-partnerid">partnerID</a></span> <span class="signature">↔ String</span>  
A unique ID representing the partner. The same id is used also in other parts of the API and other related HERE APIs.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-evchargingtariff-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-evchargingtariff-type">type</a></span> <span class="signature">↔ <a href="sdk-for-flutter-explore-search-evchargingtarifftype">EVChargingTariffType</a></span>  
Indicates the pricing model.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-explore-search-evchargingtariff-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-evchargingtariff-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-explore-search-evchargingtariff-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

