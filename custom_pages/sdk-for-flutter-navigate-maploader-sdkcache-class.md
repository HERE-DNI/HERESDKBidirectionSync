---
title: "SDKCache class - maploader library - Dart API"
slug: "sdk-for-flutter-navigate-maploader-sdkcache-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- SDKCache-class.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="maploader/maploader-library-sidebar.html" data-below-sidebar="maploader/SDKCache-class-sidebar.html">

<div>

# <span class="kind-class">SDKCache</span> class <a href="https://dart.dev/language/class-modifiers#abstract" class="feature feature-abstract" title="This type can not be directly constructed.">abstract</a>

</div>

<div class="section desc markdown">

A class to manage SDK Cache.

Path for SDKCache is specified via <a href="sdk-for-flutter-navigate-core-engine-sdkoptions-cachepath">SDKOptions.cachePath</a>. SDKCache manages temporary downloaded map data during map interaction and follows LRU (least recently used) strategy to delete map data when cache size exceeds the specified <a href="sdk-for-flutter-navigate-core-engine-sdkoptions-cachesizeinbytes">SDKOptions.cacheSizeInBytes</a>.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-maploader-sdkcache-sdkcache">SDKCache</a></span><span class="signature">()</span>  

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-maploader-sdkcache-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-maploader-sdkcache-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-maploader-sdkcache-clearappcache">clearAppCache</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-clearAppCache-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-maploader-sdkcachecallback">SDKCacheCallback</a></span> <span class="parameter-name">callback</span></span>) <span class="returntype parameter">→ void</span> </span>  
Clears all data that is currently stored in the SDK cache.

<span class="name"><a href="sdk-for-flutter-navigate-maploader-sdkcache-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-maploader-sdkcache-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-maploader-sdkcache-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

## Static Methods

<span class="name"><a href="sdk-for-flutter-navigate-maploader-sdkcache-fromsdkengine">fromSdkEngine</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-fromSdkEngine-param-sdkEngine" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-engine-sdknativeengine-class">SDKNativeEngine</a></span> <span class="parameter-name">sdkEngine</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-maploader-sdkcache-class">SDKCache</a></span> </span>  
Gets a single instance of this class per provided <a href="sdk-for-flutter-navigate-core-engine-sdknativeengine-class">SDKNativeEngine</a>.

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
