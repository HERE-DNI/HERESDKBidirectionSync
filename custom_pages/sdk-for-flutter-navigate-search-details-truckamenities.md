---
title: "truckAmenities property"
slug: "sdk-for-flutter-navigate-search-details-truckamenities"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- truckAmenities.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-search-search-library</li>
<li>/sdk-for-flutter-navigate-search-details-class</li>
<li class="self-crumb">truckAmenities property</li>
</ol>
<div class="self-name">truckAmenities</div>
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
<div class="main-content" data-above-sidebar="search/Details-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>truckAmenities property</h1></div>
<section class="multi-line-signature">
/sdk-for-flutter-navigate-search-truckamenities-class?
        truckAmenities
<div class="features">getter/setter pair</div>
</section>
<section class="desc markdown">
<p>Additional information that is available only for places that contain truck amenities.
It is fully supported for offline search, provided that /sdk-for-flutter-navigate-core-engine-layerconfigurationfeature
is enabled in /sdk-for-flutter-navigate-core-engine-sdkoptions-layerconfiguration.</p>
<p><strong>Note:</strong> Currently, for online search, this is a closed-alpha feature, so it is available
only for selected customers. The field is always null for everyone that is not part of
the closed-alpha group.
Participants of the closed-alpha group can get access from HERE to use this feature.
If the credentials are not enabled, a /sdk-for-flutter-navigate-search-searcherror will be propagated.</p>
<p>For online search, this feature is only available if it is explicitly enabled.
To do that, call <code>SearchEngine.set_custom_option()</code> with arguments:
name: "lookup.show" or "discover.show" or "autosuggest.show" or "browse.show"
value: "truck"
To enable this feature for all queries, call <code>SearchEngine.set_custom_option()</code> for all:
"lookup.show", "discover.show", "autosuggest.show" and "browse.show".
To enable both <code>truck_amenities</code> and <code>fuel_station</code> features, set the value to "fuel,truck".</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and
unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">TruckAmenities? truckAmenities;</code></pre>
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
<li>/sdk-for-flutter-navigate-search-search-library</li>
<li>/sdk-for-flutter-navigate-search-details-class</li>
<li class="self-crumb">truckAmenities property</li>
</ol>
<h5>Details class</h5>
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
