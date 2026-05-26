---
title: "PolygonTileSourceLoadResultHandler class abstract"
slug: "sdk-for-flutter-explore-mapview-datasource-polygontilesourceloadresulthandler-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- PolygonTileSourceLoadResultHandler-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="mapview.datasource/PolygonTileSourceLoadResultHandler-class.html#constructors">Constructors</a></li>
<li><a href="mapview.datasource/PolygonTileSourceLoadResultHandler/PolygonTileSourceLoadResultHandler.html">PolygonTileSourceLoadResultHandler</a></li>
<li class="section-title inherited">
<a href="mapview.datasource/PolygonTileSourceLoadResultHandler-class.html#instance-properties">Properties</a>
</li>
<li class="inherited"><a href="mapview.datasource/PolygonTileSourceLoadResultHandler/hashCode.html">hashCode</a></li>
<li class="inherited"><a href="mapview.datasource/PolygonTileSourceLoadResultHandler/runtimeType.html">runtimeType</a></li>
<li class="section-title"><a href="mapview.datasource/PolygonTileSourceLoadResultHandler-class.html#instance-methods">Methods</a></li>
<li><a href="mapview.datasource/PolygonTileSourceLoadResultHandler/failed.html">failed</a></li>
<li><a href="mapview.datasource/PolygonTileSourceLoadResultHandler/loaded.html">loaded</a></li>
<li class="inherited"><a href="mapview.datasource/PolygonTileSourceLoadResultHandler/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="mapview.datasource/PolygonTileSourceLoadResultHandler/toString.html">toString</a></li>
<li class="section-title inherited"><a href="mapview.datasource/PolygonTileSourceLoadResultHandler-class.html#operators">Operators</a></li>
<li class="inherited"><a href="mapview.datasource/PolygonTileSourceLoadResultHandler/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-mapview-datasource-mapview-datasource-library</li>
<li class="self-crumb">PolygonTileSourceLoadResultHandler class</li>
</ol>
<div class="self-name">PolygonTileSourceLoadResultHandler</div>
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
<div class="main-content" data-above-sidebar="mapview.datasource/mapview.datasource-library-sidebar.html" data-below-sidebar="mapview.datasource/PolygonTileSourceLoadResultHandler-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>PolygonTileSourceLoadResultHandler class abstract</h1></div>
<section class="desc markdown">
<p>Result handler of a load tile request.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="PolygonTileSourceLoadResultHandler">
/sdk-for-flutter-explore-mapview-datasource-polygontilesourceloadresulthandler-polygontilesourceloadresulthandler(void loadedLambda(/sdk-for-flutter-explore-mapview-datasource-tilekey-class, List&lt;<wbr/>/sdk-for-flutter-explore-mapview-datasource-polygondata-class&gt;, /sdk-for-flutter-explore-mapview-datasource-tilesourcetilemetadata-class), void failedLambda(/sdk-for-flutter-explore-mapview-datasource-tilekey-class))
</dt>
<dd>
          Result handler of a load tile request.
            <div class="constructor-modifier features">factory</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property inherited" id="hashCode">
/sdk-for-flutter-explore-mapview-datasource-polygontilesourceloadresulthandler-hashcode
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-explore-mapview-datasource-polygontilesourceloadresulthandler-runtimetype
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable" id="failed">
/sdk-for-flutter-explore-mapview-datasource-polygontilesourceloadresulthandler-failed(<wbr/>/sdk-for-flutter-explore-mapview-datasource-tilekey-class tileKey)
    → void

</dt>
<dd>
  Called upon failed load tile request.
  

</dd>
<dt class="callable" id="loaded">
/sdk-for-flutter-explore-mapview-datasource-polygontilesourceloadresulthandler-loaded(<wbr/>/sdk-for-flutter-explore-mapview-datasource-tilekey-class tileKey, List&lt;<wbr/>/sdk-for-flutter-explore-mapview-datasource-polygondata-class&gt; data, /sdk-for-flutter-explore-mapview-datasource-tilesourcetilemetadata-class metadata)
    → void

</dt>
<dd>
  Called upon successful load tile request.
  

</dd>
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-explore-mapview-datasource-polygontilesourceloadresulthandler-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-explore-mapview-datasource-polygontilesourceloadresulthandler-tostring(<wbr/>)
    → String

</dt>
<dd class="inherited">
  A string representation of this object.
  <div class="features">inherited</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="operators">
<h2>Operators</h2>
<dl class="callables">
<dt class="callable inherited" id="operator ==">
/sdk-for-flutter-explore-mapview-datasource-polygontilesourceloadresulthandler-operator-equals(<wbr/>Object other)
    → bool

</dt>
<dd class="inherited">
  The equality operator.
  <div class="features">inherited</div>
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
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-mapview-datasource-mapview-datasource-library</li>
<li class="self-crumb">PolygonTileSourceLoadResultHandler class</li>
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
