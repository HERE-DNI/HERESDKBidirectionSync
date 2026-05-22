---
title: "Untitled"
slug: "sdk-for-flutter-navigate-search-offlinesearchengine-setindexoptions"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- setIndexOptions.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-search-search-library</li>
<li>/sdk-for-flutter-navigate-search-offlinesearchengine-class</li>
<li class="self-crumb">setIndexOptions static method</li>
</ol>
<div class="self-name">setIndexOptions</div>
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
<div class="main-content" data-above-sidebar="search/OfflineSearchEngine-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>setIndexOptions static method</h1></div>
<section class="multi-line-signature">
/sdk-for-flutter-navigate-search-offlinesearchindexerror?
setIndexOptions(<wbr/><ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-core-engine-sdknativeengine-class sdkEngine, </li>
<li>/sdk-for-flutter-navigate-search-offlinesearchindexoptions-class options, </li>
<li>/sdk-for-flutter-navigate-search-offlinesearchindexlistener-class listener</li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Enables or disables indexing.</p>
<p>When indexing is enabled, HERE SDK will create a detailed index over persistent
map data and update it as needed.
A detailed index enables finding data faster and over entire persistent map.
Creating an index takes time, but usually no more than a few seconds up to a couple of
minutes, depending on persistent map size.
As the feature is improved, the indexing time will improve.
Also please note that this is a heavy processing task.
The stored index increases the space taken by offline maps by around 2-5%.
This may also improve in future versions.</p>
<p>Indexing is disabled by default.
If you want it enabled, make sure to call setIndexOptions with <code>OfflineSearchIndex.Options.enabled</code> as <code>true</code> before
any operations in <code>MapDownloader</code> or <code>MapUpdater</code> that modify the persistent map.
Calling setIndexOptions may also create or remove map index to match the previously
installed map regions. If the matching index for installed map regions is found, then
indexing is skipped.
While a new index is being created, <code>OfflineSearchEngine</code> functionality can still be used.
However, without a valid index in place yet, it operates as though indexing is disabled.
If <code>SDKNativeEngine</code> is disposed during indexing (for example, by closing the app),
the indexing is cancelled. Recreating <code>SDKNativeEngine</code> and enabling indexing will
ensure that index is created.</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected
behaviors. Related APIs may change for new releases without a deprecation process.</p>
<ul>
<li>
<p><code>sdkEngine</code> Indexing is enabled and disabled per SDKNativeEngine instance.
The index is created inside the related /sdk-for-flutter-navigate-core-engine-sdkoptions-persistentmapstoragepath.</p>
</li>
<li>
<p><code>options</code> Sets indexing options.</p>
</li>
<li>
<p><code>listener</code> The listener that will receive updates about indexing process.
When <code>OfflineSearchIndex.Options.enabled</code> is true, SDK would store listener and the listener will receive updates
about indexing progress every time it is performed.
When <code>OfflineSearchIndex.Options.enabled</code> is false, SDK would report indexing removal progress to the listener
one last time and remove storage of listener.</p>
</li>
</ul>
<p>Returns /sdk-for-flutter-navigate-search-offlinesearchindexerror. An error in case there was one.</p>
<p>It's <code>null</code> if the indexing listener could be
configured successfully.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">static OfflineSearchIndexError? setIndexOptions(SDKNativeEngine sdkEngine, OfflineSearchIndexOptions options, OfflineSearchIndexListener listener) =&gt; $prototype.setIndexOptions(sdkEngine, options, listener);</code></pre>
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
<li>/sdk-for-flutter-navigate-search-offlinesearchengine-class</li>
<li class="self-crumb">setIndexOptions static method</li>
</ol>
<h5>OfflineSearchEngine class</h5>
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
