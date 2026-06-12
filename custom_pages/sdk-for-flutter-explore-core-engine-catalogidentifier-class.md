---
title: "CatalogIdentifier class"
slug: "sdk-for-flutter-explore-core-engine-catalogidentifier-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- CatalogIdentifier-class.html -->


<div>
<h1>CatalogIdentifier class</h1></div>

<p>This class is used to identify any catalog in the HERE platform.</p>
<p>A catalog is a storage-representation to store map data on the HERE platform.
The data inside a catalog is divided into layers, where each layer consists
of datasets with similar functional attributes in the physical world.
For example, there can be a layer for road-topology, a layer for
road-attributes (such as speed limits) and a layer for places and business
addresses. All these layers, in different geographic regions, can be grouped together into a
catalog to create a representation of the world we live in, called HERE map.
It can be also used to render a <code>MapView</code>. Each geographic region is cut into geospatial
tiles for efficient search, map display, routing, map matching, and driver warnings.
Each tile partitions the map data (in one or more layers, depending on the product)
in the geolocation of that specific tile.
The data inside a catalog is logically managed and access controlled
as a single set. If you have any data that you want to bring to the HERE
platform, you need a catalog to contain it.
For additional information about catalogs, and related concepts of data representation
on the HERE platform, refer to
<a href="https://www.here.com/docs/bundle/data-api-developer-guide/page/rest/catalogs.html">the Data API</a>
and <a href="https://www.here.com/docs/bundle/introduction-to-mapping-concepts-user-guide/page/topics/maps-layers-tiles.html">Introduction to Mapping Concepts</a></p>


<h2>Constructors</h2>
<ul><li><a href="/sdk-for-flutter-explore-core-engine-catalogidentifier-catalogidentifier">CatalogIdentifier</a></li></ul>


<h2>Properties</h2>
<ul><li><a href="/sdk-for-flutter-explore-core-engine-catalogidentifier-hashcode">hashCode</a></li><li><a href="/sdk-for-flutter-explore-core-engine-catalogidentifier-hrn">hrn</a></li><li><a href="/sdk-for-flutter-explore-core-engine-catalogidentifier-runtimetype">runtimeType</a></li><li><a href="/sdk-for-flutter-explore-core-engine-catalogidentifier-version">version</a></li></ul>


<h2>Methods</h2>
<ul><li><a href="/sdk-for-flutter-explore-core-engine-catalogidentifier-nosuchmethod">noSuchMethod</a></li><li><a href="/sdk-for-flutter-explore-core-engine-catalogidentifier-tostring">toString</a></li></ul>


<h2>Operators</h2>
<ul><li><a href="/sdk-for-flutter-explore-core-engine-catalogidentifier-operator-equals">operator ==</a></li></ul>

 



</div>
`
}</HTMLBlock>
