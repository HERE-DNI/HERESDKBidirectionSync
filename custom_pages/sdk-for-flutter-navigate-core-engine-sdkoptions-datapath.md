---
title: "Untitled"
slug: "sdk-for-flutter-navigate-core-engine-sdkoptions-datapath"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- dataPath.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-core-engine-core-engine-library</li>
<li>/sdk-for-flutter-navigate-core-engine-sdkoptions-class</li>
<li class="self-crumb">dataPath property</li>
</ol>
<div class="self-name">dataPath</div>
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
<h1>dataPath property</h1></div>
<section class="multi-line-signature">
        
        String
        dataPath
<div class="features">getter/setter pair</div>
</section>
<section class="desc markdown">
<p>Path used for storing application internal data, such as the offline search index and other essential data required for proper functionality.</p>
<p><strong>Note:</strong> For common use cases, prefer /sdk-for-flutter-navigate-core-engine-sdkoptions-persistentmapstoragepath, or keep the default paths. Use <code>dataPath</code> only as a fallback if /sdk-for-flutter-navigate-core-engine-sdkoptions-persistentmapstoragepath is not writable, for example, when you have an agreement with HERE to flash data at factory time.</p>
<p>By default, this returns an empty string. In this case, the same path as /sdk-for-flutter-navigate-core-engine-sdkoptions-persistentmapstoragepath will be used.
If an absolute path is set, it will be used instead.
If a relative path is set then directory
<code>Application Library directory</code> for iOS and <code>Context.getFilesDir().getPath()</code> for Android is used as parent path.
Application must have read/write permissions to the given desired path.
It is recommended that the application has exclusive access to this path.
Avoid using shared or public directories such as <code>Download</code> or <code>Documents</code>.
Using such directories may cause certain HERE SDK features to behave with limitations.
For example, index creation for offline search may fail or not function as expected.
It is recommended not to use the application cache paths like
<code>&lt;Application_Home&gt;/Library/Caches</code> for iOS and <code>Context.getCacheDir().getPath()</code> for Android, since operating system manages data in this location
and data can be deleted if the device is low on storage space, which will result in application malfunction.
The path can be on internal or external storage. The internal storage is recommended due to the file I/O speed.
Note:
If the /sdk-for-flutter-navigate-core-engine-sdkoptions-persistentmapstoragepath is writable, <code>dataPath</code> can be left empty.
If the /sdk-for-flutter-navigate-core-engine-sdkoptions-persistentmapstoragepath is not writable, <code>dataPath</code> must be set and also be writable. Note that <code>dataPath</code> is used to store essential HERE SDK data.</p>
<p><strong>Important:</strong>
There is no automatic migration of stored data between the /sdk-for-flutter-navigate-core-engine-sdkoptions-persistentmapstoragepath and the <code>dataPath</code>. For ease of management,
it's recommended to set the persistence path as writable and ignore <code>dataPath</code>.
If <code>dataPath</code> is set differently from the /sdk-for-flutter-navigate-core-engine-sdkoptions-persistentmapstoragepath, some data that would typically be saved in the /sdk-for-flutter-navigate-core-engine-sdkoptions-persistentmapstoragepath will now be saved to <code>dataPath</code>.
If <code>dataPath</code> is set and later unset, any data stored there will remain inaccessible and will not be migrated back.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">String dataPath;</code></pre>
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
<li class="self-crumb">dataPath property</li>
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
