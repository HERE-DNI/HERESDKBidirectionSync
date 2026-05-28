---
title: "ElectronicHorizonEngine class abstract"
slug: "sdk-for-flutter-navigate-electronic-horizon-electronichorizonengine-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- ElectronicHorizonEngine-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="electronic_horizon/ElectronicHorizonEngine-class.html#constructors">Constructors</a></li>
<li><a href="electronic_horizon/ElectronicHorizonEngine/ElectronicHorizonEngine.WithOptionsAndRoutePathEvaluator.html">WithOptionsAndRoutePathEvaluator</a></li>
<li class="section-title">
<a href="electronic_horizon/ElectronicHorizonEngine-class.html#instance-properties">Properties</a>
</li>
<li class="inherited"><a href="electronic_horizon/ElectronicHorizonEngine/hashCode.html">hashCode</a></li>
<li><a href="electronic_horizon/ElectronicHorizonEngine/route.html">route</a></li>
<li class="inherited"><a href="electronic_horizon/ElectronicHorizonEngine/runtimeType.html">runtimeType</a></li>
<li class="section-title"><a href="electronic_horizon/ElectronicHorizonEngine-class.html#instance-methods">Methods</a></li>
<li><a href="electronic_horizon/ElectronicHorizonEngine/addElectronicHorizonListener.html">addElectronicHorizonListener</a></li>
<li class="inherited"><a href="electronic_horizon/ElectronicHorizonEngine/noSuchMethod.html">noSuchMethod</a></li>
<li><a href="electronic_horizon/ElectronicHorizonEngine/removeElectronicHorizonListener.html">removeElectronicHorizonListener</a></li>
<li class="inherited"><a href="electronic_horizon/ElectronicHorizonEngine/toString.html">toString</a></li>
<li><a href="electronic_horizon/ElectronicHorizonEngine/update.html">update</a></li>
<li class="section-title inherited"><a href="electronic_horizon/ElectronicHorizonEngine-class.html#operators">Operators</a></li>
<li class="inherited"><a href="electronic_horizon/ElectronicHorizonEngine/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-electronic-horizon-electronic-horizon-library</li>
<li class="self-crumb">ElectronicHorizonEngine class</li>
</ol>
<div class="self-name">ElectronicHorizonEngine</div>
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
<div class="main-content" data-above-sidebar="electronic_horizon/electronic_horizon-library-sidebar.html" data-below-sidebar="electronic_horizon/ElectronicHorizonEngine-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>ElectronicHorizonEngine class abstract</h1></div>
<section class="desc markdown">
<p>Provides an electronic horizon engine that continuously predicts
the road network ahead of the vehicle by using detailed map data, including road topography that is
currently out of sight.</p>
<p>You can subscribe to electronic horizon updates based on position updates by using /sdk-for-flutter-navigate-electronic-horizon-electronichorizonlistener-class.
For more information about sub path levels, see /sdk-for-flutter-navigate-electronic-horizon-electronichorizonoptions-lookaheaddistancesinmeters.</p>
<p>The electronic horizon engine uses map-matched locations and can optionally use a /sdk-for-flutter-navigate-routing-route-class
to improve the most-preferred path (MPP).</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
behaviors. Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="ElectronicHorizonEngine.WithOptionsAndRoutePathEvaluator">
/sdk-for-flutter-navigate-electronic-horizon-electronichorizonengine-electronichorizonengine-withoptionsandroutepathevaluator(/sdk-for-flutter-navigate-core-engine-sdknativeengine-class sdkEngine, /sdk-for-flutter-navigate-electronic-horizon-electronichorizonoptions-class options, /sdk-for-flutter-navigate-transport-transportmode transportMode, /sdk-for-flutter-navigate-routing-route-class? route)
</dt>
<dd>
          Creates a new instance of /sdk-for-flutter-navigate-electronic-horizon-electronichorizonengine-class.
            <div class="constructor-modifier features">factory</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property inherited" id="hashCode">
/sdk-for-flutter-navigate-electronic-horizon-electronichorizonengine-hashcode
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="route">
/sdk-for-flutter-navigate-electronic-horizon-electronichorizonengine-route
↔ /sdk-for-flutter-navigate-routing-route-class?
</dt>
<dd>
  The instance of /sdk-for-flutter-navigate-routing-route-class that is being used by /sdk-for-flutter-navigate-electronic-horizon-electronichorizonengine-class.
You can override this property to rebuild the electronic horizon based on a different route.
Gets the instance of /sdk-for-flutter-navigate-routing-route-class or <code>null</code> if /sdk-for-flutter-navigate-routing-route-class is not set.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-electronic-horizon-electronichorizonengine-runtimetype
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
<dt class="callable" id="addElectronicHorizonListener">
/sdk-for-flutter-navigate-electronic-horizon-electronichorizonengine-addelectronichorizonlistener(<wbr/>/sdk-for-flutter-navigate-electronic-horizon-electronichorizonlistener-class electronicHorizonListener)
    → void

</dt>
<dd>
  Adds an /sdk-for-flutter-navigate-electronic-horizon-electronichorizonlistener-class to the subscription list.
  

</dd>
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-navigate-electronic-horizon-electronichorizonengine-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable" id="removeElectronicHorizonListener">
/sdk-for-flutter-navigate-electronic-horizon-electronichorizonengine-removeelectronichorizonlistener(<wbr/>/sdk-for-flutter-navigate-electronic-horizon-electronichorizonlistener-class electronicHorizonListener)
    → void

</dt>
<dd>
  Removes an /sdk-for-flutter-navigate-electronic-horizon-electronichorizonlistener-class from the subscription list.
  

</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-electronic-horizon-electronichorizonengine-tostring(<wbr/>)
    → String

</dt>
<dd class="inherited">
  A string representation of this object.
  <div class="features">inherited</div>
</dd>
<dt class="callable" id="update">
/sdk-for-flutter-navigate-electronic-horizon-electronichorizonengine-update(<wbr/>/sdk-for-flutter-navigate-navigation-mapmatchedlocation-class mapMatchedLocation)
    → void

</dt>
<dd>
  Updates the electronic horizon paths based on the provided map-matched location.
  

</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="operators">
<h2>Operators</h2>
<dl class="callables">
<dt class="callable inherited" id="operator ==">
/sdk-for-flutter-navigate-electronic-horizon-electronichorizonengine-operator-equals(<wbr/>Object other)
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
<li>/sdk-for-flutter-navigate-electronic-horizon-electronic-horizon-library</li>
<li class="self-crumb">ElectronicHorizonEngine class</li>
</ol>
<h5>electronic_horizon library</h5>
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
