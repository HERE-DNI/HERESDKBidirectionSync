---
title: "CatalogUpdateInfo class"
slug: "sdk-for-flutter-navigate-maploader-catalogupdateinfo-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- CatalogUpdateInfo-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="maploader/CatalogUpdateInfo-class.html#constructors">Constructors</a></li>
<li><a href="maploader/CatalogUpdateInfo/CatalogUpdateInfo.html">CatalogUpdateInfo</a></li>
<li class="section-title">
<a href="maploader/CatalogUpdateInfo-class.html#instance-properties">Properties</a>
</li>
<li><a href="maploader/CatalogUpdateInfo/diskSizeInBytes.html">diskSizeInBytes</a></li>
<li><a href="maploader/CatalogUpdateInfo/hashCode.html">hashCode</a></li>
<li><a href="maploader/CatalogUpdateInfo/installedCatalog.html">installedCatalog</a></li>
<li><a href="maploader/CatalogUpdateInfo/latestVersion.html">latestVersion</a></li>
<li><a href="maploader/CatalogUpdateInfo/networkSizeInBytes.html">networkSizeInBytes</a></li>
<li class="inherited"><a href="maploader/CatalogUpdateInfo/runtimeType.html">runtimeType</a></li>
<li><a href="maploader/CatalogUpdateInfo/state.html">state</a></li>
<li><a href="maploader/CatalogUpdateInfo/temporaryDiskRequirementInBytes.html">temporaryDiskRequirementInBytes</a></li>
<li class="section-title inherited"><a href="maploader/CatalogUpdateInfo-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="maploader/CatalogUpdateInfo/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="maploader/CatalogUpdateInfo/toString.html">toString</a></li>
<li class="section-title"><a href="maploader/CatalogUpdateInfo-class.html#operators">Operators</a></li>
<li><a href="maploader/CatalogUpdateInfo/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-maploader-maploader-library</li>
<li class="self-crumb">CatalogUpdateInfo class</li>
</ol>
<div class="self-name">CatalogUpdateInfo</div>
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
<div class="main-content" data-above-sidebar="maploader/maploader-library-sidebar.html" data-below-sidebar="maploader/CatalogUpdateInfo-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>CatalogUpdateInfo class</h1></div>
<section class="desc markdown">
<p>Holds information for the catalog update intent.</p>
<p>Provides information regarding installed catalog
and its latest available version.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="CatalogUpdateInfo">
/sdk-for-flutter-navigate-maploader-catalogupdateinfo-catalogupdateinfo(/sdk-for-flutter-navigate-maploader-installedcatalog-class installedCatalog, int latestVersion)
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="diskSizeInBytes">
/sdk-for-flutter-navigate-maploader-catalogupdateinfo-disksizeinbytes
↔ int
</dt>
<dd>
  Estimates the size of the offline maps after an update.
<strong>Note</strong>
In order to estimate, if catalog update is feasible, given the amount of free space on the disk,
application can compare amount of the free space on the disk with <code>disk_size_in_bytes + temporary_disk_requirement_in_bytes</code>.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="hashCode">
/sdk-for-flutter-navigate-maploader-catalogupdateinfo-hashcode
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="installedCatalog">
/sdk-for-flutter-navigate-maploader-catalogupdateinfo-installedcatalog
↔ /sdk-for-flutter-navigate-maploader-installedcatalog-class
</dt>
<dd>
  Installed catalog.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="latestVersion">
/sdk-for-flutter-navigate-maploader-catalogupdateinfo-latestversion
↔ int
</dt>
<dd>
  Latest version available for a catalog.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="networkSizeInBytes">
/sdk-for-flutter-navigate-maploader-catalogupdateinfo-networksizeinbytes
↔ int
</dt>
<dd>
  Total size in bytes that needs to be downloaded over the network to update the installed catalog.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-maploader-catalogupdateinfo-runtimetype
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="state">
/sdk-for-flutter-navigate-maploader-catalogupdateinfo-state
↔ /sdk-for-flutter-navigate-maploader-catalogupdatestate
</dt>
<dd>
  State of current catalog update.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="temporaryDiskRequirementInBytes">
/sdk-for-flutter-navigate-maploader-catalogupdateinfo-temporarydiskrequirementinbytes
↔ int
</dt>
<dd>
  Performing an update requires additional storage on top of existing offline maps.
This space is used to store intermittent copy of map content according to
the specified /sdk-for-flutter-navigate-maploader-mapupdatermapupdateversioncommitpolicy.
<strong>Note</strong>
In order to estimate, if catalog update is feasible, given the amount of free space on the disk,
application can compare amount of the free space on the disk with <code>disk_size_in_bytes + temporary_disk_requirement_in_bytes</code>.
  <div class="features">getter/setter pair</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-navigate-maploader-catalogupdateinfo-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-maploader-catalogupdateinfo-tostring(<wbr/>)
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
/sdk-for-flutter-navigate-maploader-catalogupdateinfo-operator-equals(<wbr/>Object other)
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
<li class="self-crumb">CatalogUpdateInfo class</li>
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
