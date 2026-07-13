---
title: "W3WSearchEngine class - search library - Dart API"
slug: "sdk-for-flutter-navigate-search-w3wsearchengine-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- W3WSearchEngine-class.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="search/search-library-sidebar.html" data-below-sidebar="search/W3WSearchEngine-class-sidebar.html">

<div>

# <span class="kind-class">W3WSearchEngine</span> class <a href="https://dart.dev/language/class-modifiers#abstract" class="feature feature-abstract" title="This type can not be directly constructed.">abstract</a>

</div>

<div class="section desc markdown">

what3words is an alternative geocode system designed to identify any location on the planet.

The system divides the world into a grid of 57 trillion 3-by-3-metre squares, each of which has a three-word address. For example, the front door of HERE’s Berlin office is identified by "///wage.mere.heap". `W3WSearchEngine` allows you to convert 3 word addresses to coordinates and also coordinates to 3 word addresses.

**Note:** Using W3WSearchEngine requires a licence to access HERE what3words APIs.

**Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-search-w3wsearchengine-w3wsearchengine">W3WSearchEngine</a></span><span class="signature">()</span>  
Creates a new instance of this class.

<div class="constructor-modifier features">

factory

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-w3wsearchengine-w3wsearchengine-withsdkengine">W3WSearchEngine.withSdkEngine</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-withSdkEngine-param-sdkEngine" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-engine-sdknativeengine-class">SDKNativeEngine</a></span> <span class="parameter-name">sdkEngine</span></span>)</span>  
Creates a new instance of this class.

<div class="constructor-modifier features">

factory

</div>

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-search-w3wsearchengine-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-w3wsearchengine-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-search-w3wsearchengine-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-w3wsearchengine-searchbycoordinates">searchByCoordinates</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-searchByCoordinates-param-coordinates" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-geocoordinates-class">GeoCoordinates</a></span> <span class="parameter-name">coordinates</span>, </span><span id="sdk-for-flutter-navigate-searchByCoordinates-param-language" class="parameter"><span class="type-annotation">String?</span> <span class="parameter-name">language</span>, </span><span id="sdk-for-flutter-navigate-searchByCoordinates-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-search-w3wsearchcallback">W3WSearchCallback</a></span> <span class="parameter-name">callback</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a></span> </span>  
Performs an asynchronous request to search for a <a href="sdk-for-flutter-navigate-search-w3wsquare-class">W3WSquare</a>, which includes the 3 word address, that corresponds to the given coordinates.

<span class="name"><a href="sdk-for-flutter-navigate-search-w3wsearchengine-searchbywords">searchByWords</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-searchByWords-param-words" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">words</span>, </span><span id="sdk-for-flutter-navigate-searchByWords-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-search-w3wsearchcallback">W3WSearchCallback</a></span> <span class="parameter-name">callback</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a></span> </span>  
Performs an asynchronous request to search for a <a href="sdk-for-flutter-navigate-search-w3wsquare-class">W3WSquare</a> that corresponds to the given 3 words.

<span class="name"><a href="sdk-for-flutter-navigate-search-w3wsearchengine-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-search-w3wsearchengine-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
