---
title: "MapViewLifecycleListener class abstract"
slug: "sdk-for-flutter-navigate-mapview-mapviewlifecyclelistener-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MapViewLifecycleListener-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="mapview/MapViewLifecycleListener-class.html#constructors">Constructors</a></li>
<li><a href="mapview/MapViewLifecycleListener/MapViewLifecycleListener.html">MapViewLifecycleListener</a></li>
<li class="section-title inherited">
<a href="mapview/MapViewLifecycleListener-class.html#instance-properties">Properties</a>
</li>
<li class="inherited"><a href="mapview/MapViewLifecycleListener/hashCode.html">hashCode</a></li>
<li class="inherited"><a href="mapview/MapViewLifecycleListener/runtimeType.html">runtimeType</a></li>
<li class="section-title"><a href="mapview/MapViewLifecycleListener-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="mapview/MapViewLifecycleListener/noSuchMethod.html">noSuchMethod</a></li>
<li><a href="mapview/MapViewLifecycleListener/onAttach.html">onAttach</a></li>
<li><a href="mapview/MapViewLifecycleListener/onDestroy.html">onDestroy</a></li>
<li><a href="mapview/MapViewLifecycleListener/onDetach.html">onDetach</a></li>
<li><a href="mapview/MapViewLifecycleListener/onPause.html">onPause</a></li>
<li><a href="mapview/MapViewLifecycleListener/onResume.html">onResume</a></li>
<li class="inherited"><a href="mapview/MapViewLifecycleListener/toString.html">toString</a></li>
<li class="section-title inherited"><a href="mapview/MapViewLifecycleListener-class.html#operators">Operators</a></li>
<li class="inherited"><a href="mapview/MapViewLifecycleListener/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-mapview-mapview-library</li>
<li class="self-crumb">MapViewLifecycleListener class</li>
</ol>
<div class="self-name">MapViewLifecycleListener</div>
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
<div class="main-content" data-above-sidebar="mapview/mapview-library-sidebar.html" data-below-sidebar="mapview/MapViewLifecycleListener-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>MapViewLifecycleListener class abstract</h1></div>
<section class="desc markdown">
<p>Provides a mechanism for observing a lifecycle of a map view and/or implementing components
whose lifecycle needs to be linked with that of a map view.</p>
<p>A <code>MapView</code> is using a</p>
<p><a href="https://developer.android.com/reference/android/view/SurfaceView">SurfaceView</a> for Android and
<a href="https://developer.apple.com/documentation/quartzcore/cametallayer">CAMetalLayer</a> for iOS
to render its content.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="MapViewLifecycleListener">
/sdk-for-flutter-navigate-mapview-mapviewlifecyclelistener-mapviewlifecyclelistener(void onAttachLambda(/sdk-for-flutter-navigate-mapview-mapviewbase-class), void onDetachLambda(/sdk-for-flutter-navigate-mapview-mapviewbase-class), void onPauseLambda(), void onResumeLambda(), void onDestroyLambda())
</dt>
<dd>
          Provides a mechanism for observing a lifecycle of a map view and/or implementing components
whose lifecycle needs to be linked with that of a map view.
            <div class="constructor-modifier features">factory</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property inherited" id="hashCode">
/sdk-for-flutter-navigate-mapview-mapviewlifecyclelistener-hashcode
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-mapview-mapviewlifecyclelistener-runtimetype
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
/sdk-for-flutter-navigate-mapview-mapviewlifecyclelistener-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable" id="onAttach">
/sdk-for-flutter-navigate-mapview-mapviewlifecyclelistener-onattach(<wbr/>/sdk-for-flutter-navigate-mapview-mapviewbase-class mapView)
    → void

</dt>
<dd>
  Called when adding /sdk-for-flutter-navigate-mapview-mapviewlifecyclelistener-class to the map view.
  

</dd>
<dt class="callable" id="onDestroy">
/sdk-for-flutter-navigate-mapview-mapviewlifecyclelistener-ondestroy(<wbr/>)
    → void

</dt>
<dd>
  Called when the map view to which this is attached to is destroyed.
  

</dd>
<dt class="callable" id="onDetach">
/sdk-for-flutter-navigate-mapview-mapviewlifecyclelistener-ondetach(<wbr/>/sdk-for-flutter-navigate-mapview-mapviewbase-class mapView)
    → void

</dt>
<dd>
  Called when removing /sdk-for-flutter-navigate-mapview-mapviewlifecyclelistener-class from the map view.
  

</dd>
<dt class="callable" id="onPause">
/sdk-for-flutter-navigate-mapview-mapviewlifecyclelistener-onpause(<wbr/>)
    → void

</dt>
<dd>
  Called when the map view to which this /sdk-for-flutter-navigate-mapview-mapviewlifecyclelistener-class is attached to gets paused
(usually when the app goes into background).
  

</dd>
<dt class="callable" id="onResume">
/sdk-for-flutter-navigate-mapview-mapviewlifecyclelistener-onresume(<wbr/>)
    → void

</dt>
<dd>
  Called when the map view to which this /sdk-for-flutter-navigate-mapview-mapviewlifecyclelistener-class is attached to gets resumed
(usually when the app goes into foreground).
  

</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-mapview-mapviewlifecyclelistener-tostring(<wbr/>)
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
/sdk-for-flutter-navigate-mapview-mapviewlifecyclelistener-operator-equals(<wbr/>Object other)
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
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-mapview-mapview-library</li>
<li class="self-crumb">MapViewLifecycleListener class</li>
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
`
}</HTMLBlock>
