---
title: "EVSearchEngine class - search library - Dart API"
slug: "sdk-for-flutter-explore-search-evsearchengine-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- EVSearchEngine-class.html -->
<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="search/search-library-sidebar.html" data-below-sidebar="search/EVSearchEngine-class-sidebar.html">

<div>

# <span class="kind-class">EVSearchEngine</span> class <a href="https://dart.dev/language/class-modifiers#abstract" class="feature feature-abstract" title="This type can not be directly constructed.">abstract</a>

</div>

<div class="section desc markdown">

The `EVSearchEngine` API provides detailed information about charging locations.

It requires an online connection to execute the requests. A licence is required to use this API. Details can be found in <a href="https://www.here.com/docs/bundle/ev-charge-points-api-v3-developer-guide/page/topics/quick-start-platform.html">HERE EV Charge Points API v3 - Developer Guide</a>.

**Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

</div>

<div class="section">

Implemented types  
- <a href="sdk-for-flutter-explore-search-evsearchinterface-class">EVSearchInterface</a>

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-explore-search-evsearchengine-evsearchengine">EVSearchEngine</a></span><span class="signature">()</span>  
Creates a new instance of this class.

<div class="constructor-modifier features">

factory

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-evsearchengine-evsearchengine-withsdkengine">EVSearchEngine.withSdkEngine</a></span><span class="signature">(<span id="sdk-for-flutter-explore-withSdkEngine-param-sdkEngine" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-engine-sdknativeengine-class">SDKNativeEngine</a></span> <span class="parameter-name">sdkEngine</span></span>)</span>  
Creates a new instance of this class.

<div class="constructor-modifier features">

factory

</div>

## Properties

<span class="name"><a href="sdk-for-flutter-explore-search-evsearchinterface-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-evsearchinterface-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-explore-search-evsearchinterface-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-evsearchinterface-search">search</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-search-param-ids" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter">String</span>\></span></span> <span class="parameter-name">ids</span>, </span><span id="sdk-for-flutter-explore-search-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-search-evsearchcallback">EVSearchCallback</a></span> <span class="parameter-name">callback</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-explore-core-threading-taskhandle-class">TaskHandle</a></span> </span>  
Performs an asynchronous request for <a href="sdk-for-flutter-explore-search-evcharginglocation-class">EVChargingLocation</a> instances with given Place IDs.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-evsearchengine-setoptions">setOptions</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-setOptions-param-options" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-search-evsearchoptions-class">EVSearchOptions</a></span> <span class="parameter-name">options</span></span>) <span class="returntype parameter">→ void</span> </span>  
Configures the behavior of `EVSearchEngine` using the provided input options.

<span class="name"><a href="sdk-for-flutter-explore-search-evsearchinterface-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-explore-search-evsearchinterface-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
