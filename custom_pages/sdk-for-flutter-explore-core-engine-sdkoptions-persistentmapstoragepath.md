---
title: "Implementation"
slug: "sdk-for-flutter-explore-core-engine-sdkoptions-persistentmapstoragepath"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- persistentMapStoragePath.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../../core.engine/core.engine-library.html">/sdk-for-flutter-explore-core-engine-core-engine-library</a></li>
<li><a href="../../core.engine/SDKOptions-class.html">/sdk-for-flutter-explore-core-engine-sdkoptions-class</a></li>
<li class="self-crumb">persistentMapStoragePath property</li>
</ol>
<div class="self-name">persistentMapStoragePath</div>
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
<h1>persistentMapStoragePath property</h1></div>
<section class="multi-line-signature">
        
        String
        persistentMapStoragePath
<div class="features">getter/setter pair</div>
</section>
<section class="desc markdown">
<p>Path to store persistent map data. This should be the a path to the desired location for which the application has read/write permissions.
The path can be on internal or external storage.
By default, this returns an empty string. Setting a new string, will overwrite the internally used default paths:</p>
<p><code>Application Library directory</code> for iOS and <code>Context.getFilesDir().getPath()</code> for Android.
If an absolute path is set, it will be used instead.
If a relative path is set then directory
<code>Application Library directory</code> for iOS and <code>Context.getFilesDir().getPath()</code> for Android is used as parent path.
<strong>Note</strong>: Offline maps stored at <code>&lt;persistent_map_storage_path&gt;/v1/&lt;access_key_id&gt;/ocm-map/</code>, where <code>&lt;access_key_id&gt;</code> is
taken from <code>SDKOptions.authenticationMode</code>.
When <code>SDKOptions</code> initialized with <code>AuthenticationMode.withToken</code> or <code>AuthenticationMode.withExternal</code>, then <code>&lt;access_key_id&gt;</code> left empty.</p>
<p>Note: If the persistent map storage location has the read only permission, then the <a href="../../core.engine/SDKOptions/dataPath.html">/sdk-for-flutter-explore-core-engine-sdkoptions-datapath</a> must be configured.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">String persistentMapStoragePath;</code></pre>
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
<li><a href="../../core.engine/core.engine-library.html">/sdk-for-flutter-explore-core-engine-core-engine-library</a></li>
<li><a href="../../core.engine/SDKOptions-class.html">/sdk-for-flutter-explore-core-engine-sdkoptions-class</a></li>
<li class="self-crumb">persistentMapStoragePath property</li>
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
</div></div>
</div>
</HTMLBlock>
