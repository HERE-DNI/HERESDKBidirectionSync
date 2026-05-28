---
title: "Region class"
slug: "sdk-for-flutter-navigate-maploader-region-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- Region-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="maploader/Region-class.html#constructors">Constructors</a></li>
<li><a href="maploader/Region/Region.html">Region</a></li>
<li class="section-title">
<a href="maploader/Region-class.html#instance-properties">Properties</a>
</li>
<li><a href="maploader/Region/childRegions.html">childRegions</a></li>
<li><a href="maploader/Region/hashCode.html">hashCode</a></li>
<li><a href="maploader/Region/name.html">name</a></li>
<li><a href="maploader/Region/navigability.html">navigability</a></li>
<li><a href="maploader/Region/regionId.html">regionId</a></li>
<li class="inherited"><a href="maploader/Region/runtimeType.html">runtimeType</a></li>
<li><a href="maploader/Region/sizeOnDiskInBytes.html">sizeOnDiskInBytes</a></li>
<li><a href="maploader/Region/sizeOnNetworkInBytes.html">sizeOnNetworkInBytes</a></li>
<li class="section-title inherited"><a href="maploader/Region-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="maploader/Region/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="maploader/Region/toString.html">toString</a></li>
<li class="section-title"><a href="maploader/Region-class.html#operators">Operators</a></li>
<li><a href="maploader/Region/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-maploader-maploader-library</li>
<li class="self-crumb">Region class</li>
</ol>
<div class="self-name">Region</div>
<form class="search navbar-right" role="search">
<input autocomplete="off" class="form-control typeahead" disabled="" id="search-box" placeholder="Loading search..." type="text"/>
</form>
<div class="toggle" id="theme-button" title="Toggle brightness">
<label for="theme">
<input id="theme" type="checkbox" value="light-theme"/>

        dark_mode
      

        light_mode
      
</label>
</div>
</header>
<main>
<div class="main-content" data-above-sidebar="maploader/maploader-library-sidebar.html" data-below-sidebar="maploader/Region-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>Region class</h1></div>
<section class="desc markdown">
<p>Defines an area, especially part of a country or the world that can be downloaded.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="Region">
/sdk-for-flutter-navigate-maploader-region-region(/sdk-for-flutter-navigate-maploader-regionid-class regionId)
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="childRegions">
/sdk-for-flutter-navigate-maploader-region-childregions
↔ List&lt;<wbr/>/sdk-for-flutter-navigate-maploader-region-class&gt;?
</dt>
<dd>
  All child regions for current region.
Note that each child can again contain multiple children.
A downloadable region will contain the content of all children.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="hashCode">
/sdk-for-flutter-navigate-maploader-region-hashcode
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="name">
/sdk-for-flutter-navigate-maploader-region-name
↔ String
</dt>
<dd>
  Name of region. Language is determined by the requested /sdk-for-flutter-navigate-core-languagecode. By default,
it is in /sdk-for-flutter-navigate-core-languagecode.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="navigability">
/sdk-for-flutter-navigate-maploader-region-navigability
↔ /sdk-for-flutter-navigate-maploader-navigabilitytype
</dt>
<dd>
  Indicates the navigability type of this region.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="regionId">
/sdk-for-flutter-navigate-maploader-region-regionid
↔ /sdk-for-flutter-navigate-maploader-regionid-class
</dt>
<dd>
  Unique identifier specifying a region.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-maploader-region-runtimetype
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="sizeOnDiskInBytes">
/sdk-for-flutter-navigate-maploader-region-sizeondiskinbytes
↔ int
</dt>
<dd>
  Represents the total size of the region on disk in bytes, assuming no pre-existing data on the disk.
This value is a theoretical maximum for the region's size allocation.
Note: If overlapping regions exist or data is already present on the disk,
the actual size occupied might be less than this value due to shared or reused map data.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="sizeOnNetworkInBytes">
/sdk-for-flutter-navigate-maploader-region-sizeonnetworkinbytes
↔ int
</dt>
<dd>
  Region size, for downloading/during network operations, in bytes. Regions are downloaded in
compressed form and hence they have reduced size on network.
Note: This value represents the theoretical maximum size required for the
region during transfer. If overlapping data already exists, the actual size
downloaded may be smaller due to map data reuse.
  <div class="features">getter/setter pair</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-navigate-maploader-region-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-maploader-region-tostring(<wbr/>)
    → String

</dt>
<dd class="inherited">
  A string representation of this object.
  <div class="features">inherited</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="operators">
<h2>Operators</h2>
<dl class="callables">
<dt class="callable" id="operator ==">
/sdk-for-flutter-navigate-maploader-region-operator-equals(<wbr/>Object other)
    → bool

</dt>
<dd>
  The equality operator.
  

</dd>
</dl>
</section>
</div>
<div class="sidebar sidebar-offcanvas-left" id="dartdoc-sidebar-left">
<header class="hidden-l" id="header-search-sidebar">
<form class="search-sidebar" role="search">
<input autocomplete="off" class="form-control typeahead" disabled="" id="search-sidebar" placeholder="Loading search..." type="text"/>
</form>
</header>
<ol class="breadcrumbs gt-separated dark hidden-l" id="sidebar-nav">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-maploader-maploader-library</li>
<li class="self-crumb">Region class</li>
</ol>
<h5>maploader library</h5>
<div id="dartdoc-sidebar-left-content"></div>
</div>
<div class="sidebar sidebar-offcanvas-right" id="dartdoc-sidebar-right">
</div>
</main>
<footer>

    here_sdk
      4.26.0
  
</footer>
</div></div>
</div>
`
}</HTMLBlock>
