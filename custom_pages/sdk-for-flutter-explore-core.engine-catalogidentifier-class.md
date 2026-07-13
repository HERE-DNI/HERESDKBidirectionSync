---
title: "CatalogIdentifier class - core.engine library - Dart API"
slug: "sdk-for-flutter-explore-core.engine-catalogidentifier-class"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="core.engine/core.engine-library-sidebar.html" data-below-sidebar="core.engine/CatalogIdentifier-class-sidebar.html">

<div>

# <span class="kind-class">CatalogIdentifier</span> class

</div>

<div class="section desc markdown">

This class is used to identify any catalog in the HERE platform.

A catalog is a storage-representation to store map data on the HERE platform. The data inside a catalog is divided into layers, where each layer consists of datasets with similar functional attributes in the physical world. For example, there can be a layer for road-topology, a layer for road-attributes (such as speed limits) and a layer for places and business addresses. All these layers, in different geographic regions, can be grouped together into a catalog to create a representation of the world we live in, called HERE map. It can be also used to render a `MapView`. Each geographic region is cut into geospatial tiles for efficient search, map display, routing, map matching, and driver warnings. Each tile partitions the map data (in one or more layers, depending on the product) in the geolocation of that specific tile. The data inside a catalog is logically managed and access controlled as a single set. If you have any data that you want to bring to the HERE platform, you need a catalog to contain it. For additional information about catalogs, and related concepts of data representation on the HERE platform, refer to <a href="https://www.here.com/docs/bundle/data-api-developer-guide/page/rest/catalogs.html">the Data API</a> and <a href="https://www.here.com/docs/bundle/introduction-to-mapping-concepts-user-guide/page/topics/maps-layers-tiles.html">Introduction to Mapping Concepts</a>

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-explore-core-engine-catalogidentifier-catalogidentifier">CatalogIdentifier</a></span><span class="signature">()</span>  

## Properties

<span class="name"><a href="sdk-for-flutter-explore-core-engine-catalogidentifier-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-core-engine-catalogidentifier-hrn">hrn</a></span> <span class="signature">↔ String</span>  
A HERE Resource Name (HRN) for this catalog. This is a unique string returned by the HERE platform when you add a new catalog to your project. For information about catalog creation process refer to <a href="https://www.here.com/docs/bundle/data-api-developer-guide/page/rest/creating-a-catalog.html">the Data API</a> By default, this field points to a default catalog on HERE platform, which contains data for the whole world excluding the region of Japan. Use <a href="sdk-for-flutter-explore-core-engine-catalogconfiguration-getdefault">CatalogConfiguration.getDefault</a> to get the default HRN value for use with the HERE platform.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-core-engine-catalogidentifier-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-core-engine-catalogidentifier-version">version</a></span> <span class="signature">↔ int?</span>  
A version number for a catalog. When accessing a catalog, this version must be specified. Set `null` to automatically get the latest version for a catalog. The field defaults to `null`. Since the data inside a catalog can be updated, each published modification needs to correlate to a specific version number. Note: when `CatalogIdentifier` created with <a href="sdk-for-flutter-explore-core-engine-desiredcatalog-class">DesiredCatalog</a> then:

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-explore-core-engine-catalogidentifier-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-core-engine-catalogidentifier-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-explore-core-engine-catalogidentifier-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

