---
title: "CatalogVersionHint class - core.engine library - Dart API"
slug: "sdk-for-flutter-navigate-core.engine-catalogversionhint-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- CatalogVersionHint-class.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="core.engine/core.engine-library-sidebar.html" data-below-sidebar="core.engine/CatalogVersionHint-class-sidebar.html">

<div>

# <span class="kind-class">CatalogVersionHint</span> class <a href="https://dart.dev/language/class-modifiers#abstract" class="feature feature-abstract" title="This type can not be directly constructed.">abstract</a>

</div>

<div class="section desc markdown">

This is a class for capturing user's intent for the desired catalog version to use in <a href="sdk-for-flutter-navigate-core-engine-desiredcatalog-class">DesiredCatalog</a> class.

You can request a specific or latest version of a catalog by calling the static functions <a href="sdk-for-flutter-navigate-core-engine-catalogversionhint-specific">CatalogVersionHint.specific</a> and <a href="sdk-for-flutter-navigate-core-engine-catalogversionhint-latestwithignoringcacheddata">CatalogVersionHint.latestWithIgnoringCachedData</a> respectively. The HERE platform will make the best effort to provide an appropriate version for the catalog based on this version hint. Please take note that for the API <a href="sdk-for-flutter-navigate-core-engine-catalogversionhint-specific">CatalogVersionHint.specific</a> to function properly, it is essential that the mutable and persistent storage should be cleaned.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-core-engine-catalogversionhint-catalogversionhint">CatalogVersionHint</a></span><span class="signature">()</span>  

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-core-engine-catalogversionhint-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-core-engine-catalogversionhint-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-core-engine-catalogversionhint-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-core-engine-catalogversionhint-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-core-engine-catalogversionhint-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

## Static Methods

<span class="name"><a href="sdk-for-flutter-navigate-core-engine-catalogversionhint-latestwithignoringcacheddata">latestWithIgnoringCachedData</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-latestWithIgnoringCachedData-param-ignoreCachedData" class="parameter"><span class="type-annotation">bool</span> <span class="parameter-name">ignoreCachedData</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-core-engine-catalogversionhint-class">CatalogVersionHint</a></span> </span>  
This static method can be called when you are interested in getting the most latest version of a catalog when initializing the HERE SDK with `SDKOptions` where you can specify the catalog(s) you want to use.

<span class="name"><a href="sdk-for-flutter-navigate-core-engine-catalogversionhint-specific">specific</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-specific-param-version" class="parameter"><span class="type-annotation">int</span> <span class="parameter-name">version</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-core-engine-catalogversionhint-class">CatalogVersionHint</a></span> </span>  
This static method is used when you are interested in a specific version of a catalog, that you want to specify manually.

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
