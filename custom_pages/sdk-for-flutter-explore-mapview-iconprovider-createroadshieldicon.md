---
title: "Implementation"
slug: "sdk-for-flutter-explore-mapview-iconprovider-createroadshieldicon"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- createRoadShieldIcon.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../../mapview/mapview-library.html">/sdk-for-flutter-explore-mapview-mapview-library</a></li>
<li><a href="../../mapview/IconProvider-class.html">/sdk-for-flutter-explore-mapview-iconprovider-class</a></li>
<li class="self-crumb">createRoadShieldIcon method</li>
</ol>
<div class="self-name">createRoadShieldIcon</div>
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
<h1>createRoadShieldIcon method</h1></div>
<section class="multi-line-signature">
void
createRoadShieldIcon(<wbr/><ol class="parameter-list"> <li><a href="../../mapview/RoadShieldIconProperties-class.html">/sdk-for-flutter-explore-mapview-roadshieldiconproperties-class</a> properties, </li>
<li><a href="../../mapview/MapScheme.html">/sdk-for-flutter-explore-mapview-mapscheme</a> mapScheme, </li>
<li><a href="../../mapview/IconProviderAssetType.html">/sdk-for-flutter-explore-mapview-iconproviderassettype</a> assetType, </li>
<li>int widthConstraintInPixels, </li>
<li>int heightConstraintInPixels, </li>
<li><a href="../../mapview/IconProviderCallback.html">/sdk-for-flutter-explore-mapview-iconprovidercallback</a> callback, </li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Creates an image displaying a road shield according to the given parameters.</p>
<p><code>properties</code> The properties which determine the kind of road shield to be created.</p>
<p><code>mapScheme</code> The map scheme for which the road shield should be created.</p>
<p><code>assetType</code> The asset type for which the road shield should be created.</p>
<p><code>widthConstraintInPixels</code> The maximum width of the road shield in pixels.
  The value is capped to a maximum of 4096 pixels. The image will be created as large as
  possible within the width and height constraints while maintaining the aspect ratio.
  If set to 0, the width will be calculated based on the heightConstraintInPixels to
  preserve the aspect ratio.</p>
<p><code>heightConstraintInPixels</code> The maximum height of the road shield in pixels.
  The value is capped to a maximum of 4096 pixels. The image will be created as large as
  possible within the width and height constraints while maintaining the aspect ratio.
  If set to 0, the original image-asset's height will be used.</p>
<p><code>callback</code> The callback which is used to return the created image along with a description of the icon based on the
  type of road and/or place it is used, or an error code.</p>
<p>Note: This feature is in BETA state and thus there can be bugs and unexpected behavior.
Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void createRoadShieldIcon(
    RoadShieldIconProperties properties,
    MapScheme mapScheme,
    IconProviderAssetType assetType,
    int widthConstraintInPixels,
    int heightConstraintInPixels,
    IconProviderCallback callback) {
  _createRoadShieldIcon(properties,
    mapScheme,
    assetType,
    widthConstraintInPixels,
    heightConstraintInPixels,
    callback);
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
<li><a href="../../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../../mapview/mapview-library.html">/sdk-for-flutter-explore-mapview-mapview-library</a></li>
<li><a href="../../mapview/IconProvider-class.html">/sdk-for-flutter-explore-mapview-iconprovider-class</a></li>
<li class="self-crumb">createRoadShieldIcon method</li>
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
</HTMLBlock>
