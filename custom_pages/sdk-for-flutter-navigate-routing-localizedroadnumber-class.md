---
title: "LocalizedRoadNumber class - routing library - Dart API"
slug: "sdk-for-flutter-navigate-routing-localizedroadnumber-class"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="routing/routing-library-sidebar.html" data-below-sidebar="routing/LocalizedRoadNumber-class-sidebar.html">

<div>

# <span class="kind-class">LocalizedRoadNumber</span> class

</div>

<div class="section desc markdown">

Used to represent road number localized to specific language with optional direction and route type information.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-routing-localizedroadnumber-localizedroadnumber">LocalizedRoadNumber</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-param-localizedNumber" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-localizedtext-class">LocalizedText</a></span> <span class="parameter-name">localizedNumber</span>, </span><span id="sdk-for-flutter-navigate-param-routeType" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-routetype">RouteType</a></span> <span class="parameter-name">routeType</span></span>)</span>  

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-routing-localizedroadnumber-direction">direction</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-core-cardinaldirection">CardinalDirection</a>?</span>  
Road direction. This property indicates the official directional identifier assigned to highways. Can be `null` when direction is not assigned to highways. The direction indicates the same information as on the signpost shield: For example, if is "101 West", the directions contains WEST. Note that the official direction is not necessarily the travel direction. For example, US-101 through the city of Sunnyvale is physically located East to West. However, the official direction on sign is North/South.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-localizedroadnumber-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-localizedroadnumber-localizednumber">localizedNumber</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-core-localizedtext-class">LocalizedText</a></span>  
Road number with locale information.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-localizedroadnumber-routetype">routeType</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-core-routetype">RouteType</a></span>  
The route type of the LocalizedRoadNumber.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-localizedroadnumber-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-routing-localizedroadnumber-gettextwithdirection">getTextWithDirection</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
Returns the whole road number information including its cardinal direction.

<span class="name"><a href="sdk-for-flutter-navigate-routing-localizedroadnumber-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-localizedroadnumber-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-routing-localizedroadnumber-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

