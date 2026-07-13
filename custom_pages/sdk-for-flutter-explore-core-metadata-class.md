---
title: "Metadata class - core library - Dart API"
slug: "sdk-for-flutter-explore-core-metadata-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- Metadata-class.html -->
<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="core/core-library-sidebar.html" data-below-sidebar="core/Metadata-class-sidebar.html">

<div>

# <span class="kind-class">Metadata</span> class <a href="https://dart.dev/language/class-modifiers#abstract" class="feature feature-abstract" title="This type can not be directly constructed.">abstract</a>

</div>

<div class="section desc markdown">

Holds metadata on behalf of a map item.

An instance of this class can contain metadata items of varying types, such as String, Integer, Double, GeoCoordinates etc. and can also hold arbitrary metadata types by the use of the CustomMetadataValue abstract class.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-explore-core-metadata-metadata">Metadata</a></span><span class="signature">()</span>  
Creates an instance of this class.

<div class="constructor-modifier features">

factory

</div>

## Properties

<span class="name"><a href="sdk-for-flutter-explore-core-metadata-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-core-metadata-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-explore-core-metadata-getcustomvalue">getCustomValue</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-getCustomValue-param-key" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">key</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-explore-core-custommetadatavalue-class">CustomMetadataValue</a>?</span> </span>  
Obtains an instance of the CustomMetadataValue class associated with a given key.

<span class="name"><a href="sdk-for-flutter-explore-core-metadata-getdouble">getDouble</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-getDouble-param-key" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">key</span></span>) <span class="returntype parameter">→ double?</span> </span>  
Obtains a Double value associated with a given key.

<span class="name"><a href="sdk-for-flutter-explore-core-metadata-getgeocoordinates">getGeoCoordinates</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-getGeoCoordinates-param-key" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">key</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-explore-core-geocoordinates-class">GeoCoordinates</a>?</span> </span>  
Obtains a GeoCoordinates value associated with a given key.

<span class="name"><a href="sdk-for-flutter-explore-core-metadata-getinteger">getInteger</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-getInteger-param-key" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">key</span></span>) <span class="returntype parameter">→ int?</span> </span>  
Obtains an Integer value associated with a given key.

<span class="name"><a href="sdk-for-flutter-explore-core-metadata-getstring">getString</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-getString-param-key" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">key</span></span>) <span class="returntype parameter">→ String?</span> </span>  
Obtains a String value associated with a given key.

<span class="name"><a href="sdk-for-flutter-explore-core-metadata-gettype">getType</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-getType-param-key" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">key</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-explore-core-metadatatype">MetadataType</a>?</span> </span>  
Determines the type of a metadata value.

<span class="name"><a href="sdk-for-flutter-explore-core-metadata-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-core-metadata-removevalue">removeValue</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-removeValue-param-key" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">key</span></span>) <span class="returntype parameter">→ void</span> </span>  
Removes a metadata key and its associated value.

<span class="name"><a href="sdk-for-flutter-explore-core-metadata-setcustomvalue">setCustomValue</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-setCustomValue-param-key" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">key</span>, </span><span id="sdk-for-flutter-explore-setCustomValue-param-value" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-custommetadatavalue-class">CustomMetadataValue</a></span> <span class="parameter-name">value</span></span>) <span class="returntype parameter">→ void</span> </span>  
Creates a key:value pair, where the value is a type derived from CustomMetadataValue.

<span class="name"><a href="sdk-for-flutter-explore-core-metadata-setdouble">setDouble</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-setDouble-param-key" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">key</span>, </span><span id="sdk-for-flutter-explore-setDouble-param-value" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">value</span></span>) <span class="returntype parameter">→ void</span> </span>  
Creates a key:value pair, where the value is of type Double.

<span class="name"><a href="sdk-for-flutter-explore-core-metadata-setgeocoordinates">setGeoCoordinates</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-setGeoCoordinates-param-key" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">key</span>, </span><span id="sdk-for-flutter-explore-setGeoCoordinates-param-value" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-geocoordinates-class">GeoCoordinates</a></span> <span class="parameter-name">value</span></span>) <span class="returntype parameter">→ void</span> </span>  
Creates a key:value pair, where the value is of type GeoCoordinates.

<span class="name"><a href="sdk-for-flutter-explore-core-metadata-setinteger">setInteger</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-setInteger-param-key" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">key</span>, </span><span id="sdk-for-flutter-explore-setInteger-param-value" class="parameter"><span class="type-annotation">int</span> <span class="parameter-name">value</span></span>) <span class="returntype parameter">→ void</span> </span>  
Creates a key:value pair, where the value is of type Integer.

<span class="name"><a href="sdk-for-flutter-explore-core-metadata-setstring">setString</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-setString-param-key" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">key</span>, </span><span id="sdk-for-flutter-explore-setString-param-value" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">value</span></span>) <span class="returntype parameter">→ void</span> </span>  
Creates a key:value pair, where the value is of type String.

<span class="name"><a href="sdk-for-flutter-explore-core-metadata-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-explore-core-metadata-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
