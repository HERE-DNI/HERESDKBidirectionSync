---
title: "EVMobilityServiceProviderPreferences class - routing library - Dart API"
slug: "sdk-for-flutter-explore-routing-evmobilityserviceproviderpreferences-class"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="routing/routing-library-sidebar.html" data-below-sidebar="routing/EVMobilityServiceProviderPreferences-class-sidebar.html">

<div>

# <span class="kind-class">EVMobilityServiceProviderPreferences</span> class

</div>

<div class="section desc markdown">

Defines preference level per known E-Mobility Service Provider.

The E-Mobility Service Provider ID partner id as received from <https://www.here.com/docs/bundle/ev-charge-points-api-developer-guide/page/topics/resource-roamings.html> An alternative way to get `partnerId` is the `eMobilityServiceProviders.partnerId` as part of `HERE SDK Search`. Maximum number of E-Mobility Service Providers is limited to 10 across all preference. Defaults to using all available providers with no prioritization.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-explore-routing-evmobilityserviceproviderpreferences-evmobilityserviceproviderpreferences">EVMobilityServiceProviderPreferences</a></span><span class="signature">()</span>  

## Properties

<span class="name"><a href="sdk-for-flutter-explore-routing-evmobilityserviceproviderpreferences-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-evmobilityserviceproviderpreferences-high">high</a></span> <span class="signature">↔ List<span class="signature">\<<wbr></wbr><span class="type-parameter">String</span>\></span></span>  
Specifies the E-Mobility Service Provider partnerId that are preferred the most.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-evmobilityserviceproviderpreferences-low">low</a></span> <span class="signature">↔ List<span class="signature">\<<wbr></wbr><span class="type-parameter">String</span>\></span></span>  
Specifies the E-Mobility Service Provider partnerId that are preferred the least.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-evmobilityserviceproviderpreferences-medium">medium</a></span> <span class="signature">↔ List<span class="signature">\<<wbr></wbr><span class="type-parameter">String</span>\></span></span>  
Specifies the E-Mobility Service Provider partnerId that can be used when no better provider could be found or reached.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-evmobilityserviceproviderpreferences-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-explore-routing-evmobilityserviceproviderpreferences-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-evmobilityserviceproviderpreferences-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-explore-routing-evmobilityserviceproviderpreferences-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

