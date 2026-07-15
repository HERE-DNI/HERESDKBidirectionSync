---
title: "DesiredCatalog class - core.engine library - Dart API"
slug: "sdk-for-flutter-navigate-core-engine-desiredcatalog-class"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="core.engine/core.engine-library-sidebar.html" data-below-sidebar="core.engine/DesiredCatalog-class-sidebar.html">

<div>

# <span class="kind-class">DesiredCatalog</span> class

</div>

<div class="section desc markdown">

This class provides an interface to the user, to identify a catalog on the HERE platform, whose data he wants to access.

The user can specify the HERE Resource Name (HRN) for the catalog along with a hint for the desired version. If the desired version is not available, the HERE platform will determine the best version to use for a specific catalog or result in error logs. For information on how to specify the catalog version, see <a href="sdk-for-flutter-navigate-core-engine-catalogversionhint-class">CatalogVersionHint</a>. For information about catalogs and related concepts see <a href="sdk-for-flutter-navigate-core-engine-catalogidentifier-class">CatalogIdentifier</a>.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-core-engine-desiredcatalog-desiredcatalog">DesiredCatalog</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-param-hrn" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">hrn</span>, </span><span id="sdk-for-flutter-navigate-param-version" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-engine-catalogversionhint-class">CatalogVersionHint</a></span> <span class="parameter-name">version</span></span>)</span>  
Creates a new instance.

<div class="constructor-modifier features">

factory

</div>

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-core-engine-desiredcatalog-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-core-engine-desiredcatalog-id">id</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-core-engine-catalogidentifier-class">CatalogIdentifier</a></span>  
The identifier for the catalog to be accessed on the HERE platform. See <a href="sdk-for-flutter-navigate-core-engine-catalogidentifier-class">CatalogIdentifier</a>.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-core-engine-desiredcatalog-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-core-engine-desiredcatalog-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-core-engine-desiredcatalog-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-core-engine-desiredcatalog-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

