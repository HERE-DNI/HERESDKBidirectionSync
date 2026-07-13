---
title: "MyPlaces class - search library - Dart API"
slug: "sdk-for-flutter-navigate-search-myplaces-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MyPlaces-class.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="search/search-library-sidebar.html" data-below-sidebar="search/MyPlaces-class-sidebar.html">

<div>

# <span class="kind-class">MyPlaces</span> class <a href="https://dart.dev/language/class-modifiers#abstract" class="feature feature-abstract" title="This type can not be directly constructed.">abstract</a>

</div>

<div class="section desc markdown">

Provides means to populate personal places data source.

Also acts as a owner of the collection of personal places. MyPlaces is memory-only object: nothing is persisted and/or sent over the network. Client has full control on how to store personal places.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-search-myplaces-myplaces">MyPlaces</a></span><span class="signature">()</span>  
Creates a new instance of this class.

<div class="constructor-modifier features">

factory

</div>

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-search-myplaces-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-myplaces-places">places</a></span> <span class="signature">→ List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-search-geoplace-class">GeoPlace</a></span>\></span></span>  
The list of places which currently belong to this data source. This list is a clone of the internal list and thus changing it has no effect on the data source. Gets the list of places which currently belongs to this data source. The returned list is a clone of the internal list and thus changing it has no effect on the data source.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-myplaces-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-search-myplaces-addplace">addPlace</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-addPlace-param-place" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-search-geoplace-class">GeoPlace</a></span> <span class="parameter-name">place</span>, </span><span id="sdk-for-flutter-navigate-addPlace-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-threading-ontaskcompleted">OnTaskCompleted</a></span> <span class="parameter-name">callback</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a></span> </span>  
Adds a place to this data source.

<span class="name"><a href="sdk-for-flutter-navigate-search-myplaces-addplaces">addPlaces</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-addPlaces-param-places" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-search-geoplace-class">GeoPlace</a></span>\></span></span> <span class="parameter-name">places</span>, </span><span id="sdk-for-flutter-navigate-addPlaces-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-threading-ontaskcompleted">OnTaskCompleted</a></span> <span class="parameter-name">callback</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a></span> </span>  
Adds a list of places to this data source.

<span class="name"><a href="sdk-for-flutter-navigate-search-myplaces-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-myplaces-removeall">removeAll</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-removeAll-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-threading-ontaskcompleted">OnTaskCompleted</a></span> <span class="parameter-name">callback</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a></span> </span>  
Removes all places from this data source.

<span class="name"><a href="sdk-for-flutter-navigate-search-myplaces-removeplace">removePlace</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-removePlace-param-placeId" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">placeId</span>, </span><span id="sdk-for-flutter-navigate-removePlace-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-threading-ontaskcompleted">OnTaskCompleted</a></span> <span class="parameter-name">callback</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a></span> </span>  
Removes a place from this data source.

<span class="name"><a href="sdk-for-flutter-navigate-search-myplaces-removeplaces">removePlaces</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-removePlaces-param-placeIds" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter">String</span>\></span></span> <span class="parameter-name">placeIds</span>, </span><span id="sdk-for-flutter-navigate-removePlaces-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-threading-ontaskcompleted">OnTaskCompleted</a></span> <span class="parameter-name">callback</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a></span> </span>  
Removes a list of places from this data source.

<span class="name"><a href="sdk-for-flutter-navigate-search-myplaces-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-search-myplaces-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
