---
title: "Constructors"
slug: "sdk-for-flutter-explore-mapview-mapidlelistener-class"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- MapIdleListener-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="mapview/MapIdleListener-class.html#constructors">Constructors</a></li>
<li><a href="mapview/MapIdleListener/MapIdleListener.html">MapIdleListener</a></li>
<li class="section-title inherited">
<a href="mapview/MapIdleListener-class.html#instance-properties">Properties</a>
</li>
<li class="inherited"><a href="mapview/MapIdleListener/hashCode.html">hashCode</a></li>
<li class="inherited"><a href="mapview/MapIdleListener/runtimeType.html">runtimeType</a></li>
<li class="section-title"><a href="mapview/MapIdleListener-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="mapview/MapIdleListener/noSuchMethod.html">noSuchMethod</a></li>
<li><a href="mapview/MapIdleListener/onMapBusy.html">onMapBusy</a></li>
<li><a href="mapview/MapIdleListener/onMapIdle.html">onMapIdle</a></li>
<li class="inherited"><a href="mapview/MapIdleListener/toString.html">toString</a></li>
<li class="section-title inherited"><a href="mapview/MapIdleListener-class.html#operators">Operators</a></li>
<li class="inherited"><a href="mapview/MapIdleListener/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../mapview/mapview-library.html">/sdk-for-flutter-explore-mapview-mapview-library</a></li>
<li class="self-crumb">MapIdleListener class</li>
</ol>
<div class="self-name">MapIdleListener</div>
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
<div class="main-content" data-above-sidebar="mapview/mapview-library-sidebar.html" data-below-sidebar="mapview/MapIdleListener-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>MapIdleListener class abstract</h1></div>
<section class="desc markdown">
<p>Used to detect when the map becomes idle or busy.</p>
<p>Map is considered busy when its state changes (for example as a result of camera manipulation)
and/or when it requires a redraw (for example, as a result of map data being downloaded).</p>
<p>Map is considered idle when current state is fully rendered and no further
redraws are necessary.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="MapIdleListener">
<a href="../mapview/MapIdleListener/MapIdleListener.html">/sdk-for-flutter-explore-mapview-mapidlelistener-mapidlelistener</a>(void onMapBusyLambda(), void onMapIdleLambda())
</dt>
<dd>
          Used to detect when the map becomes idle or busy.
            <div class="constructor-modifier features">factory</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property inherited" id="hashCode">
<a href="../mapview/MapIdleListener/hashCode.html">/sdk-for-flutter-explore-mapview-mapidlelistener-hashcode</a>
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property inherited" id="runtimeType">
<a href="../mapview/MapIdleListener/runtimeType.html">/sdk-for-flutter-explore-mapview-mapidlelistener-runtimetype</a>
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
<dt class="callable inherited" id="noSuchMethod">
<a href="../mapview/MapIdleListener/noSuchMethod.html">/sdk-for-flutter-explore-mapview-mapidlelistener-nosuchmethod</a>(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable" id="onMapBusy">
<a href="../mapview/MapIdleListener/onMapBusy.html">/sdk-for-flutter-explore-mapview-mapidlelistener-onmapbusy</a>(<wbr/>)
    → void

</dt>
<dd>
  Called when map becomes invalidated and is about to be updated.
  

</dd>
<dt class="callable" id="onMapIdle">
<a href="../mapview/MapIdleListener/onMapIdle.html">/sdk-for-flutter-explore-mapview-mapidlelistener-onmapidle</a>(<wbr/>)
    → void

</dt>
<dd>
  Called when map finishes all state updates.
  

</dd>
<dt class="callable inherited" id="toString">
<a href="../mapview/MapIdleListener/toString.html">/sdk-for-flutter-explore-mapview-mapidlelistener-tostring</a>(<wbr/>)
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
<a href="../mapview/MapIdleListener/operator_equals.html">/sdk-for-flutter-explore-mapview-mapidlelistener-operator-equals</a>(<wbr/>Object other)
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
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../mapview/mapview-library.html">/sdk-for-flutter-explore-mapview-mapview-library</a></li>
<li class="self-crumb">MapIdleListener class</li>
</ol>
<h5>mapview library</h5>
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
</HTMLBlock>
