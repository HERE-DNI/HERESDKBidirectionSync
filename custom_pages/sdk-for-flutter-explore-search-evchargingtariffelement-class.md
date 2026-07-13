---
title: "EVChargingTariffElement class - search library - Dart API"
slug: "sdk-for-flutter-explore-search-evchargingtariffelement-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- EVChargingTariffElement-class.html -->
<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="search/search-library-sidebar.html" data-below-sidebar="search/EVChargingTariffElement-class-sidebar.html">

<div>

# <span class="kind-class">EVChargingTariffElement</span> class

</div>

<div class="section desc markdown">

Represents a tariff element, which defines how pricing is applied.

The associated condition assists the client in selecting the appropriate element for a charging session. **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-explore-search-evchargingtariffelement-evchargingtariffelement">EVChargingTariffElement</a></span><span class="signature">()</span>  

## Properties

<span class="name"><a href="sdk-for-flutter-explore-search-evchargingtariffelement-components">components</a></span> <span class="signature">↔ List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-explore-search-evchargingtariffpricecomponent-class">EVChargingTariffPriceComponent</a></span>\></span></span>  
List of price components that describe the tariff. Each of the components should have a different <a href="sdk-for-flutter-explore-search-evchargingtariffdimension">EVChargingTariffDimension</a>.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-evchargingtariffelement-condition">condition</a></span> <span class="signature">↔ <a href="sdk-for-flutter-explore-search-evchargingtariffelementcondition-class">EVChargingTariffElementCondition</a>?</span>  
Condition that the charging session needs to meet to apply the tariff element. An element without any condition is typically present for charging sessions that do not meet any of the conditions.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-evchargingtariffelement-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-evchargingtariffelement-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-explore-search-evchargingtariffelement-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-evchargingtariffelement-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-explore-search-evchargingtariffelement-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
