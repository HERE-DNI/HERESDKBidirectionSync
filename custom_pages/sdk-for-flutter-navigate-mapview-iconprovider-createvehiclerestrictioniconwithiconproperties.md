---
title: "createVehicleRestrictionIconWithIconProperties method"
slug: "sdk-for-flutter-navigate-mapview-iconprovider-createvehiclerestrictioniconwithiconproperties"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- createVehicleRestrictionIconWithIconProperties.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-mapview-mapview-library</li>
<li>/sdk-for-flutter-navigate-mapview-iconprovider-class</li>
<li class="self-crumb">createVehicleRestrictionIconWithIconProperties method</li>
</ol>
<div class="self-name">createVehicleRestrictionIconWithIconProperties</div>
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
<div class="main-content" data-above-sidebar="mapview/IconProvider-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>createVehicleRestrictionIconWithIconProperties method</h1></div>
<section class="multi-line-signature">
void
createVehicleRestrictionIconWithIconProperties(<wbr/><ol class="parameter-list"> <li>/sdk-for-flutter-navigate-mapview-vehiclerestrictioniconproperties-class properties, </li>
<li>/sdk-for-flutter-navigate-mapview-mapscheme mapScheme, </li>
<li>/sdk-for-flutter-navigate-mapview-iconproviderassettype assetType, </li>
<li>/sdk-for-flutter-navigate-core-size2d-class sizeConstraintsInPixels, </li>
<li>/sdk-for-flutter-navigate-mapview-iconprovidercallback callback, </li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Creates an image representing a vehicle restriction as shown on the map.</p>
<p>In case when /sdk-for-flutter-navigate-transport-vehiclerestriction-class object specifies multiple types of restrictions, then the icon is generated
for the first one according to the following priority: /sdk-for-flutter-navigate-transport-vehiclerestriction-restriction, /sdk-for-flutter-navigate-transport-vehiclerestriction-axlecount,
/sdk-for-flutter-navigate-transport-vehiclerestriction-axlecountingroup, /sdk-for-flutter-navigate-transport-vehiclerestriction-hazmatrestriction, /sdk-for-flutter-navigate-transport-vehiclerestriction-trailercount.</p>
<p><code>properties</code> The properties of a restriction icon to be created.</p>
<p><code>mapScheme</code> The map scheme for which the vehicle restriction icon should be created.</p>
<p><code>assetType</code> The asset type for which the vehicle restriction icon should be created.</p>
<p><code>sizeConstraintsInPixels</code> The maximum width and height of the icon in pixels.
  The values are capped to a maximum of 4096 pixels. The image will be created as large as
  possible within the width and height constraints while maintaining the aspect ratio.
  If either width or height is set to 0, it will be calculated automatically based on icon's
  aspect ratio.</p>
<p><code>callback</code> The callback which is used to return the created image along with a description of the icon based on the
  type of road and/or place it is used, or an error code.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void createVehicleRestrictionIconWithIconProperties(
    VehicleRestrictionIconProperties properties,
    MapScheme mapScheme,
    IconProviderAssetType assetType,
    Size2D sizeConstraintsInPixels,
    IconProviderCallback callback) {
  _createVehicleRestrictionIconWithIconProperties(
      properties, mapScheme, assetType, sizeConstraintsInPixels, callback);
}</code></pre>
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
<li>/sdk-for-flutter-navigate-mapview-iconprovider-class</li>
<li class="self-crumb">createVehicleRestrictionIconWithIconProperties method</li>
</ol>
<h5>IconProvider class</h5>
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
