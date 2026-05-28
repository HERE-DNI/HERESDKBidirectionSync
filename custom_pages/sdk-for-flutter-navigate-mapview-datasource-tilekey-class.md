---
title: "TileKey class"
slug: "sdk-for-flutter-navigate-mapview-datasource-tilekey-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- TileKey-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="mapview.datasource/TileKey-class.html#constructors">Constructors</a></li>
<li><a href="mapview.datasource/TileKey/TileKey.html">TileKey</a></li>
<li class="section-title">
<a href="mapview.datasource/TileKey-class.html#instance-properties">Properties</a>
</li>
<li><a href="mapview.datasource/TileKey/hashCode.html">hashCode</a></li>
<li><a href="mapview.datasource/TileKey/level.html">level</a></li>
<li class="inherited"><a href="mapview.datasource/TileKey/runtimeType.html">runtimeType</a></li>
<li><a href="mapview.datasource/TileKey/x.html">x</a></li>
<li><a href="mapview.datasource/TileKey/y.html">y</a></li>
<li class="section-title inherited"><a href="mapview.datasource/TileKey-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="mapview.datasource/TileKey/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="mapview.datasource/TileKey/toString.html">toString</a></li>
<li class="section-title"><a href="mapview.datasource/TileKey-class.html#operators">Operators</a></li>
<li><a href="mapview.datasource/TileKey/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-mapview-datasource-mapview-datasource-library</li>
<li class="self-crumb">TileKey class</li>
</ol>
<div class="self-name">TileKey</div>
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
<div class="main-content" data-above-sidebar="mapview.datasource/mapview.datasource-library-sidebar.html" data-below-sidebar="mapview.datasource/TileKey-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>TileKey class</h1></div>
<section class="desc markdown">
<p>Key of a data source tile.</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected
behavior. Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="TileKey">
/sdk-for-flutter-navigate-mapview-datasource-tilekey-tilekey(int x, int y, int level)
</dt>
<dd>
          Creates a new instance.
        </dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="hashCode">
/sdk-for-flutter-navigate-mapview-datasource-tilekey-hashcode
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="level">
/sdk-for-flutter-navigate-mapview-datasource-tilekey-level
↔ int
</dt>
<dd>
  Level of the tile. Supported range [0, 31].
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-mapview-datasource-tilekey-runtimetype
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="x">
/sdk-for-flutter-navigate-mapview-datasource-tilekey-x
↔ int
</dt>
<dd>
  X coordinate of the tile. This ranges from 0 to 2^level − 1.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="y">
/sdk-for-flutter-navigate-mapview-datasource-tilekey-y
↔ int
</dt>
<dd>
  Y coordinate of the tile. This ranges from 0 to 2^level − 1.
  <div class="features">getter/setter pair</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-navigate-mapview-datasource-tilekey-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-mapview-datasource-tilekey-tostring(<wbr/>)
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
/sdk-for-flutter-navigate-mapview-datasource-tilekey-operator-equals(<wbr/>Object other)
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
<li>/sdk-for-flutter-navigate-mapview-datasource-mapview-datasource-library</li>
<li class="self-crumb">TileKey class</li>
</ol>
<h5>mapview.datasource library</h5>
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
