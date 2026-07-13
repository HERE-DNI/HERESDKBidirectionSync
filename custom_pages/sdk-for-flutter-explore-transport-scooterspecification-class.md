---
title: "ScooterSpecification class - transport library - Dart API"
slug: "sdk-for-flutter-explore-transport-scooterspecification-class"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="transport/transport-library-sidebar.html" data-below-sidebar="transport/ScooterSpecification-class-sidebar.html">

<div>

# <span class="kind-class">ScooterSpecification</span> class

</div>

<div class="section desc markdown">

Scooter specific settings.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-explore-transport-scooterspecification-scooterspecification">ScooterSpecification</a></span><span class="signature">()</span>  

## Properties

<span class="name"><a href="sdk-for-flutter-explore-transport-scooterspecification-allowscooteronhighway">allowScooterOnHighway</a></span> <span class="signature">↔ bool</span>  
Specifies whether scooter is allowed on highway or not. `True` means scooter is allowed to use highways and `false` means otherwise. Defaults to `false`. Note that there is a similar parameter in `AvoidanceOptions`, to disallow highway usage, see `RoadFeatures.CONTROLLED_ACCESS_HIGHWAY`. As the avoidance options takes precedence, if this parameter is also used, then scooters are not allowed to use highways even if `allowHighway` is set to `true`. However, if no alternative route is possible, the calculated route may use highways. In such a case, a `SectionNotice` will be provided in the related `Section` to indicate that the highway usage restriction is violated on this route. A few examples:

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-transport-scooterspecification-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-transport-scooterspecification-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-explore-transport-scooterspecification-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-transport-scooterspecification-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-explore-transport-scooterspecification-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

