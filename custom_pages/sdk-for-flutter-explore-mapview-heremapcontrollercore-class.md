---
title: "Constructors"
slug: "sdk-for-flutter-explore-mapview-heremapcontrollercore-class"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- HereMapControllerCore-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="mapview/HereMapControllerCore-class.html#constructors">Constructors</a></li>
<li><a href="mapview/HereMapControllerCore/HereMapControllerCore.html">HereMapControllerCore</a></li>
<li class="section-title">
<a href="mapview/HereMapControllerCore-class.html#instance-properties">Properties</a>
</li>
<li class="inherited"><a href="mapview/HereMapControllerCore/hashCode.html">hashCode</a></li>
<li class="inherited"><a href="mapview/HereMapControllerCore/runtimeType.html">runtimeType</a></li>
<li><a href="mapview/HereMapControllerCore/style.html">style</a></li>
<li class="section-title"><a href="mapview/HereMapControllerCore-class.html#instance-methods">Methods</a></li>
<li><a href="mapview/HereMapControllerCore/addMapIdleListener.html">addMapIdleListener</a></li>
<li class="inherited"><a href="mapview/HereMapControllerCore/noSuchMethod.html">noSuchMethod</a></li>
<li><a href="mapview/HereMapControllerCore/removeMapIdleListener.html">removeMapIdleListener</a></li>
<li class="inherited"><a href="mapview/HereMapControllerCore/toString.html">toString</a></li>
<li class="section-title inherited"><a href="mapview/HereMapControllerCore-class.html#operators">Operators</a></li>
<li class="inherited"><a href="mapview/HereMapControllerCore/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../mapview/mapview-library.html">/sdk-for-flutter-explore-mapview-mapview-library</a></li>
<li class="self-crumb">HereMapControllerCore class</li>
</ol>
<div class="self-name">HereMapControllerCore</div>
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
<div class="main-content" data-above-sidebar="mapview/mapview-library-sidebar.html" data-below-sidebar="mapview/HereMapControllerCore-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>HereMapControllerCore class abstract</h1></div>
<section class="desc markdown">
<p>The representation of a dynamic and interactive geographic map.</p>
<p>The map manages a collection of layers of objects and spaces, presents them in a stacked layout and offers the means to focus on a certain area.
The layers, their relation to the objects and spaces, the layout and the representation style is described through a configuration.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="HereMapControllerCore">
<a href="../mapview/HereMapControllerCore/HereMapControllerCore.html">/sdk-for-flutter-explore-mapview-heremapcontrollercore-heremapcontrollercore</a>()
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property inherited" id="hashCode">
<a href="../mapview/HereMapControllerCore/hashCode.html">/sdk-for-flutter-explore-mapview-heremapcontrollercore-hashcode</a>
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property inherited" id="runtimeType">
<a href="../mapview/HereMapControllerCore/runtimeType.html">/sdk-for-flutter-explore-mapview-heremapcontrollercore-runtimetype</a>
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="style">
<a href="../mapview/HereMapControllerCore/style.html">/sdk-for-flutter-explore-mapview-heremapcontrollercore-style</a>
→ <a href="../mapview/Style-class.html">/sdk-for-flutter-explore-mapview-style-class</a>
</dt>
<dd>
  The style that the map uses to customize the visual appearance of rendered features.
Changes made to the map style using <a href="../mapview/Style/update.html">/sdk-for-flutter-explore-mapview-style-update</a> are lost when new scene is loaded using
<a href="../mapview/MapScene/loadSceneForMapScheme.html">/sdk-for-flutter-explore-mapview-mapscene-loadsceneformapscheme</a> and its variants as well as
when map features are enabled or disabled using <a href="../mapview/MapScene/enableFeatures.html">/sdk-for-flutter-explore-mapview-mapscene-enablefeatures</a> and <a href="../mapview/MapScene/disableFeatures.html">/sdk-for-flutter-explore-mapview-mapscene-disablefeatures</a>.
  <div class="features">no setter</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable" id="addMapIdleListener">
<a href="../mapview/HereMapControllerCore/addMapIdleListener.html">/sdk-for-flutter-explore-mapview-heremapcontrollercore-addmapidlelistener</a>(<wbr/><a href="../mapview/MapIdleListener-class.html">/sdk-for-flutter-explore-mapview-mapidlelistener-class</a> listener)
    → void

</dt>
<dd>
  Adds a listener for receiving idle state
notifications and notifies it of the current state.
  

</dd>
<dt class="callable inherited" id="noSuchMethod">
<a href="../mapview/HereMapControllerCore/noSuchMethod.html">/sdk-for-flutter-explore-mapview-heremapcontrollercore-nosuchmethod</a>(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable" id="removeMapIdleListener">
<a href="../mapview/HereMapControllerCore/removeMapIdleListener.html">/sdk-for-flutter-explore-mapview-heremapcontrollercore-removemapidlelistener</a>(<wbr/><a href="../mapview/MapIdleListener-class.html">/sdk-for-flutter-explore-mapview-mapidlelistener-class</a> listener)
    → void

</dt>
<dd>
  Removes a listener from receiving idle state notifications.
  

</dd>
<dt class="callable inherited" id="toString">
<a href="../mapview/HereMapControllerCore/toString.html">/sdk-for-flutter-explore-mapview-heremapcontrollercore-tostring</a>(<wbr/>)
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
<a href="../mapview/HereMapControllerCore/operator_equals.html">/sdk-for-flutter-explore-mapview-heremapcontrollercore-operator-equals</a>(<wbr/>Object other)
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
<li class="self-crumb">HereMapControllerCore class</li>
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
