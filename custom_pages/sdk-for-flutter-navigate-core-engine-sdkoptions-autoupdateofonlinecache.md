---
title: "Untitled"
slug: "sdk-for-flutter-navigate-core-engine-sdkoptions-autoupdateofonlinecache"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- autoUpdateOfOnlineCache.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-core-engine-core-engine-library</li>
<li>/sdk-for-flutter-navigate-core-engine-sdkoptions-class</li>
<li class="self-crumb">autoUpdateOfOnlineCache property</li>
</ol>
<div class="self-name">autoUpdateOfOnlineCache</div>
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
<div class="main-content" data-above-sidebar="core.engine/SDKOptions-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>autoUpdateOfOnlineCache property</h1></div>
<section class="multi-line-signature">
        
        bool
        autoUpdateOfOnlineCache
<div class="features">getter/setter pair</div>
</section>
<section class="desc markdown">
<p>Parameter to enable automatic cache updates.</p>
<p>When it is false, the cache will always use the same map version as
offline maps. If offline maps are updated, the cache will be also updated.
The cache version will never be older than the offline maps version.</p>
<p>When it is true, the cache will be automatically updated to use the latest map data
that is available. In that case, the cache may contain map data that is newer than
the offline maps data. Note that auto updates may also lead to increased network traffic, as
the cached data will be evicted tile-by-tile before it is filled with newer map data. This
process continues everytime the user views a new map view area until the data is replaced.
Once also the offline map data is updated by the user, both map versions will
be the same again.</p>
<p>If the value is also specified via the manifest (Android) or plist (iOS), than the
value set via <code>SDKOptions</code> will overrule the value that was set in manifest/plist - until
the current session ends and the value is read/set again.</p>
<p>Note that offline maps are only available for the Navigate license.</p>
<p>Defaults to <code>false</code>.</p>
<p><strong>Note:</strong> Do not use this yet, the behavior of this feature may be inconsistent.
Once it will be usable, it will be announced in the regular HERE SDK release notes.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">bool autoUpdateOfOnlineCache;</code></pre>
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
<li>/sdk-for-flutter-navigate-core-engine-core-engine-library</li>
<li>/sdk-for-flutter-navigate-core-engine-sdkoptions-class</li>
<li class="self-crumb">autoUpdateOfOnlineCache property</li>
</ol>
<h5>SDKOptions class</h5>
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
