---
title: "TollFare class - routing library - Dart API"
slug: "sdk-for-flutter-explore-routing-tollfare-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- TollFare-class.html -->
<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="routing/routing-library-sidebar.html" data-below-sidebar="routing/TollFare-class-sidebar.html">

<div>

# <span class="kind-class">TollFare</span> class

</div>

<div class="section desc markdown">

This struct presents all the fare data for a toll.

**Note**: If you're using the `OfflineRoutingEngine`, be aware that this feature is currently in **beta**. As a result, there may be some bugs or unexpected behaviors. Additionally, this feature and related APIs may be updated in future releases without going through the deprecation process. Note that the `OfflineRoutingEngine` is only available for the Navigate license. If you're using the `RoutingEngine`, this feature is considered to be stable.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-explore-routing-tollfare-tollfare">TollFare</a></span><span class="signature">(<span id="sdk-for-flutter-explore-param-currency" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">currency</span>, </span><span id="sdk-for-flutter-explore-param-price" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">price</span>, </span><span id="sdk-for-flutter-explore-param-paymentMethods" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-explore-routing-paymentmethod">PaymentMethod</a></span>\></span></span> <span class="parameter-name">paymentMethods</span>, \<a href="sdk-for-flutter-explore-core-timerule-class"></span><span id="sdk-for-flutter-explore-param-timeRule" class="parameter"><span class="type-annotation">[TimeRule</a>?</span> <span class="parameter-name">timeRule</span> = <span class="default-value">null</span>, </span><span id="sdk-for-flutter-explore-param-transponders" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter">String</span>\></span></span> <span class="parameter-name">transponders</span> = <span class="default-value">const \[\]</span>, </span><span id="sdk-for-flutter-explore-param-pass" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-routing-tollfarepass-class">TollFarePass</a>?</span> <span class="parameter-name">pass</span> = <span class="default-value">null</span></span>\])</span>  
Creates a new instance.

## Properties

<span class="name"><a href="sdk-for-flutter-explore-routing-tollfare-currency">currency</a></span> <span class="signature">↔ String</span>  
The currency in which the toll is to be paid in ISO 4217 format, e.g. "USD".

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-tollfare-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-tollfare-pass">pass</a></span> <span class="signature">↔ <a href="sdk-for-flutter-explore-routing-tollfarepass-class">TollFarePass</a>?</span>  
Specifies whether this <a href="sdk-for-flutter-explore-routing-tollfare-class">TollFare</a> is a multi-travel pass, and its characteristics.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-tollfare-paymentmethods">paymentMethods</a></span> <span class="signature">↔ List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-explore-routing-paymentmethod">PaymentMethod</a></span>\></span></span>  
The list of accepted payment methods like cash and credit card.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-tollfare-price">price</a></span> <span class="signature">↔ double</span>  
The amount of the toll be paid.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-tollfare-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-tollfare-timerule">timeRule</a></span> <span class="signature">↔ <a href="sdk-for-flutter-explore-core-timerule-class">TimeRule</a>?</span>  
The time domain when this fare is valid. If this field is missing, it means the fare is always valid. For a detailed description of the Time Domain specification and usage in routing services, please refer to the documentation available in the <a href="https://www.here.com/docs/bundle/routing-api-developer-guide-v8/page/topics/time-domain.html">Time Domain</a>

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-tollfare-transponders">transponders</a></span> <span class="signature">↔ List<span class="signature">\<<wbr></wbr><span class="type-parameter">String</span>\></span></span>  
The list of available transponders.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-explore-routing-tollfare-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-tollfare-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-explore-routing-tollfare-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
