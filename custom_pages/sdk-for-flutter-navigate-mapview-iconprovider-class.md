---
title: "IconProvider class"
slug: "sdk-for-flutter-navigate-mapview-iconprovider-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- IconProvider-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="mapview/IconProvider-class.html#constructors">Constructors</a></li>
<li><a href="mapview/IconProvider/IconProvider.html">IconProvider</a></li>
<li class="section-title inherited">
<a href="mapview/IconProvider-class.html#instance-properties">Properties</a>
</li>
<li class="inherited"><a href="mapview/IconProvider/hashCode.html">hashCode</a></li>
<li class="inherited"><a href="mapview/IconProvider/runtimeType.html">runtimeType</a></li>
<li class="section-title"><a href="mapview/IconProvider-class.html#instance-methods">Methods</a></li>
<li><a href="mapview/IconProvider/createRoadShieldIcon.html">createRoadShieldIcon</a></li>
<li><a href="mapview/IconProvider/createVehicleRestrictionIcon.html">createVehicleRestrictionIcon</a></li>
<li><a href="mapview/IconProvider/createVehicleRestrictionIconWithIconProperties.html">createVehicleRestrictionIconWithIconProperties</a></li>
<li class="inherited"><a href="mapview/IconProvider/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="mapview/IconProvider/toString.html">toString</a></li>
<li class="section-title inherited"><a href="mapview/IconProvider-class.html#operators">Operators</a></li>
<li class="inherited"><a href="mapview/IconProvider/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-mapview-mapview-library</li>
<li class="self-crumb">IconProvider class</li>
</ol>
<div class="self-name">IconProvider</div>
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
<div class="main-content" data-above-sidebar="mapview/mapview-library-sidebar.html" data-below-sidebar="mapview/IconProvider-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>IconProvider class</h1></div>
<section class="desc markdown">
<p>This provider creates icons from a given set of parameters for map content and constraints
for icon dimensions for a particular map scheme. The icon creation currently does not rely
on map data. Therefore, it works without online connection.</p>
<p>Note: This feature is in BETA state and thus there can be bugs and unexpected behavior.
Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="IconProvider">
/sdk-for-flutter-navigate-mapview-iconprovider-iconprovider(/sdk-for-flutter-navigate-mapview-mapcontext-class mapContext)
</dt>
<dd>
          Constructor.
<code>mapContext</code> The map context instance which is obtained using /sdk-for-flutter-navigate-mapview-mapviewbase-mapcontext.
        </dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property inherited" id="hashCode">
/sdk-for-flutter-navigate-mapview-iconprovider-hashcode
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-mapview-iconprovider-runtimetype
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
<dt class="callable" id="createRoadShieldIcon">
/sdk-for-flutter-navigate-mapview-iconprovider-createroadshieldicon(<wbr/>/sdk-for-flutter-navigate-mapview-roadshieldiconproperties-class properties, /sdk-for-flutter-navigate-mapview-mapscheme mapScheme, /sdk-for-flutter-navigate-mapview-iconproviderassettype assetType, int widthConstraintInPixels, int heightConstraintInPixels, /sdk-for-flutter-navigate-mapview-iconprovidercallback callback)
    → void

</dt>
<dd>
  Creates an image displaying a road shield according to the given parameters.
  

</dd>
<dt class="callable" id="createVehicleRestrictionIcon">
/sdk-for-flutter-navigate-mapview-iconprovider-createvehiclerestrictionicon(<wbr/>/sdk-for-flutter-navigate-mapview-pickvehiclerestrictionsresult-class pickingResult, /sdk-for-flutter-navigate-mapview-mapscheme mapScheme, /sdk-for-flutter-navigate-mapview-iconproviderassettype assetType, /sdk-for-flutter-navigate-core-size2d-class sizeConstraintsInPixels, /sdk-for-flutter-navigate-mapview-iconprovidercallback callback)
    → void

</dt>
<dd>
  Creates an image representing a vehicle restriction as shown on the map, based on map content picking result.
  

</dd>
<dt class="callable" id="createVehicleRestrictionIconWithIconProperties">
/sdk-for-flutter-navigate-mapview-iconprovider-createvehiclerestrictioniconwithiconproperties(<wbr/>/sdk-for-flutter-navigate-mapview-vehiclerestrictioniconproperties-class properties, /sdk-for-flutter-navigate-mapview-mapscheme mapScheme, /sdk-for-flutter-navigate-mapview-iconproviderassettype assetType, /sdk-for-flutter-navigate-core-size2d-class sizeConstraintsInPixels, /sdk-for-flutter-navigate-mapview-iconprovidercallback callback)
    → void

</dt>
<dd>
  Creates an image representing a vehicle restriction as shown on the map.
  

</dd>
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-navigate-mapview-iconprovider-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-mapview-iconprovider-tostring(<wbr/>)
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
/sdk-for-flutter-navigate-mapview-iconprovider-operator-equals(<wbr/>Object other)
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
<li class="self-crumb">IconProvider class</li>
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
