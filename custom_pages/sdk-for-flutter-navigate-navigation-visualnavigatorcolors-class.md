---
title: "VisualNavigatorColors class - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-visualnavigatorcolors-class"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/navigation-library-sidebar.html" data-below-sidebar="navigation/VisualNavigatorColors-class-sidebar.html">

<div>

# <span class="kind-class">VisualNavigatorColors</span> class <a href="https://dart.dev/language/class-modifiers#abstract" class="feature feature-abstract" title="This type can not be directly constructed.">abstract</a>

</div>

<div class="section desc markdown">

This class contains colors used by <a href="sdk-for-flutter-navigate-navigation-visualnavigator-class">VisualNavigator</a> to render the route and the maneuver arrow visualization.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-navigation-visualnavigatorcolors-visualnavigatorcolors">VisualNavigatorColors</a></span><span class="signature">()</span>  

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-navigation-visualnavigatorcolors-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-visualnavigatorcolors-maneuverarrowcolor">maneuverArrowColor</a></span> <span class="signature">↔ Color</span>  
Maneuver arrow color. The object containing color used to draw maneuver arrows on the route to highlight lane directions at the end of a street. The alpha channel is ignored. The color is interpreted as fully opaque. Gets the color used to draw maneuver arrows on the route.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-visualnavigatorcolors-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-visualnavigatorcolors-trafficonroutecolors">trafficOnRouteColors</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-navigation-trafficonroutecolors-class">TrafficOnRouteColors</a></span>  
Colors used to visualize traffic conditions on the route ahead of the current location, for segments with a jam factor of 4.0 or higher. For route segments with a jam factor below 4.0 and those behind the current location, <a href="sdk-for-flutter-navigate-navigation-routeprogresscolors-class">RouteProgressColors</a> are used instead. Gets colors used for visualization of traffic conditions on route.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-navigation-visualnavigatorcolors-getrouteprogresscolors">getRouteProgressColors</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-getRouteProgressColors-param-sectionTransportMode" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-sectiontransportmode">SectionTransportMode</a></span> <span class="parameter-name">sectionTransportMode</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-navigation-routeprogresscolors-class">RouteProgressColors</a></span> </span>  
Gets route color for visualization.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-visualnavigatorcolors-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-visualnavigatorcolors-setrouteprogresscolors">setRouteProgressColors</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-setRouteProgressColors-param-sectionTransportMode" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-sectiontransportmode">SectionTransportMode</a></span> <span class="parameter-name">sectionTransportMode</span>, </span><span id="sdk-for-flutter-navigate-setRouteProgressColors-param-routeProgressColors" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-routeprogresscolors-class">RouteProgressColors</a></span> <span class="parameter-name">routeProgressColors</span></span>) <span class="returntype parameter">→ void</span> </span>  
Sets route color for visualization.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-visualnavigatorcolors-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-navigation-visualnavigatorcolors-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

## Static Methods

<span class="name"><a href="sdk-for-flutter-navigate-navigation-visualnavigatorcolors-daycolors">dayColors</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-navigation-visualnavigatorcolors-class">VisualNavigatorColors</a></span> </span>  
Retrieves HERE day color presets for route and maneuver arrow visualization.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-visualnavigatorcolors-nightcolors">nightColors</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-navigation-visualnavigatorcolors-class">VisualNavigatorColors</a></span> </span>  
Retrieves HERE night color presets for route and maneuver arrow visualization.

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

