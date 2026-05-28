---
title: "InstalledRegion class"
slug: "sdk-for-flutter-navigate-maploader-installedregion-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- InstalledRegion-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="maploader/InstalledRegion-class.html#constructors">Constructors</a></li>
<li><a href="maploader/InstalledRegion/InstalledRegion.html">InstalledRegion</a></li>
<li class="section-title">
<a href="maploader/InstalledRegion-class.html#instance-properties">Properties</a>
</li>
<li><a href="maploader/InstalledRegion/hashCode.html">hashCode</a></li>
<li><a href="maploader/InstalledRegion/lastUpdateTime.html">lastUpdateTime</a></li>
<li><a href="maploader/InstalledRegion/parentId.html">parentId</a></li>
<li><a href="maploader/InstalledRegion/regionId.html">regionId</a></li>
<li class="inherited"><a href="maploader/InstalledRegion/runtimeType.html">runtimeType</a></li>
<li><a href="maploader/InstalledRegion/sizeOnDiskInBytes.html">sizeOnDiskInBytes</a></li>
<li><a href="maploader/InstalledRegion/status.html">status</a></li>
<li class="section-title inherited"><a href="maploader/InstalledRegion-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="maploader/InstalledRegion/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="maploader/InstalledRegion/toString.html">toString</a></li>
<li class="section-title"><a href="maploader/InstalledRegion-class.html#operators">Operators</a></li>
<li><a href="maploader/InstalledRegion/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-maploader-maploader-library</li>
<li class="self-crumb">InstalledRegion class</li>
</ol>
<div class="self-name">InstalledRegion</div>
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
<div class="main-content" data-above-sidebar="maploader/maploader-library-sidebar.html" data-below-sidebar="maploader/InstalledRegion-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>InstalledRegion class</h1></div>
<section class="desc markdown">
<p>Represents a region, from persistent map storage.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="InstalledRegion">
/sdk-for-flutter-navigate-maploader-installedregion-installedregion(/sdk-for-flutter-navigate-maploader-regionid-class regionId, /sdk-for-flutter-navigate-maploader-regionid-class parentId, int sizeOnDiskInBytes, /sdk-for-flutter-navigate-maploader-installedregionstatus status)
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="hashCode">
/sdk-for-flutter-navigate-maploader-installedregion-hashcode
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="lastUpdateTime">
/sdk-for-flutter-navigate-maploader-installedregion-lastupdatetime
↔ DateTime?
</dt>
<dd>
  The last update time of the region in the persistent map storage.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="parentId">
/sdk-for-flutter-navigate-maploader-installedregion-parentid
↔ /sdk-for-flutter-navigate-maploader-regionid-class
</dt>
<dd>
  Parent region identifier. Continents have a parent_id of 0.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="regionId">
/sdk-for-flutter-navigate-maploader-installedregion-regionid
↔ /sdk-for-flutter-navigate-maploader-regionid-class
</dt>
<dd>
  Unique identifier specifying a region.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-maploader-installedregion-runtimetype
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="sizeOnDiskInBytes">
/sdk-for-flutter-navigate-maploader-installedregion-sizeondiskinbytes
↔ int
</dt>
<dd>
  Region size on disk in bytes.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="status">
/sdk-for-flutter-navigate-maploader-installedregion-status
↔ /sdk-for-flutter-navigate-maploader-installedregionstatus
</dt>
<dd>
  Status of the region in the persistent map storage.
  <div class="features">getter/setter pair</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-navigate-maploader-installedregion-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-maploader-installedregion-tostring(<wbr/>)
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
/sdk-for-flutter-navigate-maploader-installedregion-operator-equals(<wbr/>Object other)
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
<li class="self-crumb">InstalledRegion class</li>
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
