---
title: "WidgetPin class - mapview library - Dart API"
slug: "sdk-for-flutter-explore-mapview-widgetpin-class"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/mapview-library-sidebar.html" data-below-sidebar="mapview/WidgetPin-class-sidebar.html">

<div>

# <span class="kind-class">WidgetPin</span> class <a href="https://dart.dev/language/class-modifiers#abstract" class="feature feature-abstract" title="This type can not be directly constructed.">abstract</a>

</div>

<div class="section desc markdown">

Controller for a `Widget` pinned at a fixed geographical location on the map.

A pinned Widget tracks the geographical location as the map is being manipulated. It behaves like a <a href="sdk-for-flutter-explore-mapview-mapmarker-class">MapMarker</a>, only it's a regular Flutter Widget and is not part of normal map rendering.

WidgetPin allows modifying the geographical location of the pinned Widget as well as its placement relative to it.

Use <a href="sdk-for-flutter-explore-mapview-heremapcontroller-pinwidget">HereMapController.pinWidget</a> to pin (add) a `Widget` to a map and obtain in instance of <a href="sdk-for-flutter-explore-mapview-widgetpin-class">WidgetPin</a> that controls it.

To unpin (remove) a Widget from the map, use <a href="sdk-for-flutter-explore-mapview-heremapcontroller-unpinwidget">HereMapController.unpinWidget</a>. or <a href="sdk-for-flutter-explore-mapview-widgetpin-unpin">WidgetPin.unpin</a>.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-explore-mapview-widgetpin-widgetpin">WidgetPin</a></span><span class="signature">({<span id="sdk-for-flutter-explore-param-child" class="parameter">required <span class="type-annotation">Widget</span> <span class="parameter-name">child</span>, </span><span id="sdk-for-flutter-explore-param-coordinates" class="parameter">required <span class="type-annotation"><a href="sdk-for-flutter-explore-core-geocoordinates-class">GeoCoordinates</a></span> <span class="parameter-name">coordinates</span>, </span><span id="sdk-for-flutter-explore-param-anchor" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-anchor2d-class">Anchor2D</a>?</span> <span class="parameter-name">anchor</span>, </span><span id="sdk-for-flutter-explore-param-onChange" class="parameter"><span class="type-annotation">dynamic</span> <span class="parameter-name">onChange</span>()?, </span><span id="sdk-for-flutter-explore-param-onUnpin" class="parameter"><span class="type-annotation">dynamic</span> <span class="parameter-name">onUnpin</span>(<span id="sdk-for-flutter-explore-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-widgetpin-class">WidgetPin</a></span></span>)?</span>})</span>  
Creates a <a href="sdk-for-flutter-explore-mapview-widgetpin-class">WidgetPin</a> displaying child `Widget` at coordinates location on the map Don't use this constructor directly. Instead use <a href="sdk-for-flutter-explore-mapview-heremapcontroller-pinwidget">HereMapController.pinWidget</a> to create a <a href="sdk-for-flutter-explore-mapview-widgetpin-class">WidgetPin</a>.

<div class="constructor-modifier features">

factory

</div>

## Properties

<span class="name"><a href="sdk-for-flutter-explore-mapview-widgetpin-anchor">anchor</a></span> <span class="signature">↔ <a href="sdk-for-flutter-explore-core-anchor2d-class">Anchor2D</a></span>  
Gets pinned `Widget`'s placement relative to geographical location,

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-mapview-widgetpin-child">child</a></span> <span class="signature">→ Widget</span>  
The pinned Widget controlled by this <a href="sdk-for-flutter-explore-mapview-widgetpin-class">WidgetPin</a>.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-mapview-widgetpin-coordinates">coordinates</a></span> <span class="signature">↔ <a href="sdk-for-flutter-explore-core-geocoordinates-class">GeoCoordinates</a></span>  
Gets geographical location of the <a href="sdk-for-flutter-explore-mapview-widgetpin-class">WidgetPin</a>.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-mapview-widgetpin-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-mapview-widgetpin-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-explore-mapview-widgetpin-makewidget">makeWidget</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-makeWidget-param-context" class="parameter"><span class="type-annotation">BuildContext</span> <span class="parameter-name">context</span></span>) <span class="returntype parameter">→ Widget</span> </span>  
Creates a widget for this <a href="sdk-for-flutter-explore-mapview-widgetpin-class">WidgetPin</a>.

<span class="name"><a href="sdk-for-flutter-explore-mapview-widgetpin-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-mapview-widgetpin-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-mapview-widgetpin-unpin">unpin</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ dynamic</span> </span>  
Removes this <a href="sdk-for-flutter-explore-mapview-widgetpin-class">WidgetPin</a> from the map.

<span class="name"><a href="sdk-for-flutter-explore-mapview-widgetpin-updatescreenposition">updateScreenPosition</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-updateScreenPosition-param-screenPosition" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-point2d-class">Point2D</a>?</span> <span class="parameter-name">screenPosition</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  

## Operators

<span class="name"><a href="sdk-for-flutter-explore-mapview-widgetpin-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

