---
title: "IsolineOptions class - routing library - Dart API"
slug: "sdk-for-flutter-explore-routing-isolineoptions-class"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="routing/routing-library-sidebar.html" data-below-sidebar="routing/IsolineOptions-class-sidebar.html">

<div>

# <span class="kind-class">IsolineOptions</span> class

</div>

<div class="section desc markdown">

Specifies options for isolines calculation.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-explore-routing-isolineoptions-isolineoptions-withcaroptions" class="deprecated">IsolineOptions.withCarOptions</a></span><span class="signature">(<span id="sdk-for-flutter-explore-withCarOptions-param-calculationOptions" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-routing-isolineoptionscalculation-class">IsolineOptionsCalculation</a></span> <span class="parameter-name">calculationOptions</span>, </span><span id="sdk-for-flutter-explore-withCarOptions-param-carOptions" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-routing-caroptions-class" class="deprecated">CarOptions</a></span> <span class="parameter-name">carOptions</span></span>)</span>  
Constructs options to calculate isolines from destination or origin, with preferences for isoline calculation and car routing options.

<div class="constructor-modifier features">

factory

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-isolineoptions-isolineoptions-withevcaroptions" class="deprecated">IsolineOptions.withEVCarOptions</a></span><span class="signature">(<span id="sdk-for-flutter-explore-withEVCarOptions-param-calculationOptions" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-routing-isolineoptionscalculation-class">IsolineOptionsCalculation</a></span> <span class="parameter-name">calculationOptions</span>, </span><span id="sdk-for-flutter-explore-withEVCarOptions-param-evCarOptions" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-routing-evcaroptions-class" class="deprecated">EVCarOptions</a></span> <span class="parameter-name">evCarOptions</span></span>)</span>  
Constructs options to calculate isolines from destination or origin, with preferences for isoline calculation and electric car routing options.

<div class="constructor-modifier features">

factory

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-isolineoptions-isolineoptions-withevtruckoptions" class="deprecated">IsolineOptions.withEVTruckOptions</a></span><span class="signature">(<span id="sdk-for-flutter-explore-withEVTruckOptions-param-calculationOptions" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-routing-isolineoptionscalculation-class">IsolineOptionsCalculation</a></span> <span class="parameter-name">calculationOptions</span>, </span><span id="sdk-for-flutter-explore-withEVTruckOptions-param-evTruckOptions" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-routing-evtruckoptions-class" class="deprecated">EVTruckOptions</a></span> <span class="parameter-name">evTruckOptions</span></span>)</span>  
Constructs options to calculate isolines from destination or origin, with preferences for isoline calculation and electric truck routing options.

<div class="constructor-modifier features">

factory

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-isolineoptions-isolineoptions-withroutingoptions">IsolineOptions.withRoutingOptions</a></span><span class="signature">(<span id="sdk-for-flutter-explore-withRoutingOptions-param-calculationOptions" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-routing-isolineoptionscalculation-class">IsolineOptionsCalculation</a></span> <span class="parameter-name">calculationOptions</span>, </span><span id="sdk-for-flutter-explore-withRoutingOptions-param-routingOptions" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-routing-routingoptions-class">RoutingOptions</a></span> <span class="parameter-name">routingOptions</span></span>)</span>  
Constructs options to calculate isolines from destination or origin, with preferences for isoline calculation and routing options.

<div class="constructor-modifier features">

factory

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-isolineoptions-isolineoptions-withtruckoptions" class="deprecated">IsolineOptions.withTruckOptions</a></span><span class="signature">(<span id="sdk-for-flutter-explore-withTruckOptions-param-calculationOptions" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-routing-isolineoptionscalculation-class">IsolineOptionsCalculation</a></span> <span class="parameter-name">calculationOptions</span>, </span><span id="sdk-for-flutter-explore-withTruckOptions-param-truckOptions" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-routing-truckoptions-class" class="deprecated">TruckOptions</a></span> <span class="parameter-name">truckOptions</span></span>)</span>  
Constructs options to calculate isolines from destination or origin, with preferences for isoline calculation and truck routing options.

<div class="constructor-modifier features">

factory

</div>

## Properties

<span class="name"><a href="sdk-for-flutter-explore-routing-isolineoptions-calculationoptions">calculationOptions</a></span> <span class="signature">↔ <a href="sdk-for-flutter-explore-routing-isolineoptionscalculation-class">IsolineOptionsCalculation</a></span>  
Specifies isoline parameters.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-isolineoptions-caroptions" class="deprecated">carOptions</a></span> <span class="signature">↔ <a href="sdk-for-flutter-explore-routing-caroptions-class" class="deprecated">CarOptions</a>?</span>  
Specifies options for calculation of isolines for car. Mutually exclusive with <a href="sdk-for-flutter-explore-routing-isolineoptions-truckoptions" class="deprecated">IsolineOptions.truckOptions</a>, <a href="sdk-for-flutter-explore-routing-isolineoptions-evcaroptions" class="deprecated">IsolineOptions.evCarOptions</a>, <a href="sdk-for-flutter-explore-routing-isolineoptions-evtruckoptions" class="deprecated">IsolineOptions.evTruckOptions</a> and <a href="sdk-for-flutter-explore-routing-isolineoptions-routingoptions">IsolineOptions.routingOptions</a>.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-isolineoptions-evcaroptions" class="deprecated">evCarOptions</a></span> <span class="signature">↔ <a href="sdk-for-flutter-explore-routing-evcaroptions-class" class="deprecated">EVCarOptions</a>?</span>  
Specifies options for calculation of isolines for electric car. Mutually exclusive with <a href="sdk-for-flutter-explore-routing-isolineoptions-caroptions" class="deprecated">IsolineOptions.carOptions</a>, <a href="sdk-for-flutter-explore-routing-isolineoptions-truckoptions" class="deprecated">IsolineOptions.truckOptions</a>, <a href="sdk-for-flutter-explore-routing-isolineoptions-evtruckoptions" class="deprecated">IsolineOptions.evTruckOptions</a> and <a href="sdk-for-flutter-explore-routing-isolineoptions-routingoptions">IsolineOptions.routingOptions</a>.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-isolineoptions-evtruckoptions" class="deprecated">evTruckOptions</a></span> <span class="signature">↔ <a href="sdk-for-flutter-explore-routing-evtruckoptions-class" class="deprecated">EVTruckOptions</a>?</span>  
Specifies options for calculation of isolines for electric truck. Mutually exclusive with <a href="sdk-for-flutter-explore-routing-isolineoptions-caroptions" class="deprecated">IsolineOptions.carOptions</a>, <a href="sdk-for-flutter-explore-routing-isolineoptions-truckoptions" class="deprecated">IsolineOptions.truckOptions</a>, <a href="sdk-for-flutter-explore-routing-isolineoptions-evcaroptions" class="deprecated">IsolineOptions.evCarOptions</a> and <a href="sdk-for-flutter-explore-routing-isolineoptions-routingoptions">IsolineOptions.routingOptions</a>.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-isolineoptions-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-isolineoptions-routingoptions">routingOptions</a></span> <span class="signature">↔ <a href="sdk-for-flutter-explore-routing-routingoptions-class">RoutingOptions</a>?</span>  
Specifies options for calculation of isolines for any vehicle type. Mutually exclusive with <a href="sdk-for-flutter-explore-routing-isolineoptions-caroptions" class="deprecated">IsolineOptions.carOptions</a>, <a href="sdk-for-flutter-explore-routing-isolineoptions-truckoptions" class="deprecated">IsolineOptions.truckOptions</a>, <a href="sdk-for-flutter-explore-routing-isolineoptions-evcaroptions" class="deprecated">IsolineOptions.evCarOptions</a> and <a href="sdk-for-flutter-explore-routing-isolineoptions-evtruckoptions" class="deprecated">IsolineOptions.evTruckOptions</a>.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-isolineoptions-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-isolineoptions-truckoptions" class="deprecated">truckOptions</a></span> <span class="signature">↔ <a href="sdk-for-flutter-explore-routing-truckoptions-class" class="deprecated">TruckOptions</a>?</span>  
Specifies options for calculation of isolines for truck. Mutually exclusive with <a href="sdk-for-flutter-explore-routing-isolineoptions-caroptions" class="deprecated">IsolineOptions.carOptions</a>, <a href="sdk-for-flutter-explore-routing-isolineoptions-evcaroptions" class="deprecated">IsolineOptions.evCarOptions</a>, <a href="sdk-for-flutter-explore-routing-isolineoptions-evtruckoptions" class="deprecated">IsolineOptions.evTruckOptions</a> and <a href="sdk-for-flutter-explore-routing-isolineoptions-routingoptions">IsolineOptions.routingOptions</a>.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-explore-routing-isolineoptions-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-isolineoptions-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-explore-routing-isolineoptions-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

