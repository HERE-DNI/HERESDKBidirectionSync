---
title: "Untitled"
slug: "sdk-for-flutter-explore-mapview-iconprovidercallback"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- IconProviderCallback.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-mapview-mapview-library</li>
<li class="self-crumb">IconProviderCallback typedef</li>
</ol>
<div class="self-name">IconProviderCallback</div>
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
<div class="main-content" data-above-sidebar="mapview/mapview-library-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>IconProviderCallback typedef</h1></div>
<section class="multi-line-signature">
IconProviderCallback =
     void Function(ImageInfo? imageInfo, String? iconDescription, /sdk-for-flutter-explore-mapview-iconprovidererror? error)
</section>
<section class="desc markdown">
<p>A callback of this type is invoked when an icon is received from the /sdk-for-flutter-explore-mapview-iconprovider-class in
the <code>ImageInfo</code> format. The callback provides information about the loaded icon, or an
/sdk-for-flutter-explore-mapview-iconprovidererror if one occurred.</p>
<p><code>imageInfo</code> The created <code>ImageInfo</code> containing the icon, or <code>null</code> if an error occurred.</p>
<p><code>iconDescription</code> An English description of the created icon. For example, "Federal Highway"
                  for the road shield icon with the /sdk-for-flutter-explore-core-routetype in Brazil.
                  It will be <code>null</code> if an error occurred.</p>
<p><code>error</code> The error that occurred, or <code>null</code> if the icon is loaded successfully.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">typedef IconProviderCallback = void Function(
    ImageInfo? imageInfo, String? iconDescription, IconProviderError? error);</code></pre>
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
<li>/sdk-for-flutter-explore-mapview-mapview-library</li>
<li class="self-crumb">IconProviderCallback typedef</li>
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



</div>
`
}</HTMLBlock>
