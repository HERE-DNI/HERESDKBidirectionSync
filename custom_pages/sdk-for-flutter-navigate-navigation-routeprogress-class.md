---
title: "RouteProgress class - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-routeprogress-class"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/navigation-library-sidebar.html" data-below-sidebar="navigation/RouteProgress-class-sidebar.html">

<div>

# <span class="kind-class">RouteProgress</span> class

</div>

<div class="section desc markdown">

Contains all the relevant information on the user's progress along a route.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-navigation-routeprogress-routeprogress">RouteProgress</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-param-sectionProgress" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-navigation-sectionprogress-class">SectionProgress</a></span>\></span></span> <span class="parameter-name">sectionProgress</span>, </span><span id="sdk-for-flutter-navigate-param-maneuverProgress" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-navigation-maneuverprogress-class">ManeuverProgress</a></span>\></span></span> <span class="parameter-name">maneuverProgress</span></span>)</span>  

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-navigation-routeprogress-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-routeprogress-maneuverprogress">maneuverProgress</a></span> <span class="signature">↔ List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-navigation-maneuverprogress-class">ManeuverProgress</a></span>\></span></span>  
The progress for next and next-next maneuvers (see <a href="sdk-for-flutter-navigate-routing-maneuver-class">Maneuver</a>). Note that the list can contain at maximum two items (for next and next-next maneuvers) and one or zero when approaching the destination.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-routeprogress-routematchedlocation">routeMatchedLocation</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-navigation-routematchedlocation-class">RouteMatchedLocation</a></span>  
Route matched location.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-routeprogress-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-routeprogress-sectionindex" class="deprecated">sectionIndex</a></span> <span class="signature">↔ int</span>  
Index of the <a href="sdk-for-flutter-navigate-routing-section-class">Section</a> in the route. Note that this section index does not point to the current <a href="sdk-for-flutter-navigate-navigation-sectionprogress-class">SectionProgress</a> but to the route <a href="sdk-for-flutter-navigate-routing-section-class">Section</a> that you can access via <a href="sdk-for-flutter-navigate-navigation-navigatorinterface-route">NavigatorInterface.route</a> and <a href="sdk-for-flutter-navigate-routing-route-sections">Route.sections</a>.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-routeprogress-sectionprogress">sectionProgress</a></span> <span class="signature">↔ List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-navigation-sectionprogress-class">SectionProgress</a></span>\></span></span>  
The progress for each <a href="sdk-for-flutter-navigate-routing-section-class">Section</a> from the current one to the last one. Note that the progress information is accumulated successively, therefore information relative to the final destination is in the last item of the list. The list is guaranteed to be non-empty.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-routeprogress-spanindex" class="deprecated">spanIndex</a></span> <span class="signature">↔ int</span>  
Index of the <a href="sdk-for-flutter-navigate-routing-span-class">Span</a> in the route section.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-navigation-routeprogress-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-routeprogress-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-navigation-routeprogress-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

