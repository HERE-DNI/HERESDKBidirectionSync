---
title: "RoadShieldIconProperties class - mapview library - Dart API"
slug: "sdk-for-flutter-navigate-mapview-roadshieldiconproperties-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- RoadShieldIconProperties-class.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/mapview-library-sidebar.html" data-below-sidebar="mapview/RoadShieldIconProperties-class-sidebar.html">

<div>

# <span class="kind-class">RoadShieldIconProperties</span> class

</div>

<div class="section desc markdown">

Contains the information required to create a road shield image.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-mapview-roadshieldiconproperties-roadshieldiconproperties">RoadShieldIconProperties</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-param-routeType" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-routetype">RouteType</a></span> <span class="parameter-name">routeType</span>, </span><span id="sdk-for-flutter-navigate-param-countryCode" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">countryCode</span>, </span><span id="sdk-for-flutter-navigate-param-stateCode" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">stateCode</span>, </span><span id="sdk-for-flutter-navigate-param-routeNumberName" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">routeNumberName</span>, </span><span id="sdk-for-flutter-navigate-param-shieldText" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">shieldText</span></span>)</span>  
Creates a new instance.

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-mapview-roadshieldiconproperties-countrycode">countryCode</a></span> <span class="signature">↔ String</span>  
The country code in ISO-3166-1 alpha-3 format, which will determine the type of road shield.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-roadshieldiconproperties-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-roadshieldiconproperties-routenumbername">routeNumberName</a></span> <span class="signature">↔ String</span>  
A string that is used to additionally determine the road shield's visual representation. In a routing context, the text can be taken from a `LocalizedRoadNumber`, which is available for each `Span` of a `Route` object. Typically, the string contains the number of a road, such as "E100". Internally, the text is parsed with a RegEx pattern and the results will be used along with other properties such as `routeType`, `countryCode` and `stateCode` to identify the visual representation of a road shield icon.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-roadshieldiconproperties-routetype">routeType</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-core-routetype">RouteType</a></span>  
The type of route indicating the significance of the road in a range from 0 to 6. A value of 1 stands for the most major route and 6 the most minor, with 0 being of unknown type.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-roadshieldiconproperties-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-roadshieldiconproperties-shieldtext">shieldText</a></span> <span class="signature">↔ String</span>  
The text of the road-shield. This is the text which is displayed on the road-shield in reality. It will be in the output road-shield icon.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-roadshieldiconproperties-statecode">stateCode</a></span> <span class="signature">↔ String</span>  
The state code for the road. It's a 2-letter code in ISO 3166-2 format. For example the ones listed for US on this page <https://en.wikipedia.org/wiki/ISO_3166-2:US>. The code "AL" is for Alabama. Another example is the code for autonomous communities listed on <https://en.wikipedia.org/wiki/ISO_3166-2:ES>. Can be empty if not required for the particular country.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-mapview-roadshieldiconproperties-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-roadshieldiconproperties-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-mapview-roadshieldiconproperties-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
